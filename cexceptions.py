from termcolor import colored
import difflib


class CBaseException:
    def __init__(self, ctx):
        self.ctx = ctx
        self.error = 'No error message'

    @property
    def line(self):
        return self.ctx.start.line

    def new_line(self):
        self.error += '\n'

    def __repr__(self):
        return colored(self.error, 'red')


class CAttributeNotFound(CBaseException):
    def __init__(self, ctx, clazz_map, attribute: str):
        super().__init__(ctx)
        self.clazz_map = clazz_map
        self.attribute = attribute

        self.error = self.ctx.getText()
        self.new_line()
        l = len(self.ctx.getText())
        l1 = len(self.ctx.start.text)
        l2 = len(self.ctx.stop.text)

        self.error += '_' * l1
        self.error += '_' * (l - l1 - l2)
        self.error += '^' * l2

        self.new_line()
        self.error += f'Error <CAttributeNotFound: Line {self.line}>: '

        self.error += f'class `{self.clazz_map.name}` does not have attribute `{self.attribute}`'
        match = self.closest_match(
            self.attribute,
            self.clazz_map.attributes.keys()
        )
        if match:
            self.error += f'\nDid you mean `{match}`?'

        print(self)

    def closest_match(self, target, word_list):
        matches = difflib.get_close_matches(target, word_list)
        return matches[0] if matches else None

from termcolor import colored

def print_error(error: str):
    print(colored(error, 'red'))

class Arg:
    def __init__(self, name, clazz_name):
        self.name = name
        self.clazz_name = clazz_name


class Function:
    def __init__(self, name, alias):
        self.name = name
        self.alias = alias
        self.args: list[Arg] = []

    def add_arg(self, arg: Arg):
        self.args.append(arg)


class Attribute:
    def __init__(self, name, type_specifier):
        self.name: str = name
        self.type_specifier: str = type_specifier

    def __eq__(self, other):
        return self.name == other.name


class Clazz:
    def __init__(self, name, alias):
        self.name: str = name
        self.alias: str = alias
        self.constructor: Function | None = None
        self.methods: list[Function] = []
        self.attributes: list[Attribute] = []

    def add_method(self, method: Function):
        self.methods.append(method)

    def add_attribute(self, attribute: Attribute):
        if attribute in self.attributes:
            print_error(f'error: duplicate member `{attribute.name}`')
        self.attributes.append(attribute)

    def get_method(self, name) -> Function:
        for method in self.methods:
            if method.name == name:
                return method
        raise Exception(f'Method {name} does not exist!')


class Obj:
    def __init__(self, name, clazz_name):
        self.name: str = name
        # should this be an instance of a class?
        self.clazz_name: str = clazz_name


class Manager:
    def __init__(self):
        self.functions: list[Function] = []
        self.clazzes: list[Clazz] = []
        self.objs: list[Obj] = []
        self.current_clazz: Clazz | None = None
        self.current_function: Function | None = None

    def add_clazz(self, clazz: Clazz):
        self.clazzes.append(clazz)

    def get_clazz(self, name):
        for clazz in self.clazzes:
            if clazz.name == name:
                return clazz
        raise Exception(f'Class {name} does not exist!')

    def add_obj(self, obj: Obj) -> None:
        self.objs.append(obj)

    def get_obj(self, name) -> Obj | None:
        for obj in self.objs:
            if obj.name == name:
                return obj
        return None

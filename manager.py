import llvmlite.ir as ir
from termcolor import colored
from enum import Enum


class ScopeType(Enum):
    GLOBAL = 0
    FUNC = 1
    CLAZZ = 2


def print_error(error: str):
    print(colored(error, 'red'))


class Scope:
    def __init__(self, scope_type: ScopeType, function=None):
        self.parent: Scope | None = None
        self.function = function
        self.scope_type: ScopeType = scope_type
        self.functions = []
        self.variables = []
        self.clazzes = []
        self.scopes: list[Scope] = []
        # a scope has vars, objs, functions, methods and attributes

    def add_scope(self, scope: 'Scope'):
        self.scopes.append(scope)

    def add_variable(self, variable):
        self.variables.append(variable)

    def add_function(self, func):
        self.functions.append(func)

    def add_clazz(self, clazz):
        self.clazzes.append(clazz)


class GlobalScope(Scope):
    def __init__(self):
        super().__init__(ScopeType.GLOBAL)


class ScopeStack:
    def __init__(self):
        self.stack: list[Scope] = [GlobalScope()]

    def push(self, scope: Scope) -> None:
        self.stack.append(scope)

    def pop(self) -> Scope | None:
        try:
            return self.stack.pop()
        except IndexError:
            return None

    def is_global_scope(self):
        return isinstance(self.stack[-1], GlobalScope)

    def add_variable(self, variable) -> None:
        self.stack[-1].add_variable(variable)

    def get_variable(self, identifier):
        # this need optimisation meh not bothered for now
        # TODO: fix flaw where it skips func args
        # TODO: probably fixed it
        for lvl, scope in enumerate(self.stack[::-1]):
            for _, var in enumerate(scope.variables[::-1]):
                if var.name == identifier:
                    return var
            if scope.scope_type == ScopeType.FUNC:
                for _, arg in enumerate(scope.function.args):
                    if arg.name == identifier:
                        return arg
        else:
            print_error(f'`{identifier}` has never been declared!')

    def add_function(self, func):
        self.stack[-1].add_function(func)

    def get_function(self, identifier):
        # this need optimisation meh not bothered for now
        for lvl, scope in enumerate(self.stack[::-1]):
            for _, var in enumerate(scope.functions[::-1]):
                if var.name == identifier:
                    return var
        else:
            print_error(f'`{identifier}` has never been declared!')

    def add_clazz(self, clazz):
        self.stack[-1].add_clazz(clazz)

    def get_clazz(self, identifier):
        # this need optimisation meh not bothered for now
        for lvl, scope in enumerate(self.stack[::-1]):
            for _, clazz in enumerate(scope.clazzes[::-1]):
                if clazz.name == identifier:
                    return clazz
        else:
            print_error(f'`{identifier}` has never been declared!')


class Manager:
    def __init__(self):
        # this is for nested scope push and pop
        self.scope_stack: ScopeStack = ScopeStack()
        self.functions = []
        self.variables = []
        self.clazzes = []
        self.current_clazz = None
        self.current_function: ir.Function | None = None
        self.builder: ir.IRBuilder | None = None

        # string literal counter to prevent global duplication
        self.__slc = 0

    @property
    def slc(self):
        self.__slc += 1
        return f'.str.{self.__slc}'

    def add_variable(self, variable):
        self.scope_stack.add_variable(variable)

    def add_function(self, func):
        self.scope_stack.add_function(func)

    def push_scope(self, scope):
        self.scope_stack.push(scope)

    def add_clazz(self, clazz):
        self.scope_stack.add_clazz(clazz)

    def get_clazz(self, identifier):
        return self.scope_stack.get_clazz(identifier)

    def get_variable(self, identifier):
        return self.scope_stack.get_variable(identifier)

    def get_function(self, identifier):
        return self.scope_stack.get_function(identifier)

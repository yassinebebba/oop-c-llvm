from termcolor import colored
from enum import Enum


class ScopeType(Enum):
    FUNC = 0
    CLAZZ = 1


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

    def get_arg(self, obj_name):
        for arg in self.args:
            if arg.name == obj_name:
                return arg
        else:
            raise Exception(f'ARG {obj_name} does not exist')


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


class Variable:
    def __init__(self, name, type_specifier):
        self.name: str = name
        self.clazz_name: str = type_specifier


class Scope:
    def __init__(self, scope_type: ScopeType, parent: 'Scope'):
        self.parent: Scope = parent
        self.scope_type: ScopeType = scope_type
        self.functions: list[Function] = []
        self.variables: list[Variable] = []
        self.clazzes: list[Clazz] = []
        self.objs: list[Obj] = []
        self.scopes: list[Scope] = []
        # a scope has vars, objs, functions, methods and attributes


class GlobalScope:
    def __init__(self):
        self.functions: list[Function] = []
        self.variables: list[Variable] = []
        self.clazzes: list[Clazz] = []
        self.objs: list[Obj] = []
        self.scopes: list[Scope] = []

    def add_scope(self, scope: Scope):
        self.scopes.append(scope)


class ScopeQueue:
    def __init__(self):
        self.queue: list[Scope] = []

    def push(self, scope: Scope) -> None:
        self.queue.append(scope)

    def pop(self) -> Scope | None:
        try:
            return self.queue.pop()
        except IndexError:
            return None


class Manager:
    def __init__(self):
        self.global_scope: GlobalScope = GlobalScope()

        # this is for nested scope push and pop
        self.scope_queue: ScopeQueue = ScopeQueue()
        self.functions: list[Function] = []
        self.variables: list[Variable] = []
        self.clazzes: list[Clazz] = []
        self.objs: list[Obj] = []
        self.current_clazz: Clazz | None = None
        self.current_function: Function | None = None

    def add_variable(self, variable: Variable):
        self.variables.append(variable)

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

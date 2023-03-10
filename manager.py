import llvmlite.ir as ir
from termcolor import colored
from enum import Enum


class ScopeType(Enum):
    GLOBAL = 0
    FUNC = 1
    CLAZZ = 2


def print_error(error: str):
    print(colored(error, 'red'))


class Arg:
    def __init__(self, type_specifier: str, name: str | None,
                 clazz: 'Clazz' or None):
        self.type_specifier = type_specifier
        self.name = name
        self.clazz: Clazz | None = clazz

    def __repr__(self):
        return f'{type(self).__name__}' \
               f'(type={self.type_specifier}, name={self.name})'


class Function:
    def __init__(self, rtype, name, alias, args):
        self.rtype = rtype
        self.name = name
        self.alias = alias
        self.args: list[Arg] = args

    def add_arg(self, arg: Arg):
        self.args.append(arg)

    def get_arg(self, obj_name):
        for arg in self.args:
            if arg.name == obj_name:
                return arg
        else:
            raise Exception(f'Arg {obj_name} does not exist')

    def __repr__(self):
        return f'{type(self).__name__}' \
               f'(rtype={self.rtype},' \
               f' name={self.name},' \
               f' alias={self.alias},' \
               f' args={self.args})'


class Attribute:
    def __init__(self, name, type_specifier, clazz: 'Clazz' or None):
        self.type_specifier: str = type_specifier
        self.name: str = name
        self.clazz: Clazz | None = clazz

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

    def get_attribute(self, name) -> Attribute:
        for attribute in self.attributes:
            if attribute.name == name:
                return attribute
        raise NameError(f'Attribute {name} does not exist!')

    def get_method(self, name) -> Function:
        for method in self.methods:
            if method.name == name:
                return method
        raise Exception(f'Method {name} does not exist!')


class Obj:
    def __init__(self, name, clazz: Clazz):
        self.name: str = name
        # should this be an instance of a class?
        self.clazz: Clazz = clazz

    def __repr__(self):
        return f'{type(self).__name__}(name={self.name}, class={self.clazz})'


class Variable:
    def __init__(self, name, type_specifier, ir_type):
        self.name: str = name
        self.clazz_name: str = type_specifier
        self.ir_type = ir_type


class Scope:
    def __init__(self, scope_type: ScopeType):
        self.parent: Scope | None = None
        self.scope_type: ScopeType = scope_type
        self.functions: list[Function] = []
        self.variables = []
        self.clazzes: list[Clazz] = []
        self.objs: list[Obj] = []
        self.scopes: list[Scope] = []
        # a scope has vars, objs, functions, methods and attributes

    def add_scope(self, scope: 'Scope'):
        self.scopes.append(scope)

    def add_variable(self, variable):
        self.variables.append(variable)


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

    def add_variable(self, variable) -> None:
        self.stack[-1].add_variable(variable)

    def get_variable(self, identifier):
        # this need optimisation meh not bothered for now
        for lvl, scope in enumerate(self.stack[::-1]):
            for _, var in enumerate(scope.variables[::-1]):
                if var.name == identifier:
                    return var
        else:
            raise NameError(f'`{identifier}` has never been declared!')


class Manager:
    def __init__(self):
        # this is for nested scope push and pop
        self.scope_stack: ScopeStack = ScopeStack()
        self.functions: list[Function] = []
        self.variables: list[Variable] = []
        self.clazzes: list[Clazz] = []
        self.objs: list[Obj] = []
        self.current_clazz: Clazz | None = None
        self.current_function: ir.Function | None = None
        self.builder: ir.IRBuilder | None = None

    def add_variable(self, variable: Variable):
        self.variables.append(variable)

    def add_clazz(self, clazz: Clazz):
        self.clazzes.append(clazz)

    def get_clazz(self, name):
        for clazz in self.clazzes:
            if clazz.name == name:
                return clazz
        raise NameError(f'Class {name} does not exist!')

    def add_obj(self, obj: Obj) -> None:
        self.objs.append(obj)

    def get_obj(self, name) -> Obj | None:
        for obj in self.objs:
            if obj.name == name:
                return obj
        return None

    def get_variable(self, name) -> Variable | None:
        for var in self.variables:
            if var.name == name:
                return var
        return None

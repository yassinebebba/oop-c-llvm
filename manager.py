import llvmlite.ir as ir
from termcolor import colored
from typing import Union


def print_error(error: str):
    print(colored(error, 'red'))

class ClazzMethod:
    def __init__(self, name, mangled_name, is_constructor=False):
        self.name = name
        self.mangled_name = mangled_name
        self.is_constructor = is_constructor
class ClazzMap:
    """
    this is a map for class and is not part of the scope stack
    """

    def __init__(self, name: str, alias: str):
        self.name = name
        self.alias = alias
        self.attributes = {}
        self.methods = {}

    def add_attribute(self, index, name):
        self.attributes[name] = {
            'index': index,
        }

    def get_attribute(self, name):
        return self.attributes.get(name, None)

    def add_method(self, method: ClazzMethod):
        self.methods[method.name] = method
    def get_method(self, name):
        return self.methods.get(name, None)

class Func:
    def __init__(self, name: str):
        self.name = name


class Variable:
    def __init__(self, name: str):
        self.name = name


class Scope:
    def __init__(self):
        self.symbol_table = {}

    def add_variable(self, variable: Variable) -> None:
        self.symbol_table[variable.name] = variable

    def get_variable(self, identifier: str) -> Variable:
        return self.symbol_table.get(identifier, None)

    def add_function(self, func: Func) -> None:
        self.symbol_table[func.name] = func

    def get_function(self, identifier: str) -> Func:
        return self.symbol_table.get(identifier, None)

    def add_clazz(self, clazz) -> None:
        self.symbol_table[clazz.name] = clazz


class GlobalScope(Scope):
    def __init__(self):
        super().__init__()


class FuncScope(Scope):
    def __init__(self, func: ir.Function = None, builder: ir.IRBuilder = None):
        super().__init__()
        self.func = func
        self.builder = builder
        is_clazz_method = False
        is_constructor = False

    def get_variable(self, identifier: str) -> Variable | None:
        var = super().get_variable(identifier)
        if var:
            return var
        else:
            for arg in self.func.args:
                if arg.name == identifier:
                    return arg
            else:
                print_error(f'`{identifier}` has never been declared!')

    def get_function(self, identifier: str) -> None:
        # functions cannot be nested
        return None


class ClazzScope(Scope):
    def __init__(self, clazz):
        super().__init__()
        self.clazz = clazz


ALL_SCOPES = Union[GlobalScope, FuncScope]


class ScopeStack:
    def __init__(self):
        self.stack: list[ALL_SCOPES] = [GlobalScope()]

    def push(self, scope: ALL_SCOPES) -> None:
        self.stack.append(scope)

    def pop(self) -> ALL_SCOPES | None:
        try:
            return self.stack.pop()
        except IndexError:
            return None

    def is_global_scope(self):
        return isinstance(self.stack[-1], GlobalScope)

    def add_variable(self, variable: Variable) -> None:
        self.stack[-1].add_variable(variable)

    def get_variable(self, identifier: str) -> Variable:
        for scope in self.stack[::-1]:
            var = scope.get_variable(identifier)
            if var:
                return var
        else:
            print_error(f'`{identifier}` has never been declared!')

    def add_function(self, func):
        self.stack[-1].add_function(func)

    def get_function(self, module, identifier):
        # functions are global so use module.get_global from llvm
        try:
            return module.get_global(identifier)
        except KeyError:
            print_error(f'`{identifier}` has never been declared!')

    def add_clazz(self, clazz: ClazzScope):
        self.stack[-1].add_clazz(clazz)

    def get_clazz(self, identifier):
        # this need optimisation meh not bothered for now
        for lvl, scope in enumerate(self.stack[::-1]):
            for _, clazz in enumerate(scope.clazzes[::-1]):
                if clazz.name == identifier:
                    return clazz
        else:
            print_error(f'`{identifier}` has never been declared!')

    def get_last_builder(self):
        for scope in self.stack[::-1]:
            if isinstance(scope, FuncScope):
                return scope.builder
        else:
            return None

    def get_last_function(self):
        for scope in self.stack[::-1]:
            if isinstance(scope, FuncScope):
                return scope.func
        else:
            return None


class Manager:
    def __init__(self):
        # this is for nested scope push and pop
        self.scope_stack: ScopeStack = ScopeStack()
        self.current_clazz = None
        # string literal counter to prevent global duplication
        self.__slc = 0

    @property
    def slc(self):
        self.__slc += 1
        return f'.str.{self.__slc}'

    def push_scope(self, scope):
        self.scope_stack.push(scope)

    def pop_scope(self):
        return self.scope_stack.pop()

    def add_variable(self, variable):
        self.scope_stack.add_variable(variable)

    def get_variable(self, identifier):
        return self.scope_stack.get_variable(identifier)

    def add_function(self, func):
        self.scope_stack.add_function(func)

    def get_function(self, module, identifier):
        return self.scope_stack.get_function(module, identifier)

    def add_clazz(self, clazz):
        self.scope_stack.add_clazz(clazz)

    def get_clazz(self, identifier):
        return self.scope_stack.get_clazz(identifier)

    def get_last_function(self):
        return self.scope_stack.get_last_function()
    def get_last_builder(self):
        return self.scope_stack.get_last_builder()

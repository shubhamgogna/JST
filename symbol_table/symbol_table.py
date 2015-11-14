# This file is part of JST.
#
# JST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# JST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with JST.  If not, see <http://www.gnu.org/licenses/>.

from symbol_table.scope import Scope
from symbol_table.symbol import Symbol


class SymbolTable(object):
    # Initializes the symbol table
    def __init__(self):
        self.table = []

    # Pushes a scope onto the table.
    # 'scope' Scope to push. Leave as default to push empty Scope.
    def push(self, scope=None):
        if scope is None:
            scope = Scope()
        if type(scope) is Scope:
            self.table.append(scope)
        else:
            raise TypeError("'scope' is not an instance of Scope.")

    # Pops the top-most Scope from the table and returns it.
    def pop(self):
        return self.table.pop()

    # Inserts a symbol into the top-most Scope.
    # Returns a tuple of the result and a list of shadowed Symbols or
    # re-declared Symbol.
    def insert(self, symbol):
        if not isinstance(symbol, Symbol):
            raise TypeError("'symbol' is not an instance of Symbol.")
        elif not self.table:
            raise Exception('Table has no scopes available to insert into. Offending symbol: {}'.format(symbol))

        shadowed_symbols = []
        for scope in self.table:
            result = scope.find(symbol.identifier)
            if result is not None:
                if scope is not self.table[-1]:
                    shadowed_symbols.append(result)
                else:
                    return Scope.INSERT_REDECL, [result]

        self.table[-1].insert(symbol)

        if len(shadowed_symbols) is 0:
            return Scope.INSERT_SUCCESS, []
        else:
            return Scope.INSERT_SHADOWED, shadowed_symbols

    # Finds a symbol in the table by searching the top-most Scope to the
    # bottom-most Scope.
    # 'name' String identifier for the Symbol to find.
    # Returns a tuple of the Symbol and the Scope index it was found in.
    def find(self, name):
        for index, scope in enumerate(reversed(self.table)):
            result = scope.find(name)
            if result is not None:
                scope_level = (len(self.table) - (index + 1))
                return result, scope_level
        return None, None

    # Replaces a symbol in the table by searching the top-most Scope to
    # the bottom-most Scope. The symbols are compared by reference (not
    # by identifier).
    # 'original' Original symbol in the table.
    # 'replacement' Symbol to replace original.
    # Returns true if replaced and false if not.
    def replace(self, original, replacement):
        for scope in reversed(self.table):
            if scope.replace(original, replacement):
                return True
        return False

    # Finds a symbol in the table by searching only the top-most Scope.
    # 'name' String identifier for the Symbol to find.
    # Returns 'None' or the Symbol.
    def find_in_top(self, name):
        return self.table[-1].find(name)

    ## TODO: if we implement this
    def find_type(self, identifier):
        pass

    # Returns the number of Scopes in the table.
    def size(self):
        return len(self.table)

    # Clones the current SymbolTable and returns the deep copy.
    def clone(self):
        result = SymbolTable()
        result.table = []
        for scope in self.table:
            result.table.append(scope.clone())
        return result

    # Converts the current SymbolTable to its String representation.
    def __repr__(self):
        scopes = []
        for index, scope in enumerate(self.table):
            scopes.append('Scope #' + repr(index) + '\n' + repr(scope))
        return '\n'.join(scopes)

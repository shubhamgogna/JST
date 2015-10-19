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
    def __init__(self):
        self.table = [Scope()]

    def push(self, scope=None):
        if scope is None:
            scope = Scope()
        if type(scope) is Scope:
            self.table.append(scope)
        else:
            raise TypeError("'scope' is not an instance of Scope.")

    def pop(self):
        return self.table.pop()

    def insert(self, symbol):
        if type(symbol) is Symbol:
            shawdowed = False

            for scope in self.table:
                result = scope.find(symbol.identifier)
                if result is not None:
                    if scope is self.table[-1]:
                        return "EXISTS"
                    else:
                        shawdowed = True

            self.table[-1].insert(symbol)
            return "SUCCESS" if not shawdowed else "SHADOWED"
        else:
            raise TypeError("'symbol' is not an instance of Symbol.")

    def find(self, name):
        for scope in reversed(self.table):
            result = scope.find(name)
            if result is not None:
                return result
        return None

    def find_type(self, name):
        pass

    def insert_type(self, name, actual_type=None):
        pass

    def find_enum_constant_value(self, identifier):
        pass

    def size(self):
        return len(self.table)

    def clone(self):
        result = SymbolTable()
        result.table = []
        for scope in self.table:
            result.append(scope)
        return result

    def __repr__(self):
        scopes = []
        for index, scope in enumerate(self.table):
            scopes.append(repr(index) + '\n' + repr(scope))
        return "\n".join(scopes)

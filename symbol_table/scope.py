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

from bintrees import RBTree
from symbol_table.symbol import Symbol


class Scope(object):
    INSERT_SUCCESS = 0
    INSERT_SHADOWED = 1
    INSERT_REDECL = 2

    def __init__(self):
        self.map = RBTree()

    def insert(self, symbol):
        if not isinstance(symbol, Symbol):
            raise TypeError("'symbol' is not an instance of Symbol.")

        if symbol.identifier not in self.map:
            existing = self.map[symbol.identifier] = []
        else:
            existing = self.map[symbol.identifier]

        for item in existing:
            # Allow at most one of each type
            if type(item) is type(symbol):
                return Scope.INSERT_REDECL

        existing.append(symbol)
        return Scope.INSERT_SUCCESS

    def find_with_type(self, name, search_type):
        results = self.map.get(name, None)
        if results is None:
            return None

        for result in results:
            if type(result) is search_type:
                return result
        return None

    def size(self):
        return len(self.map)

    def clone(self):
        result = Scope()
        for identifier, value in self.map.items():
            result.map[identifier] = []
            for elem in value:
                result.map[identifier].append(elem.clone())
        return result

    def __repr__(self):
        symbols = []
        for key, value in self.map.items():
            symbols.append("  " + key + " : " + repr(value))
        return "\n".join(symbols)

    def __find(self, name):
        return self.map.get(name, None)

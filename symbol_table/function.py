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

from symbol_table.symbol import Symbol

# Functions are made up of a return type, name, and a list of parameters.
# They have a type associated with them for function pointers that results
# from a mix of their return type and parameters.
class Function(Symbol):
    def __init__(self, identifier='', returns=None, params=None):
        super().__init__(identifier=identifier)
        self.params = [] if (params is None) else params
        self.returns = returns

    # TODO To support function pointers, we can add self.type
    # that returns the type of the function pointer than can point
    # to this function

    def __repr__(self):
        prefix = 'Function > ' + repr(self.returns) + ' ' + self.identifier + '('
        lst = []
        for param in self.params:
            lst.append(param)
        return prefix + ', '.join(lst) + ')'

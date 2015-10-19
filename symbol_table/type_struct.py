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

# Structs are complicated. This is just a basic placeholder for now.
class TypeStruct(Symbol):
    def __init__(self, identifier='', members=None):
        super().__init__(identifier=identifier)
        self.members = [] if (members is None) else members

    def __repr__(self):
        lst = []
        for member in self.members:
            lst.append(repr(member))
        return 'Struct > ' + self.identifier + '\n' + '\n'.join(lst)

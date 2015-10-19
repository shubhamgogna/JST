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

# Typedefs are aliased types. They are actually of the specified type
# and not an actual, separate type. However, they are treated like a different
# type (note: implicit conversions?).
class TypeTypedef(Symbol):
    def __init__(self, identifier='', actual_type=None):
        super().__init__(identifier=identifier)
        self.actual_type = actual_type

    def __repr__(self):
        return 'Typedef > ' + self.identifier + ' -> ' + repr(self.actual_type)

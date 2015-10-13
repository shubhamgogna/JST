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
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

from symbol_table.symbol import Symbol


class SymbolBuilder(object):
    """A placeholder so I can continue working."""

    def __init__(self):
        self.id = None
        self.type = Type()

    def build(self):
        return Symbol(self.id)


class Type(object):
    """Also a placeholder."""

    def __init__(self):
        self.type_name = ""
        self.storage_specifiers = []  # auto, static, extern, etc.
        self.type_qualifier = None    # const, volatile
        self.type_specifier = None    # int, float, etc.
        self.pointer_count = 0
        self.is_struct = False
        self.is_union = False
        self.is_function = False
        self.arg_list = []


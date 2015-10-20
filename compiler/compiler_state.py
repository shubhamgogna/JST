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

from symbol_table.symbol_table import SymbolTable


class CompilerState:
    def __init__(self):
        self.insert_mode = True
        # self.most_recent_type_declaration = TypeDeclaration()  FIXME Replaced
        self.symbol_table = SymbolTable()
        # lex uses 1 based indexing for line numbers, we are using 0 based for source_code
        self.source_code = []

        # for debugging purposes
        self.clone_symbol_table_on_scope_exit = False
        self.cloned_tables = []

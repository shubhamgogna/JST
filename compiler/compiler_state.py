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

###############################################################################
# File Description: Class definition for a shared object between the Scanner,
# parser, and symbol table.
###############################################################################

from symbol_table.symbol_table import SymbolTable
from symbol_table.symbol import TypeDeclaration

## A simple class to share state among objects.
#
# This class is used by the Lexer and Parser, and contains information and items relevant to both classes that does not
# belong exclusively in either one.
#
class CompilerState:
    def __init__(self, source_code):
        self.symbol_table = SymbolTable()

        self.function_scope_entered = False

        self.insert_mode = True
        self.most_recent_type_declaration = TypeDeclaration()


        # lex uses 1 based indexing for line numbers, we are using 0 based for source_code
        self.source_code = source_code.split('\n')
        self.last_lineno = -1

        # for debugging purposes
        self.clone_symbol_table_on_scope_exit = False
        self.cloned_tables = []

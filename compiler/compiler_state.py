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

import sys
from symbol_table.symbol_table import SymbolTable
from loggers.logger import Logger


# A simple class to share state among objects.
#
# Used by the Lexer and Parser. Contains information and items relevant to both
# classes that does not belong exclusively in either one.
class CompilerState:
    def __init__(self, source_code=None,
                 print_table=False, table_logfile='log_symbol_table.txt',
                 print_tokens=False, print_source_scanner=True, scanner_logfile='log_scanner_tokens.txt',
                 print_productions=False, print_source_parser=False, print_info=False, parser_logfile=sys.stdout):#'log_parser_productions.txt'):

        # Initialize table
        self.symbol_table = SymbolTable()

        # Lex uses 1 based indexing for line numbers.
        # We are using 0 based for source_code.
        if source_code is not None:
            self.source_code = source_code.split('\n')
        else:
            self.source_code = None

        # Initialize symbol table logger
        if table_logfile in {sys.stdout, sys.stderr}:
            self.symbol_table_logger = Logger(table_logfile)
        else:
            self.symbol_table_logger = Logger(open(table_logfile, 'w'))

        if print_table is True:
            self.symbol_table_logger.add_switch(Logger.SYMBOL_TABLE)

        # Initialize token/lexer logger
        if scanner_logfile in {sys.stdout, sys.stderr}:
            self.token_logger = Logger(scanner_logfile)
        else:
            self.token_logger = Logger(open(scanner_logfile, 'w'))

        if print_source_scanner is True:
            self.token_logger.add_switch(Logger.SOURCE)

        if print_tokens is True:
            self.token_logger.add_switch(Logger.TOKEN)

        # Initialize parser logger
        if parser_logfile in {sys.stdout, sys.stderr}:
            self.parser_logger = Logger(parser_logfile)
        else:
            self.parser_logger = Logger(open(parser_logfile, 'w'))

        if print_source_parser is True:
            self.parser_logger.add_switch(Logger.SOURCE)

        if print_productions is True:
            self.parser_logger.add_switch(Logger.PRODUCTION)

        if print_info is True:
            self.parser_logger.add_switch(Logger.INFO)

        # Other stuff
        self.function_scope_entered = False

        self.insert_mode = True

        # for debugging purposes
        self.clone_symbol_table_on_scope_exit = False
        self.cloned_tables = []

    def get_symbol_table_logger(self):
        return self.symbol_table_logger

    def get_token_logger(self):
        return self.token_logger

    def get_parser_logger(self):
        return self.parser_logger

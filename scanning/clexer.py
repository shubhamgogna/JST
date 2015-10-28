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
# File Description: Lexer class definition for tokenizing the input program
# file and returning tokens to the Parser.
###############################################################################

import sys
import ply.lex as lex
from exceptions.compile_error import CompileError


class Lexer(object):
    def __init__(self, compiler_state=None, **kwargs):

        self.lexer = lex.lex(module=self, **kwargs)

        self.compiler_state = compiler_state
        self.table_logger = self.compiler_state.get_symbol_table_logger()
        self.token_logger = self.compiler_state.get_token_logger()

        self.last_token = None

    def teardown(self):
        self.token_logger.finalize()
        self.table_logger.finalize()

    def input(self, data):
        self.lexer.input(data)

        # Print out the first line (otherwise it will be missed)
        self.token_logger.source(self.compiler_state.source_code[0])

    # Compute column.
    # 'token' is a token instance
    # http://www.dabeaz.com/ply/ply.html#ply_nn9
    def find_column(self, token):
        last_newline = self.lexer.lexdata.rfind('\n', 0, token.lexpos)
        return max(0, (token.lexpos - last_newline) - 1)

    def token(self):
        self.last_token = self.lexer.token()
        self.last_token.lineno = self.lexer.lineno
        self.last_token.column = self.find_column(self.last_token)

        if self.last_token is not None:
            self.token_logger.token(str(self.last_token.type) + ' ' + str(self.last_token.value))
        return self.last_token

    # Define a rule so we can track line numbers
    # 'token' is a token instance
    # http://www.dabeaz.com/ply/ply.html#ply_nn9
    def t_newline(self, token):
        r'\n+'
        self.token_logger.source(self.compiler_state.source_code[self.lexer.lineno])
        self.lexer.lineno += len(token.value)

    # Reserved words
    reserved = (
        'AUTO', 'BREAK', 'CASE', 'CHAR', 'CONST', 'CONTINUE', 'DEFAULT', 'DO', 'DOUBLE',
        'ELSE', 'ENUM', 'EXTERN', 'FLOAT', 'FOR', 'GOTO', 'IF', 'INT', 'LONG', 'REGISTER',
        'RETURN', 'SHORT', 'SIGNED', 'SIZEOF', 'STATIC', 'STRUCT', 'SWITCH', 'TYPEDEF',
        'UNION', 'UNSIGNED', 'VOID', 'VOLATILE', 'WHILE',
        )

    tokens = reserved + (
        # Literals (identifier, integer constant, float constant, string constant, char const)
        # NOTE: also need to include Enumeration Const!
        'ID', 'TYPEID', 'ICONST', 'FCONST', 'SCONST', 'CCONST', 'ECONST',

        # Operators (+,-,*,/,%,|,&,~,^,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=)
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
        'OR', 'AND', 'NOT', 'XOR', 'LSHIFT', 'RSHIFT',
        'LOR', 'LAND', 'LNOT',
        'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

        # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
        'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
        'LSHIFTEQUAL','RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',

        # Increment/decrement (++,--)
        'PLUSPLUS', 'MINUSMINUS',

        # Structure dereference (->)
        'ARROW',

        # Conditional operator (?)
        'CONDOP',

        # Delimeters ( ) [ ] { } , . ; :
        'LPAREN', 'RPAREN',
        'LBRACKET', 'RBRACKET',
        'LBRACE', 'RBRACE',
        'COMMA', 'PERIOD', 'SEMI', 'COLON',

        # Ellipsis (...)
        'ELLIPSIS',

        # NOTE: we must also include range
        # 'RANGE',  # TODO: I propose we throw this out. -Terence

        # Need to include error token for warning issues?
        #'ERROR' # TODO: if we decide we want the parser to handle all errors/error reporting this will be good
                 # TODO: otherwise let's toss it (I'm in favor of passing all errors to the parser for unified
                 # TODO: error management, but it will take some figuring out. -Terence)
        )

    # Completely ignored characters
    # TODO Check if this is actually ignoring? Isn't the regex for this r'[ \t\x0c]'?
    t_ignore           = ' \t\x0c'

    # Operators
    t_PLUS             = r'\+'
    t_MINUS            = r'-'
    t_TIMES            = r'\*'
    t_DIVIDE           = r'/'
    t_MOD              = r'%'
    t_OR               = r'\|'
    t_AND              = r'&'
    t_NOT              = r'~'
    t_XOR              = r'\^'
    t_LSHIFT           = r'<<'
    t_RSHIFT           = r'>>'
    t_LOR              = r'\|\|'
    t_LAND             = r'&&'
    t_LNOT             = r'!'
    t_LT               = r'<'
    t_GT               = r'>'
    t_LE               = r'<='
    t_GE               = r'>='
    t_EQ               = r'=='
    t_NE               = r'!='

    # Assignment operators
    t_EQUALS           = r'='
    t_TIMESEQUAL       = r'\*='
    t_DIVEQUAL         = r'/='
    t_MODEQUAL         = r'%='
    t_PLUSEQUAL        = r'\+='
    t_MINUSEQUAL       = r'-='
    t_LSHIFTEQUAL      = r'<<='
    t_RSHIFTEQUAL      = r'>>='
    t_ANDEQUAL         = r'&='
    t_OREQUAL          = r'\|='
    t_XOREQUAL         = r'\^='

    # Increment/decrement
    t_PLUSPLUS         = r'\+\+'
    t_MINUSMINUS       = r'--'

    # ->
    t_ARROW            = r'->'

    # ?
    t_CONDOP           = r'\?'

    # Delimeters
    t_LPAREN           = r'\('
    t_RPAREN           = r'\)'
    t_LBRACKET         = r'\['
    t_RBRACKET         = r'\]'

    def t_LBRACE(self, t):
        r'\{'
        self.table_logger.symbol_table("Opening Brace. Symbol Table:\n")
        self.table_logger.symbol_table(str(self.compiler_state.symbol_table))
        self.table_logger.symbol_table('\n')
        return t

    def t_RBRACE(self, t):
        r'\}'
        self.table_logger.symbol_table("Closing Brace. Symbol Table:\n")
        self.table_logger.symbol_table(str(self.compiler_state.symbol_table))
        self.table_logger.symbol_table('\n')
        return t

    t_COMMA            = r','
    t_PERIOD           = r'\.'
    t_SEMI             = r';'
    t_COLON            = r':'
    t_ELLIPSIS         = r'\.\.\.'

    # Identifiers and reserved words (so they are ignored in RE check)
    reserved_map = {r.lower(): r for r in reserved}

    def t_DUMP_SYMBOL_TABLE(self, t):
        r'!!S'

        #Note: since !!S is not token, it will not be printed for DEBUG_TOKENS.
        self.table_logger.symbol_table("!!S encountered. Symbol Table dump: " +
                            str(self.compiler_state.symbol_table))

    def t_PRINT_DEBUG_MESSAGE(self, t):
        r'!!P(.*)!'
        # This allows us to use "!!P(this is a debug message)!" in code we test and have the message printed
        message = t.value
        message = message.replace('!!P(', '').replace(')!', '')
        print(message)

    # Debug symbol that will produce a token that can force productions to be completed
    def t_FORCE_COMPLETIONS(self, t):
        r'!!F'

    # debug symbol that produce clone of symbol table in its currents state
    def t_CLONE_SYMBOL_TABLE(self, t):
        r'!!C'

        self.compiler_state.clone_symbol_table_on_scope_exit = True

        # # print message saying table will be cloned and print original table
        # self.st_logger.symbol_table('!!C encountered. Table is clonning.')
        # self.st_logger.symbol_table("Original Table")
        # self.st_logger.symbol_table(str(self.compiler_state.symbol_table))
        # self.st_logger.symbol_table('\n')
        #
        # # clone table and print cloned table
        # cloned = self.compiler_state.symbol_table.clone()
        # self.st_logger.symbol_table("Cloned Table")
        # self.st_logger.symbol_table(str(cloned))
        # self.st_logger.symbol_table('\n')
        #
        # # add cloned to list of cloned
        # self.compiler_state.cloned_tables.append(cloned)

    # NOTE: \w is equivalent to [A-Za-z0-9]
    def t_ID(self, t):
        r'[A-Za-z_][\w_]*'

        reserved_word = self.reserved_map.get(t.value, None)
        if reserved_word is not None:
            t.type = reserved_word
        elif self.compiler_state.symbol_table.find_type(t.value):
            t.type = 'TYPEID'
        else:
            t.type = 'ID'
        return t

    # Floating literal
    def t_FCONST(self, t):
        r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

        if Lexer.string_to_float_fails(t.value):
            raise Exception("Specified constant float value ({}) is unacceptable.".format(t.value))

        t.value = float(t.value)
        return t

    # Integer literal
    def t_ICONST(self, t):
        r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

        if Lexer.string_to_int_fails(t.value):
            raise Exception("Specified constant integer value ({}) is unacceptable".format(t.value))

        t.value = int(t.value)
        return t

    # Character constant 'c' or L'c'
    def t_CCONST(self, t):
        r'(L)?\'([^\\\n]|(\\.))*?\''

        t.value = t.value.replace("'", "")
        t.value = ord(t.value)
        return t

    # String literal
    t_SCONST = r'\"(\\.|[^\\\"])*\"'  # r'\"([^\\\n]|(\\.))*?\"'


    # SHOULD NOW BE HANDLED IN ID STUFF
    # NOTE: Enumeration Constant
    #       For now this should be used as ID instead - and a error will be pointed out in parser
    #t_ECONST = r''

    # SHOULD NOW BE HANDLED IN ID STUFF
    # NOTE: Typedef name ( TypeID )
    #       For now this should be used as ID instead - and a error will be pointed out in parser
    #t_TYPEID = r''

    # Comments
    def t_comment(self, t):
        r' (/\*(.|\n)*?\*/)|(//.*\n)'
        t.lineno += t.value.count('\n')

    # Preprocessor directive (ignored)
    def t_preprocessor(self, t):
        r'\#(.)*?\n'
        t.lineno += 1

    def t_error(self, t):
        self.token_logger.token("Illegal Character in input: {}".format(t.value))
        raise CompileError('Illegal token: ' + t.value, t.lineno, t.column, self.compiler_state.source_code[t.lineno])

    @staticmethod
    def string_to_int_fails(value):
        int_representation = int(value)
        if int_representation >= 0:
            return ((2 * sys.maxsize) + 1) < int_representation
        else:
            return int_representation < -sys.maxsize - 1

    @staticmethod
    def string_to_float_fails(value):
        float_representation = float(value)
        return (float_representation == float("inf") or float_representation == -float("inf"))

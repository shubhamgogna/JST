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

import ply.lex as lex
import sys
from symbol_table.symbol import Symbol


class Lexer(object):
    # NOTE:  These aren't the S and L debug things that Harris had
    #             Not sure how to set debugging for symbol table...
    NO_DEBUG = 0
    DEBUG_TOKENS = 1
    DEBUG_SOURCE_CODE = 2
    DEBUG_SOURCE_AND_TOKENS = 3

    # to keep track of current source code line
    CURRENT_LINE_START = 0

    # to keep track of file name for the token and symbol table files
    TOKEN_FILE = "scanner_dump_tokens.txt"
    SYMBOL_TABLE_FILE = "scanner_dump_symbol_table.txt"

    # need to add in a possible token file name is option -o is given
    def __init__(self, symbol_table=None, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.symbol_table = symbol_table

        # have to add in way to change debug level based on input?
        self.debug_level =  Lexer.DEBUG_SOURCE_AND_TOKENS

        # if no -o option, default to stdout for now, will need to change this later.
        if Lexer.TOKEN_FILE == None:
            self.dout = sys.stdout
        else:
            self.dout = open(Lexer.TOKEN_FILE, 'w')

        # open file for symbol table dubugging dumps
        self.symbolout = open(Lexer.SYMBOL_TABLE_FILE, 'w')


    def input(self, data):
        self.lexer.input(data)

    def token(self):
        token = self.lexer.token()
        if token != None:
            self.debug_out_tokens(token.type, token.value)
            #self.CURRENT_LINE_START = self.CURRENT_LINE_START + len(token.value)
            #print(self.CURRENT_LINE_START)
        return token

    def debug_out_tokens(self,tok_type, tok_value):
        # Confirm with Terence the way of doing this?
        if self.debug_level == Lexer.DEBUG_TOKENS or self.debug_level == Lexer.DEBUG_SOURCE_AND_TOKENS:
            self.dout.write(str(tok_type) + ' ' + str(tok_value) + '\n')

    def debug_out_source(self,message):
        # Confirm with Terence the way of doing this?

        if self.debug_level == Lexer.DEBUG_SOURCE_CODE or self.debug_level == Lexer.DEBUG_SOURCE_AND_TOKENS:
            self.dout.write('\nSource Code: ' + '\n' + message + '\n-----\n\n')

    def print_source_debug(self):
        source_code = self.lexer.lexdata
        current_ln = ''
        i = self.CURRENT_LINE_START
        t = source_code[i]

        # output of source code ignores block comments
        if t + source_code[i+1] != '/*' and t != '\n':
            while t != '\n':
               current_ln = current_ln + t
               i = i+1
               t = source_code[i]
            self.debug_out_source(current_ln)

    def print_source_line(self):
        source_code = self.lexer.lexdata
        current_ln = ''
        i = self.CURRENT_LINE_START
        t = source_code[i]
        while t != '\n':
           current_ln = current_ln + t
           i = i+1
           t = source_code[i]
        sys.stderr.write(current_ln + '\n')

        spacing = ''
        for i in range(0, (self.lexer.lexpos - self.lexer.current - 1)):
            spacing = spacing + ' '
        sys.stderr.write( spacing + '^\n')

    @staticmethod
    def does_int_overflow(value):
        int_representation = int(value)
        if int_representation >= 0:
            return int_representation <= ((2 * sys.maxsize) + 1), int_representation
        else:
            return int_representation > -sys.maxsize - 1

    @staticmethod
    def float_is_acceptable(value):
        float_representation = float(value)
        return not (float_representation == float("inf") or float_representation == -float("inf"))

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
        'RANGE',

        # Need to include error token for warning issues?
        'ERROR'
        )

    # Completely ignored characters
    t_ignore           = ' \t\x0c'

    # Newlines
    def t_NEWLINE(self, t):
        r'\n+'

        #Note: Newline is not a token and thus will not be printed for DEBUG_TOKENS

        # Handle writing source code line
        self.print_source_debug()

        # reset current line start
        self.CURRENT_LINE_START = t.lexer.lexpos

        # deal with line and col numbers
        t.lexer.lineno += t.value.count("\n")
        t.lexer.current = t.lexer.lexpos -1

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
    t_XOREQUAL         = r'^='

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

    def t_LBRACE(self,t):
        r'\{'
        self.symbolout.write("Opening brace encountered, symbol table dumped: \n")
        #self.symbolout.write(self.symbol_table)
        self.symbolout.write('\n')
        return t

    def t_RBRACE(self,t):
        r'\}'
        self.symbolout.write("Closing brace encountered, symbol table dumped: \n")
        #self.symbolout.write(self.symbol_table)
        self.symbolout.write('\n')
        return t

    t_COMMA            = r','
    t_PERIOD           = r'\.'
    t_SEMI             = r';'
    t_COLON            = r':'
    t_ELLIPSIS         = r'\.\.\.'

    # Identifiers and reserved words (so they are ignored in RE check)
    reserved_map = {r.lower(): r for r in reserved}
    # for r in reserved:
    #     reserved_map[r.lower()] = r



    def t_DUMP_SYMBOl_TABLE(self, t):
        r'!!S'
        #Note: since !!S is not token, it will not be printed for DEBUG_TOKENS.
        self.symbolout.write("!!S encountered, symbol table dumped: \n")
        #self.symbolout.write(self.symbol_table)
        self.symbolout.write('\n')


    # NOTE: \w is equivalent to [A-Za-z0-9]
    def t_ID(self, t):
        r'[A-Za-z_][\w_]*'
        t.type = self.reserved_map.get(t.value,"ID")

        if t.type is not "ID":
            return t.type

        inserting = False  # TODO: add driver class, use the flag in the driver
        if inserting:
            symbol = Symbol(t.value)
            result = self.symbol_table.insert(symbol)
            if result is "SHADOWED":
                raise NotImplemented("Do shit about shadowing")
            elif result is "EXISTS":
                raise Exception("Redeclaration of {} not allowed.".format(t.value))
            
            return symbol
        else:
            symbol = self.symbol_table.find(t.value)
            if symbol is None:
                raise Exception("{} was not declared in this scope.".format(t.value))
            return symbol

    # Integer literal
    def t_ICONST(self, t):
        r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
        # if self.check_overflow(t.value):
        #     t.type = self.reserved_map.get(t.value,"ERROR")
        #     self.t_error(t)

        if Lexer.does_int_overflow(t.value[0]):
            raise Exception("Specified constant integer value ({}) unacceptable".format(t.value[0]))
        return t

    # Floating literal
    t_FCONST = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

    # String literal
    t_SCONST = r'\"([^\\\n]|(\\.))*?\"'

    # Character constant 'c' or L'c'
    t_CCONST = r'(L)?\'([^\\\n]|(\\.))*?\''

    # NOTE: Enumeration Constant
    #       For now this should be used as ID instead - and a error will be pointed out in parser
    #t_ECONST = r''

    # NOTE: Typedef name ( TypeID )
    #       For now this should be used as ID instead - and a error will be pointed out in parser
    #t_TYPEID = r''

    # Comments
    def t_comment(self, t):
        r' /\*(.|\n)*?\*/'
        t.lineno += t.value.count('\n')

    # Preprocessor directive (ignored)
    def t_preprocessor(self, t):
        r'\#(.)*?\n'
        t.lineno += 1

    def t_error(self, t):
        # Note: Will need to change to actual error token later perhaps??
        raise Exception('Illegal character: ' + t.value[0])

        self.debug_out_tokens(t.type, t.value[0])
        sys.stderr.write('ERROR: line ' + str(t.lexer.lineno) + ', column: ' + str(t.lexer.lexpos - t.lexer.current) + '\n' )
        sys.stderr.write("Illegal character %s \n" % repr(t.value[0]))
        self.print_source_line()
        t.lexer.skip(1)


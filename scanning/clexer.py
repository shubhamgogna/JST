# This file is part of Parser.
#
# Parser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Parser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
import ply.lex as lex
import sys

class Lexer(object):


    # NOTE:  These aren't the S and L debug things that Harris had
    #             Not sure how to set debugging for symbol table...
    NO_DEBUG = 0
    DEBUG_TOKENS = 1
    DEBUG_SOURCE_CODE = 2
    DEBGUG_SOURCE_AND_TOKENS = 3

    # to keep track of current source code line
    CURRENT_LINE_START = 0

    # to keep track of file name for the token file
    TOKEN_FILE = "tokens.txt"

    # need to add in a possible token file name is option -o is given
    def __init__(self, symbol_table=None, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.symbol_table = symbol_table


        # have to add in way to change debug level based on input?
        self.debug_level =  Lexer.DEBUG_TOKENS

        # if no -o option, default to stdout for now, will need to change later.
        if Lexer.TOKEN_FILE == None:
            self.dout = sys.stdout
        else:
            self.dout = open(Lexer.TOKEN_FILE, 'w')

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
        if self.debug_level == Lexer.DEBUG_TOKENS or self.debug_level == Lexer.DEBGUG_SOURCE_AND_TOKENS:
            self.dout.write(str(tok_type) + ' ' + str(tok_value) + '\n')

    def debug_out_source(self,message):
        # Confirm with Terence the way of doing this?
        if self.debug_level == Lexer.DEBUG_SOURCE_CODE or self.debug_level == Lexer.DEBGUG_SOURCE_AND_TOKENS:
            self.dout.write(message + '\n')

    def print_source_debug(self):
        source_code = self.lexer.lexdata
        current_ln = ''
        i = self.CURRENT_LINE_START
        t = source_code[i]

        # output of source code ignores block comments
        if t + source_code[i+1] != '/*':
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
        print(current_ln)

        spacing = ''
        for i in range(0, (self.lexer.lexpos - self.lexer.current - 1)):
            spacing = spacing + ' '
        print( spacing + '^')
        



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
    t_LBRACE           = r'\{'
    t_RBRACE           = r'\}'
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
        print(self.symbol_table)


    # NOTE: \w is equivalent to [A-Za-z0-9]
    def t_ID(self, t):
        r'[A-Za-z_][\w_]*'
        t.type = self.reserved_map.get(t.value,"ID")
        return t

    # Integer literal
    t_ICONST = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

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
        print('ERROR: line ' + str(t.lexer.lineno) + ', column: ' + str(t.lexer.lexpos - t.lexer.current)  )
        print("Illegal character %s" % repr(t.value[0]))
        self.print_source_line()    
        t.lexer.skip(1)





# import sys

# from clexer import Lexer

# # Testing!!!!!!
# lexer = Lexer() 

# data = '''
# /* The "hello world" program in C
# Date written 2/12/5

# 사랑해
# */

# '''

# lexer.input(data)
# while True:
#   tok = lexer.token()
#   if not tok:
#     break
#   print(tok)
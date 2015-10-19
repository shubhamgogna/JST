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
from loggers.logger import Logger

class Lexer(object):

    # to keep track of current source code line
    CURRENT_LINE_START = 0

    def __init__(self, compiler_state=None, print_tokens=True, print_source=True, print_table=True, st_filename = 'scanner_dump_symbol_table.txt', tok_filename = 'scanner_dump_tokens.txt', **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

        self.compiler_state = compiler_state

        # set up loggers based on debug flags
        if st_filename not in {sys.stdout, sys.stderr}:
             st_file = open(st_filename, 'w')
        else:
             st_file = st_filename
        self.st_logger = Logger(st_file)

        if tok_filename not in {sys.stdout, sys.stderr}:
            tok_file = open(tok_filename,'w')
        else:
            tok_file = tok_filename
        self.token_logger = Logger(tok_file)

        if print_table is True:
            self.st_logger.add_switch(Logger.INFO)

        if print_tokens is True:
            self.token_logger.add_switch(Logger.TOKEN)

        if print_source is True:
            self.token_logger.add_switch(Logger.SOURCE)

        self.last_token = None

    def teardown(self):
        self.token_logger.finalize()
        self.st_logger.finalize()

    def input(self, data):
        self.lexer.input(data)

    def token(self):
        self.last_token = self.lexer.token()
        if self.last_token != None:
            self.debug_out_tokens(self.last_token.type, self.last_token.value)

        # TODO: make line/position stuff nicer with something like this
        # self.last_token.lineno -= 1
        # self.last_token.lexpos = Lexer.getColumnFromLexPos(self.last_token.lexpos)

        return self.last_token

    def debug_out_tokens(self,tok_type, tok_value):
        self.token_logger.token(str(tok_type) + ' ' + str(tok_value) + '\n')

    def debug_out_source(self):
        source_code = self.lexer.lexdata
        current_ln = ''
        i = self.CURRENT_LINE_START
        t = source_code[i]

        if t + source_code[i+1] != '/*' and t != '\n':
            while t != '\n':
                current_ln = current_ln + t
                i = i+1
                t = source_code[i]
            # print source to token file
            self.token_logger.source('\nSource Code: ' + '\n' + current_ln + '\n-----\n\n')
            # add source to compiler state
            self.compiler_state.source_code.append(current_ln)

    # print source code to stderr for illegal tokens
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
        #'ERROR'  # TODO: if we decide we want the parser to handle all errors/error reporting this will be good
                 # TODO: otherwise let's toss it (I'm in favor of passing all errors to the parser for unified
                 # TODO: error management, but it will take some figuring out. -Terence)
        )

    # Completely ignored characters
    t_ignore           = ' \t\x0c'

    # Newlines
    def t_NEWLINE(self, t):
        r'\n+'

        #Note: Newline is not a token and thus will not be printed for DEBUG_TOKENS

        # Handle writing source code line
        self.debug_out_source()

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

    def t_LBRACE(self,t):
        r'\{'
        self.st_logger.info("Opening brace encountered, symbol table dumped: \n")
        self.st_logger.info(str(self.compiler_state.symbol_table))
        self.st_logger.info('\n')
        return t

    def t_RBRACE(self,t):
        r'\}'
        self.st_logger.info("Closing brace encountered, symbol table dumped: \n")
        self.st_logger.info(str(self.compiler_state.symbol_table))
        self.st_logger.info('\n')
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
        self.st_logger.info("!!S encountered, symbol table dumped: \n")
        self.st_logger.info(str(self.compiler_state.symbol_table))
        self.st_logger.info('\n')

    def t_PRINT_DEBUG_MESSAGE(self, t):
        r'!!P(.*)!'
        # This allows us to use "!!P(this is a debug message)!" in code we test and have the message printed
        message = t.value
        message = message.replace('!!P(', '').replace(')!', '')
        print(message)


    # Debug symbol that will produce a token that can force productions to be completed
    def t_FORCE_COMPLETIONS(self,t):
        r'!!F'


    # debug symbol that produce clone of symbol table in its currents state
    def t_CLONE_SYMBOL_TABLE(self,t):
        r'!!C'

        # print message saying table will be cloned and print original table
        self.st_logger.info('!!C encountered. Table is clonning.')
        self.st_logger.info("Original Table")
        self.st_logger.info(str(self.compiler_state.symbol_table))
        self.st_logger.info('\n')

        # clone table and print cloned table
        cloned = self.compiler_state.symbol_table.clone()
        self.st_logger.info("Cloned Table")
        self.st_logger.info(str(cloned))
        self.st_logger.info('\n')

        # add cloned to list of cloned
        self.compiler_state.cloned_tables.append(cloned)

    # NOTE: \w is equivalent to [A-Za-z0-9]
    def t_ID(self, t):
        r'[A-Za-z_][\w_]*'

        t.type = self.get_identifier_type(identifier=t.value)

        if t.type is "ID":
            symbol = self.compiler_state.symbol_table.find(name=t.value)
            if symbol is None:
                symbol = Symbol(identifier=t.value)
                self.compiler_state.symbol_table.insert(symbol)
            t.value = symbol
        elif t.type is "TYPEID":
            t.value = self.compiler_state.symbol_table.find_type(t.value)
        elif t.type is "ECONST":
            t.type = 'ECONST'
            t.value = self.compiler_state.symbol_table.find_enum_constant_value(t.value)

        return t

        # Terence:
        # Taking out the 'lookup mode' stuff here, no one else seems to use it
        #
        # if self.compiler_state is not None:  # like in the case of unit testing the lexer
        #     if self.compiler_state.insert_mode:
        #         symbol = Symbol(t.value)
        #         result = self.compiler_state.symbol_table.insert(symbol)
        #         if result is "SHADOWED":
        #             raise NotImplemented("Do shit about shadowing")
        #         elif result is "EXISTS":
        #             raise Exception("Redeclaration of {} not allowed.".format(t.value))
        #
        #         t.value = symbol
        #     else:
        #         symbol = self.compiler_state.symbol_table.find(t.value)
        #         if symbol is None:
        #             raise Exception("{} was not declared in this scope.".format(t.value))
        #         t.value = symbol
        #
        # return t

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

    # String literal
    t_SCONST = r'\"([^\\\n]|(\\.))*?\"'

    # Character constant 'c' or L'c'
    t_CCONST = r'(L)?\'([^\\\n]|(\\.))*?\''

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
        # Note: Will need to change to actual error token later perhaps??
        raise Exception('Illegal character: ' + t.value[0])

        self.debug_out_tokens(t.type, t.value[0])
        sys.stderr.write('ERROR: line ' + str(t.lexer.lineno) + ', column: ' + str(t.lexer.lexpos - t.lexer.current) + '\n' )
        sys.stderr.write("Illegal character %s \n" % repr(t.value[0]))
        self.print_source_line()
        t.lexer.skip(1)

    def get_identifier_type(self, identifier):
        keyword_value = self.reserved_map.get(identifier, None)
        typedef_name = self.compiler_state.symbol_table.find_type(identifier)
        enum_value = self.compiler_state.symbol_table.find_enum_constant_value(identifier)

        if keyword_value is not None:
            return keyword_value
        elif typedef_name is not None:
            return 'TYPEID'
        elif enum_value is not None:
            return 'ECONST'
        else:
            return 'ID'

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

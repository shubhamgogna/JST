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

import ply.yacc as yacc
import sys

from loggers.logger import Logger
from scanning.clexer import Lexer
from symbol_table.symbol import Symbol, PointerDeclaration, TypeDeclaration, ConstantValue


class Parser(object):
    DEFAULT_PRODUCTION_DUMP_FILE = 'parsing_dump_productions.txt'

    def __init__(self, compiler_state, lexer=None, print_productions=True, print_source=True, print_info=True,
                 prod_filename=sys.stdout, **kwargs):
        self.compiler_state = compiler_state

        if lexer is None:
            lexer = Lexer(compiler_state)
        self.lexer = lexer
        self.tokens = lexer.tokens

        self.parser = yacc.yacc(module=self, start='translation_unit')

        # set up loggers based on debug flags
        if prod_filename not in {sys.stdout, sys.stderr}:
            prod_file = open(prod_filename, 'w')
        else:
            prod_file = prod_filename
        self.prod_logger = Logger(prod_file)

        if print_productions is True:
            self.prod_logger.add_switch(Logger.PRODUCTION)

        if print_source is True:
            self.prod_logger.add_switch(Logger.SOURCE)

        if print_info is True:
            self.prod_logger.add_switch(Logger.INFO)


    def teardown(self):
        self.prod_logger.finalize()

    def parse(self, data):
        parse_result = self.parser.parse(input=data, lexer=self.lexer)

        if self.compiler_state.clone_symbol_table_on_scope_exit:
            self.prod_logger.info('cloning the symbol table')
            self.compiler_state.cloned_tables.append(self.compiler_state.symbol_table.clone())
            self.compiler_state.clone_symbol_table_on_scope_exit = False

        return parse_result

    #
    # p_error
    #
    def p_error(self, t):
        print('--- ERROR ---')
        print('Last token: {}'.format(self.lexer.last_token))

        self.prod_logger.implement_me("p_error")
        raise NotImplemented("p_error")

    #
    # translation-unit:
    #
    def p_translation_unit(self, t):
        """translation_unit : translation_unit_opt"""
        self.prod_logger.production('translation_unit -> translation_unit_opt')

    def p_translation_unit_1(self, t):
        """translation_unit_opt : external_declaration"""
        self.prod_logger.production('translation_unit_1 -> external_declaration')

    def p_translation_unit_2(self, t):
        """translation_unit_opt : translation_unit external_declaration"""
        self.prod_logger.production('translation_unit_2 -> translation_unit external_declaration')

    #
    # external-declaration:
    #
    def p_external_declaration_1(self, t):
        """external_declaration : function_definition"""
        self.prod_logger.production('external_declaration -> function_definition')

    def p_external_declaration_2(self, t):
        """external_declaration : declaration"""
        self.prod_logger.production('external_declaration -> declaration')

    #
    # function-definition:
    #
    def p_function_definition_1(self, t):
        """function_definition : declaration_specifiers declarator declaration_list compound_statement"""
        self.prod_logger.production(
            'function_definition -> declaration_specifiers declarator declaration_list compound_statement')

    def p_function_definition_2(self, t):
        """function_definition : declarator declaration_list compound_statement"""
        self.prod_logger.production('function_definition -> declarator declaration_list compound_statement')

    def p_function_definition_3(self, t):
        """function_definition : declarator compound_statement"""
        self.prod_logger.production('function_definition -> declarator declaration_list compound_statement')

    def p_function_definition_4(self, t):
        """function_definition : declaration_specifiers declarator compound_statement"""
        self.prod_logger.production('function_definition -> declaration_specifiers declarator compound_statement')

        declarator = t[2]
        declarator.type = t[1]
        declarator.add_compound_statements(t[3])

        # t[2]['direct_declarator'].set_as_function(t[1], t[2]['parameter_type_list'], t[3])
        # t[2].type = t[1]
        # t[]
    #
    # declaration:
    #
    def p_declaration_1(self, t):
        """declaration : declaration_specifiers init_declarator_list SEMI"""
        self.prod_logger.production('declaration -> declaration_specifiers init_declarator_list SEMI')

        init_declarator_list = t[2]
        declaration_specifiers = t[1]

        for init_declarator in init_declarator_list:
            init_declarator['declarator'].set_as_variable(declaration_specifiers)

    def p_declaration_2(self, t):
        """declaration : declaration_specifiers SEMI"""
        self.prod_logger.production('declaration -> declaration_specifiers SEMI')

    #
    # declaration-list:
    #
    def p_declaration_list_1(self, t):
        """declaration_list : declaration"""
        self.prod_logger.production('declaration_list -> declaration')

    def p_declaration_list_2(self, t):
        """
        declaration_list : declaration_list declaration
        """
        self.prod_logger.production('declaration_list -> declaration_list declaration')

    #
    # declaration-specifiers
    #
    def p_declaration_specifiers_1(self, t):
        """
        declaration_specifiers : storage_class_specifier declaration_specifiers
        """
        self.prod_logger.production('declaration_specifiers -> storage_class_specifier declaration_specifiers')

        t[2].add_storage_class(t[1])
        t[0] = t[2]

    def p_declaration_specifiers_2(self, t):
        """
        declaration_specifiers : type_specifier declaration_specifiers
        """
        self.prod_logger.production('declaration_specifiers -> type_specifier declaration_specifiers')

        t[2].add_type_specifier(t[1])
        t[0] = t[2]

    def p_declaration_specifiers_3(self, t):
        """
        declaration_specifiers : type_qualifier declaration_specifiers
        """
        self.prod_logger.production('declaration_specifiers -> type_qualifier declaration_specifiers')

        t[2].add_qualifier(t[1])
        t[0] = t[2]

    def p_declaration_specifiers_4(self, t):
        """
        declaration_specifiers : storage_class_specifier
        """
        self.prod_logger.production('declaration_specifiers -> storage_class_specifier')

        t[0] = TypeDeclaration()
        t[0].add_storage_class(t[1])

    def p_declaration_specifiers_5(self, t):
        """
        declaration_specifiers : type_specifier
        """
        self.prod_logger.production('declaration_specifiers -> type_specifier')

        t[0] = TypeDeclaration()
        t[0].add_type_specifier(t[1])

    def p_declaration_specifiers_6(self, t):
        """
        declaration_specifiers : type_qualifier
        """
        self.prod_logger.production('declaration_specifiers -> type_qualifier')

        t[0] = TypeDeclaration()
        t[0].add_qualifier(t[1])

    #
    # storage-class-specifier
    #
    def p_storage_class_specifier_auto(self, t):
        """storage_class_specifier : AUTO"""
        self.prod_logger.production('storage_class_specifier -> AUTO')

        t[0] = t[1]

    def p_storage_class_specifie_register(self, t):
        """storage_class_specifier : REGISTER"""
        self.prod_logger.production('storage_class_specifier -> REGISTER')

        t[0] = t[1]

    def p_storage_class_specifier_static(self, t):
        """storage_class_specifier : STATIC"""
        self.prod_logger.production('storage_class_specifier -> STATIC')

        t[0] = t[1]

    def p_storage_class_specifier_extern(self, t):
        """storage_class_specifier : EXTERN"""
        self.prod_logger.production('storage_class_specifier -> EXTERN')

        t[0] = t[1]

    def p_storage_class_specifier_typedef(self, t):
        """storage_class_specifier : TYPEDEF"""
        self.prod_logger.production('storage_class_specifier -> TYPEDEF')

        t[0] = t[1]

    #
    # type-specifier:
    #
    def p_type_specifier_void(self, t):
        """
        type_specifier : VOID
        """
        self.prod_logger.production('type_specifier -> VOID')

        t[0] = 'void'

    def p_type_specifier_char(self, t):
        """
        type_specifier : CHAR
        """
        self.prod_logger.production('type_specifier -> CHAR')

        t[0] = 'char'

    def p_type_specifier_short(self, t):
        """
        type_specifier : SHORT
        """
        self.prod_logger.production('type_specifier -> SHORT')

        t[0] = 'short'

    def p_type_specifier_int(self, t):
        """
        type_specifier : INT
        """
        self.prod_logger.production('type_specifier -> INT')

        t[0] = 'int'

    def p_type_specifier_long(self, t):
        """
        type_specifier : LONG
        """
        self.prod_logger.production('type_specifier -> LONG')

        t[0] = 'long'

    def p_type_specifier_float(self, t):
        """
        type_specifier : FLOAT
        """
        self.prod_logger.production('type_specifier -> FLOAT')

        t[0] = 'float'

    def p_type_specifier_double(self, t):
        """
        type_specifier : DOUBLE
        """
        self.prod_logger.production('type_specifier -> DOUBLE')

        t[0] = 'double'

    def p_type_specifier_signed(self, t):
        """
        type_specifier : SIGNED
        """
        self.prod_logger.production('type_specifier -> SIGNED')

        t[0] = 'signed'

    def p_type_specifier_unsigned(self, t):
        """
        type_specifier : UNSIGNED
        """
        self.prod_logger.production('type_specifier -> UNSIGNED')

        t[0] = 'unsigned'

    def p_type_specifier_struct_or_union(self, t):
        """
        type_specifier : struct_or_union_specifier
        """
        self.prod_logger.production('type_specifier -> struct_or_union_specifier')

        t[0] = t[1]

    def p_type_specifier_enum(self, t):
        """
        type_specifier : enum_specifier
        """
        self.prod_logger.production('type_specifier -> enum_specifier')

        t[0] = t[1]

    def p_type_specifier_typeid(self, t):
        """
        type_specifier : TYPEID
        """
        self.prod_logger.production('type_specifier -> TYPEID')

        t[0] = t[1]

    #
    # type-qualifier:
    #
    def p_type_qualifier_const(self, t):
        """type_qualifier : CONST"""
        self.prod_logger.production('type_qualifier -> CONST')

        t[0] = t[1]

    def p_type_qualifier_volatile(self, t):
        """type_qualifier : VOLATILE"""
        self.prod_logger.production('type_qualifier -> VOLATILE')

        t[0] = t[1]

    #
    # struct-or-union-specifier
    #
    def p_struct_or_union_specifier_1(self, t):
        """struct_or_union_specifier : struct_or_union identifier LBRACE struct_declaration_list RBRACE"""
        self.prod_logger.production(
            'struct_or_union_specifier : struct_or_union identifier LBRACE struct_declaration_list RBRACE')

        if t[1] is "struct":
            t[2].add_struct_members(t[4])
        elif t[1] is "union":
            t[2].add_union_members(t[4])

        t[0] = t[2]

    def p_struct_or_union_specifier_2(self, t):
        """
        struct_or_union_specifier : struct_or_union LBRACE struct_declaration_list RBRACE
        """
        self.prod_logger.production('struct_or_union_specifier : struct_or_union LBRACE struct_declaration_list RBRACE')

        raise NotImplemented('p_struct_or_union_specifier_2; how to do anonymous struct?')

    def p_struct_or_union_specifier_3(self, t):
        """
        struct_or_union_specifier : struct_or_union identifier
        """
        self.prod_logger.production('struct_or_union_specifier : struct_or_union identifier')

    #
    # struct-or-union:
    #
    def p_struct_or_union_struct(self, t):
        """struct_or_union : STRUCT"""
        self.prod_logger.production('struct_or_union -> STRUCT')

        t[0] = t[1]

    def p_struct_or_union_union(self, t):
        """struct_or_union : UNION"""
        self.prod_logger.production('struct_or_union -> UNION')

        t[0] = t[1]

    #
    # struct-declaration-list:
    #
    def p_struct_declaration_list_1(self, t):
        """struct_declaration_list : struct_declaration"""
        self.prod_logger.production('struct_declaration_list : struct_declaration')

        t[0] = [t[1]]

    def p_struct_declaration_list_2(self, t):
        """struct_declaration_list : struct_declaration_list struct_declaration"""
        # I changed 'struct_declarator_list' to 'struct_declaration_list'
        self.prod_logger.production('struct_declaration_list : struct_declaration_list struct_declaration')

        t[0] = t[1] + t[2]

    #
    # init-declarator-list:
    #
    def p_init_declarator_list_1(self, t):
        """
        init_declarator_list : init_declarator
        """
        self.prod_logger.production('init_declarator_list -> init_declarator')

        t[0] = [t[1]]

    def p_init_declarator_list_2(self, t):
        """
        init_declarator_list : init_declarator_list COMMA init_declarator
        """
        self.prod_logger.production('init_declarator_list -> init_declarator_list COMMA init_declarator')

        # Concat the new init_declarator to the existing list
        t[0] = t[1] + [t[3]]

    #
    # init-declarator
    #
    def p_init_declarator_1(self, t):
        """
        init_declarator : declarator
        """
        self.prod_logger.production('init_declarator -> declarator')

        t[0] = {"declarator": t[1], "initializer": None}

    def p_init_declarator_2(self, t):
        """init_declarator : declarator EQUALS initializer"""
        self.prod_logger.production('init_declarator : declarator EQUALS initializer')

        t[0] = {"declarator": t[1], "initializer": t[3]}

    #
    # struct-declaration:
    #
    def p_struct_declaration(self, t):
        """struct_declaration : specifier_qualifier_list struct_declarator_list SEMI"""
        self.prod_logger.production('struct_declaration : specifier_qualifier_list struct_declarator_list SEMI')

    #
    # specifier-qualifier-list:
    #
    def p_specifier_qualifier_list_1(self, t):
        """specifier_qualifier_list : type_specifier specifier_qualifier_list"""
        self.prod_logger.production('specifier_qualifier_list : type_specifier specifier_qualifier_list')

    def p_specifier_qualifier_list_2(self, t):
        """specifier_qualifier_list : type_specifier"""
        self.prod_logger.production('specifier_qualifier_list -> type_specifier')

    def p_specifier_qualifier_list_3(self, t):
        """specifier_qualifier_list : type_qualifier specifier_qualifier_list"""
        self.prod_logger.production('specifier_qualifier_list -> type_qualifier specifier_qualifier_list')

    def p_specifier_qualifier_list_4(self, t):
        """specifier_qualifier_list : type_qualifier"""
        self.prod_logger.production('specifier_qualifier_list -> type_qualifier')

    #
    # struct-declarator-list:
    #
    def p_struct_declarator_list_1(self, t):
        """struct_declarator_list : struct_declarator"""
        self.prod_logger.production('struct_declarator_list -> struct_declarator')

    def p_struct_declarator_list_2(self, t):
        """struct_declarator_list : struct_declarator_list COMMA struct_declarator"""
        self.prod_logger.production('struct_declarator_list -> struct_declarator_list COMMA struct_declarator')

    #
    # struct-declarator:
    #
    def p_struct_declarator_1(self, t):
        """struct_declarator : declarator"""
        self.prod_logger.production('struct_declarator -> declarator')

    def p_struct_declarator_2(self, t):
        """struct_declarator : declarator COLON constant_expression"""
        self.prod_logger.production('struct_declarator -> declarator COLON constant_expression')

    def p_struct_declarator_3(self, t):
        """struct_declarator : COLON constant_expression"""
        self.prod_logger.production('struct_declarator -> COLON constant_expression')

    #
    # enum-specifier:
    #
    def p_enum_specifier_1(self, t):
        """enum_specifier : ENUM identifier LBRACE enumerator_list RBRACE"""
        self.prod_logger.production('enum_specifier -> ENUM identifier LBRACE enumerator_list RBRACE')

        t[2].is_enum = True
        t[2].add_enum_members(t[4])
        t[0] = t[2]

    def p_enum_specifier_2(self, t):
        """enum_specifier : ENUM LBRACE enumerator_list RBRACE"""
        self.prod_logger.production('enum_specifier -> ENUM LBRACE enumerator_list RBRACE')

        raise NotImplemented('p_enum_specifier_2; how to do anonymous enum?')

    def p_enum_specifier_3(self, t):
        """enum_specifier : ENUM identifier"""
        self.prod_logger.production('enum_specifier -> ENUM identifier')

        t[2].is_enum = True
        t[0] = t[2]

    #
    # enumerator_list:
    #
    def p_enumerator_list_1(self, t):
        """enumerator_list : enumerator"""
        self.prod_logger.production('enumerator_list -> enumerator')

        t[0] = t[1]

    def p_enumerator_list_2(self, t):
        """enumerator_list : enumerator_list COMMA enumerator"""
        self.prod_logger.production('enumerator_list -> enumerator_list COMMA enumerator')

        t[0] = t[1].append_enum_member(t[3])

    #
    # enumerator:
    #
    def p_enumerator_1(self, t):
        """enumerator : identifier"""
        self.prod_logger.production('enumerator -> identifier')

        t[0] = t[1].set_constant_value(-1)  # TODO: create an enum value ticket counter

    def p_enumerator_2(self, t):
        """enumerator : identifier EQUALS constant_expression"""
        self.prod_logger.production('enumerator -> identifier EQUALS constant_expression')

        t[0] = t[1].set_constant_value(int(t[3][1]))  # t[3] should be a tuple like (value, type)
        # not checking for negativity, we can allow negative values for enums
        # TODO: create an enum value ticket counter

    #
    # declarator:
    #
    def p_declarator_1(self, t):
        """
        declarator : pointer direct_declarator
        """
        self.prod_logger.production('declarator -> pointer direct_declarator')

        t[2].add_pointer_level(t[1])
        t[0] = t[2]

    def p_declarator_2(self, t):
        """
        declarator : direct_declarator
        """
        self.prod_logger.production('declarator -> direct_declarator')

        t[0] = t[1]

    #
    # direct-declarator:
    #
    def p_direct_declarator_1(self, t):
        """
        direct_declarator : identifier
        """
        self.prod_logger.production('direct_declarator -> identifier')

        t[0] = t[1]  # whatever the declaration, it should have been built up by now

    def p_direct_declarator_2(self, t):
        """direct_declarator : LPAREN declarator RPAREN"""
        self.prod_logger.production('direct_declarator : LPAREN declarator RPAREN')

        t[0] = t[1]  # declarator should have been initialized by the time it gets here

    def p_direct_declarator_3(self, t):
        """
        direct_declarator : direct_declarator LBRACKET constant_expression_option RBRACKET
        """
        self.prod_logger.production(
            'direct_declarator -> direct_declarator LBRACKET constant_expression_option RBRACKET')

        if issubclass(type(t[3]), ConstantValue) and t[3].type == 'int':
            t[1].add_array_dimension(t[3].value)  # TODO validate?
        elif t[3] is None:
            t[1].add_array_dimension(Symbol.EMPTY_ARRAY_DIM)
        else:
            raise Exception(
                'Only integral types may be used to specify array dimensions ({} given)'.format(t[3].type))

        t[0] = t[1]

    def p_direct_declarator_4(self, t):
        """direct_declarator : direct_declarator LPAREN parameter_type_list RPAREN"""
        self.prod_logger.production('direct_declarator : direct_declarator LPAREN parameter_type_list RPAREN')

        direct_declarator = t[1]

        print(direct_declarator, type(direct_declarator), 'line 620')

        parameter_type_list = t[3]
        direct_declarator.add_parameters(parameter_type_list)
        t[0] = direct_declarator

        # # TODO LPAREN is kind of the start of a scope
        # t[0] = {'direct_declarator': t[1], 'parameter_type_list': t[3]}

    def p_direct_declarator_5(self, t):
        """direct_declarator : direct_declarator LPAREN identifier_list RPAREN"""
        self.prod_logger.production('direct_declarator : direct_declarator LPAREN identifier_list RPAREN')

        t[0] = t[1].add_parameters(t[3])

    def p_direct_declarator_6(self, t):
        """direct_declarator : direct_declarator LPAREN RPAREN"""
        self.prod_logger.production('direct_declarator : direct_declarator LPAREN RPAREN')

        direct_declarator = t[1]
        direct_declarator.is_function = True
        t[0] = direct_declarator
        # t[0] = {'direct_declarator': t[1], 'parameter_type_list': []}

    #
    # pointer:
    #
    def p_pointer_1(self, t):
        """
        pointer : TIMES type_qualifier_list
        """
        self.prod_logger.production('pointer -> TIMES type_qualifier_list')

        pointer_declaration = PointerDeclaration()
        pointer_declaration.add_qualifiers(t[2])
        t[0] = [pointer_declaration]

    def p_pointer_2(self, t):
        """
        pointer : TIMES
        """
        self.prod_logger.production('pointer -> TIMES')

        t[0] = [PointerDeclaration()]

    def p_pointer_3(self, t):
        """
        pointer : TIMES type_qualifier_list pointer
        """
        self.prod_logger.production('pointer -> TIMES type_qualifier_list pointer')

        first_pointer = PointerDeclaration()
        first_pointer.add_qualifiers(t[2])

        t[0] = [first_pointer] + t[3]

    def p_pointer_4(self, t):
        """
        pointer : TIMES pointer
        """
        self.prod_logger.production('pointer -> TIMES pointer')

        t[0] = [PointerDeclaration()] + t[2]

    #
    # type-qualifier-list:
    #
    def p_type_qualifier_list_1(self, t):
        """type_qualifier_list : type_qualifier"""
        self.prod_logger.production('type_qualifier_list : type_qualifier')

    def p_type_qualifier_list_2(self, t):
        """type_qualifier_list : type_qualifier_list type_qualifier"""
        self.prod_logger.production('type_qualifier_list : type_qualifier_list type_qualifier')

    #
    # parameter-type-list:
    #
    def p_parameter_type_list_1(self, t):
        """parameter_type_list : parameter_list"""
        self.prod_logger.production('parameter_type_list : parameter_list')

        t[0] = t[1]

    def p_parameter_type_list_2(self, t):
        """parameter_type_list : parameter_list COMMA ELLIPSIS"""
        self.prod_logger.production('parameter_type_list : parameter_list COMMA ELLIPSIS')

    #
    # parameter-list:
    #
    def p_parameter_list_1(self, t):
        """parameter_list : parameter_declaration"""
        self.prod_logger.production('parameter_list : parameter_declaration')

        t[0] = [t[1]]

    def p_parameter_list_2(self, t):
        """parameter_list : parameter_list COMMA parameter_declaration"""
        self.prod_logger.production('parameter_list : parameter_list COMMA parameter_declaration')

        t[0] = t[1] + [t[3]]

    #
    # parameter-declaration:
    #
    def p_parameter_declaration_1(self, t):
        """parameter_declaration : declaration_specifiers declarator"""
        self.prod_logger.production('parameter_declaration : declaration_specifiers declarator')

        t[2].type = t[1]
        t[0] = t[2]

    def p_parameter_declaration_2(self, t):
        """parameter_declaration : declaration_specifiers abstract_declarator_option"""
        self.prod_logger.production('parameter_declaration : declaration_specifiers abstract_declarator_option')

    #
    # identifier-list:
    #
    def p_identifier_list_1(self, t):
        """identifier_list : identifier"""
        self.prod_logger.production('identifier_list : identifier')

        t[0] = [t[1]]  # this begins the list parameter in the production below

    def p_identifier_list_2(self, t):
        """identifier_list : identifier_list COMMA identifier"""
        self.prod_logger.production('identifier_list : identifier_list COMMA identifier')

        t[0] = t[1].append(t[3])

    #
    # initializer:
    #
    def p_initializer_1(self, t):
        """initializer : assignment_expression"""
        self.prod_logger.production('initializer : assignment_expression')

    def p_initializer_2(self, t):
        """initializer : LBRACE initializer_list RBRACE"""
        self.prod_logger.production('initializer : LBRACE initializer_list RBRACE')

    def p_initializer_3(self, t):
        """initializer : LBRACE initializer_list COMMA RBRACE"""
        self.prod_logger.production('initializer : LBRACE initializer_list COMMA RBRACE')

    #
    # initializer-list:
    #
    def p_initializer_list_1(self, t):
        """initializer_list : initializer"""
        self.prod_logger.production('initializer_list : initializer')

    def p_initializer_list_2(self, t):
        """initializer_list : initializer_list COMMA initializer"""
        self.prod_logger.production('initializer_list : initializer_list COMMA initializer')

    #
    # type-name:
    #
    def p_type_name(self, t):
        """type_name : specifier_qualifier_list abstract_declarator_option"""
        self.prod_logger.production('type_name : specifier_qualifier_list abstract_declarator_option')

    def p_abstract_declarator_option_1(self, t):
        """abstract_declarator_option : empty"""
        self.prod_logger.production('abstract_declarator_option : empty')

    def p_abstract_declarator_option_2(self, t):
        """abstract_declarator_option : abstract_declarator"""
        self.prod_logger.production('abstract_declarator_option : abstract_declarator')

    #
    # abstract-declarator:
    #
    def p_abstract_declarator_1(self, t):
        """abstract_declarator : pointer"""
        self.prod_logger.production('abstract_declarator : pointer')

    def p_abstract_declarator_2(self, t):
        """abstract_declarator : pointer direct_abstract_declarator"""
        self.prod_logger.production('abstract_declarator : pointer direct_abstract_declarator')

    def p_abstract_declarator_3(self, t):
        """abstract_declarator : direct_abstract_declarator"""
        self.prod_logger.production('abstract_declarator : direct_abstract_declarator')

    #
    # direct-abstract-declarator:
    #
    def p_direct_abstract_declarator_1(self, t):
        """direct_abstract_declarator : LPAREN abstract_declarator RPAREN"""
        self.prod_logger.production('direct_abstract_declarator : LPAREN abstract_declarator RPAREN')

    def p_direct_abstract_declarator_2(self, t):
        """direct_abstract_declarator : direct_abstract_declarator LBRACKET constant_expression_option RBRACKET"""
        self.prod_logger.production(
            'direct_abstract_declarator : direct_abstract_declarator LBRACKET constant_expression_option RBRACKET')

    def p_direct_abstract_declarator_3(self, t):
        """direct_abstract_declarator : LBRACKET constant_expression_option RBRACKET"""
        self.prod_logger.production('direct_abstract_declarator : LBRACKET constant_expression_option RBRACKET')

    def p_direct_abstract_declarator_4(self, t):
        """direct_abstract_declarator : direct_abstract_declarator LPAREN parameter_type_list_option RPAREN"""
        self.prod_logger.production(
            'direct_abstract_declarator : direct_abstract_declarator LPAREN parameter_type_list_option RPAREN')

    def p_direct_abstract_declarator_5(self, t):
        """direct_abstract_declarator : LPAREN parameter_type_list_option RPAREN"""
        self.prod_logger.production('direct_abstract_declarator : LPAREN parameter_type_list_option RPAREN')

    #
    # Optional fields in abstract declarators
    #
    def p_constant_expression_option_1(self, t):
        """constant_expression_option : empty"""
        self.prod_logger.production('constant_expression_option : empty')

        t[0] = None

    def p_constant_expression_option_2(self, t):
        """constant_expression_option : constant_expression"""
        self.prod_logger.production('constant_expression_option : constant_expression')

        t[0] = t[1]

    def p_parameter_type_list_option_1(self, t):
        """parameter_type_list_option : empty"""
        self.prod_logger.production('parameter_type_list_option : empty')

    def p_parameter_type_list_option_2(self, t):
        """parameter_type_list_option : parameter_type_list"""
        self.prod_logger.production('parameter_type_list_option : parameter_type_list')

    #
    # statement:
    #
    def p_statement_labeled(self, t):
        """statement : labeled_statement"""
        self.prod_logger.production('statement -> labeled_statement')

    def p_statement_expression(self, t):
        """statement : expression_statement"""
        self.prod_logger.production('statement -> expression_statment')

    def p_statement_compound(self, t):
        """statement : compound_statement"""
        self.prod_logger.production('statement -> compound_statement')

    def p_statement_selection(self, t):
        """statement : selection_statement"""
        self.prod_logger.production('statement ->selection_statement')

    def p_statement_iteration(self, t):
        """
        statement : iteration_statement
        """
        self.prod_logger.production('statement ->iteration_statement')

    def p_statement_jump(self, t):
        """
        statement : jump_statement
        """
        self.prod_logger.production('statement -> jump_statement')

    #
    # labeled-statement:
    #
    def p_labeled_statement_1(self, t):
        """
        labeled_statement : identifier COLON statement
        """
        self.prod_logger.production('labeled_statement : identifier COLON statement')

    def p_labeled_statement_2(self, t):
        """
        labeled_statement : CASE constant_expression COLON statement
        """
        self.prod_logger.production('labeled_statement : CASE constant_expression COLON statement')

    def p_labeled_statement_3(self, t):
        """
        labeled_statement : DEFAULT COLON statement
        """
        self.prod_logger.production('labeled_statement : DEFAULT COLON statement')

    #
    # expression-statement:
    #
    def p_expression_statement(self, t):
        """
        expression_statement : expression_option SEMI
        """
        self.prod_logger.production('expression_statement : expression_option SEMI')

    #
    # compound-statement:
    #
    def p_compound_statement_1(self, t):
        """
        compound_statement : LBRACE enter_scope insert_mode declaration_list lookup_mode statement_list leave_scope RBRACE
        """
        self.prod_logger.production('compound_statement : LBRACE declaration_list statement_list RBRACE')

    def p_compound_statement_2(self, t):
        """
        compound_statement : LBRACE enter_scope lookup_mode statement_list leave_scope RBRACE
        """
        self.prod_logger.production('compound_statement : LBRACE statement_list RBRACE')

    def p_compound_statement_3(self, t):
        """
        compound_statement : LBRACE enter_scope insert_mode declaration_list lookup_mode leave_scope RBRACE
        """
        self.prod_logger.production('compound_statement : LBRACE declaration_list RBRACE')

    def p_compound_statement_4(self, t):
        """
        compound_statement : LBRACE RBRACE
        """
        self.prod_logger.production('compound_statement : LBRACE RBRACE')

    #
    # statement-list:
    #
    def p_statement_list_1(self, t):
        """
        statement_list : statement
        """
        self.prod_logger.production('statement_list : statement')

    def p_statement_list_2(self, t):
        """
        statement_list : statement_list statement
        """
        self.prod_logger.production('statement_list : statement_list statement')

    #
    # selection-statement
    #
    def p_selection_statement_1(self, t):
        """
        selection_statement : IF LPAREN expression RPAREN statement
        """
        self.prod_logger.production('selection_statement : IF LPAREN expression RPAREN statement')

    def p_selection_statement_2(self, t):
        """
        selection_statement : IF LPAREN expression RPAREN statement ELSE statement
        """
        self.prod_logger.production('selection_statement : IF LPAREN expression RPAREN statement ELSE statement')

    def p_selection_statement_3(self, t):
        """
        selection_statement : SWITCH LPAREN expression RPAREN statement
        """
        self.prod_logger.production('selection_statement : SWITCH LPAREN expression RPAREN statement')

    #
    # iteration_statement:
    #
    def p_iteration_statement_1(self, t):
        """
        iteration_statement : WHILE LPAREN expression RPAREN statement
        """
        self.prod_logger.production('iteration_statement : WHILE LPAREN expression RPAREN statement')

    def p_iteration_statement_2(self, t):
        """
        iteration_statement : FOR LPAREN expression_option SEMI expression_option SEMI expression_option RPAREN statement
        """
        self.prod_logger.production(
            'iteration_statement -> FOR LPAREN expression_option SEMI expression_option SEMI expression_option RPAREN '
            'statement')

    def p_iteration_statement_3(self, t):
        """
        iteration_statement : DO statement WHILE LPAREN expression RPAREN SEMI
        """
        self.prod_logger.production('iteration_statement -> DO statement WHILE LPAREN expression RPAREN SEMI')

    #
    # jump_statement:
    #
    def p_jump_statement_1(self, t):
        """
        jump_statement : GOTO identifier SEMI
        """
        self.prod_logger.production('jump_statement -> GOTO identifier SEMI')

    def p_jump_statement_2(self, t):
        """
        jump_statement : CONTINUE SEMI
        """
        self.prod_logger.production('jump_statement -> CONTINUE SEMI')

    def p_jump_statement_3(self, t):
        """
        jump_statement : BREAK SEMI
        """
        self.prod_logger.production('jump_statement -> BREAK SEMI')

    def p_jump_statement_4(self, t):
        """
        jump_statement : RETURN expression_option SEMI
        """
        self.prod_logger.production('jump_statement : RETURN expression_option SEMI')

    def p_expression_option_1(self, t):
        """
        expression_option : empty
        """
        self.prod_logger.production('empty')

    def p_expression_option_2(self, t):
        """
        expression_option : expression
        """
        self.prod_logger.production('expression_option -> expression')

    #
    # expression:
    #
    def p_expression_1(self, t):
        """
        expression : assignment_expression
        """
        self.prod_logger.production('expression : assignment_expression')

    def p_expression_2(self, t):
        """
        expression : expression COMMA assignment_expression
        """
        self.prod_logger.production('expression : expression COMMA assignment_expression')

    #
    # assigment_expression:
    #
    def p_assignment_expression_1(self, t):
        """
        assignment_expression : conditional_expression
        """
        self.prod_logger.production('assignment_expression : conditional_expression')

    def p_assignment_expression_2(self, t):
        """
        assignment_expression : unary_expression assignment_operator assignment_expression
        """
        self.prod_logger.production(
            'assignment_expression : unary_expression assignment_operator assignment_expression')

    #
    # assignment_operator:
    #
    def p_assignment_operator_equals(self, t):
        """assignment_operator : EQUALS
        """
        self.prod_logger.production('assignment_operator -> EQUALS')

    def p_assignment_operator_times(self, t):
        """assignment_operator : TIMESEQUAL
        """
        self.prod_logger.production('assignment_operator -> TIMESEQUAL')

    def p_assignment_operator_div(self, t):
        """assignment_operator : DIVEQUAL"""
        self.prod_logger.production('assignment_operator -> DIVEQUAL')

    def p_assignment_operator_mod(self, t):
        """assignment_operator : MODEQUAL
        """
        self.prod_logger.production('assignment_operator -> MODEQUAL')

    def p_assignment_operator_plus(self, t):
        """assignment_operator : PLUSEQUAL
        """
        self.prod_logger.production('assignment_operator -> PLUSEQUAL')

    def p_assignment_operator_minus(self, t):
        """assignment_operator : MINUSEQUAL
        """
        self.prod_logger.production('assignment_operator -> MINUSEQUAL')

    def p_assignment_operator_left_shift(self, t):
        """assignment_operator : LSHIFTEQUAL
        """
        self.prod_logger.production('assignment_operator -> LSHIFTEQUAL')

    def p_assignment_operator_right_shift(self, t):
        """assignment_operator : RSHIFTEQUAL
        """
        self.prod_logger.production('assignment_operator -> RSHIFTEQUAL')

    def p_assignment_operator_and(self, t):
        """assignment_operator : ANDEQUAL
        """
        self.prod_logger.production('assignment_operator -> ANDEQUAL')

    def p_assignment_operator_or(self, t):
        """assignment_operator : OREQUAL
        """
        self.prod_logger.production('assignment_operator -> OREQUAL')

    def p_assignment_operator_xor(self, t):
        """
        assignment_operator : XOREQUAL
        """
        self.prod_logger.production('assignment_operator -> XOREQUAL')

    #
    # conditional-expression
    #
    def p_conditional_expression_1(self, t):
        """
        conditional_expression : logical_or_expression
        """
        self.prod_logger.production('conditional_expression -> logical_or_expression')

        t[0] = t[1]

    def p_conditional_expression_2(self, t):
        """
        conditional_expression : logical_or_expression CONDOP expression COLON conditional_expression
        """
        self.prod_logger.production(
            'conditional_expression : logical_or_expression CONDOP expression COLON conditional_expression')

    #
    # constant-expression
    #
    def p_constant_expression(self, t):
        """
        constant_expression : conditional_expression
        """
        self.prod_logger.production('constant_expression -> conditional_expression')

        t[0] = t[1]

    #
    # logical-or-expression
    #
    def p_logical_or_expression_1(self, t):
        """
        logical_or_expression : logical_and_expression
        """
        self.prod_logger.production('logical_or_expression -> logical_and_expression')

        t[0] = t[1]

    def p_logical_or_expression_2(self, t):
        """logical_or_expression : logical_or_expression LOR logical_and_expression
        """
        self.prod_logger.production('logical_or_expression : logical_or_expression LOR logical_and_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = {"value": 1 if t[1] != 0 or t[2] != 0 else 0, "type": 'int'}
        else:
            # TODO: implement this via AST Nodes
            t[0] = None



    #
    # logical_and_expression
    #
    def p_logical_and_expression_1(self, t):
        """logical_and_expression : inclusive_or_expression
        """
        self.prod_logger.production('logical_and_expression -> inclusive_or_expression')

        t[0] = t[1]

    def p_logical_and_expression_2(self, t):
        """
        logical_and_expression : logical_and_expression LAND inclusive_or_expression
        """
        self.prod_logger.production('logical_and_expression -> logical_and_expression LAND inclusive_or_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = {"value": 0 if t[1] == 0 or t[2] == 0 else 1, "type": 'int'}
        else:
            # TODO: implement this via AST Nodes
            t[0] = None



    #
    # inclusive-or-expression:
    #
    def p_inclusive_or_expression_1(self, t):
        """
        inclusive_or_expression : exclusive_or_expression
        """
        self.prod_logger.production('inclusive_or_expression -> exclusive_or_expression')

        t[0] = t[1]

    def p_inclusive_or_expression_2(self, t):
        """
        inclusive_or_expression : inclusive_or_expression OR exclusive_or_expression
        """
        self.prod_logger.production('inclusive_or_expression -> inclusive_or_expression OR exclusive_or_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = Parser.perform_constant_expression_bitwise_operation(t[1], '|', t[3])
        else:
            # TODO: implement this via AST Nodes
            t[0] = None



    #
    # exclusive-or-expression:
    #
    def p_exclusive_or_expression_1(self, t):
        """
        exclusive_or_expression :  and_expression
        """
        self.prod_logger.production('exclusive_or_expression -> and_expression')

        t[0] = t[1]

    def p_exclusive_or_expression_2(self, t):
        """
        exclusive_or_expression :  exclusive_or_expression XOR and_expression
        """
        self.prod_logger.production('exclusive_or_expression -> exclusive_or_expression XOR and_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = Parser.perform_constant_expression_bitwise_operation(t[1], '^', t[3])
        else:
            # TODO: implement this via AST Nodes
            t[0] = None


    #
    # and_expression
    #
    def p_and_expression_1(self, t):
        """
        and_expression : equality_expression
        """
        self.prod_logger.production('and_expression -> equality_expression')

        t[0] = t[1]

    def p_and_expression_2(self, t):
        """
        and_expression : and_expression AND equality_expression
        """
        self.prod_logger.production('and_expression -> and_expression AND equality_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = Parser.perform_constant_expression_bitwise_operation(t[1], '&', t[3])
        else:
            # TODO: implement this via AST Nodes
            t[0] = None


    #
    # equality_expression:
    #
    def p_equality_expression_1(self, t):
        """equality_expression : relational_expression
        """
        self.prod_logger.production('equality_expression -> relational_expression')

        t[0] = t[1]

    def p_equality_expression_2(self, t):
        """
        equality_expression : equality_expression EQ relational_expression
        """
        self.prod_logger.production('equality_expression -> equality_expression EQ relational_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = ConstantValue(t[1].value == t[3].value, 'int')
        else:
            # TODO: implement this via AST Nodes
            t[0] = None


    def p_equality_expression_3(self, t):
        """
        equality_expression : equality_expression NE relational_expression
        """
        self.prod_logger.production('equality_expression -> equality_expression NE relational_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = ConstantValue(t[1].value != t[3].value, 'int')
        else:
            # TODO: implement this via AST Nodes
            t[0] = None



    #
    # relational-expression:
    #
    def p_relational_expression_1(self, t):
        """
        relational_expression : shift_expression
        """
        self.prod_logger.production('relational_expression -> shift_expression')

        t[0] = t[1]

    def p_relational_expression_2(self, t):
        """
        relational_expression : relational_expression LT shift_expression
        """
        self.prod_logger.production('relational_expression -> relational_expression LT shift_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = ConstantValue(t[1].value < t[3].value, 'int')
        else:
            # TODO: implement this via AST Nodes
            t[0] = None


    def p_relational_expression_3(self, t):
        """relational_expression : relational_expression GT shift_expression
        """
        self.prod_logger.production('relational_expression : relational_expression GT shift_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = ConstantValue(t[1].value > t[3].value, 'int')
        else:
            # TODO: implement this via AST Nodes
            t[0] = None



    def p_relational_expression_4(self, t):
        """relational_expression : relational_expression LE shift_expression
        """
        self.prod_logger.production('relational_expression -> relational_expression LE shift_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = ConstantValue(t[1].value <= t[3].value, 'int')
        else:
            # TODO: implement this via AST Nodes
            t[0] = None



    def p_relational_expression_5(self, t):
        """
        relational_expression : relational_expression GE shift_expression
        """
        self.prod_logger.production('relational_expression -> relational_expression GE shift_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = {"value": t[1]['value'] >= t[3]['value'], "type": 'int'}
        else:
            # TODO: implement this via AST Nodes
            t[0] = None



    #
    # shift-expression
    #
    def p_shift_expression_1(self, t):
        """shift_expression : additive_expression
        """
        self.prod_logger.production('shift_expression -> additive_expression')

        t[0] = t[1]

    def p_shift_expression_2(self, t):
        """
        shift_expression : shift_expression LSHIFT additive_expression
        """
        self.prod_logger.production('shift_expression -> shift_expression LSHIFT additive_expression')

        # t[0] = Parser.perform_constant_expression_bitwise_operation(t[1], '<<', t[3])

    def p_shift_expression_3(self, t):
        """shift_expression : shift_expression RSHIFT additive_expression
        """
        self.prod_logger.production('shift_expression -> shift_expression RSHIFT additive_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = Parser.perform_constant_expression_bitwise_operation(t[1], '>>', t[3])
        else:
            # TODO: implement this via AST Nodes
            t[0] = None



    #
    # additive-expression
    #
    def p_additive_expression_1(self, t):
        """
        additive_expression : multiplicative_expression
        """
        self.prod_logger.production('additive_expression -> multiplicative_expression')

        t[0] = t[1]

    def p_additive_expression_2(self, t):
        """
        additive_expression : additive_expression PLUS multiplicative_expression
        """
        self.prod_logger.production('additive_expression -> additive_expression PLUS multiplicative_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = ConstantValue(t[1].value + t[3].value, type=Parser.get_promoted_type(t[1].type, t[3].type))
        else:
            # TODO: implement this via AST Nodes
            t[0] = None



    def p_additive_expression_3(self, t):
        """
        additive_expression : additive_expression MINUS multiplicative_expression
        """
        self.prod_logger.production('additive_expression -> additive_expression MINUS multiplicative_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = {"value": t[1]["value"] - t[3]["value"], "type": Parser.get_promoted_type(t[1]["type"], t[3]["type"])}
        else:
            # TODO: implement this via AST Nodes
            t[0] = None

    #
    # multiplicative_expression
    #
    def p_multiplicative_expression_1(self, t):
        """
        multiplicative_expression : cast_expression
        """
        self.prod_logger.production('multiplicative_expression -> cast_expression')

        t[0] = t[1]

    def p_multiplicative_expression_2(self, t):
        """
        multiplicative_expression : multiplicative_expression TIMES cast_expression
        """
        self.prod_logger.production('multiplicative_expression -> multiplicative_expression TIMES cast_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = Parser.perform_constant_expression_arithmetic(t[1], '*', t[3])
        else:
            # TODO: implement this via AST Nodes
            t[0] = None

    def p_multiplicative_expression_3(self, t):
        """
        multiplicative_expression : multiplicative_expression DIVIDE cast_expression
        """
        self.prod_logger.production('multiplicative_expression -> multiplicative_expression DIVIDE cast_expression')

        if Parser.both_are_constant_numbers(t[1], t[3]):
            t[0] = Parser.perform_constant_expression_arithmetic(t[1], '/', t[3])
        else:
            # TODO: implement this via AST Nodes
            t[0] = None



    def p_multiplicative_expression_4(self, t):
        """
        multiplicative_expression : multiplicative_expression MOD cast_expression
        """
        self.prod_logger.production('multiplicative_expression -> multiplicative_expression MOD cast_expression')


        t[0] = Parser.perform_constant_expression_arithmetic(t[1], '%', t[3])

    #
    # cast_expression:
    #
    def p_cast_expression_1(self, t):
        """
        cast_expression : unary_expression
        """
        self.prod_logger.production('cast_expression -> unary_expression')

        t[0] = t[1]

    def p_cast_expression_2(self, t):
        """
        cast_expression : LPAREN type_name RPAREN cast_expression
        """
        self.prod_logger.production('cast_expression -> LPAREN type_name RPAREN cast_expression')

    #
    # unary_expression:
    #
    def p_unary_expression_1(self, t):
        """
        unary_expression : postfix_expression
        """
        self.prod_logger.production('unary_expression -> postfix_expression')

        t[0] = t[1]

    def p_unary_expression_2(self, t):
        """
        unary_expression : PLUSPLUS unary_expression
        """
        self.prod_logger.production('unary_expression -> PLUSPLUS unary_expression')

    def p_unary_expression_3(self, t):
        """
        unary_expression : MINUSMINUS unary_expression
        """
        self.prod_logger.production('unary_expression -> MINUSMINUS unary_expression')

    def p_unary_expression_4(self, t):
        """
        unary_expression : unary_operator cast_expression
        """
        self.prod_logger.production('unary_expression -> unary_operator cast_expression')

    def p_unary_expression_5(self, t):
        """
        unary_expression : SIZEOF unary_expression
        """
        self.prod_logger.production('unary_expression -> SIZEOF unary_expression')

    def p_unary_expression_6(self, t):
        """
        unary_expression : SIZEOF LPAREN type_name RPAREN
        """
        self.prod_logger.production('unary_expression -> SIZEOF LPAREN type_name RPAREN')

    #
    # unary_operator
    #
    def p_unary_operator_and(self, t):
        """
        unary_operator : AND
        """
        self.prod_logger.production('unary_operator -> AND')

    def p_unary_operator_times(self, t):
        """
        unary_operator : TIMES
        """
        self.prod_logger.production('unary_operator -> TIMES')

    def p_unary_operator_plus(self, t):
        """unary_operator : PLUS
        """
        self.prod_logger.production('unary_operator -> PLUS')

    def p_unary_operator_minus(self, t):
        """unary_operator : MINUS
        """
        self.prod_logger.production('unary_operator -> MINUS')

    def p_unary_operator_not(self, t):
        """unary_operator : NOT
        """
        self.prod_logger.production('unary_operator -> NOT')

    def p_unary_operator_lnot(self, t):
        """
        unary_operator : LNOT
        """
        self.prod_logger.production('unary_operator -> LNOT')

    #
    # postfix_expression:
    #
    def p_postfix_expression_1(self, t):
        """
        postfix_expression : primary_expression
        """
        self.prod_logger.production('postfix_expression -> primary_expression')

        t[0] = t[1]

    def p_postfix_expression_2(self, t):
        """
        postfix_expression : postfix_expression LBRACKET expression RBRACKET
        """
        self.prod_logger.production('postfix_expression -> postfix_expression LBRACKET expression RBRACKET')

    def p_postfix_expression_3(self, t):
        """
        postfix_expression : postfix_expression LPAREN argument_expression_list RPAREN
        """
        self.prod_logger.production('postfix_expression -> postfix_expression LPAREN argument_expression_list RPAREN')

    def p_postfix_expression_4(self, t):
        """
        postfix_expression : postfix_expression LPAREN RPAREN
        """
        self.prod_logger.production('postfix_expression -> postfix_expression LPAREN RPAREN')

    def p_postfix_expression_5(self, t):
        """
        postfix_expression : postfix_expression PERIOD identifier
        """
        self.prod_logger.production('postfix_expression -> postfix_expression PERIOD identifier')

    def p_postfix_expression_6(self, t):
        """
        postfix_expression : postfix_expression ARROW identifier
        """
        self.prod_logger.production('postfix_expression -> postfix_expression ARROW identifier')

    def p_postfix_expression_7(self, t):
        """
        postfix_expression : postfix_expression PLUSPLUS
        """
        self.prod_logger.production('postfix_expression -> postfix_expression PLUSPLUS')

    def p_postfix_expression_8(self, t):
        """
        postfix_expression : postfix_expression MINUSMINUS
        """
        self.prod_logger.production('postfix_expression -> postfix_expression MINUSMINUS')

    #
    # primary-expression:
    #
    def p_primary_expression_identifier(self, t):
        """
        primary_expression :  identifier
        """
        self.prod_logger.production('primary_expression -> identifier')

        t[0] = t[1]

    def p_primary_expression_constant(self, t):
        """
        primary_expression : constant
        """
        self.prod_logger.production('primary_expression -> constant')

        t[0] = t[1]

    def p_primary_expression_string_literal(self, t):
        """
        primary_expression : string_literal
        """
        self.prod_logger.production('primary_expression -> string_literal_list')

        t[0] = t[1]

    def p_string_literal_fragment(self, t):
        """
        string_literal : SCONST
        """
        self.prod_logger.production('string_literal_list -> SCONST')

        t[0] = t[1]

    def p_string_literal_plus_string_literal_fragment(self, t):
        """string_literal : string_literal SCONST
        """
        self.prod_logger.production('string_literal_list -> string_literal_list SCONST')

        # concatenate the string fragments into a single string literal by trimming off the quote marks
        t[0] = t[1][:-1] + t[2][1:]

    def p_primary_expression_parenthesized(self, t):
        """primary_expression : LPAREN expression RPAREN
        """
        self.prod_logger.production('primary_expression -> LPAREN expression RPAREN')

        # a parenthesised expression evaluates to the expression itself
        t[0] = t[2]

    #
    # argument-expression-list:
    #
    def p_argument_expression_list_assignment_expression(self, t):
        """
        argument_expression_list :  assignment_expression
        """
        self.prod_logger.production('argument_expression_list ->  assignment_expression')

    def p_argument_expression_list_list_comma_expression(self, t):
        """
        argument_expression_list : argument_expression_list COMMA assignment_expression
        """
        self.prod_logger.production('argument_expression_list -> argument_expression_list COMMA assignment_expression')

    #
    # constant:
    #
    def p_constant_int(self, t):
        """
        constant : ICONST
        """
        self.prod_logger.production('constant -> ICONST')

        t[0] = ConstantValue( int(t[1]), 'int')

    def p_constant_float(self, t):
        """constant : FCONST
        """
        self.prod_logger.production('constant -> FCONST')

        t[0] = ConstantValue(float(t[1]), 'float')

    def p_constant_char(self, t):
        """constant : CCONST
        """
        self.prod_logger.production('constant -> CCONST')

        t[0] = ConstantValue(t[1], 'char')

    #
    # identifier:
    #
    def p_identifier(self, t):
        """identifier : ID
        """
        self.prod_logger.production('identifier -> ID')

        # the scanner passes a symbol reference to the parser
        t[0] = t[1]

    #
    # empty:
    #
    def p_empty(self, t):
        """empty :
        """
        pass

    #
    # dummy utility productions
    #
    def p_enter_scope(self, t):
        """
        enter_scope : empty
        """
        self.prod_logger.info('Entering new scope')

        self.compiler_state.symbol_table.push()
        self.compiler_state.most_recent_type_declaration = TypeDeclaration()

    def p_insert_mode(self, t):
        """
        insert_mode : empty
        """
        self.prod_logger.info('Entering insert mode.')

        self.compiler_state.insert_mode = True

    def p_leave_scope(self, t):
        """
        leave_scope : empty
        """
        self.prod_logger.info('Leaving a scope: {}'.format(len(self.compiler_state.symbol_table.table)))

        if self.compiler_state.clone_symbol_table_on_scope_exit:
            self.prod_logger.info('cloning the symbol table')
            self.compiler_state.cloned_tables.append(self.compiler_state.symbol_table.clone())
            self.compiler_state.clone_symbol_table_on_scope_exit = False

        self.compiler_state.symbol_table.pop()

    def p_lookup_mode(self, t):
        """
        lookup_mode : empty
        """
        self.prod_logger.info('Entering lookup mode.')

        self.insert_mode = False

        # TODO: do we need a dummy production for 'reset_current_symbol'?


    @staticmethod
    def perform_constant_expression_arithmetic(operand_1, operator, operand_2):
        if operator is '+':
            pass
        elif operator is '-':
            pass
        elif operator is '*':
            pass
        elif operator is '/':
            pass
        elif operator is '%':
            pass
        else:
            raise Exception('please provide a proper operand')

    @staticmethod
    def perform_constant_expression_bitwise_operation(operand_1, operator, operand_2=None):
        if operand_1['type'] is 'float' or operand_1['type'] is 'float':
            raise Exception("Floating point values are incompatible with bitwise operator '{}'.".format(operator))

        op_1 = operand_1['value']
        type_1 = operand_1['type']

        if operand_2:
            op_2 = operand_2['value']
            type_2 = operand_2['type']

        result = 0
        if operand_2:
            if operator is '|':
                result = op_1 | op_2
            elif operator is '&':
                result = op_1 & op_2
            elif operator is '^':
                result = op_1 ^ op_2
        elif operator is '~':
            result = ~op_1
        else:
            raise Exception('please provide a proper operand')

        return {"value": result, "type": Parser.get_promoted_type(type_1, type_2)}

    @staticmethod
    def get_promoted_type(type_1, type_2):
        if type_1 == type_2:
            return type_1
        elif (type_1 is 'int' and (type_2 is 'int' or type_2 is 'char')) or (
                        type_2 is 'int' and (type_1 is 'int' or type_1 is 'char')):
            return 'int'
        elif type_1 is 'float' or type_2 is 'float':
            return 'float'

    @staticmethod
    def both_are_constant_numbers(item_1, item_2):
        return issubclass(type(item_1), ConstantValue) and issubclass(type(item_2), ConstantValue)
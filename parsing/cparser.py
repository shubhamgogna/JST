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
from symbol_table.symbol import Symbol, PointerDeclaration, TypeDeclaration, ConstantValue


## Parser Class
#
# This class is responsible for working in tandem with the Lexer to parse the given C program input and then
# constructing the Abstract Syntax Tree that corresponds to the program. Compile time checking is done by this class.
#
class Parser(object):
    ## The constructor for a new Parser object.
    #
    # @param self The object pointer.
    # @param compiler_state The object shared between the Parser and Lexer for maintaining the state of the compiler.
    # @param lexer The lexer the parser will use to tokenize the input program. Defaults to None. If the value is
    #              None, the Parser will create its own Lexer.
    # @param print_productions A boolean flag indicating if the productions should be written as they are encountered.
    #                          Defaults to False.
    # @param print_source A boolean flag indicating if the source code for each production should be written as they
    #                     are encountered. Defaults to False.
    # @param print_info A boolean flag indicating if any logging tagged as INFO should be written. Defaults to False.
    # @param prod_file_name The name of the file any output should be written to. Defaults to sys.stdout.
    # @param kwargs  Any keywork arguments for the PLY.yacc object.
    #
    # Outputs:
    #   A constructed instance of a Parser
    #
    # Purpose:
    #   The constructor initializes the object to be ready to do its job with the desired outputs labeled.
    #
    def __init__(self, compiler_state, lexer, **kwargs):
        if lexer is None:
            raise ValueError('No Lexer passed to Parser')

        self.compiler_state = compiler_state
        self.lexer = lexer
        self.tokens = lexer.tokens
        self.parser = yacc.yacc(module=self, start='program')
        self.prod_logger = self.compiler_state.get_parser_logger()

    ## A method to do any cleanup that can't be handled by typical garbage collection.
    #
    # @param self The object pointer.
    #
    # Output:
    #   None
    #
    # Called by method responsible for completing the use of the parser cleanly.
    # TODO: implement __exit__ method?
    #
    def teardown(self):
        self.prod_logger.finalize()

    ## Completes the action of parsing the given program and producing an AST.
    #
    # @param self The object pointer.
    # @param data The raw string that constitutes the given program.
    #
    # Output:
    #   An AST.
    #
    # Called by a program that supplies a program to parse.
    #
    def parse(self, data):
        return self.parser.parse(input=data, lexer=self.lexer, tracking=True)

    ## Operator precedences used by ply.yacc to correctly order productions that may be otherwise ambiguous.
    #
    precedence = (
            ('left', 'LOR'),
            ('left', 'LAND'),
            ('left', 'OR'),
            ('left', 'XOR'),
            ('left', 'AND'),
            ('left', 'EQ', 'NE'),
            ('left', 'GT', 'GE', 'LT', 'LE'),
            ('left', 'RSHIFT', 'LSHIFT'),
            ('left', 'PLUS', 'MINUS'),
            ('left', 'TIMES', 'DIVIDE', 'MOD')
        )

    ## From here on productions will not be documented.
    #
    # It is generally expected that the reader understands the structure of a production handling function for ply.yacc,
    # where the production(s) handled are specified in the method's docstring.
    # In general, all of the methods function in the following way.
    #
    # @param self The object pointer.
    # @param t The production object assembled by ply.yacc, used to determine which production was taken, what the
    #          values of the elements of the production are, etc.
    #
    # Output:
    #   (via the t[0] item) Any result or AST node of a production.
    #
    # These methods are strictly called only by the parser itself.
    #

    #
    # p_error
    #
    def p_error(self, t):
        print('--- ERROR ---')
        print('Last token: {}'.format(self.lexer.last_token))

        self.prod_logger.implement_me("p_error")
        raise NotImplemented("p_error")


    def p_program(self, t):
        """
        program : translation_unit leave_scope
        """
        t[0] = None

    #
    # translation-unit:
    #
    def p_translation_unit(self, t):
        """
        translation_unit : translation_unit_opt
                         | empty
        """
        self.output_production(t, production_message='translation_unit -> translation_unit_opt')

    def p_translation_unit_1(self, t):
        """
        translation_unit_opt : external_declaration
        """
        self.output_production(t, production_message='translation_unit_1 -> external_declaration')

    def p_translation_unit_2(self, t):
        """
        translation_unit_opt : translation_unit external_declaration
        """
        self.output_production(t, production_message='translation_unit_2 -> translation_unit external_declaration')

    #
    # external-declaration:
    #
    def p_external_declaration_1(self, t):
        """external_declaration : function_definition"""
        self.output_production(t, production_message='external_declaration -> function_definition')

    def p_external_declaration_2(self, t):
        """external_declaration : declaration"""
        self.output_production(t, production_message='external_declaration -> declaration')

    #
    # function-definition
    #
    def p_function_definition_1(self, t):
        """function_definition : declaration_specifiers declarator declaration_list enter_function_scope compound_statement"""
        self.output_production(t, production_message=
            'function_definition -> declaration_specifiers declarator declaration_list compound_statement')

    def p_function_definition_2(self, t):
        """function_definition : declarator declaration_list enter_function_scope compound_statement"""
        self.output_production(t, production_message='function_definition -> declarator declaration_list compound_statement')

    def p_function_definition_3(self, t):
        """function_definition : declarator enter_function_scope compound_statement"""
        self.output_production(t, production_message='function_definition -> declarator declaration_list compound_statement')

    def p_function_definition_4(self, t):
        """function_definition : declaration_specifiers declarator enter_function_scope compound_statement"""
        self.output_production(t, production_message='function_definition -> declaration_specifiers declarator compound_statement')

        declarator = t[2]
        declarator.type = t[1]
        declarator.add_compound_statements(t[4])

        # t[2]['direct_declarator'].set_as_function(t[1], t[2]['parameter_type_list'], t[3])
        # t[2].type = t[1]
        # t[]
    #
    # declaration:
    #
    def p_declaration_1(self, t):
        """declaration : declaration_specifiers init_declarator_list SEMI"""
        self.output_production(t, production_message='declaration -> declaration_specifiers init_declarator_list SEMI')

        init_declarator_list = t[2]
        declaration_specifiers = t[1]

        for init_declarator in init_declarator_list:
            init_declarator['declarator'].set_as_variable(declaration_specifiers)

    def p_declaration_2(self, t):
        """declaration : declaration_specifiers SEMI"""
        self.output_production(t, production_message='declaration -> declaration_specifiers SEMI')

    #
    # declaration-list:
    #
    def p_declaration_list_1(self, t):
        """declaration_list : declaration"""
        self.output_production(t, production_message='declaration_list -> declaration')

    def p_declaration_list_2(self, t):
        """
        declaration_list : declaration_list declaration
        """
        self.output_production(t, production_message='declaration_list -> declaration_list declaration')

    #
    # declaration-specifiers
    #
    def p_declaration_specifiers_1(self, t):
        """
        declaration_specifiers : storage_class_specifier declaration_specifiers
        """
        self.output_production(t, production_message='declaration_specifiers -> storage_class_specifier declaration_specifiers')

        t[2].add_storage_class(t[1])
        t[0] = t[2]

    def p_declaration_specifiers_2(self, t):
        """
        declaration_specifiers : type_specifier declaration_specifiers
        """
        self.output_production(t, production_message='declaration_specifiers -> type_specifier declaration_specifiers')

        t[2].add_type_specifier(t[1])
        t[0] = t[2]

    def p_declaration_specifiers_3(self, t):
        """
        declaration_specifiers : type_qualifier declaration_specifiers
        """
        self.output_production(t, production_message='declaration_specifiers -> type_qualifier declaration_specifiers')

        t[2].add_qualifier(t[1])
        t[0] = t[2]

    def p_declaration_specifiers_4(self, t):
        """
        declaration_specifiers : storage_class_specifier
        """
        self.output_production(t, production_message='declaration_specifiers -> storage_class_specifier')

        t[0] = TypeDeclaration()
        t[0].add_storage_class(t[1])

    def p_declaration_specifiers_5(self, t):
        """
        declaration_specifiers : type_specifier
        """
        self.output_production(t, production_message='declaration_specifiers -> type_specifier')

        t[0] = TypeDeclaration()
        t[0].add_type_specifier(t[1])

    def p_declaration_specifiers_6(self, t):
        """
        declaration_specifiers : type_qualifier
        """
        self.output_production(t, production_message='declaration_specifiers -> type_qualifier')

        t[0] = TypeDeclaration()
        t[0].add_qualifier(t[1])

    #
    # storage-class-specifier
    #
    def p_storage_class_specifier_auto(self, t):
        """storage_class_specifier : AUTO"""
        self.output_production(t, production_message='storage_class_specifier -> AUTO')

        t[0] = t[1]

    def p_storage_class_specifie_register(self, t):
        """storage_class_specifier : REGISTER"""
        self.output_production(t, production_message='storage_class_specifier -> REGISTER')

        t[0] = t[1]

    def p_storage_class_specifier_static(self, t):
        """storage_class_specifier : STATIC"""
        self.output_production(t, production_message='storage_class_specifier -> STATIC')

        t[0] = t[1]

    def p_storage_class_specifier_extern(self, t):
        """storage_class_specifier : EXTERN"""
        self.output_production(t, production_message='storage_class_specifier -> EXTERN')

        t[0] = t[1]

    def p_storage_class_specifier_typedef(self, t):
        """storage_class_specifier : TYPEDEF"""
        self.output_production(t, production_message='storage_class_specifier -> TYPEDEF')

        t[0] = t[1]

    #
    # type-specifier:
    #
    def p_type_specifier_void(self, t):
        """
        type_specifier : VOID
        """
        self.output_production(t, production_message='type_specifier -> VOID')

        t[0] = 'void'

    def p_type_specifier_char(self, t):
        """
        type_specifier : CHAR
        """
        self.output_production(t, production_message='type_specifier -> CHAR')

        t[0] = 'char'

    def p_type_specifier_short(self, t):
        """
        type_specifier : SHORT
        """
        self.output_production(t, production_message='type_specifier -> SHORT')

        t[0] = 'short'

    def p_type_specifier_int(self, t):
        """
        type_specifier : INT
        """
        self.output_production(t, production_message='type_specifier -> INT')

        t[0] = 'int'

    def p_type_specifier_long(self, t):
        """
        type_specifier : LONG
        """
        self.output_production(t, production_message='type_specifier -> LONG')

        t[0] = 'long'

    def p_type_specifier_float(self, t):
        """
        type_specifier : FLOAT
        """
        self.output_production(t, production_message='type_specifier -> FLOAT')

        t[0] = 'float'

    def p_type_specifier_double(self, t):
        """
        type_specifier : DOUBLE
        """
        self.output_production(t, production_message='type_specifier -> DOUBLE')

        t[0] = 'double'

    def p_type_specifier_signed(self, t):
        """
        type_specifier : SIGNED
        """
        self.output_production(t, production_message='type_specifier -> SIGNED')

        t[0] = 'signed'

    def p_type_specifier_unsigned(self, t):
        """
        type_specifier : UNSIGNED
        """
        self.output_production(t, production_message='type_specifier -> UNSIGNED')

        t[0] = 'unsigned'

    def p_type_specifier_struct_or_union(self, t):
        """
        type_specifier : struct_or_union_specifier
        """
        self.output_production(t, production_message='type_specifier -> struct_or_union_specifier')

        t[0] = t[1]

    def p_type_specifier_enum(self, t):
        """
        type_specifier : enum_specifier
        """
        self.output_production(t, production_message='type_specifier -> enum_specifier')

        t[0] = t[1]

    def p_type_specifier_typeid(self, t):
        """
        type_specifier : TYPEID
        """
        self.output_production(t, production_message='type_specifier -> TYPEID')

        t[0] = t[1]

    #
    # type-qualifier:
    #
    def p_type_qualifier_const(self, t):
        """type_qualifier : CONST"""
        self.output_production(t, production_message='type_qualifier -> CONST')

        t[0] = t[1]

    def p_type_qualifier_volatile(self, t):
        """type_qualifier : VOLATILE"""
        self.output_production(t, production_message='type_qualifier -> VOLATILE')

        t[0] = t[1]

    #
    # struct-or-union-specifier
    #
    def p_struct_or_union_specifier_1(self, t):
        """struct_or_union_specifier : struct_or_union identifier LBRACE struct_declaration_list RBRACE"""
        self.output_production(t, production_message=
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
        self.output_production(t, production_message='struct_or_union_specifier : struct_or_union LBRACE struct_declaration_list RBRACE')

        raise NotImplemented('p_struct_or_union_specifier_2; how to do anonymous struct?')

    def p_struct_or_union_specifier_3(self, t):
        """
        struct_or_union_specifier : struct_or_union identifier
        """
        self.output_production(t, production_message='struct_or_union_specifier : struct_or_union identifier')

    #
    # struct-or-union:
    #
    def p_struct_or_union_struct(self, t):
        """struct_or_union : STRUCT"""
        self.output_production(t, production_message='struct_or_union -> STRUCT')

        t[0] = t[1]

    def p_struct_or_union_union(self, t):
        """struct_or_union : UNION"""
        self.output_production(t, production_message='struct_or_union -> UNION')

        t[0] = t[1]

    #
    # struct-declaration-list:
    #
    def p_struct_declaration_list_1(self, t):
        """struct_declaration_list : struct_declaration"""
        self.output_production(t, production_message='struct_declaration_list : struct_declaration')

        t[0] = [t[1]]

    def p_struct_declaration_list_2(self, t):
        """struct_declaration_list : struct_declaration_list struct_declaration"""
        # I changed 'struct_declarator_list' to 'struct_declaration_list'
        self.output_production(t, production_message='struct_declaration_list : struct_declaration_list struct_declaration')

        t[0] = t[1] + t[2]

    #
    # init-declarator-list:
    #
    def p_init_declarator_list_1(self, t):
        """
        init_declarator_list : init_declarator
        """
        self.output_production(t, production_message='init_declarator_list -> init_declarator')

        t[0] = [t[1]]

    def p_init_declarator_list_2(self, t):
        """
        init_declarator_list : init_declarator_list COMMA init_declarator
        """
        self.output_production(t, production_message='init_declarator_list -> init_declarator_list COMMA init_declarator')

        # Concat the new init_declarator to the existing list
        t[0] = t[1] + [t[3]]

    #
    # init-declarator
    #
    def p_init_declarator_1(self, t):
        """
        init_declarator : declarator
        """
        self.output_production(t, production_message='init_declarator -> declarator')

        t[0] = {"declarator": t[1], "initializer": None}

    def p_init_declarator_2(self, t):
        """init_declarator : declarator EQUALS initializer"""
        self.output_production(t, production_message='init_declarator -> declarator EQUALS initializer')

        t[0] = {"declarator": t[1], "initializer": t[3]}

    #
    # struct-declaration:
    #
    def p_struct_declaration(self, t):
        """struct_declaration : specifier_qualifier_list struct_declarator_list SEMI"""
        self.output_production(t, production_message='struct_declaration -> specifier_qualifier_list struct_declarator_list SEMI')

    #
    # specifier-qualifier-list:
    #
    def p_specifier_qualifier_list_1(self, t):
        """specifier_qualifier_list : type_specifier specifier_qualifier_list"""
        self.output_production(t, production_message='specifier_qualifier_list -> type_specifier specifier_qualifier_list')

    def p_specifier_qualifier_list_2(self, t):
        """specifier_qualifier_list : type_specifier"""
        self.output_production(t, production_message='specifier_qualifier_list -> type_specifier')

    def p_specifier_qualifier_list_3(self, t):
        """specifier_qualifier_list : type_qualifier specifier_qualifier_list"""
        self.output_production(t, production_message='specifier_qualifier_list -> type_qualifier specifier_qualifier_list')

    def p_specifier_qualifier_list_4(self, t):
        """specifier_qualifier_list : type_qualifier"""
        self.output_production(t, production_message='specifier_qualifier_list -> type_qualifier')

    #
    # struct-declarator-list:
    #
    def p_struct_declarator_list_1(self, t):
        """struct_declarator_list : struct_declarator"""
        self.output_production(t, production_message='struct_declarator_list -> struct_declarator')

    def p_struct_declarator_list_2(self, t):
        """struct_declarator_list : struct_declarator_list COMMA struct_declarator"""
        self.output_production(t, production_message='struct_declarator_list -> struct_declarator_list COMMA struct_declarator')

    #
    # struct-declarator:
    #
    def p_struct_declarator_1(self, t):
        """struct_declarator : declarator"""
        self.output_production(t, production_message='struct_declarator -> declarator')

    def p_struct_declarator_2(self, t):
        """struct_declarator : declarator COLON constant_expression"""
        self.output_production(t, production_message='struct_declarator -> declarator COLON constant_expression')

    def p_struct_declarator_3(self, t):
        """struct_declarator : COLON constant_expression"""
        self.output_production(t, production_message='struct_declarator -> COLON constant_expression')

    #
    # enum-specifier:
    #
    def p_enum_specifier_1(self, t):
        """enum_specifier : ENUM identifier LBRACE enumerator_list RBRACE"""
        self.output_production(t, production_message='enum_specifier -> ENUM identifier LBRACE enumerator_list RBRACE')

        t[2].is_enum = True
        t[2].add_enum_members(t[4])
        t[0] = t[2]

    def p_enum_specifier_2(self, t):
        """enum_specifier : ENUM LBRACE enumerator_list RBRACE"""
        self.output_production(t, production_message='enum_specifier -> ENUM LBRACE enumerator_list RBRACE')

        raise NotImplemented('p_enum_specifier_2; how to do anonymous enum?')

    def p_enum_specifier_3(self, t):
        """enum_specifier : ENUM identifier"""
        self.output_production(t, production_message='enum_specifier -> ENUM identifier')

        t[2].is_enum = True
        t[0] = t[2]

    #
    # enumerator_list:
    #
    def p_enumerator_list_1(self, t):
        """enumerator_list : enumerator"""
        self.output_production(t, production_message='enumerator_list -> enumerator')

        t[0] = t[1]

    def p_enumerator_list_2(self, t):
        """enumerator_list : enumerator_list COMMA enumerator"""
        self.output_production(t, production_message='enumerator_list -> enumerator_list COMMA enumerator')

        t[0] = t[1].append_enum_member(t[3])

    #
    # enumerator:
    #
    def p_enumerator_1(self, t):
        """enumerator : identifier"""
        self.output_production(t, production_message='enumerator -> identifier')

        t[0] = t[1].set_constant_value(-1)  # TODO: create an enum value ticket counter

    def p_enumerator_2(self, t):
        """enumerator : identifier EQUALS constant_expression"""
        self.output_production(t, production_message='enumerator -> identifier EQUALS constant_expression')

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
        self.output_production(t, production_message='declarator -> pointer direct_declarator')

        t[2].add_pointer_level(t[1])
        t[0] = t[2]

    def p_declarator_2(self, t):
        """
        declarator : direct_declarator
        """
        self.output_production(t, production_message='declarator -> direct_declarator')

        t[0] = t[1]

    #
    # direct-declarator:
    #
    def p_direct_declarator_1(self, t):
        """
        direct_declarator : identifier
        """
        self.output_production(t, production_message='direct_declarator -> identifier')

        t[0] = t[1]  # whatever the declaration, it should have been built up by now

    def p_direct_declarator_2(self, t):
        """direct_declarator : LPAREN declarator RPAREN"""
        self.output_production(t, production_message='direct_declarator -> LPAREN declarator RPAREN')

        t[0] = t[1]  # declarator should have been initialized by the time it gets here

    def p_direct_declarator_3(self, t):
        """
        direct_declarator : direct_declarator LBRACKET constant_expression_option RBRACKET
        """
        self.output_production(t, production_message=
            'direct_declarator -> direct_declarator LBRACKET constant_expression_option RBRACKET')

        print(t[1], t[3])

        if issubclass(type(t[3]), ConstantValue) and t[3].type == 'int' or type(t[3]) is int:
            dimension = t[3].value if type(t[3]) is ConstantValue else t[3]
            t[1].add_array_dimension(dimension)  # TODO validate?
        elif t[3] is None:
            t[1].add_array_dimension(Symbol.EMPTY_ARRAY_DIM)
        else:
            raise Exception(
                'Only integral types may be used to specify array dimensions ({} given)'.format(t[3].type))

        t[0] = t[1]

    def p_direct_declarator_4(self, t):
        """direct_declarator : direct_declarator LPAREN parameter_type_list RPAREN"""
        self.output_production(t, production_message='direct_declarator -> direct_declarator LPAREN parameter_type_list RPAREN')

        direct_declarator = t[1]

        # print(direct_declarator, type(direct_declarator), 'line 620')

        parameter_type_list = t[3]
        direct_declarator.add_parameters(parameter_type_list)
        t[0] = direct_declarator

        # # TODO LPAREN is kind of the start of a scope
        # t[0] = {'direct_declarator': t[1], 'parameter_type_list': t[3]}

    def p_direct_declarator_5(self, t):
        """direct_declarator : direct_declarator LPAREN identifier_list RPAREN"""
        self.output_production(t, production_message='direct_declarator -> direct_declarator LPAREN identifier_list RPAREN')

        t[0] = t[1].add_parameters(t[3])

    def p_direct_declarator_6(self, t):
        """direct_declarator : direct_declarator LPAREN RPAREN"""
        self.output_production(t, production_message='direct_declarator -> direct_declarator LPAREN RPAREN')

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
        self.output_production(t, production_message='pointer -> TIMES type_qualifier_list')

        pointer_declaration = PointerDeclaration()
        pointer_declaration.add_qualifiers(t[2])
        t[0] = [pointer_declaration]

    def p_pointer_2(self, t):
        """
        pointer : TIMES
        """
        self.output_production(t, production_message='pointer -> TIMES')

        t[0] = [PointerDeclaration()]

    def p_pointer_3(self, t):
        """
        pointer : TIMES type_qualifier_list pointer
        """
        self.output_production(t, production_message='pointer -> TIMES type_qualifier_list pointer')

        first_pointer = PointerDeclaration()
        first_pointer.add_qualifiers(t[2])

        t[0] = [first_pointer] + t[3]

    def p_pointer_4(self, t):
        """
        pointer : TIMES pointer
        """
        self.output_production(t, production_message='pointer -> TIMES pointer')

        t[0] = [PointerDeclaration()] + t[2]

    #
    # type-qualifier-list:
    #
    def p_type_qualifier_list_1(self, t):
        """type_qualifier_list : type_qualifier"""
        self.output_production(t, production_message='type_qualifier_list -> type_qualifier')

    def p_type_qualifier_list_2(self, t):
        """type_qualifier_list : type_qualifier_list type_qualifier"""
        self.output_production(t, production_message='type_qualifier_list -> type_qualifier_list type_qualifier')

    #
    # parameter-type-list:
    #
    def p_parameter_type_list_1(self, t):
        """parameter_type_list : parameter_list"""
        self.output_production(t, production_message='parameter_type_list -> parameter_list')

        t[0] = t[1]

    def p_parameter_type_list_2(self, t):
        """parameter_type_list : parameter_list COMMA ELLIPSIS"""
        self.output_production(t, production_message='parameter_type_list -> parameter_list COMMA ELLIPSIS')

    #
    # parameter-list:
    #
    def p_parameter_list_1(self, t):
        """parameter_list : parameter_declaration"""
        self.output_production(t, production_message='parameter_list -> parameter_declaration')

        t[0] = [t[1]]

    def p_parameter_list_2(self, t):
        """parameter_list : parameter_list COMMA parameter_declaration"""
        self.output_production(t, production_message='parameter_list -> parameter_list COMMA parameter_declaration')

        t[0] = t[1] + [t[3]]

    #
    # parameter-declaration:
    #
    def p_parameter_declaration_1(self, t):
        """parameter_declaration : declaration_specifiers declarator"""
        self.output_production(t, production_message='parameter_declaration -> declaration_specifiers declarator')

        t[2].type = t[1]
        t[0] = t[2]

    def p_parameter_declaration_2(self, t):
        """parameter_declaration : declaration_specifiers abstract_declarator_option"""
        self.output_production(t, production_message='parameter_declaration -> declaration_specifiers abstract_declarator_option')

    #
    # identifier-list:
    #
    def p_identifier_list_1(self, t):
        """identifier_list : identifier"""
        self.output_production(t, production_message='identifier_list -> identifier')

        t[0] = [t[1]]  # this begins the list parameter in the production below

    def p_identifier_list_2(self, t):
        """identifier_list : identifier_list COMMA identifier"""
        self.output_production(t, production_message='identifier_list -> identifier_list COMMA identifier')

        t[0] = t[1].append(t[3])

    #
    # initializer:
    #
    def p_initializer_1(self, t):
        """
        initializer : assignment_expression
        """
        self.output_production(t, production_message='initializer -> assignment_expression')

    def p_initializer_2(self, t):
        """initializer : LBRACE initializer_list RBRACE"""
        self.output_production(t, production_message='initializer -> LBRACE initializer_list RBRACE')

    def p_initializer_3(self, t):
        """initializer : LBRACE initializer_list COMMA RBRACE"""
        self.output_production(t, production_message='initializer -> LBRACE initializer_list COMMA RBRACE')

    #
    # initializer-list:
    #
    def p_initializer_list_1(self, t):
        """initializer_list : initializer"""
        self.output_production(t, production_message='initializer_list -> initializer')

    def p_initializer_list_2(self, t):
        """initializer_list : initializer_list COMMA initializer"""
        self.output_production(t, production_message='initializer_list -> initializer_list COMMA initializer')

    #
    # type-name:
    #
    def p_type_name(self, t):
        """type_name : specifier_qualifier_list abstract_declarator_option"""
        self.output_production(t, production_message='type_name -> specifier_qualifier_list abstract_declarator_option')

    def p_abstract_declarator_option_1(self, t):
        """abstract_declarator_option : empty"""
        self.output_production(t, production_message='abstract_declarator_option -> empty')

    def p_abstract_declarator_option_2(self, t):
        """abstract_declarator_option : abstract_declarator"""
        self.output_production(t, production_message='abstract_declarator_option -> abstract_declarator')

    #
    # abstract-declarator:
    #
    def p_abstract_declarator_1(self, t):
        """abstract_declarator : pointer"""
        self.output_production(t, production_message='abstract_declarator -> pointer')

    def p_abstract_declarator_2(self, t):
        """abstract_declarator : pointer direct_abstract_declarator"""
        self.output_production(t, production_message='abstract_declarator -> pointer direct_abstract_declarator')

    def p_abstract_declarator_3(self, t):
        """abstract_declarator : direct_abstract_declarator"""
        self.output_production(t, production_message='abstract_declarator -> direct_abstract_declarator')

    #
    # direct-abstract-declarator:
    #
    def p_direct_abstract_declarator_1(self, t):
        """direct_abstract_declarator : LPAREN abstract_declarator RPAREN"""
        self.output_production(t, production_message='direct_abstract_declarator -> LPAREN abstract_declarator RPAREN')

    def p_direct_abstract_declarator_2(self, t):
        """direct_abstract_declarator : direct_abstract_declarator LBRACKET constant_expression_option RBRACKET"""
        self.output_production(t, production_message=
            'direct_abstract_declarator -> direct_abstract_declarator LBRACKET constant_expression_option RBRACKET')

    def p_direct_abstract_declarator_3(self, t):
        """direct_abstract_declarator : LBRACKET constant_expression_option RBRACKET"""
        self.output_production(t, production_message='direct_abstract_declarator -> LBRACKET constant_expression_option RBRACKET')

    def p_direct_abstract_declarator_4(self, t):
        """direct_abstract_declarator : direct_abstract_declarator LPAREN parameter_type_list_option RPAREN"""
        self.output_production(t, production_message=
            'direct_abstract_declarator -> direct_abstract_declarator LPAREN parameter_type_list_option RPAREN')

    def p_direct_abstract_declarator_5(self, t):
        """direct_abstract_declarator : LPAREN parameter_type_list_option RPAREN"""
        self.output_production(t, production_message='direct_abstract_declarator -> LPAREN parameter_type_list_option RPAREN')

    #
    # Optional fields in abstract declarators
    #
    def p_constant_expression_option_1(self, t):
        """constant_expression_option : empty"""
        self.output_production(t, production_message='constant_expression_option -> empty')

        t[0] = None

    def p_constant_expression_option_2(self, t):
        """constant_expression_option : constant_expression"""
        self.output_production(t, production_message='constant_expression_option -> constant_expression')

        t[0] = t[1]

    def p_parameter_type_list_option_1(self, t):
        """parameter_type_list_option : empty"""
        self.output_production(t, production_message='parameter_type_list_option -> empty')

    def p_parameter_type_list_option_2(self, t):
        """parameter_type_list_option : parameter_type_list"""
        self.output_production(t, production_message='parameter_type_list_option -> parameter_type_list')

    #
    # statement:
    #
    def p_statement_labeled(self, t):
        """statement : labeled_statement"""
        self.output_production(t, production_message='statement -> labeled_statement')

    def p_statement_expression(self, t):
        """statement : expression_statement"""
        self.output_production(t, production_message='statement -> expression_statment')

    def p_statement_compound(self, t):
        """statement : compound_statement"""
        self.output_production(t, production_message='statement -> compound_statement')

    def p_statement_selection(self, t):
        """statement : selection_statement"""
        self.output_production(t, production_message='statement -> selection_statement')

    def p_statement_iteration(self, t):
        """
        statement : iteration_statement
        """
        self.output_production(t, production_message='statement -> iteration_statement')

    def p_statement_jump(self, t):
        """
        statement : jump_statement
        """
        self.output_production(t, production_message='statement -> jump_statement')

    #
    # labeled-statement:
    #
    def p_labeled_statement_1(self, t):
        """
        labeled_statement : identifier COLON statement
        """
        self.output_production(t, production_message='labeled_statement -> identifier COLON statement')

    def p_labeled_statement_2(self, t):
        """
        labeled_statement : CASE constant_expression COLON statement
        """
        self.output_production(t, production_message='labeled_statement -> CASE constant_expression COLON statement')

    def p_labeled_statement_3(self, t):
        """
        labeled_statement : DEFAULT COLON statement
        """
        self.output_production(t, production_message='labeled_statement -> DEFAULT COLON statement')

    #
    # expression-statement:
    #
    def p_expression_statement(self, t):
        """
        expression_statement : expression_option SEMI
        """
        self.output_production(t, production_message='expression_statement -> expression_option SEMI')

    #
    # compound-statement:
    #
    def p_compound_statement_1(self, t):
        """
        compound_statement : LBRACE enter_scope insert_mode declaration_list lookup_mode statement_list leave_scope RBRACE
        """
        self.output_production(t, production_message='compound_statement -> LBRACE declaration_list statement_list RBRACE')

    def p_compound_statement_2(self, t):
        """
        compound_statement : LBRACE enter_scope lookup_mode statement_list leave_scope RBRACE
        """
        self.output_production(t, production_message='compound_statement -> LBRACE statement_list RBRACE')

    def p_compound_statement_3(self, t):
        """
        compound_statement : LBRACE enter_scope insert_mode declaration_list lookup_mode leave_scope RBRACE
        """
        self.output_production(t, production_message='compound_statement -> LBRACE declaration_list RBRACE')

    def p_compound_statement_4(self, t):
        """
        compound_statement : LBRACE RBRACE
        """
        self.output_production(t, production_message='compound_statement -> LBRACE RBRACE')

    #
    # statement-list:
    #
    def p_statement_list_1(self, t):
        """
        statement_list : statement
        """
        self.output_production(t, production_message='statement_list -> statement')

    def p_statement_list_2(self, t):
        """
        statement_list : statement_list statement
        """
        self.output_production(t, production_message='statement_list -> statement_list statement')

    #
    # selection-statement
    #
    def p_selection_statement_1(self, t):
        """
        selection_statement : IF LPAREN expression RPAREN statement
        """
        self.output_production(t, production_message='selection_statement -> IF LPAREN expression RPAREN statement')

    def p_selection_statement_2(self, t):
        """
        selection_statement : IF LPAREN expression RPAREN statement ELSE statement
        """
        self.output_production(t, production_message='selection_statement -> IF LPAREN expression RPAREN statement ELSE statement')

    def p_selection_statement_3(self, t):
        """
        selection_statement : SWITCH LPAREN expression RPAREN statement
        """
        self.output_production(t, production_message='selection_statement -> SWITCH LPAREN expression RPAREN statement')

    #
    # iteration_statement:
    #
    def p_iteration_statement_1(self, t):
        """
        iteration_statement : WHILE LPAREN expression RPAREN statement
        """
        self.output_production(t, production_message='iteration_statement -> WHILE LPAREN expression RPAREN statement')

    def p_iteration_statement_2(self, t):
        """
        iteration_statement : FOR LPAREN expression_option SEMI expression_option SEMI expression_option RPAREN statement
        """
        self.output_production(t, production_message=
            'iteration_statement -> FOR LPAREN expression_option SEMI expression_option SEMI expression_option RPAREN '
            'statement')

    def p_iteration_statement_3(self, t):
        """
        iteration_statement : DO statement WHILE LPAREN expression RPAREN SEMI
        """
        self.output_production(t, production_message='iteration_statement -> DO statement WHILE LPAREN expression RPAREN SEMI')

    #
    # jump_statement:
    #
    def p_jump_statement_1(self, t):
        """
        jump_statement : GOTO identifier SEMI
        """
        self.output_production(t, production_message='jump_statement -> GOTO identifier SEMI')

    def p_jump_statement_2(self, t):
        """
        jump_statement : CONTINUE SEMI
        """
        self.output_production(t, production_message='jump_statement -> CONTINUE SEMI')

    def p_jump_statement_3(self, t):
        """
        jump_statement : BREAK SEMI
        """
        self.output_production(t, production_message='jump_statement -> BREAK SEMI')

    def p_jump_statement_4(self, t):
        """
        jump_statement : RETURN expression_option SEMI
        """
        self.output_production(t, production_message='jump_statement -> RETURN expression_option SEMI')


    #
    # Expression Option
    #
    def p_expression_option_1(self, t):
        """
        expression_option : empty
        """
        self.output_production(t, production_message='expression_option -> empty')

    def p_expression_option_2(self, t):
        """
        expression_option : expression
        """
        self.output_production(t, production_message='expression_option -> expression')

    #
    # expression:
    #
    def p_expression_1(self, t):
        """
        expression : assignment_expression
        """
        self.output_production(t, production_message='expression -> assignment_expression')

    def p_expression_2(self, t):
        """
        expression : expression COMMA assignment_expression
        """
        self.output_production(t, production_message='expression -> expression COMMA assignment_expression')

    #
    # assigment_expression:
    #
    def p_assignment_expression_1(self, t):
        """
        assignment_expression : conditional_expression
        """
        self.output_production(t, production_message='assignment_expression -> conditional_expression')

    def p_assignment_expression_2(self, t):
        """
        assignment_expression : unary_expression assignment_operator assignment_expression
        """
        self.output_production(t, production_message=
            'assignment_expression -> unary_expression assignment_operator assignment_expression')

    #
    # assignment_operator:
    #
    def p_assignment_operator(self, t):
        """
        assignment_operator : EQUALS
                            | XOREQUAL
                            | TIMESEQUAL
                            | DIVEQUAL
                            | MODEQUAL
                            | PLUSEQUAL
                            | MINUSEQUAL
                            | LSHIFTEQUAL
                            | RSHIFTEQUAL
                            | ANDEQUAL
                            | OREQUAL
        """
        self.output_production(t, production_message='assignment_operator -> {}'.format(t[1]))

    #
    # constant-expression
    #
    def p_constant_expression(self, t):
        """
        constant_expression : conditional_expression
        """
        self.output_production(t, production_message='constant_expression -> conditional_expression')

        t[0] = t[1]

    #
    # conditional-expression
    #
    def p_conditional_expression_to_binary_expression(self, t):
        """
        conditional_expression : binary_expression
        """
        self.output_production(t, production_message='conditional_expression -> binary_expression')

        t[0] = t[1]

    def p_conditional_expression_to_ternary_expression(self, t):
        """
        conditional_expression : binary_expression CONDOP expression COLON conditional_expression
        """
        self.output_production(t, production_message=
            'conditional_expression -> binary_expression CONDOP expression COLON conditional_expression')

    def p_binary_expression_to_implementation(self, t):
        """
        binary_expression : binary_expression TIMES binary_expression
                          | binary_expression DIVIDE binary_expression
                          | binary_expression MOD binary_expression
                          | binary_expression PLUS binary_expression
                          | binary_expression MINUS binary_expression
                          | binary_expression RSHIFT binary_expression
                          | binary_expression LSHIFT binary_expression
                          | binary_expression LT binary_expression
                          | binary_expression LE binary_expression
                          | binary_expression GE binary_expression
                          | binary_expression GT binary_expression
                          | binary_expression EQ binary_expression
                          | binary_expression NE binary_expression
                          | binary_expression AND binary_expression
                          | binary_expression OR binary_expression
                          | binary_expression XOR binary_expression
                          | binary_expression LAND binary_expression
                          | binary_expression LOR binary_expression
        """
        self.output_production(t, production_message=
            'assignment_expression -> binary_expression {} binary_expression'.format(t[2]))

        if Parser.is_a_constant(t[1], t[3]):
            t[0] = Parser.perform_constant_expression_operation(t[1], t[2], t[3])
        else:
            # TODO: implement this via AST Nodes
            t[0] = None

    def p_binary_expression_to_cast_expression(self, t):
        """
        binary_expression : cast_expression
        """
        self.output_production(t, production_message='binary_expression -> cast_expression')


        t[0] = t[1]

    #
    # cast_expression:
    #
    def p_cast_expression_1(self, t):
        """
        cast_expression : unary_expression
        """
        self.output_production(t, production_message='cast_expression -> unary_expression')

        t[0] = t[1]

    def p_cast_expression_2(self, t):
        """
        cast_expression : LPAREN type_name RPAREN cast_expression
        """
        self.output_production(t, production_message='cast_expression -> LPAREN type_name RPAREN cast_expression')

    #
    # unary_expression:
    #
    def p_unary_expression_1(self, t):
        """
        unary_expression : postfix_expression
        """
        self.output_production(t, production_message='unary_expression -> postfix_expression')

        t[0] = t[1]

    def p_unary_expression_2(self, t):
        """
        unary_expression : PLUSPLUS unary_expression
        """
        self.output_production(t, production_message='unary_expression -> PLUSPLUS unary_expression')

    def p_unary_expression_3(self, t):
        """
        unary_expression : MINUSMINUS unary_expression
        """
        self.output_production(t, production_message='unary_expression -> MINUSMINUS unary_expression')

    def p_unary_expression_4(self, t):
        """
        unary_expression : unary_operator cast_expression
        """
        self.output_production(t, production_message='unary_expression -> unary_operator cast_expression')

    def p_unary_expression_5(self, t):
        """
        unary_expression : SIZEOF unary_expression
        """
        self.output_production(t, production_message='unary_expression -> SIZEOF unary_expression')

    def p_unary_expression_6(self, t):
        """
        unary_expression : SIZEOF LPAREN type_name RPAREN
        """
        self.output_production(t, production_message='unary_expression -> SIZEOF LPAREN type_name RPAREN')

    #
    # unary_operator
    #
    def p_unary_operator_and(self, t):
        """
        unary_operator : AND
        """
        self.output_production(t, production_message='unary_operator -> AND')

    def p_unary_operator_times(self, t):
        """
        unary_operator : TIMES
        """
        self.output_production(t, production_message='unary_operator -> TIMES')

    def p_unary_operator_plus(self, t):
        """unary_operator : PLUS
        """
        self.output_production(t, production_message='unary_operator -> PLUS')

    def p_unary_operator_minus(self, t):
        """unary_operator : MINUS
        """
        self.output_production(t, production_message='unary_operator -> MINUS')

    def p_unary_operator_not(self, t):
        """unary_operator : NOT
        """
        self.output_production(t, production_message='unary_operator -> NOT')

    def p_unary_operator_lnot(self, t):
        """
        unary_operator : LNOT
        """
        self.output_production(t, production_message='unary_operator -> LNOT')

    #
    # postfix_expression:
    #
    def p_postfix_expression_1(self, t):
        """
        postfix_expression : primary_expression
        """
        self.output_production(t, production_message='postfix_expression -> primary_expression')

        t[0] = t[1]

    def p_postfix_expression_2(self, t):
        """
        postfix_expression : postfix_expression LBRACKET expression RBRACKET
        """
        self.output_production(t, production_message='postfix_expression -> postfix_expression LBRACKET expression RBRACKET')

    def p_postfix_expression_3(self, t):
        """
        postfix_expression : postfix_expression LPAREN argument_expression_list RPAREN
        """
        self.output_production(t, production_message='postfix_expression -> postfix_expression LPAREN argument_expression_list RPAREN')

    def p_postfix_expression_4(self, t):
        """
        postfix_expression : postfix_expression LPAREN RPAREN
        """
        self.output_production(t, production_message='postfix_expression -> postfix_expression LPAREN RPAREN')

    def p_postfix_expression_5(self, t):
        """
        postfix_expression : postfix_expression PERIOD identifier
        """
        self.output_production(t, production_message='postfix_expression -> postfix_expression PERIOD identifier')

    def p_postfix_expression_6(self, t):
        """
        postfix_expression : postfix_expression ARROW identifier
        """
        self.output_production(t, production_message='postfix_expression -> postfix_expression ARROW identifier')

    def p_postfix_expression_7(self, t):
        """
        postfix_expression : postfix_expression PLUSPLUS
        """
        self.output_production(t, production_message='postfix_expression -> postfix_expression PLUSPLUS')

    def p_postfix_expression_8(self, t):
        """
        postfix_expression : postfix_expression MINUSMINUS
        """
        self.output_production(t, production_message='postfix_expression -> postfix_expression MINUSMINUS')

    #
    # primary-expression:
    #
    def p_primary_expression_identifier(self, t):
        """
        primary_expression :  identifier
        """
        self.output_production(t, production_message='primary_expression -> identifier')

        t[0] = t[1]

    def p_primary_expression_constant(self, t):
        """
        primary_expression : constant
        """
        self.output_production(t, production_message='primary_expression -> constant')

        t[0] = t[1]

    def p_primary_expression_string_literal(self, t):
        """
        primary_expression : string_literal
        """
        self.output_production(t, production_message='primary_expression -> string_literal_list')

        t[0] = t[1]

    def p_string_literal_fragment(self, t):
        """
        string_literal : SCONST
        """
        self.output_production(t, production_message='string_literal_list -> SCONST {}'.format(t[1]))

        t[0] = t[1]

    def p_string_literal_plus_string_literal_fragment(self, t):
        """string_literal : string_literal SCONST
        """
        self.output_production(t, production_message='string_literal_list -> string_literal_list SCONST')

        # concatenate the string fragments into a single string literal by trimming off the quote marks
        t[0] = t[1][:-1] + t[2][1:]

    def p_primary_expression_parenthesized(self, t):
        """primary_expression : LPAREN expression RPAREN
        """
        self.output_production(t, production_message='primary_expression -> LPAREN expression RPAREN')

        # a parenthesised expression evaluates to the expression itself
        t[0] = t[2]

    #
    # argument-expression-list:
    #
    def p_argument_expression_list_assignment_expression(self, t):
        """
        argument_expression_list :  assignment_expression
        """
        self.output_production(t, production_message='argument_expression_list ->  assignment_expression')

    def p_argument_expression_list_list_comma_expression(self, t):
        """
        argument_expression_list : argument_expression_list COMMA assignment_expression
        """
        self.output_production(t, production_message='argument_expression_list -> argument_expression_list COMMA assignment_expression')

    #
    # constant:
    #
    def p_constant_int(self, t):
        """
        constant : ICONST
        """
        self.output_production(t, production_message='constant -> ICONST {}'.format(t[1]))

        t[0] = ConstantValue( int(t[1]), 'int')

    def p_constant_float(self, t):
        """
        constant : FCONST
        """
        self.output_production(t, production_message='constant -> FCONST {}'.format(t[1]))

        t[0] = ConstantValue(float(t[1]), 'float')

    def p_constant_char(self, t):
        """
        constant : CCONST
        """
        self.output_production(t, production_message='constant -> CCONST {}'.format(t[1]))

        t[0] = ConstantValue(t[1], 'char')

    #
    # identifier:
    #
    def p_identifier(self, t):
        """identifier : ID
        """
        self.output_production(t, production_message='identifier -> ID {}'.format(t[1].identifier))

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
    def p_enter_function_scope(self, t):
        """
        enter_function_scope : empty
        """
        self.prod_logger.info('Entering scope {}'.format(len(self.compiler_state.symbol_table.table)))

        self.compiler_state.symbol_table.push()
        self.compiler_state.function_scope_entered = True

        # TODO: grab the parameters from the function's declaration and push them into the new scope


    def p_enter_scope(self, t):
        """
        enter_scope : empty
        """
        self.prod_logger.info('Entering scope {}'.format(len(self.compiler_state.symbol_table.table)))

        if not self.compiler_state.function_scope_entered:
            self.compiler_state.symbol_table.push()
        else:
            self.compiler_state.function_scope_entered = False

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
        self.prod_logger.info('Leaving scope {}'.format(len(self.compiler_state.symbol_table.table) - 1))

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


    ## Handles any designated output (other than standard compiler output and warnings).
    # @param self The object pointer
    # @param t The production item with info about the production, including line numbers.
    # @param production_message The production to write. Defaults to 'No Production'.
    #
    # Outputs:
    #   Logger output.
    #
    # Called by the production processing methods.
    #
    def output_production(self, t, production_message='No->Production'):
        message_parts = production_message.split(" -> ")
        production_message = '{rhs:>30} -> {lhs}'.format(rhs=message_parts[0], lhs=message_parts[1])

        line = t.lineno(1)
        self.prod_logger.source(self.compiler_state.source_code[line - 1], line=line)
        self.prod_logger.production(production_message)

    ## Determines if an object is useable in evaluating a compile-time constant expressions.
    #
    # @param item The item to be checked.
    #
    # Output:
    #   Returns True if the item is useable for hte constant expression; False otherwise.
    #
    # Called by production handling methods and possibly AST nodes.
    #
    @staticmethod
    def is_a_constant(item_1, item_2):
        # TODO: refactor to handle only one item, with constants and variables declared as constant
        return issubclass(type(item_1), ConstantValue) and issubclass(type(item_2), ConstantValue)

    ## Performs compile-time operations to evalate constant expressions.
    #
    # @param operand_1 The first operand of the operation.
    # @param operator The operator for the operation.
    # @param operand_2 The second (optional, in the case of a unary operation) operand of the operation.
    #
    # Output:
    #   Returns on object representing the (constant) result of the operation.
    #
    # Called by production handling methods.
    #
    @staticmethod
    def perform_constant_expression_operation(operand_1: ConstantValue, operator: str, operand_2: ConstantValue) -> ConstantValue:
        # TODO: refactor to completion ot include all operands (bitwise ones too)
        if operator is '+':
            print(operand_1, operand_2)
            v_1 = operand_1.value if type(operand_1) is ConstantValue else operand_1
            v_2 = operand_2.value if type(operand_2) is ConstantValue else operand_2
            return v_1 + v_2
        elif operator is '-':
            pass
        elif operator is '*':
            pass
        elif operator is '/':
            pass
        elif operator is '%':
            pass
        else:
            # raise Exception('please provide a proper operand')
            pass

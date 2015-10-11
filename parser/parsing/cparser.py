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

import sys
import ply.yacc as yacc
from symbol_table.symbol_table import SymbolTable


class Parser(object):
    NO_DEBUG = 0
    DEBUG_PRODUCTIONS = 1

    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = lexer.tokens
        self.parser = yacc.yacc(module=self)

        self.symbol_table = SymbolTable()

        self.debug_level = Parser.NO_DEBUG
        self.dout = sys.stdout

    def teardown(self):
        if self.dout not in {sys.stdout, sys.stderr}:
            self.dout.close()
        self.dout = None

    def parse(self, data):
        return self.parser.parse(input=data, lexer=self.lexer)

    def debug_out(self, message):
        # TODO: replace self.dout with a logger if it is a smooth transition

        # print("""Implement me!: debug_out""")
        if self.debug_level == Parser.DEBUG_PRODUCTIONS:
            self.dout.write(message + '\n')

    #
    # p_error
    #
    def p_error(self, t):
        print('Implement me!: p_error')
        print("Error encountered!")
        raise Exception("Error encountered!")

    #
    # translation-unit:
    #
    def p_translation_unit_1(self, t):
        """translation_unit : external_declaration"""
        self.debug_out('PRODUCTION: translation_unit -> external_declaration')

    def p_translation_unit_2(self, t):
        """translation_unit : translation_unit external_declaration"""
        self.debug_out('PRODUCTION: translation_unit -> translation_unit external_declaraion')

    #
    # external-declaration:
    #
    def p_external_declaration_1(self, t):
        """external_declaration : function_definition"""
        self.debug_out('PRODUCTION: external_declaration -> function_definition')

    def p_external_declaration_2(self, t):
        """external_declaration : declaration"""
        self.debug_out('PRODUCTION: external_declaration -> declaration')

    #
    # function-definition:
    #
    def p_function_definition_1(self, t):
        """function_definition : declaration_specifiers declarator declaration_list compound_statement"""
        self.debug_out('PRODUCTION: function_definition -> declaration_specifiers declarator declaration_list compound_statement')

    def p_function_definition_2(self, t):
        """function_definition : declarator declaration_list compound_statement"""
        self.debug_out('PRODUCTION: function_definition -> declarator declaration_list compound_statement')

    def p_function_definition_3(self, t):
        """function_definition : declarator compound_statement"""
        self.debug_out('PRODUCTION: function_definition -> declarator declaration_list compound_statement')

    def p_function_definition_4(self, t):
        """function_definition : declaration_specifiers declarator compound_statement"""
        self.debug_out('PRODUCTION: function_definition -> declaration_specifiers declarator compound_statement')

    #
    # declaration:
    #
    def p_declaration_1(self, t):
        """declaration : declaration_specifiers init_declarator_list SEMI"""
        self.debug_out('PRODUCTION: declaration -> declaration_specifiers init_declarator_list SEMI')

    def p_declaration_2(self, t):
        """declaration : declaration_specifiers SEMI"""
        self.debug_out('PRODUCTION: declaration -> declaration_specifiers SEMI')

    #
    # declaration-list:
    #
    def p_declaration_list_1(self, t):
        """declaration_list : declaration"""
        self.debug_out('PRODUCTION: declaration_list -> declaration')

    def p_declaration_list_2(self, t):
        """declaration_list : declaration_list declaration"""
        self.debug_out('PRODUCTION: declaration_list -> declaration_list declaration')

    #
    # declaration-specifiers
    #
    def p_declaration_specifiers_1(self, t):
        """declaration_specifiers : storage_class_specifier declaration_specifiers"""
        self.debug_out('PRODUCTION: declaration_specifiers -> storage_class_specifier declaration_specifiers')

    def p_declaration_specifiers_2(self, t):
        """declaration_specifiers : type_specifier declaration_specifiers"""
        self.debug_out('PRODUCTION: declaration_specifiers -> type_specifier declaration_specifiers')

    def p_declaration_specifiers_3(self, t):
        """declaration_specifiers : type_qualifier declaration_specifiers"""
        self.debug_out('PRODUCTION: declaration_specifiers : type_qualifier declaration_specifiers')

    def p_declaration_specifiers_4(self, t):
        """declaration_specifiers : storage_class_specifier"""
        self.debug_out('PRODUCTION: declaration_specifiers : storage_class_specifier')

    def p_declaration_specifiers_5(self, t):
        """declaration_specifiers : type_specifier"""
        self.debug_out('PRODUCTION: declaration_specifiers : type_specifier')

    def p_declaration_specifiers_6(self, t):
        """declaration_specifiers : type_qualifier"""
        self.debug_out('PRODUCTION: declaration_specifiers : type_qualifier')

    #
    # storage-class-specifier
    #
    def p_storage_class_specifier_auto(self, t):
        """storage_class_specifier : AUTO"""
        self.debug_out('PRODUCTION: storage_class_specifier -> AUTO')
    
    def p_storage_class_specifie_register(self, t):
        """storage_class_specifier : REGISTER"""
        self.debug_out('PRODUCTION: storage_class_specifier -> REGISTER')
    
    def p_storage_class_specifier_static(self, t):
        """storage_class_specifier : STATIC"""
        self.debug_out('PRODUCTION: storage_class_specifier -> STATIC')
    
    def p_storage_class_specifier_extern(self, t):
        """storage_class_specifier : EXTERN"""
        self.debug_out('PRODUCTION: storage_class_specifier -> EXTERN')
    
    def p_storage_class_specifier_typedef(self, t):
        """storage_class_specifier : TYPEDEF"""
        self.debug_out('PRODUCTION: storage_class_specifier -> TYPEDEF')

    #
    # type-specifier:
    #
    def p_type_specifier_void(self, t):
        """type_specifier : VOID"""
        self.debug_out('PRODUCTION: type_specifier -> VOID')
    
    def p_type_specifier_char(self, t):
        """type_specifier : CHAR"""
        self.debug_out('PRODUCTION: type_specifier -> CHAR')
    
    def p_type_specifier_short(self, t):
        """type_specifier : SHORT"""
        self.debug_out('PRODUCTION: type_specifier -> SHORT')
    
    def p_type_specifier_int(self, t):
        """type_specifier : INT"""
        self.debug_out('PRODUCTION: type_specifier -> INT')
    
    def p_type_specifier_long(self, t):
        """type_specifier : LONG"""
        self.debug_out('PRODUCTION: type_specifier -> LONG')
    
    def p_type_specifier_float(self, t):
        """type_specifier : FLOAT"""
        self.debug_out('PRODUCTION: type_specifier -> FLOAT')
    
    def p_type_specifier_double(self, t):
        """type_specifier : DOUBLE"""
        self.debug_out('PRODUCTION: type_specifier -> DOUBLE')
    
    def p_type_specifier_signed(self, t):
        """type_specifier : SIGNED"""
        self.debug_out('PRODUCTION: type_specifier -> SIGNED')
    
    def p_type_specifier_unsigned(self, t):
        """type_specifier : UNSIGNED"""
        self.debug_out('PRODUCTION: type_specifier -> UNSIGNED')
    
    def p_type_specifier_struct_or_union(self, t):
        """type_specifier : struct_or_union_specifier"""
        self.debug_out('PRODUCTION: type_specifier -> struct_or_union_specifier')
    
    def p_type_specifier_enum(self, t):
        """type_specifier : enum_specifier"""
        self.debug_out('PRODUCTION: type_specifier -> enum_specifier')
    
    def p_type_specifier_typeid(self, t):
        """type_specifier : TYPEID"""
        self.debug_out('PRODUCTION: type_specifier -> TYPEID')

    #
    # type-qualifier:
    #
    def p_type_qualifier_const(self, t):
        """type_qualifier : CONST"""
        self.debug_out('PRODUCTION: type_qualifier -> CONST')

    def p_type_qualifier_volatile(self, t):
        """type_qualifier : VOLATILE"""
        self.debug_out('PRODUCTION: type_qualifier -> VOLATILE')

    #
    # struct-or-union-specifier
    #
    def p_struct_or_union_specifier_1(self, t):
        """struct_or_union_specifier : struct_or_union identifier LBRACE struct_declaration_list RBRACE"""
        self.debug_out('PRODUCTION: struct_or_union_specifier : struct_or_union identifier LBRACE struct_declaration_list RBRACE')

    def p_struct_or_union_specifier_2(self, t):
        """struct_or_union_specifier : struct_or_union LBRACE struct_declaration_list RBRACE"""
        self.debug_out('PRODUCTION: struct_or_union_specifier : struct_or_union LBRACE struct_declaration_list RBRACE')

    def p_struct_or_union_specifier_3(self, t):
        """struct_or_union_specifier : struct_or_union identifier"""
        self.debug_out('PRODUCTION: struct_or_union_specifier : struct_or_union identifier')

    #
    # struct-or-union:
    #
    def p_struct_or_union_struct(self, t):
        """struct_or_union : STRUCT"""
        self.debug_out('PRODUCTION: struct_or_union -> STRUCT')

    def p_struct_or_union_union(self, t):
        """struct_or_union : UNION"""
        self.debug_out('PRODUCTION: struct_or_union -> UNION')

    #
    # struct-declaration-list:
    #
    def p_struct_declaration_list_1(self, t):
        """struct_declaration_list : struct_declaration"""
        self.debug_out('PRODUCTION: struct_declaration_list : struct_declaration')

    def p_struct_declaration_list_2(self, t):
        """struct_declaration_list : struct_declarator_list struct_declaration"""
        self.debug_out('PRODUCTION: struct_declaration_list : struct_declarator_list struct_declaration')

    #
    # init-declarator-list:
    #
    def p_init_declarator_list_1(self, t):
        """init_declarator_list : init_declarator"""
        self.debug_out('PRODUCTION: init_declarator_list : init_declarator')

    def p_init_declarator_list_2(self, t):
        """init_declarator_list : init_declarator_list COMMA init_declarator"""
        self.debug_out('PRODUCTION: init_declarator_list : init_declarator_list COMMA init_declarator')

    #
    # init-declarator
    #
    def p_init_declarator_1(self, t):
        """init_declarator : declarator"""
        self.debug_out('PRODUCTION: init_declarator : declarator')

    def p_init_declarator_2(self, t):
        """init_declarator : declarator EQUALS initializer"""
        self.debug_out('PRODUCTION: init_declarator : declarator EQUALS initializer')

    #
    # struct-declaration:
    #
    def p_struct_declaration(self, t):
        """struct_declaration : specifier_qualifier_list struct_declarator_list SEMI"""
        self.debug_out('PRODUCTION: struct_declaration : specifier_qualifier_list struct_declarator_list SEMI')

    #
    # specifier-qualifier-list:
    #
    def p_specifier_qualifier_list_1(self, t):
        """specifier_qualifier_list : type_specifier specifier_qualifier_list"""
        self.debug_out('PRODUCTION: specifier_qualifier_list : type_specifier specifier_qualifier_list')

    def p_specifier_qualifier_list_2(self, t):
        """specifier_qualifier_list : type_specifier"""
        self.debug_out('PRODUCTION: specifier_qualifier_list : type_specifier')

    def p_specifier_qualifier_list_3(self, t):
        """specifier_qualifier_list : type_qualifier specifier_qualifier_list"""
        self.debug_out('PRODUCTION: specifier_qualifier_list : type_qualifier specifier_qualifier_list')

    def p_specifier_qualifier_list_4(self, t):
        """specifier_qualifier_list : type_qualifier"""
        self.debug_out('PRODUCTION: specifier_qualifier_list : type_qualifier')

    #
    # struct-declarator-list:
    #
    def p_struct_declarator_list_1(self, t):
        """struct_declarator_list : struct_declarator"""
        self.debug_out('PRODUCTION: struct_declarator_list : struct_declarator')

    def p_struct_declarator_list_2(self, t):
        """struct_declarator_list : struct_declarator_list COMMA struct_declarator"""
        self.debug_out('PRODUCTION: struct_declarator_list : struct_declarator_list COMMA struct_declarator')

    #
    # struct-declarator:
    #
    def p_struct_declarator_1(self, t):
        """struct_declarator : declarator"""
        self.debug_out('PRODUCTION: struct_declarator : declarator')

    def p_struct_declarator_2(self, t):
        """struct_declarator : declarator COLON constant_expression"""
        self.debug_out('PRODUCTION: struct_declarator : declarator COLON constant_expression')

    def p_struct_declarator_3(self, t):
        """struct_declarator : COLON constant_expression"""
        self.debug_out('PRODUCTION: struct_declarator : COLON constant_expression')

    #
    # enum-specifier:
    #
    def p_enum_specifier_1(self, t):
        """enum_specifier : ENUM identifier LBRACE enumerator_list RBRACE"""
        self.debug_out('PRODUCTION: enum_specifier : ENUM identifier LBRACE enumerator_list RBRACE')

    def p_enum_specifier_2(self, t):
        """enum_specifier : ENUM LBRACE enumerator_list RBRACE"""
        self.debug_out('PRODUCTION: enum_specifier : ENUM LBRACE enumerator_list RBRACE')

    def p_enum_specifier_3(self, t):
        """enum_specifier : ENUM identifier"""
        self.debug_out('PRODUCTION: enum_specifier : ENUM identifier')

    #
    # enumerator_list:
    #
    def p_enumerator_list_1(self, t):
        """enumerator_list : enumerator"""
        self.debug_out('PRODUCTION: enumerator_list : enumerator')

    def p_enumerator_list_2(self, t):
        """enumerator_list : enumerator_list COMMA enumerator"""
        self.debug_out('PRODUCTION: enumerator_list : enumerator_list COMMA enumerator')

    #
    # enumerator:
    #
    def p_enumerator_1(self, t):
        """enumerator : identifier"""
        self.debug_out('PRODUCTION: enumerator : identifier')

    def p_enumerator_2(self, t):
        """enumerator : identifier EQUALS constant_expression"""
        self.debug_out('PRODUCTION: enumerator : identifier EQUALS constant_expression')

    #
    # declarator:
    #
    def p_declarator_1(self, t):
        """declarator : pointer direct_declarator"""
        self.debug_out('PRODUCTION: ')

    def p_declarator_2(self, t):
        """declarator : direct_declarator"""
        self.debug_out('PRODUCTION: declarator : pointer direct_declarator')

    #
    # direct-declarator:
    #
    def p_direct_declarator_1(self, t):
        """direct_declarator : identifier"""
        self.debug_out('PRODUCTION: direct_declarator : identifier')

    def p_direct_declarator_2(self, t):
        """direct_declarator : LPAREN declarator RPAREN"""
        self.debug_out('PRODUCTION: direct_declarator : LPAREN declarator RPAREN')

    def p_direct_declarator_3(self, t):
        """direct_declarator : direct_declarator LBRACKET constant_expression_opt RBRACKET"""
        self.debug_out('PRODUCTION: direct_declarator : direct_declarator LBRACKET constant_expression_opt RBRACKET')

    def p_direct_declarator_4(self, t):
        """direct_declarator : direct_declarator LPAREN parameter_type_list RPAREN"""
        self.debug_out('PRODUCTION: direct_declarator : direct_declarator LPAREN parameter_type_list RPAREN')

    def p_direct_declarator_5(self, t):
        """direct_declarator : direct_declarator LPAREN identifier_list RPAREN"""
        self.debug_out('PRODUCTION: direct_declarator : direct_declarator LPAREN identifier_list RPAREN')

    def p_direct_declarator_6(self, t):
        """direct_declarator : direct_declarator LPAREN RPAREN"""
        self.debug_out('PRODUCTION: direct_declarator : direct_declarator LPAREN RPAREN')

    #
    # pointer:
    #
    def p_pointer_1(self, t):
        """pointer : TIMES type_qualifier_list"""
        self.debug_out('PRODUCTION: pointer : TIMES type_qualifier_list')

    def p_pointer_2(self, t):
        """pointer : TIMES"""
        self.debug_out('PRODUCTION: pointer : TIMES')

    def p_pointer_3(self, t):
        """pointer : TIMES type_qualifier_list pointer"""
        self.debug_out('PRODUCTION: pointer : TIMES type_qualifier_list pointer')

    def p_pointer_4(self, t):
        """pointer : TIMES pointer"""
        self.debug_out('PRODUCTION: pointer : TIMES pointer')

    #
    # type-qualifier-list:
    #
    def p_type_qualifier_list_1(self, t):
        """type_qualifier_list : type_qualifier"""
        self.debug_out('PRODUCTION: type_qualifier_list : type_qualifier')

    def p_type_qualifier_list_2(self, t):
        """type_qualifier_list : type_qualifier_list type_qualifier"""
        self.debug_out('PRODUCTION: type_qualifier_list : type_qualifier_list type_qualifier')

    #
    # parameter-type-list:
    #
    def p_parameter_type_list_1(self, t):
        """parameter_type_list : parameter_list"""
        self.debug_out('PRODUCTION: parameter_type_list : parameter_list')

    def p_parameter_type_list_2(self, t):
        """parameter_type_list : parameter_list COMMA ELLIPSIS"""
        self.debug_out('PRODUCTION: parameter_type_list : parameter_list COMMA ELLIPSIS')

    #
    # parameter-list:
    #
    def p_parameter_list_1(self, t):
        """parameter_list : parameter_declaration"""
        self.debug_out('PRODUCTION: parameter_list : parameter_declaration')

    def p_parameter_list_2(self, t):
        """parameter_list : parameter_list COMMA parameter_declaration"""
        self.debug_out('PRODUCTION: parameter_list : parameter_list COMMA parameter_declaration')

    #
    # parameter-declaration:
    #
    def p_parameter_declaration_1(self, t):
        """parameter_declaration : declaration_specifiers declarator"""
        self.debug_out('PRODUCTION: parameter_declaration : declaration_specifiers declarator')

    def p_parameter_declaration_2(self, t):
        """parameter_declaration : declaration_specifiers abstract_declarator_opt"""
        self.debug_out('PRODUCTION: parameter_declaration : declaration_specifiers abstract_declarator_opt')

    #
    # identifier-list:
    #
    def p_identifier_list_1(self, t):
        """identifier_list : identifier"""
        self.debug_out('PRODUCTION: identifier_list : identifier')

    def p_identifier_list_2(self, t):
        """identifier_list : identifier_list COMMA identifier"""
        self.debug_out('PRODUCTION: identifier_list : identifier_list COMMA identifier')

    #
    # initializer:
    #
    def p_initializer_1(self, t):
        """initializer : assignment_expression"""
        self.debug_out('PRODUCTION: initializer : assignment_expression')

    def p_initializer_2(self, t):
        """initializer : LBRACE initializer_list RBRACE"""
        self.debug_out('PRODUCTION: initializer : LBRACE initializer_list RBRACE')

    def p_initializer_3(self, t):
        """initializer : LBRACE initializer_list COMMA RBRACE"""
        self.debug_out('PRODUCTION: initializer : LBRACE initializer_list COMMA RBRACE')

    #
    # initializer-list:
    #
    def p_initializer_list_1(self, t):
        """initializer_list : initializer"""
        self.debug_out('PRODUCTION: initializer_list : initializer')

    def p_initializer_list_2(self, t):
        """initializer_list : initializer_list COMMA initializer"""
        self.debug_out('PRODUCTION: initializer_list : initializer_list COMMA initializer')

    #
    # type-name:
    #
    def p_type_name(self, t):
        """type_name : specifier_qualifier_list abstract_declarator_opt"""
        self.debug_out('PRODUCTION: type_name : specifier_qualifier_list abstract_declarator_opt')

    def p_abstract_declarator_opt_1(self, t):
        """abstract_declarator_opt : empty"""
        self.debug_out('PRODUCTION: abstract_declarator_opt : empty')

    def p_abstract_declarator_opt_2(self, t):
        """abstract_declarator_opt : abstract_declarator"""
        self.debug_out('PRODUCTION: abstract_declarator_opt : abstract_declarator')

    #
    # abstract-declarator:
    #
    def p_abstract_declarator_1(self, t):
        """abstract_declarator : pointer"""
        self.debug_out('PRODUCTION: abstract_declarator : pointer')

    def p_abstract_declarator_2(self, t):
        """abstract_declarator : pointer direct_abstract_declarator"""
        self.debug_out('PRODUCTION: abstract_declarator : pointer direct_abstract_declarator')

    def p_abstract_declarator_3(self, t):
        """abstract_declarator : direct_abstract_declarator"""
        self.debug_out('PRODUCTION: abstract_declarator : direct_abstract_declarator')

    #
    # direct-abstract-declarator:
    #
    def p_direct_abstract_declarator_1(self, t):
        """direct_abstract_declarator : LPAREN abstract_declarator RPAREN"""
        self.debug_out('PRODUCTION: direct_abstract_declarator : LPAREN abstract_declarator RPAREN')

    def p_direct_abstract_declarator_2(self, t):
        """direct_abstract_declarator : direct_abstract_declarator LBRACKET constant_expression_opt RBRACKET"""
        self.debug_out('PRODUCTION: direct_abstract_declarator : direct_abstract_declarator LBRACKET constant_expression_opt RBRACKET')

    def p_direct_abstract_declarator_3(self, t):
        """direct_abstract_declarator : LBRACKET constant_expression_opt RBRACKET"""
        self.debug_out('PRODUCTION: direct_abstract_declarator : LBRACKET constant_expression_opt RBRACKET')

    def p_direct_abstract_declarator_4(self, t):
        """direct_abstract_declarator : direct_abstract_declarator LPAREN parameter_type_list_opt RPAREN"""
        self.debug_out('PRODUCTION: direct_abstract_declarator : direct_abstract_declarator LPAREN parameter_type_list_opt RPAREN')

    def p_direct_abstract_declarator_5(self, t):
        """direct_abstract_declarator : LPAREN parameter_type_list_opt RPAREN"""
        self.debug_out('PRODUCTION: direct_abstract_declarator : LPAREN parameter_type_list_opt RPAREN')

    #
    # Optional fields in abstract declarators
    #
    def p_constant_expression_opt_1(self, t):
        """constant_expression_opt : empty"""
        self.debug_out('PRODUCTION: constant_expression_opt : empty')

    def p_constant_expression_opt_2(self, t):
        """constant_expression_opt : constant_expression"""
        self.debug_out('PRODUCTION: constant_expression_opt : constant_expression')

    def p_parameter_type_list_opt_1(self, t):
        """parameter_type_list_opt : empty"""
        self.debug_out('PRODUCTION: parameter_type_list_opt : empty')

    def p_parameter_type_list_opt_2(self, t):
        """parameter_type_list_opt : parameter_type_list"""
        self.debug_out('PRODUCTION: parameter_type_list_opt : parameter_type_list')

    #
    # statement:
    #
    def p_statement_labeled(self, t):
        """statement : labeled_statement"""
        self.debug_out('PRODUCTION: statement -> labeled_statement')
    
    def p_statement_expression(self, t):
        """statement : expression_statement"""
        self.debug_out('PRODUCTION: statement -> expression_statment')
    
    def p_statement_compound(self, t):
        """statement : compound_statement"""
        self.debug_out('PRODUCTION: statement -> compund_statement')
    
    def p_statement_selection(self, t):
        """statement : selection_statement"""
        self.debug_out('PRODUCTION: statement ->selection_statement')
    
    def p_statement_iteration(self, t):
        """statement : iteration_statement"""
        self.debug_out('PRODUCTION: statement ->iteration_statement')
    
    def p_statement_jump(self, t):
        """statement : jump_statement"""
        self.debug_out('PRODUCTION: statement -> jump_statement')

    #
    # labeled-statement:
    #
    def p_labeled_statement_1(self, t):
        """labeled_statement : identifier COLON statement"""
        self.debug_out('PRODUCTION: labeled_statement : identifier COLON statement')

    def p_labeled_statement_2(self, t):
        """labeled_statement : CASE constant_expression COLON statement"""
        self.debug_out('PRODUCTION: labeled_statement : CASE constant_expression COLON statement')

    def p_labeled_statement_3(self, t):
        """labeled_statement : DEFAULT COLON statement"""
        self.debug_out('PRODUCTION: labeled_statement : DEFAULT COLON statement')

    #
    # expression-statement:
    #
    def p_expression_statement(self, t):
        """expression_statement : expression_opt SEMI"""
        self.debug_out('PRODUCTION: expression_statement : expression_opt SEMI')

    #
    # compound-statement:
    #
    def p_compound_statement_1(self, t):
        """compound_statement : LBRACE declaration_list statement_list RBRACE"""
        self.debug_out('PRODUCTION: compound_statement : LBRACE declaration_list statement_list RBRACE')

    def p_compound_statement_2(self, t):
        """compound_statement : LBRACE statement_list RBRACE"""
        self.debug_out('PRODUCTION: compound_statement : LBRACE statement_list RBRACE')

    def p_compound_statement_3(self, t):
        """compound_statement : LBRACE declaration_list RBRACE"""
        self.debug_out('PRODUCTION: compound_statement : LBRACE declaration_list RBRACE')

    def p_compound_statement_4(self, t):
        """compound_statement : LBRACE RBRACE"""
        self.debug_out('PRODUCTION: compound_statement : LBRACE RBRACE')

    #
    # statement-list:
    #
    def p_statement_list_1(self, t):
        """statement_list : statement"""
        self.debug_out('PRODUCTION: statement_list : statement')

    def p_statement_list_2(self, t):
        """statement_list : statement_list statement"""
        self.debug_out('PRODUCTION: statement_list : statement_list statement')

    #
    # selection-statement
    #
    def p_selection_statement_1(self, t):
        """selection_statement : IF LPAREN expression RPAREN statement"""
        self.debug_out('PRODUCTION: selection_statement : IF LPAREN expression RPAREN statement')

    def p_selection_statement_2(self, t):
        """selection_statement : IF LPAREN expression RPAREN statement ELSE statement"""
        self.debug_out('PRODUCTION: selection_statement : IF LPAREN expression RPAREN statement ELSE statement')

    def p_selection_statement_3(self, t):
        """selection_statement : SWITCH LPAREN expression RPAREN statement"""
        self.debug_out('PRODUCTION: selection_statement : SWITCH LPAREN expression RPAREN statement')

    #
    # iteration_statement:
    #
    def p_iteration_statement_1(self, t):
        """iteration_statement : WHILE LPAREN expression RPAREN statement"""
        self.debug_out('PRODUCTION: iteration_statement : WHILE LPAREN expression RPAREN statement')

    def p_iteration_statement_2(self, t):
        """iteration_statement : FOR LPAREN expression_opt SEMI expression_opt SEMI expression_opt RPAREN statement"""
        self.debug_out('PRODUCTION: iteration_statement : FOR LPAREN expression_opt SEMI expression_opt SEMI expression_opt RPAREN statement')

    def p_iteration_statement_3(self, t):
        """iteration_statement : DO statement WHILE LPAREN expression RPAREN SEMI"""
        self.debug_out('PRODUCTION: iteration_statement : DO statement WHILE LPAREN expression RPAREN SEMI')

    #
    # jump_statement:
    #
    def p_jump_statement_1(self, t):
        """jump_statement : GOTO identifier SEMI"""
        self.debug_out('PRODUCTION: jump_statement : GOTO identifier SEMI')

    def p_jump_statement_2(self, t):
        """jump_statement : CONTINUE SEMI"""
        self.debug_out('PRODUCTION: jump_statement : CONTINUE SEMI')

    def p_jump_statement_3(self, t):
        """jump_statement : BREAK SEMI"""
        self.debug_out('PRODUCTION: jump_statement : BREAK SEMI')

    def p_jump_statement_4(self, t):
        """jump_statement : RETURN expression_opt SEMI"""
        self.debug_out('PRODUCTION: jump_statement : RETURN expression_opt SEMI')

    def p_expression_opt_1(self, t):
        """expression_opt : empty"""
        self.debug_out('PRODUCTION: ')

    def p_expression_opt_2(self, t):
        """expression_opt : expression"""
        self.debug_out('PRODUCTION: expression_opt : empty')

    #
    # expression:
    #
    def p_expression_1(self, t):
        """expression : assignment_expression"""
        self.debug_out('PRODUCTION: expression : assignment_expression')

    def p_expression_2(self, t):
        """expression : expression COMMA assignment_expression"""
        self.debug_out('PRODUCTION: expression : expression COMMA assignment_expression')

    #
    # assigment_expression:
    #
    def p_assignment_expression_1(self, t):
        """assignment_expression : conditional_expression"""
        self.debug_out('PRODUCTION: assignment_expression : conditional_expression')

    def p_assignment_expression_2(self, t):
        """assignment_expression : unary_expression assignment_operator assignment_expression"""
        self.debug_out('PRODUCTION: assignment_expression : unary_expression assignment_operator assignment_expression')

    #
    # assignment_operator:
    #
    def p_assignment_operator_equals(self, t):
        """assignment_operator : EQUALS"""
        self.debug_out('PRODUCTION: assignment_operator -> EQUALS')
    
    def p_assignment_operator_times(self, t):
        """assignment_operator : TIMESEQUAL"""
        self.debug_out('PRODUCTION: assignment_operator -> TIMESEQUAL')
    
    def p_assignment_operator_div(self, t):
        """assignment_operator : DIVEQUAL"""
        self.debug_out('PRODUCTION: assignment_operator -> DIVEQUAL')
    
    def p_assignment_operator_mod(self, t):
        """assignment_operator : MODEQUAL"""
        self.debug_out('PRODUCTION: assignment_operator -> MODEQUAL')
    
    def p_assignment_operator_plus(self, t):
        """assignment_operator : PLUSEQUAL"""
        self.debug_out('PRODUCTION: assignment_operator -> PLUSEQUAL')
    
    def p_assignment_operator_minus(self, t):
        """assignment_operator : MINUSEQUAL"""
        self.debug_out('PRODUCTION: assignment_operator -> MINUSEQUAL')
    
    def p_assignment_operator_left_shift(self, t):
        """assignment_operator : LSHIFTEQUAL"""
        self.debug_out('PRODUCTION: assignment_operator -> LSHIFTEQUAL')
    
    def p_assignment_operator_right_shift(self, t):
        """assignment_operator : RSHIFTEQUAL"""
        self.debug_out('PRODUCTION: assignment_operator -> RSHIFTEQUAL')
    
    def p_assignment_operator_and(self, t):
        """assignment_operator : ANDEQUAL"""
        self.debug_out('PRODUCTION: assignment_operator -> ANDEQUAL')
    
    def p_assignment_operator_or(self, t):
        """assignment_operator : OREQUAL"""
        self.debug_out('PRODUCTION: assignment_operator -> OREQUAL')
    
    def p_assignment_operator_xor(self, t):
        """assignment_operator : XOREQUAL"""
        self.debug_out('PRODUCTION: assignment_operator -> XOREQUAL')

    #
    # conditional-expression
    #
    def p_conditional_expression_1(self, t):
        """conditional_expression : logical_or_expression"""
        self.debug_out('PRODUCTION: conditional_expression : logical_or_expression')

    def p_conditional_expression_2(self, t):
        """conditional_expression : logical_or_expression CONDOP expression COLON conditional_expression"""
        self.debug_out('PRODUCTION: conditional_expression : logical_or_expression CONDOP expression COLON conditional_expression')

    #
    # constant-expression
    #
    def p_constant_expression(self, t):
        """constant_expression : conditional_expression"""
        self.debug_out('PRODUCTION: constant_expression : conditional_expression')

    #
    # logical-or-expression
    #
    def p_logical_or_expression_1(self, t):
        """logical_or_expression : logical_and_expression"""
        self.debug_out('PRODUCTION: logical_or_expression : logical_and_expression')

    def p_logical_or_expression_2(self, t):
        """logical_or_expression : logical_or_expression LOR logical_and_expression"""
        self.debug_out('PRODUCTION: logical_or_expression : logical_or_expression LOR logical_and_expression')

    #
    # logical_and_expression
    #
    def p_logical_and_expression_1(self, t):
        """logical_and_expression : inclusive_or_expression"""
        self.debug_out('PRODUCTION: logical_and_expression : inclusive_or_expression')

    def p_logical_and_expression_2(self, t):
        """logical_and_expression : logical_and_expression LAND inclusive_or_expression"""
        self.debug_out('PRODUCTION: logical_and_expression : logical_and_expression LAND inclusive_or_expression')

    #
    # inclusive-or-expression:
    #
    def p_inclusive_or_expression_1(self, t):
        """inclusive_or_expression : exclusive_or_expression"""
        self.debug_out('PRODUCTION: inclusive_or_expression : exclusive_or_expression')

    def p_inclusive_or_expression_2(self, t):
        """inclusive_or_expression : inclusive_or_expression OR exclusive_or_expression"""
        self.debug_out('PRODUCTION: inclusive_or_expression : inclusive_or_expression OR exclusive_or_expression')

    #
    # exclusive-or-expression:
    #
    def p_exclusive_or_expression_1(self, t):
        """exclusive_or_expression :  and_expression"""
        self.debug_out('PRODUCTION: exclusive_or_expression :  and_expression')

    def p_exclusive_or_expression_2(self, t):
        """exclusive_or_expression :  exclusive_or_expression XOR and_expression"""
        self.debug_out('PRODUCTION: exclusive_or_expression :  exclusive_or_expression XOR and_expression')

    #
    # and_expression
    #
    def p_and_expression_1(self, t):
        """and_expression : equality_expression"""
        self.debug_out('PRODUCTION: and_expression : equality_expression')

    def p_and_expression_2(self, t):
        """and_expression : and_expression AND equality_expression"""
        self.debug_out('PRODUCTION: and_expression : and_expression AND equality_expression')

    #
    # equality_expression:
    #
    def p_equality_expression_1(self, t):
        """equality_expression : relational_expression"""
        self.debug_out('PRODUCTION: equality_expression : relational_expression')

    def p_equality_expression_2(self, t):
        """equality_expression : equality_expression EQ relational_expression"""
        self.debug_out('PRODUCTION: equality_expression : equality_expression EQ relational_expression')

    def p_equality_expression_3(self, t):
        """equality_expression : equality_expression NE relational_expression"""
        self.debug_out('PRODUCTION: equality_expression : equality_expression NE relational_expression')

    #
    # relational-expression:
    #
    def p_relational_expression_1(self, t):
        """relational_expression : shift_expression"""
        self.debug_out('PRODUCTION: relational_expression : shift_expression')

    def p_relational_expression_2(self, t):
        """relational_expression : relational_expression LT shift_expression"""
        self.debug_out('PRODUCTION: relational_expression : relational_expression LT shift_expression')

    def p_relational_expression_3(self, t):
        """relational_expression : relational_expression GT shift_expression"""
        self.debug_out('PRODUCTION: relational_expression : relational_expression GT shift_expression')

    def p_relational_expression_4(self, t):
        """relational_expression : relational_expression LE shift_expression"""
        self.debug_out('PRODUCTION: relational_expression : relational_expression LE shift_expression')

    def p_relational_expression_5(self, t):
        """relational_expression : relational_expression GE shift_expression"""
        self.debug_out('PRODUCTION: relational_expression : relational_expression GE shift_expression')

    #
    # shift-expression
    #
    def p_shift_expression_1(self, t):
        """shift_expression : additive_expression"""
        self.debug_out('PRODUCTION: shift_expression : additive_expression')

    def p_shift_expression_2(self, t):
        """shift_expression : shift_expression LSHIFT additive_expression"""
        self.debug_out('PRODUCTION: shift_expression : shift_expression LSHIFT additive_expression')

    def p_shift_expression_3(self, t):
        """shift_expression : shift_expression RSHIFT additive_expression"""
        self.debug_out('PRODUCTION: shift_expression : shift_expression RSHIFT additive_expression')

    #
    # additive-expression
    #
    def p_additive_expression_1(self, t):
        """additive_expression : multiplicative_expression"""
        self.debug_out('PRODUCTION: additive_expression : multiplicative_expression')

    def p_additive_expression_2(self, t):
        """additive_expression : additive_expression PLUS multiplicative_expression"""
        self.debug_out('PRODUCTION: additive_expression : additive_expression PLUS multiplicative_expression')

    def p_additive_expression_3(self, t):
        """additive_expression : additive_expression MINUS multiplicative_expression"""
        self.debug_out('PRODUCTION: additive_expression : additive_expression MINUS multiplicative_expression')

    #
    # multiplicative_expression
    #
    def p_multiplicative_expression_1(self, t):
        """multiplicative_expression : cast_expression"""
        self.debug_out('PRODUCTION: multiplicative_expression : cast_expression')

    def p_multiplicative_expression_2(self, t):
        """multiplicative_expression : multiplicative_expression TIMES cast_expression"""
        self.debug_out('PRODUCTION: multiplicative_expression : multiplicative_expression TIMES cast_expression')

    def p_multiplicative_expression_3(self, t):
        """multiplicative_expression : multiplicative_expression DIVIDE cast_expression"""
        self.debug_out('PRODUCTION: multiplicative_expression : multiplicative_expression DIVIDE cast_expression')

    def p_multiplicative_expression_4(self, t):
        """multiplicative_expression : multiplicative_expression MOD cast_expression"""
        self.debug_out('PRODUCTION: multiplicative_expression : multiplicative_expression MOD cast_expression')

    #
    # cast_expression:
    #
    def p_cast_expression_1(self, t):
        """cast_expression : unary_expression"""
        self.debug_out('PRODUCTION: cast_expression : unary_expression')

    def p_cast_expression_2(self, t):
        """cast_expression : LPAREN type_name RPAREN cast_expression"""
        self.debug_out('PRODUCTION: cast_expression : LPAREN type_name RPAREN cast_expression')

    #
    # unary_expression:
    #
    def p_unary_expression_1(self, t):
        """unary_expression : postfix_expression"""
        self.debug_out('PRODUCTION: unary_expression : postfix_expression')

    def p_unary_expression_2(self, t):
        """unary_expression : PLUSPLUS unary_expression"""
        self.debug_out('PRODUCTION: unary_expression : PLUSPLUS unary_expression')

    def p_unary_expression_3(self, t):
        """unary_expression : MINUSMINUS unary_expression"""
        self.debug_out('PRODUCTION: unary_expression : MINUSMINUS unary_expression')

    def p_unary_expression_4(self, t):
        """unary_expression : unary_operator cast_expression"""
        self.debug_out('PRODUCTION: unary_expression : unary_operator cast_expression')

    def p_unary_expression_5(self, t):
        """unary_expression : SIZEOF unary_expression"""
        self.debug_out('PRODUCTION: unary_expression : SIZEOF unary_expression')

    def p_unary_expression_6(self, t):
        """unary_expression : SIZEOF LPAREN type_name RPAREN"""
        self.debug_out('PRODUCTION: unary_expression : SIZEOF LPAREN type_name RPAREN')

    #
    # unary_operator
    #
    def p_unary_operator_and(self, t):
        """unary_operator : AND"""
        self.debug_out('PRODUCTION: unary_operator : AND')

    def p_unary_operator_times(self, t):
        """unary_operator : TIMES"""
        self.debug_out('PRODUCTION: unary_operator : TIMES')

    def p_unary_operator_plus(self, t):
        """unary_operator : PLUS"""
        self.debug_out('PRODUCTION: unary_operator : PLUS')

    def p_unary_operator_minus(self, t):
        """unary_operator : MINUS"""
        self.debug_out('PRODUCTION: unary_operator : MINUS')

    def p_unary_operator_not(self, t):
        """unary_operator : NOT"""
        self.debug_out('PRODUCTION: unary_operator : NOT')

    def p_unary_operator_lnot(self, t):
        """unary_operator : LNOT"""
        self.debug_out('PRODUCTION: unary_operator : LNOT')

    #
    # postfix_expression:
    #
    def p_postfix_expression_1(self, t):
        """postfix_expression : primary_expression"""
        self.debug_out('PRODUCTION: postfix_expression : primary_expression')

    def p_postfix_expression_2(self, t):
        """postfix_expression : postfix_expression LBRACKET expression RBRACKET"""
        self.debug_out('PRODUCTION: postfix_expression : postfix_expression LBRACKET expression RBRACKET')

    def p_postfix_expression_3(self, t):
        """postfix_expression : postfix_expression LPAREN argument_expression_list RPAREN"""
        self.debug_out('PRODUCTION: postfix_expression : postfix_expression LPAREN argument_expression_list RPAREN')

    def p_postfix_expression_4(self, t):
        """postfix_expression : postfix_expression LPAREN RPAREN"""
        self.debug_out('PRODUCTION: postfix_expression : postfix_expression LPAREN RPAREN')

    def p_postfix_expression_5(self, t):
        """postfix_expression : postfix_expression PERIOD identifier"""
        self.debug_out('PRODUCTION: postfix_expression : postfix_expression PERIOD identifier')

    def p_postfix_expression_6(self, t):
        """postfix_expression : postfix_expression ARROW identifier"""
        self.debug_out('PRODUCTION: postfix_expression : postfix_expression ARROW identifier')

    def p_postfix_expression_7(self, t):
        """postfix_expression : postfix_expression PLUSPLUS"""
        self.debug_out('PRODUCTION: postfix_expression : postfix_expression PLUSPLUS')

    def p_postfix_expression_8(self, t):
        """postfix_expression : postfix_expression MINUSMINUS"""
        self.debug_out('PRODUCTION: postfix_expression : postfix_expression MINUSMINUS')

    #
    # primary-expression:
    #
    def p_primary_expression_identifier(self, t):
        """primary_expression :  identifier"""
        self.debug_out('PRODUCTION: primary_expression : identifier')

    def p_primary_expression_constant(self, t):
        """primary_expression : constant"""
        self.debug_out('PRODUCTION: primary_expression : constant')

    def p_primary_expression_sconst(self, t):
        """primary_expression : SCONST"""
        self.debug_out('PRODUCTION: primary_expression : SCONST')

    def p_primary_expression_parentesized(self, t):
        """primary_expression : LPAREN expression RPAREN"""
        self.debug_out('PRODUCTION: primary_expression : LPAREN expression RPAREN')

    #
    # argument-expression-list:
    #
    def p_argument_expression_list_assignment_expression(self, t):
        """argument_expression_list :  assignment_expression"""
        self.debug_out('PRODUCTION: argument_expression_list :  assignment_expression')

    def p_argument_expression_list_list_comma_expression(self, t):
        """argument_expression_list : argument_expression_list COMMA assignment_expression"""
        self.debug_out('PRODUCTION: argument_expression_list : argument_expression_list COMMA assignment_expression')

    #
    # constant:
    #
    def p_constant_int(self, t):
       """constant : ICONST"""
       self.debug_out('PRODUCTION: constant : ICONST')

    def p_constant_float(self, t):
       """constant : FCONST"""
       self.debug_out('PRODUCTION: constant : FCONST')

    def p_constant_char(self, t):
       """constant : CCONST"""
       self.debug_out('PRODUCTION: constant : CCONST')

    #
    # identifier:
    #
    def p_identifier(self, t):
        """identifier : ID"""
        self.debug_out('PRODUCTION: identifier : ID')

    #
    # empty:
    #
    def p_empty(self, t):
        """empty : """
        pass

/**
 *
 */

%{
    
int g_parser_debug_level = 0;
std::ostream PARSER_DEBUG_STREAM;

enum ParserDebugLevel {
  NONE = 0,
  DEBUG_PRODUCTIONS = 5
};
%}

%start translation_unit

%token IDENTIFIER 
%token INTEGER_CONSTANT FLOATING_CONSTANT CHARACTER_CONSTANT ENUMERATION_CONSTANT 
%token STRING_LITERAL 
%token SIZEOF
%token PTR_OP 
%token INC_OP DEC_OP 
%token LEFT_OP RIGHT_OP 
%token LE_OP GE_OP EQ_OP NE_OP
%token AND_OP OR_OP 
%token MUL_ASSIGN DIV_ASSIGN MOD_ASSIGN ADD_ASSIGN SUB_ASSIGN 
%token LEFT_ASSIGN RIGHT_ASSIGN AND_ASSIGN XOR_ASSIGN OR_ASSIGN

%token OPEN_CURLY CLOSE_CURLY OPEN_PAREN CLOSE_PAREN OPEN_SQUARE CLOSE_SQUARE
%token PLUS MINUS DIV MUL
%token COLON SEMI COMMA DOT TILDE Q_MARK
%token AND OR NOT MOD XOR EQUAL
%token LE GE 

%token TYPEDEF_NAME

%token TYPEDEF EXTERN STATIC AUTO REGISTER
%token CHAR SHORT INT LONG SIGNED UNSIGNED FLOAT DOUBLE CONST VOLATILE VOID
%token STRUCT UNION ENUM ELIPSIS RANGE

%token CASE DEFAULT IF ELSE SWITCH WHILE DO FOR GOTO CONTINUE BREAK RETURN

  /****************************************************************************/
%%

translation_unit:
  external_declaration {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "translation_unit -> external_declaration\n"); }
  |
  translation_unit external_declaration {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "translation_unit -> translation_unit external_declaration\n");
  }
  ;

external_declaration:
  function_definition {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "external_declaration -> function_definition\n");
  }
  |
  declaration {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "external_declaration -> declaration\n");
  }
  ;

function_definition:
  declarator compound_statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "function_definition -> declarator compound_statement\n");
  }
  |
  declarator declaration_list compound_statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "function_definition -> declarator declaration_list compound_statement\n");
  }
  |
  declaration_specifiers declarator compound_statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "function_definition -> declaration_specifiers declarator compound_statement\n");
  }
  |
  declaration_specifiers declarator declaration_list compound_statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "function_definition -> declaration_specifiers declarator declaration_list compound_statement\n");
  }
  ;

declaration:
  declaration_specifiers SEMI {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration -> declaration_specifiers SEMI\n");
  }
  |
  declaration_specifiers init_declarator_list SEMI {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration -> declaration_specifiers init_declarator_list SEMI\n");
  }
  ;

declaration_list:
  declaration {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_list -> declaration\n");
  }
  |
  declaration_list declaration {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_list -> declaration_list declaration\n");
  }
  ;

declaration_specifiers:
  storage_class_specifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_specifiers -> storage_class_specifier\n");
  }
  |
  storage_class_specifier declaration_specifiers {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_specifiers -> storage_class_specifier declaration_specifiers\n");
  }
  |
  type_specifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_specifiers -> type_specifier\n");
  }
  |
  type_specifier declaration_specifiers {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_specifiers -> type_specifier declaration_specifiers\n");
  }
  |
  type_qualifier  {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_specifiers -> type_qualifier\n");
  }
  |
  type_qualifier declaration_specifiers {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_specifiers -> type_qualifier declaration_specifiers\n");
  }
  ;

storage_class_specifier:
  AUTO {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "storage_class_specifier -> AUTO\n");
  }
  |
  REGISTER {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "storage_class_specifier -> REGISTER\n");
  }
  |
  STATIC {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "storage_class_specifier -> STATIC\n");
  }
  |
  EXTERN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "storage_class_specifier -> EXTERN\n");
  }
  |
  TYPEDEF {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "storage_class_specifier -> TYPEDEF\n");
  }
  ;

type_specifier:
  VOID {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> VOID\n");
  }
  |
  CHAR {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> CHAR\n");
  }
  |
  SHORT {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> SHORT\n");
  }
  |
  INT {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> INT\n");
  }
  |
  LONG {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> LONG\n");
  }
  |
  FLOAT  {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> FLOAT\n");
  }
  |
  DOUBLE {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> DOUBLE\n");
  }
  |
  SIGNED {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> SIGNED\n");
  }
  |
  UNSIGNED {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> UNSIGNED\n");
  }
  |
  struct_or_union_specifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> struct_or_union_specifier\n");
  }
  |
  enum_specifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> enum_specifier\n");
  }
  |
  TYPEDEF_NAME {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> TYPEDEF_NAME\n");
  }
  ;

type_qualifier:
  CONST {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type_qualifier -> CONST\n");
  }
  |
  VOLATILE {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type_qualifier -> VOLATILE\n");
  }
  ;

struct_or_union_specifier:
  struct_or_union identifier OPEN_CURLY struct_declaration_list CLOSE_CURLY {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_or_union_specifier -> struct_or_union identifier OPEN_CURLY struct_declaration_list CLOSE_CURLY\n");
  }
  |
  struct_or_union OPEN_CURLY struct_declaration_list CLOSE_CURLY {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_or_union_specifier -> struct_or_union OPEN_CURLY struct_declaration_list CLOSE_CURLY\n");
  }
  |
  struct_or_union identifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_or_union_specifier -> struct_or_union identifier\n");
  }
  ;

struct_or_union:
  STRUCT {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_or_union -> STRUCT\n");
  }
  |
  UNION {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_or_union -> UNION\n");
  }
  ;

struct_declaration_list:
  struct_declaration {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declaration_list -> struct_declaration\n");
  }
  |
  struct_declaration_list struct_declaration {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declaration_list -> struct_declaration_list struct_declaration\n");
  }
  ;

init_declarator_list:
  init_declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "init_declarator_list -> init_declarator\n");
  }
  |
  init_declarator_list COMMA init_declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "init_declarator_list -> init_declarator_list COMMA init_declarator\n");
  }
  ;

init_declarator:
  declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "init_declarator -> declarator\n");
  }
  |
  declarator EQUAL initializer {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "init_declarator -> declarator EQUAL initializer\n");
  }
  ;

struct_declaration:
  specifier_qualifier_list struct_declarator_list SEMI {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declaration -> specifier_qualifier_list struct_declarator_list SEMI\n");
  }
  ;

specifier_qualifier_list:
  type_specifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "specifier_qualifier_list -> type_specifier\n");
  }
  |
  type_specifier specifier_qualifier_list {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "specifier_qualifier_list -> type_specifier specifier_qualifier_list\n");
  }
  |
  type_qualifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "specifier_qualifier_list -> type_qualifier\n");
  }
  |
  type_qualifier specifier_qualifier_list {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "specifier_qualifier_list -> type_qualifier specifier_qualifier_list\n");
  }
  ;

struct_declarator_list:
  struct_declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declarator_list -> struct_declarator\n");
  }
  |
  struct_declarator_list COMMA struct_declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declarator_list -> struct_declarator_list COMMA struct_declarator\n");
  }
  ;

struct_declarator:
  declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declarator -> declarator\n");
  }
  |
  COLON constant_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declarator -> COLON constant_expression\n");
  }
  |
  declarator COLON constant_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declarator -> declarator COLON constant_expression\n");
  }
  ;

enum_specifier:
  ENUM OPEN_CURLY enumerator_list CLOSE_CURLY {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enum_specifier -> ENUM OPEN_CURLY enumerator_list CLOSE_CURLY\n");
  }
  |
  ENUM identifier OPEN_CURLY enumerator_list CLOSE_CURLY {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enum_specifier -> ENUM identifier OPEN_CURLY enumerator_list CLOSE_CURLY\n");
  }
  |
  ENUM identifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enum_specifier -> ENUM identifier\n");
  }
  ;

enumerator_list:
  enumerator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enumerator_list -> enumerator\n");
  }
  |
  enumerator_list COMMA enumerator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enumerator_list -> enumerator_list COMMA enumerator\n");
  }
  ;

enumerator:
  identifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enumerator -> identifier\n");
  }
  |
  identifier EQUAL constant_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enumerator -> identifier EQUAL constant_expression\n");
  }
  ;

declarator:
  direct_declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declarator -> direct_declarator\n");
  }
  |
  pointer direct_declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declarator -> pointer direct_declarator\n");
  }
  ;

direct_declarator:
  identifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> identifier\n");
  }
  |
  OPEN_PAREN declarator CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> OPEN_PAREN declarator CLOSE_PAREN\n");
  }
  |
  direct_declarator OPEN_SQUARE CLOSE_SQUARE {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> direct_declarator OPEN_SQUARE CLOSE_SQUARE\n");
  }
  |
  direct_declarator OPEN_SQUARE constant_expression CLOSE_SQUARE {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> direct_declarator OPEN_SQUARE constant_expression CLOSE_SQUARE\n");
  }
  |
  direct_declarator OPEN_PAREN CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> direct_declarator OPEN_PAREN CLOSE_PAREN\n");
  }
  |
  direct_declarator OPEN_PAREN parameter_type_list CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> direct_declarator OPEN_PAREN parameter_type_list CLOSE_PAREN\n");
  }
  |
  direct_declarator OPEN_PAREN identifier_list CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> direct_declarator OPEN_PAREN identifier_list CLOSE_PAREN\n");
  }
  ;

pointer:
  MUL {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "pointer -> MUL\n");
  }
  |
  MUL type_qualifier_list {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "pointer -> MUL type_qualifier_list\n");
  }
  |
  MUL pointer {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "pointer -> MUL pointer\n");
  }
  |
  MUL type_qualifier_list pointer {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "pointer -> MUL type_qualifier_list pointer\n");
  }
  ;

type_qualifier_list:
  type_qualifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type_qualifier_list -> type_qualifier\n");
  }
  |
  type_qualifier_list type_qualifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type_qualifier_list -> type_qualifier_list type_qualifier\n");
  }
  ;

parameter_type_list:
  parameter_list {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_type_list -> parameter_list\n");
  }
  |
  parameter_list COMMA ELIPSIS {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_type_list -> parameter_list COMMA ELIPSIS\n");
  }
  ;

parameter_list:
  parameter_declaration {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_list -> parameter_declaration\n");
  }
  |
  parameter_list COMMA parameter_declaration {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_list -> parameter_list COMMA parameter_declaration\n");
  }
  ;

parameter_declaration:
  declaration_specifiers declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_declaration -> declaration_specifiers declarator\n");
  }
  |
  declaration_specifiers {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_declaration -> declaration_specifiers\n");
  }
  |
  declaration_specifiers abstract_declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_declaration -> declaration_specifiers abstract_declarator\n");
  }
  ;

identifier_list:
  identifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "identifier_list -> identifier\n");
  }
  |
  identifier_list COMMA identifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "identifier_list -> identifier_list COMMA identifier\n");
  }
  ;

initializer:
  assignment_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "initializer -> assignment_expression\n");
  }
  |
  OPEN_CURLY initializer_list CLOSE_CURLY {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "initializer -> OPEN_CURLY initializer_list CLOSE_CURLY\n");
  }
  |
  OPEN_CURLY initializer_list COMMA CLOSE_CURLY {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "initializer -> OPEN_CURLY initializer_list COMMA CLOSE_CURLY\n");
  }
  ;

initializer_list:
  initializer {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "initializer_list -> initializer\n");
  }
  |
  initializer_list COMMA initializer {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "initializer_list -> initializer_list COMMA initializer\n");
  }
  ;

type_name:
  specifier_qualifier_list {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type_name -> specifier_qualifier_list\n");
  }
  |
  specifier_qualifier_list abstract_declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type_name -> specifier_qualifier_list abstract_declarator\n");
  }
  ;

abstract_declarator:
  pointer {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "abstract_declarator -> pointer\n");
  }
  |
  direct_abstract_declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "abstract_declarator -> direct_abstract_declarator\n");
  }
  |
  pointer direct_abstract_declarator {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "abstract_declarator -> pointer direct_abstract_declarator\n");
  }
  ;

direct_abstract_declarator:
  OPEN_PAREN abstract_declarator CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> OPEN_PAREN abstract_declarator CLOSE_PAREN\n");
  }
  |
  OPEN_SQUARE CLOSE_SQUARE {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> OPEN_SQUARE CLOSE_SQUARE\n");
  }
  |
  OPEN_SQUARE constant_expression CLOSE_SQUARE {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> OPEN_SQUARE constant_expression CLOSE_SQUARE\n");
  }
  |
  direct_abstract_declarator OPEN_SQUARE CLOSE_SQUARE {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> direct_abstract_declarator OPEN_SQUARE CLOSE_SQUARE\n");
  }
  |
  direct_abstract_declarator OPEN_SQUARE constant_expression CLOSE_SQUARE {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> direct_abstract_declarator OPEN_SQUARE constant_expression CLOSE_SQUARE\n");
  }
  |
  OPEN_PAREN CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> OPEN_PAREN CLOSE_PAREN\n");
  }
  |
  OPEN_PAREN parameter_type_list CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> OPEN_PAREN parameter_type_list CLOSE_PAREN\n");
  }
  |
  direct_abstract_declarator OPEN_PAREN CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> direct_abstract_declarator OPEN_PAREN CLOSE_PAREN\n");
  }
  |
  direct_abstract_declarator OPEN_PAREN parameter_type_list CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> direct_abstract_declarator OPEN_PAREN parameter_type_list CLOSE_PAREN\n");
  }
  ;

statement:
  labeled_statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement -> labeled_statement\n");
  }
  |
  compound_statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement -> compound_statement\n");
  }
  |
  expression_statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement -> expression_statement\n");
  }
  |
  selection_statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement -> selection_statement\n");
  }
  |
  iteration_statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement -> iteration_statement\n");
  }
  |
  jump_statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement -> jump_statement\n");
  }
  ;

labeled_statement:
  identifier COLON statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "labeled_statement -> identifier COLON statement\n");
  }
  |
  CASE constant_expression COLON statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "labeled_statement -> CASE constant_expression COLON statement\n");
  }
  |
  DEFAULT COLON statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "labeled_statement -> DEFAULT COLON statement\n");
  }
  ;

expression_statement:
  SEMI {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "expression_statement -> SEMI\n");
  }
  |
  expression SEMI {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "expression_statement -> expression SEMI\n");
  }
  ;

compound_statement:
  OPEN_CURLY CLOSE_CURLY {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "compound_statement -> OPEN_CURLY CLOSE_CURLY\n");
  }
  |
  OPEN_CURLY statement_list CLOSE_CURLY {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "compound_statement -> OPEN_CURLY statement_list CLOSE_CURLY\n");
  }
  |
  OPEN_CURLY declaration_list CLOSE_CURLY {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "compound_statement -> OPEN_CURLY declaration_list CLOSE_CURLY\n");
  }
  |
  OPEN_CURLY declaration_list statement_list CLOSE_CURLY {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "compound_statement -> OPEN_CURLY declaration_list statement_list CLOSE_CURLY\n");
  }
  ;

statement_list:
  statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement_list -> statement\n");
  }
  |
  statement_list statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement_list -> statement_list statement\n");
  }
  ;

selection_statement:
  IF OPEN_PAREN expression CLOSE_PAREN statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "selection_statement -> IF OPEN_PAREN expression CLOSE_PAREN statement\n");
  }
  |
  IF OPEN_PAREN expression CLOSE_PAREN statement ELSE statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "selection_statement -> IF OPEN_PAREN expression CLOSE_PAREN statement ELSE statement\n");
  }
  |
  SWITCH OPEN_PAREN expression CLOSE_PAREN statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "selection_statement -> SWITCH OPEN_PAREN expression CLOSE_PAREN statement\n");
  }
  ;

iteration_statement:
  WHILE OPEN_PAREN expression CLOSE_PAREN statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> WHILE OPEN_PAREN expression CLOSE_PAREN statement\n");
  }
  |
  DO statement WHILE OPEN_PAREN expression CLOSE_PAREN SEMI {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> DO statement WHILE OPEN_PAREN expression CLOSE_PAREN SEMI\n");
  }
  |
  FOR OPEN_PAREN SEMI SEMI CLOSE_PAREN statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN SEMI SEMI CLOSE_PAREN statement\n");
  }
  |
  FOR OPEN_PAREN SEMI SEMI expression CLOSE_PAREN statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN SEMI SEMI expression CLOSE_PAREN statement\n");
  }
  |
  FOR OPEN_PAREN SEMI expression SEMI CLOSE_PAREN statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN SEMI expression SEMI CLOSE_PAREN statement\n");
  }
  |
  FOR OPEN_PAREN SEMI expression SEMI expression CLOSE_PAREN statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN SEMI expression SEMI expression CLOSE_PAREN statement\n");
  }
  |
  FOR OPEN_PAREN expression SEMI SEMI CLOSE_PAREN statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN expression SEMI SEMI CLOSE_PAREN statement\n");
  }
  |
  FOR OPEN_PAREN expression SEMI SEMI expression CLOSE_PAREN statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN expression SEMI SEMI expression CLOSE_PAREN statement\n");
  }
  |
  FOR OPEN_PAREN expression SEMI expression SEMI CLOSE_PAREN statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN expression SEMI expression SEMI CLOSE_PAREN statement\n");
  }
  |
  FOR OPEN_PAREN expression SEMI expression SEMI expression CLOSE_PAREN statement {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN expression SEMI expression SEMI expression CLOSE_PAREN statement\n");
  }
  ;

jump_statement:
  GOTO identifier SEMI {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "jump_statement -> GOTO identifier SEMI\n");
  }
  |
  CONTINUE SEMI {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "jump_statement -> CONTINUE SEMI\n");
  }
  |
  BREAK SEMI {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "jump_statement -> BREAK SEMI\n");
  }
  |
  RETURN SEMI {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "jump_statement -> RETURN SEMI\n");
  }
  |
  RETURN expression SEMI {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "jump_statement -> RETURN expression SEMI\n");
  }
  ;

expression:
  assignment_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "expression -> assignment_expression\n");
  }
  |
  expression COMMA assignment_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "expression -> expression COMMA assignment_expression\n");
  }
  ;

assignment_expression:
  conditional_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_expression -> conditional_expression\n");
  }
  |
  unary_expression assignment_operator assignment_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_expression -> unary_expression assignment_operator assignment_expression\n");
  }
  ;

assignment_operator:
  EQUAL {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> EQUAL\n");
  }
  |
  MUL_ASSIGN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> MUL_ASSIGN\n");
  }
  |
  DIV_ASSIGN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> DIV_ASSIGN\n");
  }
  |
  MOD_ASSIGN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> MOD_ASSIGN\n");
  }
  |
  ADD_ASSIGN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> ADD_ASSIGN\n");
  }
  |
  SUB_ASSIGN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> SUB_ASSIGN\n");
  }
  |
  LEFT_ASSIGN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> LEFT_ASSIGN\n");
  }
  |
  RIGHT_ASSIGN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> RIGHT_ASSIGN\n");
  }
  |
  AND_ASSIGN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> AND_ASSIGN\n");
  }
  |
  XOR_ASSIGN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> XOR_ASSIGN\n");
  }
  |
  OR_ASSIGN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> OR_ASSIGN\n");
  }
  ;

conditional_expression:
  logical_or_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "conditional_expression -> logical_or_expression\n");
  }
  |
  logical_or_expression Q_MARK expression COLON conditional_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "conditional_expression -> logical_or_expression Q_MARK expression COLON conditional_expression\n");
  }
  ;

constant_expression:
  conditional_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "constant_expression -> conditional_expression\n");
  }
  ;

logical_or_expression:
  logical_and_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "logical_or_expression -> logical_and_expression\n");
  }
  |
  logical_or_expression OR_OP logical_and_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "logical_or_expression -> logical_or_expression OR_OP logical_and_expression\n");
  }
  ;

logical_and_expression:
  inclusive_or_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "logical_and_expression -> inclusive_or_expression\n");
  }
  |
  logical_and_expression AND_OP inclusive_or_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "logical_and_expression -> logical_and_expression AND_OP inclusive_or_expression\n");
  }
  ;

inclusive_or_expression:
  exclusive_or_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "inclusive_or_expression -> exclusive_or_expression\n");
  }
  |
  inclusive_or_expression OR exclusive_or_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "inclusive_or_expression -> inclusive_or_expression OR exclusive_or_expression\n");
  }
  ;

exclusive_or_expression:
  and_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "exclusive_or_expression -> and_expression\n");
  }
  |
  exclusive_or_expression XOR and_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "exclusive_or_expression -> exclusive_or_expression XOR and_expression\n");
  }
  ;

and_expression:
  equality_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "and_expression -> equality_expression\n");
  }
  |
  and_expression AND equality_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "and_expression -> and_expression AND equality_expression\n");
  }
  ;

equality_expression:
  relational_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "equality_expression -> relational_expression\n");
  }
  |
  equality_expression EQ_OP relational_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "equality_expression -> equality_expression EQ_OP relational_expression\n");
  }
  |
  equality_expression NE_OP relational_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "equality_expression -> equality_expression NE_OP relational_expression\n");
  }
  ;

relational_expression:
  shift_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "relational_expression -> shift_expression\n");
  }
  |
  relational_expression LE shift_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "relational_expression -> relational_expression LE shift_expression\n");
  }
  |
  relational_expression GE shift_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "relational_expression -> relational_expression GE shift_expression\n");
  }
  |
  relational_expression LE_OP shift_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "relational_expression -> relational_expression LE_OP shift_expression\n");
  }
  |
  relational_expression GE_OP shift_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "relational_expression -> relational_expression GE_OP shift_expression\n");
  }
  ;

shift_expression:
  additive_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "shift_expression -> additive_expression\n");
  }
  |
  shift_expression LEFT_OP additive_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "shift_expression -> shift_expression LEFT_OP additive_expression\n");
  }
  |
  shift_expression RIGHT_OP additive_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "shift_expression -> shift_expression RIGHT_OP additive_expression\n");
  }
  ;

additive_expression:
  multiplicative_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "additive_expression -> multiplicative_expression\n");
  }
  |
  additive_expression PLUS multiplicative_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "additive_expression -> additive_expression PLUS multiplicative_expression\n");
  }
  |
  additive_expression MINUS multiplicative_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "additive_expression -> additive_expression MINUS multiplicative_expression\n");
  }
  ;

multiplicative_expression:
  cast_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "multiplicative_expression -> cast_expression\n");
  }
  |
  multiplicative_expression MUL cast_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "multiplicative_expression -> multiplicative_expression MUL cast_expression\n");
  }
  |
  multiplicative_expression DIV cast_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "multiplicative_expression -> multiplicative_expression DIV cast_expression\n");
  }
  |
  multiplicative_expression MOD cast_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "multiplicative_expression -> multiplicative_expression MOD cast_expression\n");
  }
  ;

cast_expression:
  unary_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "cast_expression -> unary_expression\n");
  }
  |
  OPEN_PAREN type_name CLOSE_PAREN cast_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "cast_expression -> OPEN_PAREN type_name CLOSE_PAREN cast_expression\n");
  }
  ;

unary_expression:
  postfix_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_expression -> postfix_expression\n");
  }
  |
  INC_OP unary_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_expression -> INC_OP unary_expression\n");
  }
  |
  DEC_OP unary_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_expression -> DEC_OP unary_expression\n");
  }
  |
  unary_operator cast_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_expression -> unary_operator cast_expression\n");
  }
  |
  SIZEOF unary_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_expression -> SIZEOF unary_expression\n");
  }
  |
  SIZEOF OPEN_PAREN type_name CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_expression -> SIZEOF OPEN_PAREN type_name CLOSE_PAREN\n");
  }
  ;

unary_operator:
  AND {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_operator -> AND\n");
  }
  |
  MUL {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_operator -> MUL\n");
  }
  |
  PLUS {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_operator -> PLUS\n");
  }
  |
  MINUS {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_operator -> MINUS\n");
  }
  |
  TILDE {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_operator -> TILDE\n");
  }
  |
  NOT {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_operator -> NOT\n");
  }
  ;

postfix_expression:
  primary_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> primary_expression\n");
  }
  |
  postfix_expression OPEN_SQUARE expression CLOSE_SQUARE {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression OPEN_SQUARE expression CLOSE_SQUARE\n");
  }
  |
  postfix_expression OPEN_PAREN CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression OPEN_PAREN CLOSE_PAREN\n");
  }
  |
  postfix_expression OPEN_PAREN argument_expression_list CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression OPEN_PAREN argument_expression_list CLOSE_PAREN\n");
  }
  |
  postfix_expression DOT identifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression DOT identifier\n");
  }
  |
  postfix_expression PTR_OP identifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression PTR_OP identifier\n");
  }
  |
  postfix_expression INC_OP {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression INC_OP\n");
  }
  |
  postfix_expression DEC_OP {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression DEC_OP\n");
  }
  ;

primary_expression:
  identifier {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "primary_expression -> identifier\n");
  }
  |
  constant {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "primary_expression -> constant\n");
  }
  |
  string {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "primary_expression -> string\n");
  }
  |
  OPEN_PAREN expression CLOSE_PAREN {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "primary_expression -> OPEN_PAREN expression CLOSE_PAREN\n");
  }
  ;

argument_expression_list:
  assignment_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "argument_expression_list -> assignment_expression\n");
  }
  |
  argument_expression_list COMMA assignment_expression {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "argument_expression_list -> argument_expression_list COMMA assignment_expression\n");
  }
  ;

constant:
  INTEGER_CONSTANT {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "constant -> INTEGER_CONSTANT\n");
  }
  |
  CHARACTER_CONSTANT {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "constant -> CHARACTER_CONSTANT\n");
  }
  |
  FLOATING_CONSTANT {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "constant -> FLOATING_CONSTANT\n");
  }
  |
  ENUMERATION_CONSTANT {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "constant -> ENUMERATION_CONSTANT\n");
  }
  ;

string:
  STRING_LITERAL {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "string -> STRING_LITERAL\n");
  }
  ;

identifier:
  IDENTIFIER {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "identifier -> IDENTIFIER\n");
  }
  ;

%%


void
debug_log(const int level, ostream& stream,
                      const char* message) {
    
/**
 * A very plain debug output function. Makes use of the global debug
 * level flag and stream for parser output.
 */

  if (level == DEBUG_PRODUCTIONS 0) {
    
    stream << message;
  }
}

yyerror(s)
char *s; {
    

  // TODO: define me!

}

/**
 *
 */

%{

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


%%

translation_unit:
  external_declaration {}
  |
  translation_unit external_declaration {}
  ;

external_declaration:
  function_definition {}
  |
  declaration {}
  ;

function_definition:
  declarator compound_statement {}
  |
  declarator declaration_list compound_statement {}
  |
  declaration_specifiers declarator compound_statement {}
  |
  declaration_specifiers declarator declaration_list compound_statement {}
  ;

declaration:
  declaration_specifiers SEMI {}
  |
  declaration_specifiers init_declarator_list SEMI {}
  ;

declaration_list:
  declaration {}
  |
  declaration_list declaration {}
  ;

declaration_specifiers:
  storage_class_specifier {}
  |
  storage_class_specifier declaration_specifiers {}
  |
  type_specifier {}
  |
  type_specifier declaration_specifiers {}
  |
  type_qualifier  {}
  |
  type_qualifier declaration_specifiers {}
  ;

storage_class_specifier:
  AUTO {}
  |
  REGISTER {}
  |
  STATIC {}
  |
  EXTERN {}
  |
  TYPEDEF {}
  ;

type_specifier:
  VOID {}
  |
  CHAR {}
  |
  SHORT {}
  |
  INT {}
  |
  LONG {}
  |
  FLOAT  {}
  |
  DOUBLE {}
  |
  SIGNED {}
  |
  UNSIGNED {}
  |
  struct_or_union_specifier {}
  |
  enum_specifier {}
  |
  TYPEDEF_NAME {}
  ;

type_qualifier:
  CONST {}
  |
  VOLATILE {}
  ;

struct_or_union_specifier:
  struct_or_union identifier OPEN_CURLY struct_declaration_list CLOSE_CURLY {}
  |
  struct_or_union OPEN_CURLY struct_declaration_list CLOSE_CURLY {}
  |
  struct_or_union identifier {}
  ;

struct_or_union:
  STRUCT {}
  |
  UNION {}
  ;

struct_declaration_list:
  struct_declaration {}
  |
  struct_declaration_list struct_declaration {}
  ;

init_declarator_list:
  init_declarator {}
  |
  init_declarator_list COMMA init_declarator {}
  ;

init_declarator:
  declarator {}
  |
  declarator EQUAL initializer {}
  ;

struct_declaration:
  specifier_qualifier_list struct_declarator_list SEMI {}
  ;

specifier_qualifier_list:
  type_specifier {}
  |
  type_specifier specifier_qualifier_list {}
  |
  type_qualifier {}
  |
  type_qualifier specifier_qualifier_list {}
  ;

struct_declarator_list:
  struct_declarator {}
  |
  struct_declarator_list COMMA struct_declarator {}
  ;

struct_declarator:
  declarator {}
  |
  COLON constant_expression {}
  |
  declarator COLON constant_expression {}
  ;

enum_specifie:
  ENUM OPEN_CURLY enumerator_list CLOSE_CURLY {}
  |
  ENUM identifier OPEN_CURLY enumerator_list CLOSE_CURLY {}
  |
  ENUM identifier {}
  ;

enumerator_list:
  enumerator {}
  |
  enumerator_list COMMA enumerator {}
  ;

enumerator:
  identifier {}
  |
  identifier EQUAL constant_expression {}
  ;

declarator:
  direct_declarator {}
  |
  pointer direct_declarator {}
  ;

direct_declarator:
  identifier {}
  |
  OPEN_PAREN declarator CLOSE_PAREN {}
  |
  direct_declarator OPEN_SQUARE CLOSE_SQUARE {}
  |
  direct_declarator OPEN_SQUARE constant_expression CLOSE_SQUARE {}
  |
  direct_declarator OPEN_PAREN CLOSE_PAREN {}
  |
  direct_declarator OPEN_PAREN parameter_type_list CLOSE_PAREN {}
  |
  direct_declarator OPEN_PAREN identifier_list CLOSE_PAREN {}
  ;

pointer:
  MUL {}
  |
  MUL type_qualifier_list {}
  |
  MUL pointer {}
  |
  MUL type_qualifier_list pointer {}
  ;

type_qualifier_list:
  type_qualifier {}
  |
  type_qualifier_list type_qualifier {}
  ;

parameter_type_list:
  parameter_list {}
  |
  parameter_list COMMA ELIPSIS {}
  ;

parameter_list:
  parameter_declaration {}
  |
  parameter_list COMMA parameter_declaration {}
  ;

parameter_declaration:
  declaration_specifiers declarator {}
  |
  declaration_specifiers {}
  |
  declaration_specifiers abstract_declarator {}
  ;

identifier_list:
  identifier {}
  |
  identifier_list COMMA identifier {}
  ;

initializer:
  assignment_expression {}
  |
  OPEN_CURLY initializer_list CLOSE_CURLY {}
  |
  OPEN_CURLY initializer_list COMMA CLOSE_CURLY {}
  ;

initializer_list:
  initializer {}
  |
  initializer_list COMMA initializer {}
  ;

type_name:
  specifier_qualifier_list {}
  |
  specifier_qualifier_list abstract_declarator {}
  ;

abstract_declarator:
  pointer {}
  |
  direct_abstract_declarator {}
  |
  pointer direct_abstract_declarator {}
  ;

direct_abstract_declarator:
  OPEN_PAREN abstract_declarator CLOSE_PAREN {}
  |
  OPEN_SQUARE CLOSE_SQUARE {}
  |
  OPEN_SQUARE constant_expression CLOSE_SQUARE {}
  |
  direct_abstract_declarator OPEN_SQUARE CLOSE_SQUARE {}
  |
  direct_abstract_declarator OPEN_SQUARE constant_expression CLOSE_SQUARE {}
  |
  OPEN_PAREN CLOSE_PAREN {}
  |
  OPEN_PAREN parameter_type_list CLOSE_PAREN {}
  |
  direct_abstract_declarator OPEN_PAREN CLOSE_PAREN {}
  |
  direct_abstract_declarator OPEN_PAREN parameter_type_list CLOSE_PAREN {}
  ;

statement:
  labeled_statement {}
  |
  compound_statement {}
  |
  expression_statement {}
  |
  selection_statement {}
  |
  iteration_statement {}
  |
  jump_statement {}
  ;

labeled_statement:
  identifier COLON statement {}
  |
  CASE constant_expression COLON statement {}
  |
  DEFAULT COLON statement {}
  ;

expression_statement:
  SEMI {}
  |
  expression SEMI {}
  ;

compound_statement:
  OPEN_CURLY CLOSE_CURLY {}
  |
  OPEN_CURLY statement_list CLOSE_CURLY {}
  |
  OPEN_CURLY declaration_list CLOSE_CURLY {}
  |
  OPEN_CURLY declaration_list statement_list CLOSE_CURLY {}
  ;

statement_list:
  statement {}
  |
  statement_list statement {}
  ;

selection_statement:
  IF OPEN_PAREN expression CLOSE_PAREN statement {}
  |
  IF OPEN_PAREN expression CLOSE_PAREN statement ELSE statement {}
  |
  SWITCH OPEN_PAREN expression CLOSE_PAREN statement {}
  ;

iteration_statement:
  WHILE OPEN_PAREN expression CLOSE_PAREN statement {}
  |
  DO statement WHILE OPEN_PAREN expression CLOSE_PAREN SEMI {}
  |
  FOR OPEN_PAREN SEMI SEMI CLOSE_PAREN statement {}
  |
  FOR OPEN_PAREN SEMI SEMI expression CLOSE_PAREN statement {}
  |
  FOR OPEN_PAREN SEMI expression SEMI CLOSE_PAREN statement {}
  |
  FOR OPEN_PAREN SEMI expression SEMI expression CLOSE_PAREN statement {}
  |
  FOR OPEN_PAREN expression SEMI SEMI CLOSE_PAREN statement {}
  |
  FOR OPEN_PAREN expression SEMI SEMI expression CLOSE_PAREN statement {}
  |
  FOR OPEN_PAREN expression SEMI expression SEMI CLOSE_PAREN statement {}
  |
  FOR OPEN_PAREN expression SEMI expression SEMI expression CLOSE_PAREN statement {}
  ;

jump_statement:
  GOTO identifier SEMI {}
  |
  CONTINUE SEMI {}
  |
  BREAK SEMI {}
  |
  RETURN SEMI {}
  |
  RETURN expression SEMI {}
  ;

expression:
  assignment_expression {}
  |
  expression COMMA assignment_expression {}
  ;

assignment_expression:
  conditional_expression {}
  |
  unary_expression assignment_operator assignment_expression {}
  ;

assignment_operator:
  EQUAL {}
  |
  MUL_ASSIGN {}
  |
  DIV_ASSIGN {}
  |
  MOD_ASSIGN {}
  |
  ADD_ASSIGN {}
  |
  SUB_ASSIGN {}
  |
  LEFT_ASSIGN {}
  |
  RIGHT_ASSIGN {}
  |
  AND_ASSIGN {}
  |
  XOR_ASSIGN {}
  |
  OR_ASSIGN {}
  ;

conditional_expression:
  logical_or_expression {}
  |
  logical_or_expression Q_MARK expression COLON conditional_expression {}
  ;

constant_expression:
  conditional_expression {}
  ;

logical_or_expression:
  logical_and_expression {}
  |
  logical_or_expression OR_OP logical_and_expression {}
  ;

logical_and_expression:
  inclusive_or_expression {}
  |
  logical_and_expression AND_OP inclusive_or_expression {}
  ;

inclusive_or_expression:
  exclusive_or_expression {}
  |
  inclusive_or_expression OR exclusive_or_expression {}
  ;

exclusive_or_expression:
  and_expression {}
  |
  exclusive_or_expression XOR and_expression {}
  ;

and_expression:
  equality_expression {}
  |
  and_expression AND equality_expression {}
  ;

equality_expression:
  relational_expression {}
  |
  equality_expression EQ_OP relational_expression {}
  |
  equality_expression NE_OP relational_expression {}
  ;

relational_expression:
  shift_expression {}
  |
  relational_expression LE shift_expression {}
  |
  relational_expression GE shift_expression {}
  |
  relational_expression LE_OP shift_expression {}
  |
  relational_expression GE_OP shift_expression {}
  ;

shift_expression:
  additive_expression {}
  |
  shift_expression LEFT_OP additive_expression {}
  |
  shift_expression RIGHT_OP additive_expression {}
  ;

additive_expression:
  multiplicative_expression {}
  |
  additive_expression PLUS multiplicative_expression {}
  |
  additive_expression MINUS multiplicative_expression {}
  ;

multiplicative_expression:
  cast_expression {}
  |
  multiplicative_expression MUL cast_expression {}
  |
  multiplicative_expression DIV cast_expression {}
  |
  multiplicative_expression MOD cast_expression {}
  ;

cast_expressio:
  unary_expression {}
  |
  OPEN_PAREN type_name CLOSE_PAREN cast_expression {}
  ;

unary_expression:
  postfix_expression {}
  |
  INC_OP unary_expression {}
  |
  DEC_OP unary_expression {}
  |
  unary_operator cast_expression {}
  |
  SIZEOF unary_expression {}
  |
  SIZEOF OPEN_PAREN type_name CLOSE_PAREN {}
  ;

unary_operator:
  AND {}
  |
  MUL {}
  |
  PLUS {}
  |
  MINUS {}
  |
  TILDE {}
  |
  NOT {}
  ;

postfix_expression:
  primary_expression {}
  |
  postfix_expression OPEN_SQUARE expression CLOSE_SQUARE {}
  |
  postfix_expression OPEN_PAREN CLOSE_PAREN {}
  |
  postfix_expression OPEN_PAREN argument_expression_list CLOSE_PAREN {}
  |
  postfix_expression '.' identifier {}
  |
  postfix_expression PTR_OP identifier {}
  |
  postfix_expression INC_OP {}
  |
  postfix_expression DEC_OP {}
  ;

primary_expression:
  identifier {}
  |
  constant {}
  |
  string {}
  |
  OPEN_PAREN expression CLOSE_PAREN {}
  ;

argument_expression_list:
  assignment_expression {}
  |
  argument_expression_list COMMA assignment_expression {}
  ;

constant:
  INTEGER_CONSTANT {}
  |
  CHARACTER_CONSTANT {}
  |
  FLOATING_CONSTANT {}
  |
  ENUMERATION_CONSTANT {}
  ;

string:
  STRING_LITERAL {}
  ;

identifier:
  IDENTIFIER {}
  ;

%%

yyerror(s)
char *s; {

  // TODO: define me!

}

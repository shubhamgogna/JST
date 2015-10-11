/*******************************************/
/* PA 6 - Lexical Analyzer                 */
/* JST Compiler                */
/*******************************************/


%{
#include <stdio.h>
#include <stdlib.h>
#include "jstc_parser.tab.h"

int yycolumn = 1;

#define YY_USER_ACTION \
    yylloc.first_line = yylloc.last_line = yylineno; \
      yylloc.first_column = yycolumn; \
      yylloc.last_column = yycolumn + yyleng - 1; \
      yycolumn += yyleng; \
      yylval.str = strdup(yytext);
%}
%option yylineno

/*******************************************/
/* Definitions                             */
/*******************************************/

digit [0-9]
number  {digit}+

ID

/*******************************************/
/* Token Descriptions and Actions          */
/*******************************************/

%%
  int line_num;
  int col_num;


"!!S"         {  /* Dump Symbol Table - NEED TO HAVE T ADD TO PARSER*/  }

IDENTIFIER

INTEGER_CONSTANT
FLOATING_CONSTANT
CHARACTER_CONSTANT
ENUMERATION_CONSTANT
STRING_LITERAL

"sizeof"      {  /* */  }

"->"          {  return PTR_OP;  }

"++"          {  return INC_OP;  }      
"--"          {  return DEC_OP;  }

"<<"          {  return LEFT_OP;  }
">>"          {  return RIGHT_OP;  }

"<="          {  return LE_OP;  }
">="          {  return GE_OP;  }
"=="          {  return EQ_OP;  }
"!="          {  return NE_OP;  }

"&&"          {  return AND_OP;  }
"||"          {  return OR_OP;  }

"*="          {  return MUL_ASSIGN;  }
"/="          {  return DIV_ASSIGN;  }
"%="          {  return MOD_ASSIGN;  }
"+="          {  return ADD_ASSIGN;  }
"-="          {  return SUB_ASSIGN;  }

"<<="         {  return LEFT_ASSIGN;  }
">>="         {  return RIGHT_ASSIGN;  }
"&="          {  return AND_ASSIGN;  }
"^="          {  return XOR_ASSIGN;  }
"|="          {  return OR_ASSIGN;  }

"{"           {  return OPEN_CURLY;  }
"}"           {  return CLOSE_CURLY;  }
"("           {  return OPEN_PAREN;  }
")"           {  return CLOSE_PAREN;  }
"["           {  return OPEN_SQUARE;  }
"]"           {  return CLOSE_SQUARE;  }

"+"           {  return PLUS;  }
"-"           {  return MINUS;  }
"/"           {  return DIV;  }
"*"           {  return MUL;  }

":"           {  return COLON;  }
";"           {  return SEMI;  }
","           {  return COMMA;  }
"."           {  return DOT;  }
"~"           {  return TILDE;  }
"?"           {  return Q_MARK;  }

"&"           {  return AND;  }
"|"           {  return OR;  }
"!"           {  return NOT;  }
"%"           {  return MOD;  }
"^"           {  return XOR;  }
"="           {  return EQUAL;  }

"<"           {  return LE;  }
">"           {  return GE;  }


TYPEDEF_NAME

"typedef"     {  return TYPEDEF;  }
"extern"      {  return EXTERN;  }
"static"      {  return STATIC;  }
"auto"        {  return AUTO;  }
"register"    {  return REGISTER;  }

"char"        {  return CHAR;  }
"short"       {  return SHORT;  }
"int"         {  return INT;  }
"long"        {  return LONG;  }
"signed"      {  return SIGNED;  }
"unsigned"    {  return UNSIGNED;  }
"float"       {  return FLOAT;  }
"double"      {  return DOUBLE;  }
"const"       {  return CONST;  }
"volatile"    {  return VOLATILE;  }
"void"        {  return VOID;  }

"struct"      {  return STRUCT;  }
"union"       {  return UNION;  }
"enum"        {  return ENUM;  }
"..."         {  return ELIPSIS;  }
RANGE         {  /* */  }

"case"        {  return CASE;  } 
"default"     {  return DEFAULT;  }
"if"          {  return IF;  }
"else"        {  return ELSE;  }
"switch"      {  return SWITCH;  }
"while"       {  return WHILE;  }
"do"          {  return DO;  }
"for"         {  return FOR;  }
"goto"        {  return GOTO;  }
"continue"    {  return CONTINUE;  } 
"break"       {  return BREAK;  } 
"return"      {  return RETURN;  }



%%

/*******************************************/
/* User-Written Code                       */
/*******************************************/





/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.0.4"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* Copy the first part of user declarations.  */
#line 5 "jstc_parser.yacc" /* yacc.c:339  */

    
int g_parser_debug_level = 0;
std::ostream PARSER_DEBUG_STREAM;

enum ParserDebugLevel {
  NONE = 0,
  DEBUG_PRODUCTIONS = 5
};

#line 77 "y.tab.c" /* yacc.c:339  */

# ifndef YY_NULLPTR
#  if defined __cplusplus && 201103L <= __cplusplus
#   define YY_NULLPTR nullptr
#  else
#   define YY_NULLPTR 0
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif


/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    IDENTIFIER = 258,
    INTEGER_CONSTANT = 259,
    FLOATING_CONSTANT = 260,
    CHARACTER_CONSTANT = 261,
    ENUMERATION_CONSTANT = 262,
    STRING_LITERAL = 263,
    SIZEOF = 264,
    PTR_OP = 265,
    INC_OP = 266,
    DEC_OP = 267,
    LEFT_OP = 268,
    RIGHT_OP = 269,
    LE_OP = 270,
    GE_OP = 271,
    EQ_OP = 272,
    NE_OP = 273,
    AND_OP = 274,
    OR_OP = 275,
    MUL_ASSIGN = 276,
    DIV_ASSIGN = 277,
    MOD_ASSIGN = 278,
    ADD_ASSIGN = 279,
    SUB_ASSIGN = 280,
    LEFT_ASSIGN = 281,
    RIGHT_ASSIGN = 282,
    AND_ASSIGN = 283,
    XOR_ASSIGN = 284,
    OR_ASSIGN = 285,
    OPEN_CURLY = 286,
    CLOSE_CURLY = 287,
    OPEN_PAREN = 288,
    CLOSE_PAREN = 289,
    OPEN_SQUARE = 290,
    CLOSE_SQUARE = 291,
    PLUS = 292,
    MINUS = 293,
    DIV = 294,
    MUL = 295,
    COLON = 296,
    SEMI = 297,
    COMMA = 298,
    DOT = 299,
    TILDE = 300,
    Q_MARK = 301,
    AND = 302,
    OR = 303,
    NOT = 304,
    MOD = 305,
    XOR = 306,
    EQUAL = 307,
    LE = 308,
    GE = 309,
    TYPEDEF_NAME = 310,
    TYPEDEF = 311,
    EXTERN = 312,
    STATIC = 313,
    AUTO = 314,
    REGISTER = 315,
    CHAR = 316,
    SHORT = 317,
    INT = 318,
    LONG = 319,
    SIGNED = 320,
    UNSIGNED = 321,
    FLOAT = 322,
    DOUBLE = 323,
    CONST = 324,
    VOLATILE = 325,
    VOID = 326,
    STRUCT = 327,
    UNION = 328,
    ENUM = 329,
    ELIPSIS = 330,
    RANGE = 331,
    CASE = 332,
    DEFAULT = 333,
    IF = 334,
    ELSE = 335,
    SWITCH = 336,
    WHILE = 337,
    DO = 338,
    FOR = 339,
    GOTO = 340,
    CONTINUE = 341,
    BREAK = 342,
    RETURN = 343
  };
#endif
/* Tokens.  */
#define IDENTIFIER 258
#define INTEGER_CONSTANT 259
#define FLOATING_CONSTANT 260
#define CHARACTER_CONSTANT 261
#define ENUMERATION_CONSTANT 262
#define STRING_LITERAL 263
#define SIZEOF 264
#define PTR_OP 265
#define INC_OP 266
#define DEC_OP 267
#define LEFT_OP 268
#define RIGHT_OP 269
#define LE_OP 270
#define GE_OP 271
#define EQ_OP 272
#define NE_OP 273
#define AND_OP 274
#define OR_OP 275
#define MUL_ASSIGN 276
#define DIV_ASSIGN 277
#define MOD_ASSIGN 278
#define ADD_ASSIGN 279
#define SUB_ASSIGN 280
#define LEFT_ASSIGN 281
#define RIGHT_ASSIGN 282
#define AND_ASSIGN 283
#define XOR_ASSIGN 284
#define OR_ASSIGN 285
#define OPEN_CURLY 286
#define CLOSE_CURLY 287
#define OPEN_PAREN 288
#define CLOSE_PAREN 289
#define OPEN_SQUARE 290
#define CLOSE_SQUARE 291
#define PLUS 292
#define MINUS 293
#define DIV 294
#define MUL 295
#define COLON 296
#define SEMI 297
#define COMMA 298
#define DOT 299
#define TILDE 300
#define Q_MARK 301
#define AND 302
#define OR 303
#define NOT 304
#define MOD 305
#define XOR 306
#define EQUAL 307
#define LE 308
#define GE 309
#define TYPEDEF_NAME 310
#define TYPEDEF 311
#define EXTERN 312
#define STATIC 313
#define AUTO 314
#define REGISTER 315
#define CHAR 316
#define SHORT 317
#define INT 318
#define LONG 319
#define SIGNED 320
#define UNSIGNED 321
#define FLOAT 322
#define DOUBLE 323
#define CONST 324
#define VOLATILE 325
#define VOID 326
#define STRUCT 327
#define UNION 328
#define ENUM 329
#define ELIPSIS 330
#define RANGE 331
#define CASE 332
#define DEFAULT 333
#define IF 334
#define ELSE 335
#define SWITCH 336
#define WHILE 337
#define DO 338
#define FOR 339
#define GOTO 340
#define CONTINUE 341
#define BREAK 342
#define RETURN 343

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);



/* Copy the second part of user declarations.  */

#line 301 "y.tab.c" /* yacc.c:358  */

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE
# if (defined __GNUC__                                               \
      && (2 < __GNUC__ || (__GNUC__ == 2 && 96 <= __GNUC_MINOR__)))  \
     || defined __SUNPRO_C && 0x5110 <= __SUNPRO_C
#  define YY_ATTRIBUTE(Spec) __attribute__(Spec)
# else
#  define YY_ATTRIBUTE(Spec) /* empty */
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# define YY_ATTRIBUTE_PURE   YY_ATTRIBUTE ((__pure__))
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# define YY_ATTRIBUTE_UNUSED YY_ATTRIBUTE ((__unused__))
#endif

#if !defined _Noreturn \
     && (!defined __STDC_VERSION__ || __STDC_VERSION__ < 201112)
# if defined _MSC_VER && 1200 <= _MSC_VER
#  define _Noreturn __declspec (noreturn)
# else
#  define _Noreturn YY_ATTRIBUTE ((__noreturn__))
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN \
    _Pragma ("GCC diagnostic push") \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")\
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif


#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYSIZE_T yynewbytes;                                            \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / sizeof (*yyptr);                          \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, (Count) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYSIZE_T yyi;                         \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  45
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   1604

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  89
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  67
/* YYNRULES -- Number of rules.  */
#define YYNRULES  224
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  378

/* YYTRANSLATE[YYX] -- Symbol number corresponding to YYX as returned
   by yylex, with out-of-bounds checking.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   343

#define YYTRANSLATE(YYX)                                                \
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, without out-of-bounds checking.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    88
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,    48,    48,    51,    57,    61,    67,    71,    75,    79,
      85,    89,    95,    99,   105,   109,   113,   117,   121,   125,
     131,   135,   139,   143,   147,   153,   157,   161,   165,   169,
     173,   177,   181,   185,   189,   193,   197,   203,   207,   213,
     217,   221,   227,   231,   237,   241,   247,   251,   257,   261,
     267,   273,   277,   281,   285,   291,   295,   301,   305,   309,
     315,   319,   323,   329,   333,   339,   343,   349,   353,   359,
     363,   367,   371,   375,   379,   383,   389,   393,   397,   401,
     407,   411,   417,   421,   427,   431,   437,   441,   445,   451,
     455,   461,   465,   469,   475,   479,   485,   489,   495,   499,
     503,   509,   513,   517,   521,   525,   529,   533,   537,   541,
     547,   551,   555,   559,   563,   567,   573,   577,   581,   587,
     591,   597,   601,   605,   609,   615,   619,   625,   629,   633,
     639,   643,   647,   651,   655,   659,   663,   667,   671,   675,
     681,   685,   689,   693,   697,   703,   707,   713,   717,   723,
     727,   731,   735,   739,   743,   747,   751,   755,   759,   763,
     769,   773,   779,   785,   789,   795,   799,   805,   809,   815,
     819,   825,   829,   835,   839,   843,   849,   853,   857,   861,
     865,   871,   875,   879,   885,   889,   893,   899,   903,   907,
     911,   917,   921,   927,   931,   935,   939,   943,   947,   953,
     957,   961,   965,   969,   973,   979,   983,   987,   991,   995,
     999,  1003,  1007,  1013,  1017,  1021,  1025,  1031,  1035,  1041,
    1045,  1049,  1053,  1059,  1065
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "IDENTIFIER", "INTEGER_CONSTANT",
  "FLOATING_CONSTANT", "CHARACTER_CONSTANT", "ENUMERATION_CONSTANT",
  "STRING_LITERAL", "SIZEOF", "PTR_OP", "INC_OP", "DEC_OP", "LEFT_OP",
  "RIGHT_OP", "LE_OP", "GE_OP", "EQ_OP", "NE_OP", "AND_OP", "OR_OP",
  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN",
  "LEFT_ASSIGN", "RIGHT_ASSIGN", "AND_ASSIGN", "XOR_ASSIGN", "OR_ASSIGN",
  "OPEN_CURLY", "CLOSE_CURLY", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_SQUARE",
  "CLOSE_SQUARE", "PLUS", "MINUS", "DIV", "MUL", "COLON", "SEMI", "COMMA",
  "DOT", "TILDE", "Q_MARK", "AND", "OR", "NOT", "MOD", "XOR", "EQUAL",
  "LE", "GE", "TYPEDEF_NAME", "TYPEDEF", "EXTERN", "STATIC", "AUTO",
  "REGISTER", "CHAR", "SHORT", "INT", "LONG", "SIGNED", "UNSIGNED",
  "FLOAT", "DOUBLE", "CONST", "VOLATILE", "VOID", "STRUCT", "UNION",
  "ENUM", "ELIPSIS", "RANGE", "CASE", "DEFAULT", "IF", "ELSE", "SWITCH",
  "WHILE", "DO", "FOR", "GOTO", "CONTINUE", "BREAK", "RETURN", "$accept",
  "translation_unit", "external_declaration", "function_definition",
  "declaration", "declaration_list", "declaration_specifiers",
  "storage_class_specifier", "type_specifier", "type_qualifier",
  "struct_or_union_specifier", "struct_or_union",
  "struct_declaration_list", "init_declarator_list", "init_declarator",
  "struct_declaration", "specifier_qualifier_list",
  "struct_declarator_list", "struct_declarator", "enum_specifier",
  "enumerator_list", "enumerator", "declarator", "direct_declarator",
  "pointer", "type_qualifier_list", "parameter_type_list",
  "parameter_list", "parameter_declaration", "identifier_list",
  "initializer", "initializer_list", "type_name", "abstract_declarator",
  "direct_abstract_declarator", "statement", "labeled_statement",
  "expression_statement", "compound_statement", "statement_list",
  "selection_statement", "iteration_statement", "jump_statement",
  "expression", "assignment_expression", "assignment_operator",
  "conditional_expression", "constant_expression", "logical_or_expression",
  "logical_and_expression", "inclusive_or_expression",
  "exclusive_or_expression", "and_expression", "equality_expression",
  "relational_expression", "shift_expression", "additive_expression",
  "multiplicative_expression", "cast_expression", "unary_expression",
  "unary_operator", "postfix_expression", "primary_expression",
  "argument_expression_list", "constant", "string", "identifier", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   314,
     315,   316,   317,   318,   319,   320,   321,   322,   323,   324,
     325,   326,   327,   328,   329,   330,   331,   332,   333,   334,
     335,   336,   337,   338,   339,   340,   341,   342,   343
};
# endif

#define YYPACT_NINF -179

#define yypact_value_is_default(Yystate) \
  (!!((Yystate) == (-179)))

#define YYTABLE_NINF -1

#define yytable_value_is_error(Yytable_value) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int16 yypact[] =
{
     862,  -179,   109,    31,  -179,  -179,  -179,  -179,  -179,  -179,
    -179,  -179,  -179,  -179,  -179,  -179,  -179,  -179,  -179,  -179,
    -179,  -179,  -179,    15,   690,  -179,  -179,  -179,    54,  1489,
    1489,  1489,  -179,    19,  -179,   883,   191,    55,  -179,   -21,
    -179,  -179,    31,    14,    -4,  -179,  -179,  -179,    84,  -179,
     735,  -179,  -179,  -179,   530,    43,   403,  -179,   883,    54,
    -179,   903,   990,   191,  -179,  -179,  -179,   119,  -179,    30,
      14,  -179,   109,  1037,   883,  -179,   530,   530,   331,  -179,
      99,   530,  -179,  -179,  -179,  -179,  -179,  1413,  1426,  1426,
    -179,   777,  -179,  -179,  -179,  -179,  -179,  -179,  -179,  1473,
      26,    59,    65,   113,   691,   152,    14,   147,   151,  1050,
     489,  -179,  -179,  -179,  -179,   575,  -179,  -179,  -179,    91,
    -179,  -179,    53,   181,   155,   159,   167,   135,    25,   193,
     211,    78,  -179,   481,  1473,     9,  -179,  -179,  -179,   179,
    -179,  -179,   177,  -179,    74,   206,   201,  -179,    86,  -179,
    -179,  -179,   214,  -179,  -179,  -179,    14,  1473,   126,  -179,
    1037,  -179,  -179,  -179,  -179,  -179,  -179,  -179,  1473,   229,
    -179,   218,   358,   777,  -179,  1473,  -179,  -179,   178,   208,
     107,   243,   691,  1473,  1473,  1473,   170,  1097,   253,  -179,
    -179,  -179,   238,  -179,   633,  -179,  -179,  -179,  1473,  1473,
    1473,  1473,  1473,  1473,  1473,  1473,  1473,  1473,  1473,  1473,
    1473,  1473,  1473,  1473,  1473,  1473,  1473,  1473,  -179,  -179,
    -179,  -179,  -179,  -179,  -179,  -179,  -179,  -179,  -179,  1473,
    -179,    14,  -179,  -179,  1114,  1473,    14,   691,   820,  1161,
    -179,    51,  -179,   195,  -179,  1529,  -179,    14,  -179,  -179,
    -179,  -179,  -179,   127,  -179,  -179,    99,  1473,  -179,   266,
    1468,   199,  -179,  1473,  -179,   691,  -179,   133,   138,   140,
     269,  1174,   240,  -179,  -179,  -179,  -179,   181,   192,   155,
     159,   167,   135,    25,    25,   193,   193,   193,   193,   211,
     211,    78,    78,  -179,  -179,  -179,  -179,  -179,  -179,  -179,
     143,    32,  -179,  -179,  -179,   271,   272,  -179,   273,   195,
    1509,  1221,  -179,  -179,  -179,  -179,   975,  -179,  -179,  -179,
    -179,  -179,   691,   691,   691,  1473,  1238,   246,  1285,  1473,
    -179,  1473,  -179,  -179,  -179,  -179,  -179,   276,  -179,   277,
    -179,  -179,   232,  -179,  -179,   144,   691,   145,  1302,  1349,
     248,  -179,  -179,  -179,  -179,   691,   274,  -179,   691,   691,
     158,   691,   161,  1366,  -179,  -179,  -179,  -179,   691,  -179,
     691,   691,   162,  -179,  -179,  -179,   691,  -179
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
       0,   224,     0,    76,    36,    24,    23,    22,    20,    21,
      26,    27,    28,    29,    32,    33,    30,    31,    37,    38,
      25,    42,    43,     0,     0,     2,     4,     5,     0,    14,
      16,    18,    34,     0,    35,     0,    67,     0,    69,     0,
      80,    78,    77,     0,    62,     1,     3,    10,     0,    46,
      48,    15,    17,    19,     0,    41,     0,    12,     0,     0,
       6,     0,     0,    68,    70,    81,    79,     0,    63,    65,
       0,    11,     0,     0,     0,     8,    51,    53,     0,    44,
       0,     0,   219,   221,   220,   222,   223,     0,     0,     0,
     121,     0,   201,   202,   200,   119,   203,   199,   204,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   125,   110,   112,   111,     0,   113,   114,   115,     0,
     145,   147,   160,   163,   165,   167,   169,   171,   173,   176,
     181,   184,   187,   191,     0,   193,   205,   214,   215,   213,
      13,     7,    48,    73,    87,     0,    82,    84,     0,    89,
      71,   162,     0,   191,   213,    60,     0,     0,     0,    47,
       0,    49,    91,     9,    52,    54,    40,    45,     0,     0,
      55,    57,     0,     0,   197,     0,   194,   195,    96,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   141,
     142,   143,     0,   123,     0,   122,   126,   120,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   150,   151,
     152,   153,   154,   155,   156,   157,   158,   159,   149,     0,
     196,     0,   211,   212,     0,     0,     0,     0,     0,     0,
      86,    98,    88,    99,    74,     0,    75,     0,    72,    64,
      66,    61,    94,     0,    58,    50,     0,     0,    39,     0,
       0,    98,    97,     0,   216,     0,   118,     0,     0,     0,
       0,     0,     0,   140,   144,   124,   146,   164,     0,   166,
     168,   170,   172,   174,   175,   179,   180,   177,   178,   182,
     183,   185,   186,   189,   188,   190,   148,   210,   207,   217,
       0,     0,   209,   116,   106,     0,     0,   102,     0,   100,
       0,     0,    83,    85,    90,    92,     0,    56,    59,   198,
     192,   117,     0,     0,     0,     0,     0,     0,     0,     0,
     208,     0,   206,   107,   101,   103,   108,     0,   104,     0,
      93,    95,   127,   129,   130,     0,     0,     0,     0,     0,
       0,   161,   218,   109,   105,     0,     0,   132,     0,     0,
       0,     0,     0,     0,   128,   131,   133,   134,     0,   136,
       0,     0,     0,   135,   137,   138,     0,   139
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -179,  -179,   290,  -179,    45,   -41,     1,  -179,   -42,   121,
    -179,  -179,   236,  -179,   247,   -67,   -25,  -179,    62,  -179,
     250,   165,    36,   -33,    13,  -179,   -55,  -179,    80,  -179,
    -155,  -179,   153,  -118,  -178,  -101,  -179,  -179,   110,   237,
    -179,  -179,  -179,   -62,   -63,  -179,   -14,   -92,  -179,   129,
     148,   146,   149,   150,    93,    69,    92,    94,  -126,   128,
    -179,  -179,  -179,  -179,  -179,  -179,     0
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,    24,    25,    26,    57,    58,    59,    29,    30,    31,
      32,    33,    78,    48,    49,    79,    80,   169,   170,    34,
      67,    68,    35,    36,    37,    42,   305,   146,   147,   148,
     161,   253,   179,   306,   243,   111,   112,   113,   114,   115,
     116,   117,   118,   119,   120,   229,   121,   152,   122,   123,
     124,   125,   126,   127,   128,   129,   130,   131,   132,   133,
     134,   135,   136,   300,   137,   138,   154
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_uint16 yytable[] =
{
      38,    28,    38,   186,    63,   252,   145,   181,   230,    74,
     162,   167,    76,    64,   196,   110,    41,     1,     1,   231,
     232,   233,     1,    44,    38,    28,   242,    70,    38,   180,
      51,    52,    53,    55,    76,    76,    76,    38,    39,    76,
     207,   208,   234,    69,   235,    27,    43,   192,   151,    76,
      54,   164,   165,   236,     1,    66,   139,     1,     1,    38,
     262,   149,   144,   309,    50,   250,   178,   182,   332,    27,
      69,     3,    38,   199,    81,   198,   254,     1,   209,   210,
      38,   266,   157,   309,   238,   151,   239,     2,     2,   293,
     294,   295,   183,   196,     3,   142,    47,   162,   184,   200,
      18,    19,     1,   140,   139,   167,   188,   238,   142,   239,
     139,   180,     1,   180,     3,   139,   171,   215,   216,   140,
     246,   267,   268,   269,    40,   272,    71,    72,   217,   247,
      76,    76,     2,   197,   198,   276,   303,   320,   278,     3,
     168,   264,     2,   151,    38,    60,   185,   308,   178,     3,
     198,   155,   205,   206,   151,   140,    69,   241,   251,   315,
      75,   341,   156,    65,   321,   318,   296,   322,   141,   156,
     316,   299,   323,   301,   324,    77,   198,   330,   356,   358,
     240,   198,   139,   198,   163,   187,   331,   198,   198,   189,
     153,   261,   368,   190,   139,   370,   376,    77,    77,    77,
     201,   198,    77,   202,   198,   198,   211,   212,    63,   327,
     203,   260,    77,   239,   204,   174,   176,   177,     3,   339,
     237,   342,   343,   344,    61,   151,    62,   153,   310,    73,
     311,   297,   260,   329,   239,   198,   302,   139,    38,   144,
     244,    38,   263,   151,   245,   357,   144,   314,   213,   214,
     248,   241,   270,   162,   364,   337,    38,   366,   367,   257,
     369,   144,   153,   345,   347,   139,   350,   373,   352,   374,
     375,   255,   256,   261,    39,   377,   285,   286,   287,   288,
     274,   198,   328,   198,   265,   153,   360,   362,   348,   198,
     363,   198,   171,    77,    77,   273,   153,   151,   283,   284,
     319,   372,   325,   289,   290,   333,   334,   291,   292,   335,
     353,   144,   355,   354,    46,   351,   365,   172,   317,   159,
     158,   249,   139,   139,   139,   313,   259,   153,   277,   153,
     153,   153,   153,   153,   153,   153,   153,   153,   153,   153,
     153,   153,   153,   153,   153,   153,   139,   194,   280,   279,
       0,     0,   281,     0,   282,   139,     0,     0,   139,   139,
       0,   139,     0,   166,     0,     0,     0,   153,   139,     0,
     139,   139,     0,     0,     0,     0,   139,     0,     0,     0,
       0,     0,     0,     0,     0,   153,     4,     0,     0,     0,
     258,   153,    10,    11,    12,    13,    14,    15,    16,    17,
      18,    19,    20,    21,    22,    23,     1,    82,    83,    84,
      85,    86,    87,     4,    88,    89,     0,     0,     0,    10,
      11,    12,    13,    14,    15,    16,    17,    18,    19,    20,
      21,    22,    23,     0,    56,    90,    91,     0,     0,   153,
      92,    93,     0,    94,     0,    95,     0,     0,    96,     0,
      97,     0,    98,     0,     0,     0,     0,   153,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,     0,     0,
      99,   100,   101,     0,   102,   103,   104,   105,   106,   107,
     108,   109,     1,    82,    83,    84,    85,    86,    87,     0,
      88,    89,   218,   219,   220,   221,   222,   223,   224,   225,
     226,   227,     0,     0,     0,     0,     0,     0,     0,     0,
      56,   193,    91,     0,     0,     0,    92,    93,     0,    94,
       0,    95,     0,   228,    96,     0,    97,     0,    98,     0,
       0,     0,     0,     0,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,     0,     0,    99,   100,   101,     0,
     102,   103,   104,   105,   106,   107,   108,   109,     1,    82,
      83,    84,    85,    86,    87,     4,    88,    89,     0,     0,
       0,    10,    11,    12,    13,    14,    15,    16,    17,    18,
      19,    20,    21,    22,    23,     0,    56,   195,    91,     0,
       0,     0,    92,    93,     0,    94,     0,    95,     0,     0,
      96,     0,    97,     0,    98,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     1,    82,    83,    84,
      85,    86,    87,     0,    88,    89,     0,     0,     0,     0,
       0,     0,    99,   100,   101,     0,   102,   103,   104,   105,
     106,   107,   108,   109,    56,   275,    91,     0,     0,     0,
      92,    93,     0,    94,     0,    95,     0,     0,    96,     0,
      97,     0,    98,     0,     0,     0,     0,     0,     0,     0,
      45,     0,     0,     1,     1,    82,    83,    84,    85,    86,
      87,     0,    88,    89,     0,     0,     0,     0,     0,     0,
      99,   100,   101,     0,   102,   103,   104,   105,   106,   107,
     108,   109,    56,     2,    91,     0,     0,     0,    92,    93,
       3,    94,     0,    95,     0,     0,    96,     0,    97,     0,
      98,     0,     0,     0,     0,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    16,    17,    18,
      19,    20,    21,    22,    23,     0,    56,     0,    99,   100,
     101,     0,   102,   103,   104,   105,   106,   107,   108,   109,
       1,    82,    83,    84,    85,    86,    87,    73,    88,    89,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    18,    19,    20,    21,    22,    23,
      91,     0,     0,     0,    92,    93,     0,    94,     0,     0,
       0,     0,    96,     1,    97,     0,    98,     0,     0,     0,
       0,     0,     4,     0,     0,     0,     0,     0,    10,    11,
      12,    13,    14,    15,    16,    17,    18,    19,    20,    21,
      22,    23,     0,   238,   304,   239,     0,     0,     0,     0,
       3,     0,     0,     0,     0,     1,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    16,    17,    18,
      19,    20,    21,    22,    23,     2,     0,     0,     0,     0,
       0,     0,     3,     0,     0,     0,     1,     0,     0,     0,
       0,     0,     0,     0,    56,     0,     0,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,   143,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,     1,    82,
      83,    84,    85,    86,    87,     0,    88,    89,     0,     0,
       0,     0,     0,     1,    82,    83,    84,    85,    86,    87,
       0,    88,    89,     0,     0,     0,   160,   340,    91,     0,
       0,     0,    92,    93,     0,    94,     0,     0,     0,     0,
      96,     0,    97,    91,    98,     0,   150,    92,    93,     0,
      94,     0,     0,     0,     0,    96,     0,    97,     0,    98,
       1,    82,    83,    84,    85,    86,    87,     0,    88,    89,
       0,     0,     0,     1,    82,    83,    84,    85,    86,    87,
       0,    88,    89,     0,     0,     0,     0,     0,   160,     0,
      91,     0,     0,     0,    92,    93,     0,    94,     0,     0,
       0,     0,    96,    91,    97,     0,    98,    92,    93,     0,
      94,     0,   191,     0,     0,    96,     0,    97,     0,    98,
       1,    82,    83,    84,    85,    86,    87,     0,    88,    89,
       0,     0,     0,     0,     0,     0,     0,     1,    82,    83,
      84,    85,    86,    87,     0,    88,    89,     0,     0,     0,
      91,     0,     0,     0,    92,    93,     0,    94,     0,   271,
       0,     0,    96,     0,    97,     0,    98,    91,   298,     0,
       0,    92,    93,     0,    94,     0,     0,     0,     0,    96,
       0,    97,     0,    98,     1,    82,    83,    84,    85,    86,
      87,     0,    88,    89,     0,     0,     0,     1,    82,    83,
      84,    85,    86,    87,     0,    88,    89,     0,     0,     0,
       0,     0,     0,     0,    91,     0,     0,   307,    92,    93,
       0,    94,     0,     0,     0,     0,    96,    91,    97,     0,
      98,    92,    93,     0,    94,     0,   326,     0,     0,    96,
       0,    97,     0,    98,     1,    82,    83,    84,    85,    86,
      87,     0,    88,    89,     0,     0,     0,     0,     0,     0,
       0,     1,    82,    83,    84,    85,    86,    87,     0,    88,
      89,     0,     0,     0,    91,     0,     0,   338,    92,    93,
       0,    94,     0,     0,     0,     0,    96,     0,    97,     0,
      98,    91,   346,     0,     0,    92,    93,     0,    94,     0,
       0,     0,     0,    96,     0,    97,     0,    98,     1,    82,
      83,    84,    85,    86,    87,     0,    88,    89,     0,     0,
       0,     0,     0,     0,     0,     1,    82,    83,    84,    85,
      86,    87,     0,    88,    89,     0,     0,     0,    91,     0,
       0,     0,    92,    93,     0,    94,     0,   349,     0,     0,
      96,     0,    97,     0,    98,    91,   359,     0,     0,    92,
      93,     0,    94,     0,     0,     0,     0,    96,     0,    97,
       0,    98,     1,    82,    83,    84,    85,    86,    87,     0,
      88,    89,     0,     0,     0,     0,     0,     0,     0,     1,
      82,    83,    84,    85,    86,    87,     0,    88,    89,     0,
       0,     0,    91,   361,     0,     0,    92,    93,     0,    94,
       0,     0,     0,     0,    96,     0,    97,     0,    98,    91,
     371,     0,     0,    92,    93,     0,    94,     0,     0,     0,
       0,    96,     0,    97,     0,    98,     1,    82,    83,    84,
      85,    86,    87,     0,    88,    89,     0,     0,     0,     1,
      82,    83,    84,    85,    86,    87,     0,    88,    89,     0,
       0,     0,     0,     0,     0,     0,   173,     0,     0,     0,
      92,    93,     0,    94,     0,     0,     0,     0,    96,   175,
      97,     0,    98,    92,    93,     0,    94,     0,     0,     0,
       0,    96,     0,    97,     0,    98,     1,    82,    83,    84,
      85,    86,    87,     0,    88,    89,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   260,   304,   239,     0,     0,    91,     0,     3,     0,
      92,    93,     0,    94,     0,     0,     0,     0,    96,     0,
      97,     0,    98,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,    17,    18,    19,    20,
      21,    22,    23,   336,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,   312
};

static const yytype_int16 yycheck[] =
{
       0,     0,     2,   104,    37,   160,    61,    99,   134,    50,
      73,    78,    54,    34,   115,    56,     3,     3,     3,    10,
      11,    12,     3,    23,    24,    24,   144,    31,    28,    91,
      29,    30,    31,    33,    76,    77,    78,    37,     2,    81,
      15,    16,    33,    43,    35,     0,    31,   109,    62,    91,
      31,    76,    77,    44,     3,    42,    56,     3,     3,    59,
     178,    61,    61,   241,    28,   157,    91,    41,    36,    24,
      70,    40,    72,    20,    31,    43,   168,     3,    53,    54,
      80,   182,    52,   261,    33,    99,    35,    33,    33,   215,
     216,   217,    33,   194,    40,    59,    42,   160,    33,    46,
      69,    70,     3,    58,   104,   172,   106,    33,    72,    35,
     110,   173,     3,   175,    40,   115,    80,    39,    40,    74,
      34,   183,   184,   185,     3,   187,    42,    43,    50,    43,
     172,   173,    33,    42,    43,   198,   237,   263,   200,    40,
      41,    34,    33,   157,   144,    35,    33,   239,   173,    40,
      43,    32,    17,    18,   168,   110,   156,   144,    32,    32,
      50,   316,    43,    42,   265,   257,   229,    34,    58,    43,
      43,   234,    34,   235,    34,    54,    43,    34,    34,    34,
     144,    43,   182,    43,    74,    33,    43,    43,    43,    42,
      62,   178,    34,    42,   194,    34,    34,    76,    77,    78,
      19,    43,    81,    48,    43,    43,    13,    14,   241,   271,
      51,    33,    91,    35,    47,    87,    88,    89,    40,   311,
      41,   322,   323,   324,    33,   239,    35,    99,    33,    52,
      35,   231,    33,    41,    35,    43,   236,   237,   238,   238,
      34,   241,    34,   257,    43,   346,   245,   247,    37,    38,
      36,   238,    82,   316,   355,   310,   256,   358,   359,    41,
     361,   260,   134,   325,   326,   265,   328,   368,   331,   370,
     371,    42,    43,   260,   238,   376,   207,   208,   209,   210,
      42,    43,    42,    43,    41,   157,   348,   349,    42,    43,
      42,    43,   256,   172,   173,    42,   168,   311,   205,   206,
      34,   363,    33,   211,   212,    34,    34,   213,   214,    36,
      34,   310,    80,    36,    24,   329,    42,    81,   256,    72,
      70,   156,   322,   323,   324,   245,   173,   199,   199,   201,
     202,   203,   204,   205,   206,   207,   208,   209,   210,   211,
     212,   213,   214,   215,   216,   217,   346,   110,   202,   201,
      -1,    -1,   203,    -1,   204,   355,    -1,    -1,   358,   359,
      -1,   361,    -1,    32,    -1,    -1,    -1,   239,   368,    -1,
     370,   371,    -1,    -1,    -1,    -1,   376,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   257,    55,    -1,    -1,    -1,
      32,   263,    61,    62,    63,    64,    65,    66,    67,    68,
      69,    70,    71,    72,    73,    74,     3,     4,     5,     6,
       7,     8,     9,    55,    11,    12,    -1,    -1,    -1,    61,
      62,    63,    64,    65,    66,    67,    68,    69,    70,    71,
      72,    73,    74,    -1,    31,    32,    33,    -1,    -1,   311,
      37,    38,    -1,    40,    -1,    42,    -1,    -1,    45,    -1,
      47,    -1,    49,    -1,    -1,    -1,    -1,   329,    55,    56,
      57,    58,    59,    60,    61,    62,    63,    64,    65,    66,
      67,    68,    69,    70,    71,    72,    73,    74,    -1,    -1,
      77,    78,    79,    -1,    81,    82,    83,    84,    85,    86,
      87,    88,     3,     4,     5,     6,     7,     8,     9,    -1,
      11,    12,    21,    22,    23,    24,    25,    26,    27,    28,
      29,    30,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      31,    32,    33,    -1,    -1,    -1,    37,    38,    -1,    40,
      -1,    42,    -1,    52,    45,    -1,    47,    -1,    49,    -1,
      -1,    -1,    -1,    -1,    55,    56,    57,    58,    59,    60,
      61,    62,    63,    64,    65,    66,    67,    68,    69,    70,
      71,    72,    73,    74,    -1,    -1,    77,    78,    79,    -1,
      81,    82,    83,    84,    85,    86,    87,    88,     3,     4,
       5,     6,     7,     8,     9,    55,    11,    12,    -1,    -1,
      -1,    61,    62,    63,    64,    65,    66,    67,    68,    69,
      70,    71,    72,    73,    74,    -1,    31,    32,    33,    -1,
      -1,    -1,    37,    38,    -1,    40,    -1,    42,    -1,    -1,
      45,    -1,    47,    -1,    49,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,
       7,     8,     9,    -1,    11,    12,    -1,    -1,    -1,    -1,
      -1,    -1,    77,    78,    79,    -1,    81,    82,    83,    84,
      85,    86,    87,    88,    31,    32,    33,    -1,    -1,    -1,
      37,    38,    -1,    40,    -1,    42,    -1,    -1,    45,    -1,
      47,    -1,    49,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
       0,    -1,    -1,     3,     3,     4,     5,     6,     7,     8,
       9,    -1,    11,    12,    -1,    -1,    -1,    -1,    -1,    -1,
      77,    78,    79,    -1,    81,    82,    83,    84,    85,    86,
      87,    88,    31,    33,    33,    -1,    -1,    -1,    37,    38,
      40,    40,    -1,    42,    -1,    -1,    45,    -1,    47,    -1,
      49,    -1,    -1,    -1,    -1,    55,    56,    57,    58,    59,
      60,    61,    62,    63,    64,    65,    66,    67,    68,    69,
      70,    71,    72,    73,    74,    -1,    31,    -1,    77,    78,
      79,    -1,    81,    82,    83,    84,    85,    86,    87,    88,
       3,     4,     5,     6,     7,     8,     9,    52,    11,    12,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      33,    -1,    -1,    -1,    37,    38,    -1,    40,    -1,    -1,
      -1,    -1,    45,     3,    47,    -1,    49,    -1,    -1,    -1,
      -1,    -1,    55,    -1,    -1,    -1,    -1,    -1,    61,    62,
      63,    64,    65,    66,    67,    68,    69,    70,    71,    72,
      73,    74,    -1,    33,    34,    35,    -1,    -1,    -1,    -1,
      40,    -1,    -1,    -1,    -1,     3,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    55,    56,    57,    58,    59,
      60,    61,    62,    63,    64,    65,    66,    67,    68,    69,
      70,    71,    72,    73,    74,    33,    -1,    -1,    -1,    -1,
      -1,    -1,    40,    -1,    -1,    -1,     3,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    31,    -1,    -1,    55,    56,    57,
      58,    59,    60,    61,    62,    63,    64,    65,    66,    67,
      68,    69,    70,    71,    72,    73,    74,    34,    55,    56,
      57,    58,    59,    60,    61,    62,    63,    64,    65,    66,
      67,    68,    69,    70,    71,    72,    73,    74,    55,    56,
      57,    58,    59,    60,    61,    62,    63,    64,    65,    66,
      67,    68,    69,    70,    71,    72,    73,    74,     3,     4,
       5,     6,     7,     8,     9,    -1,    11,    12,    -1,    -1,
      -1,    -1,    -1,     3,     4,     5,     6,     7,     8,     9,
      -1,    11,    12,    -1,    -1,    -1,    31,    32,    33,    -1,
      -1,    -1,    37,    38,    -1,    40,    -1,    -1,    -1,    -1,
      45,    -1,    47,    33,    49,    -1,    36,    37,    38,    -1,
      40,    -1,    -1,    -1,    -1,    45,    -1,    47,    -1,    49,
       3,     4,     5,     6,     7,     8,     9,    -1,    11,    12,
      -1,    -1,    -1,     3,     4,     5,     6,     7,     8,     9,
      -1,    11,    12,    -1,    -1,    -1,    -1,    -1,    31,    -1,
      33,    -1,    -1,    -1,    37,    38,    -1,    40,    -1,    -1,
      -1,    -1,    45,    33,    47,    -1,    49,    37,    38,    -1,
      40,    -1,    42,    -1,    -1,    45,    -1,    47,    -1,    49,
       3,     4,     5,     6,     7,     8,     9,    -1,    11,    12,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    -1,    11,    12,    -1,    -1,    -1,
      33,    -1,    -1,    -1,    37,    38,    -1,    40,    -1,    42,
      -1,    -1,    45,    -1,    47,    -1,    49,    33,    34,    -1,
      -1,    37,    38,    -1,    40,    -1,    -1,    -1,    -1,    45,
      -1,    47,    -1,    49,     3,     4,     5,     6,     7,     8,
       9,    -1,    11,    12,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    -1,    11,    12,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    33,    -1,    -1,    36,    37,    38,
      -1,    40,    -1,    -1,    -1,    -1,    45,    33,    47,    -1,
      49,    37,    38,    -1,    40,    -1,    42,    -1,    -1,    45,
      -1,    47,    -1,    49,     3,     4,     5,     6,     7,     8,
       9,    -1,    11,    12,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,     3,     4,     5,     6,     7,     8,     9,    -1,    11,
      12,    -1,    -1,    -1,    33,    -1,    -1,    36,    37,    38,
      -1,    40,    -1,    -1,    -1,    -1,    45,    -1,    47,    -1,
      49,    33,    34,    -1,    -1,    37,    38,    -1,    40,    -1,
      -1,    -1,    -1,    45,    -1,    47,    -1,    49,     3,     4,
       5,     6,     7,     8,     9,    -1,    11,    12,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,
       8,     9,    -1,    11,    12,    -1,    -1,    -1,    33,    -1,
      -1,    -1,    37,    38,    -1,    40,    -1,    42,    -1,    -1,
      45,    -1,    47,    -1,    49,    33,    34,    -1,    -1,    37,
      38,    -1,    40,    -1,    -1,    -1,    -1,    45,    -1,    47,
      -1,    49,     3,     4,     5,     6,     7,     8,     9,    -1,
      11,    12,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,
       4,     5,     6,     7,     8,     9,    -1,    11,    12,    -1,
      -1,    -1,    33,    34,    -1,    -1,    37,    38,    -1,    40,
      -1,    -1,    -1,    -1,    45,    -1,    47,    -1,    49,    33,
      34,    -1,    -1,    37,    38,    -1,    40,    -1,    -1,    -1,
      -1,    45,    -1,    47,    -1,    49,     3,     4,     5,     6,
       7,     8,     9,    -1,    11,    12,    -1,    -1,    -1,     3,
       4,     5,     6,     7,     8,     9,    -1,    11,    12,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    33,    -1,    -1,    -1,
      37,    38,    -1,    40,    -1,    -1,    -1,    -1,    45,    33,
      47,    -1,    49,    37,    38,    -1,    40,    -1,    -1,    -1,
      -1,    45,    -1,    47,    -1,    49,     3,     4,     5,     6,
       7,     8,     9,    -1,    11,    12,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    33,    34,    35,    -1,    -1,    33,    -1,    40,    -1,
      37,    38,    -1,    40,    -1,    -1,    -1,    -1,    45,    -1,
      47,    -1,    49,    55,    56,    57,    58,    59,    60,    61,
      62,    63,    64,    65,    66,    67,    68,    69,    70,    71,
      72,    73,    74,    34,    55,    56,    57,    58,    59,    60,
      61,    62,    63,    64,    65,    66,    67,    68,    69,    70,
      71,    72,    73,    74,    55,    56,    57,    58,    59,    60,
      61,    62,    63,    64,    65,    66,    67,    68,    69,    70,
      71,    72,    73,    74,    55,    56,    57,    58,    59,    60,
      61,    62,    63,    64,    65,    66,    67,    68,    69,    70,
      71,    72,    73,    74,    75
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    33,    40,    55,    56,    57,    58,    59,    60,
      61,    62,    63,    64,    65,    66,    67,    68,    69,    70,
      71,    72,    73,    74,    90,    91,    92,    93,    95,    96,
      97,    98,    99,   100,   108,   111,   112,   113,   155,   111,
      98,   113,   114,    31,   155,     0,    91,    42,   102,   103,
     111,    95,    95,    95,    31,   155,    31,    93,    94,    95,
     127,    33,    35,   112,    34,    98,   113,   109,   110,   155,
      31,    42,    43,    52,    94,   127,    97,    98,   101,   104,
     105,    31,     4,     5,     6,     7,     8,     9,    11,    12,
      32,    33,    37,    38,    40,    42,    45,    47,    49,    77,
      78,    79,    81,    82,    83,    84,    85,    86,    87,    88,
      94,   124,   125,   126,   127,   128,   129,   130,   131,   132,
     133,   135,   137,   138,   139,   140,   141,   142,   143,   144,
     145,   146,   147,   148,   149,   150,   151,   153,   154,   155,
      93,   127,   111,    34,    95,   115,   116,   117,   118,   155,
      36,   135,   136,   148,   155,    32,    43,    52,   109,   103,
      31,   119,   133,   127,   105,   105,    32,   104,    41,   106,
     107,   111,   101,    33,   148,    33,   148,   148,   105,   121,
     132,   136,    41,    33,    33,    33,   124,    33,   155,    42,
      42,    42,   132,    32,   128,    32,   124,    42,    43,    20,
      46,    19,    48,    51,    47,    17,    18,    15,    16,    53,
      54,    13,    14,    37,    38,    39,    40,    50,    21,    22,
      23,    24,    25,    26,    27,    28,    29,    30,    52,   134,
     147,    10,    11,    12,    33,    35,    44,    41,    33,    35,
     111,   113,   122,   123,    34,    43,    34,    43,    36,   110,
     136,    32,   119,   120,   136,    42,    43,    41,    32,   121,
      33,   113,   122,    34,    34,    41,   124,   132,   132,   132,
      82,    42,   132,    42,    42,    32,   133,   138,   132,   139,
     140,   141,   142,   143,   143,   144,   144,   144,   144,   145,
     145,   146,   146,   147,   147,   147,   133,   155,    34,   133,
     152,   132,   155,   124,    34,   115,   122,    36,   136,   123,
      33,    35,    75,   117,   155,    32,    43,   107,   136,    34,
     147,   124,    34,    34,    34,    33,    42,   132,    42,    41,
      34,    43,    36,    34,    34,    36,    34,   115,    36,   136,
      32,   119,   124,   124,   124,   132,    34,   132,    42,    42,
     132,   135,   133,    34,    36,    80,    34,   124,    34,    34,
     132,    34,   132,    42,   124,    42,   124,   124,    34,   124,
      34,    34,   132,   124,   124,   124,    34,   124
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,    89,    90,    90,    91,    91,    92,    92,    92,    92,
      93,    93,    94,    94,    95,    95,    95,    95,    95,    95,
      96,    96,    96,    96,    96,    97,    97,    97,    97,    97,
      97,    97,    97,    97,    97,    97,    97,    98,    98,    99,
      99,    99,   100,   100,   101,   101,   102,   102,   103,   103,
     104,   105,   105,   105,   105,   106,   106,   107,   107,   107,
     108,   108,   108,   109,   109,   110,   110,   111,   111,   112,
     112,   112,   112,   112,   112,   112,   113,   113,   113,   113,
     114,   114,   115,   115,   116,   116,   117,   117,   117,   118,
     118,   119,   119,   119,   120,   120,   121,   121,   122,   122,
     122,   123,   123,   123,   123,   123,   123,   123,   123,   123,
     124,   124,   124,   124,   124,   124,   125,   125,   125,   126,
     126,   127,   127,   127,   127,   128,   128,   129,   129,   129,
     130,   130,   130,   130,   130,   130,   130,   130,   130,   130,
     131,   131,   131,   131,   131,   132,   132,   133,   133,   134,
     134,   134,   134,   134,   134,   134,   134,   134,   134,   134,
     135,   135,   136,   137,   137,   138,   138,   139,   139,   140,
     140,   141,   141,   142,   142,   142,   143,   143,   143,   143,
     143,   144,   144,   144,   145,   145,   145,   146,   146,   146,
     146,   147,   147,   148,   148,   148,   148,   148,   148,   149,
     149,   149,   149,   149,   149,   150,   150,   150,   150,   150,
     150,   150,   150,   151,   151,   151,   151,   152,   152,   153,
     153,   153,   153,   154,   155
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     2,     1,     1,     2,     3,     3,     4,
       2,     3,     1,     2,     1,     2,     1,     2,     1,     2,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     5,
       4,     2,     1,     1,     1,     2,     1,     3,     1,     3,
       3,     1,     2,     1,     2,     1,     3,     1,     2,     3,
       4,     5,     2,     1,     3,     1,     3,     1,     2,     1,
       3,     3,     4,     3,     4,     4,     1,     2,     2,     3,
       1,     2,     1,     3,     1,     3,     2,     1,     2,     1,
       3,     1,     3,     4,     1,     3,     1,     2,     1,     1,
       2,     3,     2,     3,     3,     4,     2,     3,     3,     4,
       1,     1,     1,     1,     1,     1,     3,     4,     3,     1,
       2,     2,     3,     3,     4,     1,     2,     5,     7,     5,
       5,     7,     6,     7,     7,     8,     7,     8,     8,     9,
       3,     2,     2,     2,     3,     1,     3,     1,     3,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     5,     1,     1,     3,     1,     3,     1,     3,     1,
       3,     1,     3,     1,     3,     3,     1,     3,     3,     3,
       3,     1,     3,     3,     1,     3,     3,     1,     3,     3,
       3,     1,     4,     1,     2,     2,     2,     2,     4,     1,
       1,     1,     1,     1,     1,     1,     4,     3,     4,     3,
       3,     2,     2,     1,     1,     1,     3,     1,     3,     1,
       1,     1,     1,     1,     1
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                  \
do                                                              \
  if (yychar == YYEMPTY)                                        \
    {                                                           \
      yychar = (Token);                                         \
      yylval = (Value);                                         \
      YYPOPSTACK (yylen);                                       \
      yystate = *yyssp;                                         \
      goto yybackup;                                            \
    }                                                           \
  else                                                          \
    {                                                           \
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;                                                  \
    }                                                           \
while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*----------------------------------------.
| Print this symbol's value on YYOUTPUT.  |
`----------------------------------------*/

static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  FILE *yyo = yyoutput;
  YYUSE (yyo);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# endif
  YYUSE (yytype);
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyoutput, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yytype_int16 *yyssp, YYSTYPE *yyvsp, int yyrule)
{
  unsigned long int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[yyssp[yyi + 1 - yynrhs]],
                       &(yyvsp[(yyi + 1) - (yynrhs)])
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
static YYSIZE_T
yystrlen (const char *yystr)
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            /* Fall through.  */
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYSIZE_T yysize1 = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (! (yysize <= yysize1
                         && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
                    return 2;
                  yysize = yysize1;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    YYSIZE_T yysize1 = yysize + yystrlen (yyformat);
    if (! (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
      return 2;
    yysize = yysize1;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
{
  YYUSE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        YYSTYPE *yyvs1 = yyvs;
        yytype_int16 *yyss1 = yyss;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * sizeof (*yyssp),
                    &yyvs1, yysize * sizeof (*yyvsp),
                    &yystacksize);

        yyss = yyss1;
        yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yytype_int16 *yyss1 = yyss;
        union yyalloc *yyptr =
          (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
                  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 2:
#line 48 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "translation_unit -> external_declaration\n"); }
#line 1927 "y.tab.c" /* yacc.c:1646  */
    break;

  case 3:
#line 51 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "translation_unit -> translation_unit external_declaration\n");
  }
#line 1935 "y.tab.c" /* yacc.c:1646  */
    break;

  case 4:
#line 57 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "external_declaration -> function_definition\n");
  }
#line 1943 "y.tab.c" /* yacc.c:1646  */
    break;

  case 5:
#line 61 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "external_declaration -> declaration\n");
  }
#line 1951 "y.tab.c" /* yacc.c:1646  */
    break;

  case 6:
#line 67 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "function_definition -> declarator compound_statement\n");
  }
#line 1959 "y.tab.c" /* yacc.c:1646  */
    break;

  case 7:
#line 71 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "function_definition -> declarator declaration_list compound_statement\n");
  }
#line 1967 "y.tab.c" /* yacc.c:1646  */
    break;

  case 8:
#line 75 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "function_definition -> declaration_specifiers declarator compound_statement\n");
  }
#line 1975 "y.tab.c" /* yacc.c:1646  */
    break;

  case 9:
#line 79 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "function_definition -> declaration_specifiers declarator declaration_list compound_statement\n");
  }
#line 1983 "y.tab.c" /* yacc.c:1646  */
    break;

  case 10:
#line 85 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration -> declaration_specifiers SEMI\n");
  }
#line 1991 "y.tab.c" /* yacc.c:1646  */
    break;

  case 11:
#line 89 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration -> declaration_specifiers init_declarator_list SEMI\n");
  }
#line 1999 "y.tab.c" /* yacc.c:1646  */
    break;

  case 12:
#line 95 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_list -> declaration\n");
  }
#line 2007 "y.tab.c" /* yacc.c:1646  */
    break;

  case 13:
#line 99 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_list -> declaration_list declaration\n");
  }
#line 2015 "y.tab.c" /* yacc.c:1646  */
    break;

  case 14:
#line 105 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_specifiers -> storage_class_specifier\n");
  }
#line 2023 "y.tab.c" /* yacc.c:1646  */
    break;

  case 15:
#line 109 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_specifiers -> storage_class_specifier declaration_specifiers\n");
  }
#line 2031 "y.tab.c" /* yacc.c:1646  */
    break;

  case 16:
#line 113 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_specifiers -> type_specifier\n");
  }
#line 2039 "y.tab.c" /* yacc.c:1646  */
    break;

  case 17:
#line 117 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_specifiers -> type_specifier declaration_specifiers\n");
  }
#line 2047 "y.tab.c" /* yacc.c:1646  */
    break;

  case 18:
#line 121 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_specifiers -> type_qualifier\n");
  }
#line 2055 "y.tab.c" /* yacc.c:1646  */
    break;

  case 19:
#line 125 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declaration_specifiers -> type_qualifier declaration_specifiers\n");
  }
#line 2063 "y.tab.c" /* yacc.c:1646  */
    break;

  case 20:
#line 131 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "storage_class_specifier -> AUTO\n");
  }
#line 2071 "y.tab.c" /* yacc.c:1646  */
    break;

  case 21:
#line 135 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "storage_class_specifier -> REGISTER\n");
  }
#line 2079 "y.tab.c" /* yacc.c:1646  */
    break;

  case 22:
#line 139 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "storage_class_specifier -> STATIC\n");
  }
#line 2087 "y.tab.c" /* yacc.c:1646  */
    break;

  case 23:
#line 143 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "storage_class_specifier -> EXTERN\n");
  }
#line 2095 "y.tab.c" /* yacc.c:1646  */
    break;

  case 24:
#line 147 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "storage_class_specifier -> TYPEDEF\n");
  }
#line 2103 "y.tab.c" /* yacc.c:1646  */
    break;

  case 25:
#line 153 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> VOID\n");
  }
#line 2111 "y.tab.c" /* yacc.c:1646  */
    break;

  case 26:
#line 157 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> CHAR\n");
  }
#line 2119 "y.tab.c" /* yacc.c:1646  */
    break;

  case 27:
#line 161 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> SHORT\n");
  }
#line 2127 "y.tab.c" /* yacc.c:1646  */
    break;

  case 28:
#line 165 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> INT\n");
  }
#line 2135 "y.tab.c" /* yacc.c:1646  */
    break;

  case 29:
#line 169 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> LONG\n");
  }
#line 2143 "y.tab.c" /* yacc.c:1646  */
    break;

  case 30:
#line 173 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> FLOAT\n");
  }
#line 2151 "y.tab.c" /* yacc.c:1646  */
    break;

  case 31:
#line 177 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> DOUBLE\n");
  }
#line 2159 "y.tab.c" /* yacc.c:1646  */
    break;

  case 32:
#line 181 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> SIGNED\n");
  }
#line 2167 "y.tab.c" /* yacc.c:1646  */
    break;

  case 33:
#line 185 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> UNSIGNED\n");
  }
#line 2175 "y.tab.c" /* yacc.c:1646  */
    break;

  case 34:
#line 189 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> struct_or_union_specifier\n");
  }
#line 2183 "y.tab.c" /* yacc.c:1646  */
    break;

  case 35:
#line 193 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> enum_specifier\n");
  }
#line 2191 "y.tab.c" /* yacc.c:1646  */
    break;

  case 36:
#line 197 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type type_specifier -> TYPEDEF_NAME\n");
  }
#line 2199 "y.tab.c" /* yacc.c:1646  */
    break;

  case 37:
#line 203 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type_qualifier -> CONST\n");
  }
#line 2207 "y.tab.c" /* yacc.c:1646  */
    break;

  case 38:
#line 207 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type_qualifier -> VOLATILE\n");
  }
#line 2215 "y.tab.c" /* yacc.c:1646  */
    break;

  case 39:
#line 213 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_or_union_specifier -> struct_or_union identifier OPEN_CURLY struct_declaration_list CLOSE_CURLY\n");
  }
#line 2223 "y.tab.c" /* yacc.c:1646  */
    break;

  case 40:
#line 217 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_or_union_specifier -> struct_or_union OPEN_CURLY struct_declaration_list CLOSE_CURLY\n");
  }
#line 2231 "y.tab.c" /* yacc.c:1646  */
    break;

  case 41:
#line 221 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_or_union_specifier -> struct_or_union identifier\n");
  }
#line 2239 "y.tab.c" /* yacc.c:1646  */
    break;

  case 42:
#line 227 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_or_union -> STRUCT\n");
  }
#line 2247 "y.tab.c" /* yacc.c:1646  */
    break;

  case 43:
#line 231 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_or_union -> UNION\n");
  }
#line 2255 "y.tab.c" /* yacc.c:1646  */
    break;

  case 44:
#line 237 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declaration_list -> struct_declaration\n");
  }
#line 2263 "y.tab.c" /* yacc.c:1646  */
    break;

  case 45:
#line 241 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declaration_list -> struct_declaration_list struct_declaration\n");
  }
#line 2271 "y.tab.c" /* yacc.c:1646  */
    break;

  case 46:
#line 247 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "init_declarator_list -> init_declarator\n");
  }
#line 2279 "y.tab.c" /* yacc.c:1646  */
    break;

  case 47:
#line 251 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "init_declarator_list -> init_declarator_list COMMA init_declarator\n");
  }
#line 2287 "y.tab.c" /* yacc.c:1646  */
    break;

  case 48:
#line 257 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "init_declarator -> declarator\n");
  }
#line 2295 "y.tab.c" /* yacc.c:1646  */
    break;

  case 49:
#line 261 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "init_declarator -> declarator EQUAL initializer\n");
  }
#line 2303 "y.tab.c" /* yacc.c:1646  */
    break;

  case 50:
#line 267 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declaration -> specifier_qualifier_list struct_declarator_list SEMI\n");
  }
#line 2311 "y.tab.c" /* yacc.c:1646  */
    break;

  case 51:
#line 273 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "specifier_qualifier_list -> type_specifier\n");
  }
#line 2319 "y.tab.c" /* yacc.c:1646  */
    break;

  case 52:
#line 277 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "specifier_qualifier_list -> type_specifier specifier_qualifier_list\n");
  }
#line 2327 "y.tab.c" /* yacc.c:1646  */
    break;

  case 53:
#line 281 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "specifier_qualifier_list -> type_qualifier\n");
  }
#line 2335 "y.tab.c" /* yacc.c:1646  */
    break;

  case 54:
#line 285 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "specifier_qualifier_list -> type_qualifier specifier_qualifier_list\n");
  }
#line 2343 "y.tab.c" /* yacc.c:1646  */
    break;

  case 55:
#line 291 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declarator_list -> struct_declarator\n");
  }
#line 2351 "y.tab.c" /* yacc.c:1646  */
    break;

  case 56:
#line 295 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declarator_list -> struct_declarator_list COMMA struct_declarator\n");
  }
#line 2359 "y.tab.c" /* yacc.c:1646  */
    break;

  case 57:
#line 301 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declarator -> declarator\n");
  }
#line 2367 "y.tab.c" /* yacc.c:1646  */
    break;

  case 58:
#line 305 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declarator -> COLON constant_expression\n");
  }
#line 2375 "y.tab.c" /* yacc.c:1646  */
    break;

  case 59:
#line 309 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "struct_declarator -> declarator COLON constant_expression\n");
  }
#line 2383 "y.tab.c" /* yacc.c:1646  */
    break;

  case 60:
#line 315 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enum_specifier -> ENUM OPEN_CURLY enumerator_list CLOSE_CURLY\n");
  }
#line 2391 "y.tab.c" /* yacc.c:1646  */
    break;

  case 61:
#line 319 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enum_specifier -> ENUM identifier OPEN_CURLY enumerator_list CLOSE_CURLY\n");
  }
#line 2399 "y.tab.c" /* yacc.c:1646  */
    break;

  case 62:
#line 323 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enum_specifier -> ENUM identifier\n");
  }
#line 2407 "y.tab.c" /* yacc.c:1646  */
    break;

  case 63:
#line 329 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enumerator_list -> enumerator\n");
  }
#line 2415 "y.tab.c" /* yacc.c:1646  */
    break;

  case 64:
#line 333 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enumerator_list -> enumerator_list COMMA enumerator\n");
  }
#line 2423 "y.tab.c" /* yacc.c:1646  */
    break;

  case 65:
#line 339 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enumerator -> identifier\n");
  }
#line 2431 "y.tab.c" /* yacc.c:1646  */
    break;

  case 66:
#line 343 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "enumerator -> identifier EQUAL constant_expression\n");
  }
#line 2439 "y.tab.c" /* yacc.c:1646  */
    break;

  case 67:
#line 349 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declarator -> direct_declarator\n");
  }
#line 2447 "y.tab.c" /* yacc.c:1646  */
    break;

  case 68:
#line 353 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "declarator -> pointer direct_declarator\n");
  }
#line 2455 "y.tab.c" /* yacc.c:1646  */
    break;

  case 69:
#line 359 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> identifier\n");
  }
#line 2463 "y.tab.c" /* yacc.c:1646  */
    break;

  case 70:
#line 363 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> OPEN_PAREN declarator CLOSE_PAREN\n");
  }
#line 2471 "y.tab.c" /* yacc.c:1646  */
    break;

  case 71:
#line 367 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> direct_declarator OPEN_SQUARE CLOSE_SQUARE\n");
  }
#line 2479 "y.tab.c" /* yacc.c:1646  */
    break;

  case 72:
#line 371 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> direct_declarator OPEN_SQUARE constant_expression CLOSE_SQUARE\n");
  }
#line 2487 "y.tab.c" /* yacc.c:1646  */
    break;

  case 73:
#line 375 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> direct_declarator OPEN_PAREN CLOSE_PAREN\n");
  }
#line 2495 "y.tab.c" /* yacc.c:1646  */
    break;

  case 74:
#line 379 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> direct_declarator OPEN_PAREN parameter_type_list CLOSE_PAREN\n");
  }
#line 2503 "y.tab.c" /* yacc.c:1646  */
    break;

  case 75:
#line 383 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_declarator -> direct_declarator OPEN_PAREN identifier_list CLOSE_PAREN\n");
  }
#line 2511 "y.tab.c" /* yacc.c:1646  */
    break;

  case 76:
#line 389 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "pointer -> MUL\n");
  }
#line 2519 "y.tab.c" /* yacc.c:1646  */
    break;

  case 77:
#line 393 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "pointer -> MUL type_qualifier_list\n");
  }
#line 2527 "y.tab.c" /* yacc.c:1646  */
    break;

  case 78:
#line 397 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "pointer -> MUL pointer\n");
  }
#line 2535 "y.tab.c" /* yacc.c:1646  */
    break;

  case 79:
#line 401 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "pointer -> MUL type_qualifier_list pointer\n");
  }
#line 2543 "y.tab.c" /* yacc.c:1646  */
    break;

  case 80:
#line 407 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type_qualifier_list -> type_qualifier\n");
  }
#line 2551 "y.tab.c" /* yacc.c:1646  */
    break;

  case 81:
#line 411 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type_qualifier_list -> type_qualifier_list type_qualifier\n");
  }
#line 2559 "y.tab.c" /* yacc.c:1646  */
    break;

  case 82:
#line 417 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_type_list -> parameter_list\n");
  }
#line 2567 "y.tab.c" /* yacc.c:1646  */
    break;

  case 83:
#line 421 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_type_list -> parameter_list COMMA ELIPSIS\n");
  }
#line 2575 "y.tab.c" /* yacc.c:1646  */
    break;

  case 84:
#line 427 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_list -> parameter_declaration\n");
  }
#line 2583 "y.tab.c" /* yacc.c:1646  */
    break;

  case 85:
#line 431 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_list -> parameter_list COMMA parameter_declaration\n");
  }
#line 2591 "y.tab.c" /* yacc.c:1646  */
    break;

  case 86:
#line 437 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_declaration -> declaration_specifiers declarator\n");
  }
#line 2599 "y.tab.c" /* yacc.c:1646  */
    break;

  case 87:
#line 441 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_declaration -> declaration_specifiers\n");
  }
#line 2607 "y.tab.c" /* yacc.c:1646  */
    break;

  case 88:
#line 445 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "parameter_declaration -> declaration_specifiers abstract_declarator\n");
  }
#line 2615 "y.tab.c" /* yacc.c:1646  */
    break;

  case 89:
#line 451 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "identifier_list -> identifier\n");
  }
#line 2623 "y.tab.c" /* yacc.c:1646  */
    break;

  case 90:
#line 455 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "identifier_list -> identifier_list COMMA identifier\n");
  }
#line 2631 "y.tab.c" /* yacc.c:1646  */
    break;

  case 91:
#line 461 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "initializer -> assignment_expression\n");
  }
#line 2639 "y.tab.c" /* yacc.c:1646  */
    break;

  case 92:
#line 465 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "initializer -> OPEN_CURLY initializer_list CLOSE_CURLY\n");
  }
#line 2647 "y.tab.c" /* yacc.c:1646  */
    break;

  case 93:
#line 469 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "initializer -> OPEN_CURLY initializer_list COMMA CLOSE_CURLY\n");
  }
#line 2655 "y.tab.c" /* yacc.c:1646  */
    break;

  case 94:
#line 475 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "initializer_list -> initializer\n");
  }
#line 2663 "y.tab.c" /* yacc.c:1646  */
    break;

  case 95:
#line 479 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "initializer_list -> initializer_list COMMA initializer\n");
  }
#line 2671 "y.tab.c" /* yacc.c:1646  */
    break;

  case 96:
#line 485 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type_name -> specifier_qualifier_list\n");
  }
#line 2679 "y.tab.c" /* yacc.c:1646  */
    break;

  case 97:
#line 489 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "type_name -> specifier_qualifier_list abstract_declarator\n");
  }
#line 2687 "y.tab.c" /* yacc.c:1646  */
    break;

  case 98:
#line 495 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "abstract_declarator -> pointer\n");
  }
#line 2695 "y.tab.c" /* yacc.c:1646  */
    break;

  case 99:
#line 499 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "abstract_declarator -> direct_abstract_declarator\n");
  }
#line 2703 "y.tab.c" /* yacc.c:1646  */
    break;

  case 100:
#line 503 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "abstract_declarator -> pointer direct_abstract_declarator\n");
  }
#line 2711 "y.tab.c" /* yacc.c:1646  */
    break;

  case 101:
#line 509 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> OPEN_PAREN abstract_declarator CLOSE_PAREN\n");
  }
#line 2719 "y.tab.c" /* yacc.c:1646  */
    break;

  case 102:
#line 513 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> OPEN_SQUARE CLOSE_SQUARE\n");
  }
#line 2727 "y.tab.c" /* yacc.c:1646  */
    break;

  case 103:
#line 517 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> OPEN_SQUARE constant_expression CLOSE_SQUARE\n");
  }
#line 2735 "y.tab.c" /* yacc.c:1646  */
    break;

  case 104:
#line 521 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> direct_abstract_declarator OPEN_SQUARE CLOSE_SQUARE\n");
  }
#line 2743 "y.tab.c" /* yacc.c:1646  */
    break;

  case 105:
#line 525 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> direct_abstract_declarator OPEN_SQUARE constant_expression CLOSE_SQUARE\n");
  }
#line 2751 "y.tab.c" /* yacc.c:1646  */
    break;

  case 106:
#line 529 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> OPEN_PAREN CLOSE_PAREN\n");
  }
#line 2759 "y.tab.c" /* yacc.c:1646  */
    break;

  case 107:
#line 533 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> OPEN_PAREN parameter_type_list CLOSE_PAREN\n");
  }
#line 2767 "y.tab.c" /* yacc.c:1646  */
    break;

  case 108:
#line 537 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> direct_abstract_declarator OPEN_PAREN CLOSE_PAREN\n");
  }
#line 2775 "y.tab.c" /* yacc.c:1646  */
    break;

  case 109:
#line 541 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "direct_abstract_declarator -> direct_abstract_declarator OPEN_PAREN parameter_type_list CLOSE_PAREN\n");
  }
#line 2783 "y.tab.c" /* yacc.c:1646  */
    break;

  case 110:
#line 547 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement -> labeled_statement\n");
  }
#line 2791 "y.tab.c" /* yacc.c:1646  */
    break;

  case 111:
#line 551 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement -> compound_statement\n");
  }
#line 2799 "y.tab.c" /* yacc.c:1646  */
    break;

  case 112:
#line 555 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement -> expression_statement\n");
  }
#line 2807 "y.tab.c" /* yacc.c:1646  */
    break;

  case 113:
#line 559 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement -> selection_statement\n");
  }
#line 2815 "y.tab.c" /* yacc.c:1646  */
    break;

  case 114:
#line 563 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement -> iteration_statement\n");
  }
#line 2823 "y.tab.c" /* yacc.c:1646  */
    break;

  case 115:
#line 567 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement -> jump_statement\n");
  }
#line 2831 "y.tab.c" /* yacc.c:1646  */
    break;

  case 116:
#line 573 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "labeled_statement -> identifier COLON statement\n");
  }
#line 2839 "y.tab.c" /* yacc.c:1646  */
    break;

  case 117:
#line 577 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "labeled_statement -> CASE constant_expression COLON statement\n");
  }
#line 2847 "y.tab.c" /* yacc.c:1646  */
    break;

  case 118:
#line 581 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "labeled_statement -> DEFAULT COLON statement\n");
  }
#line 2855 "y.tab.c" /* yacc.c:1646  */
    break;

  case 119:
#line 587 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "expression_statement -> SEMI\n");
  }
#line 2863 "y.tab.c" /* yacc.c:1646  */
    break;

  case 120:
#line 591 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "expression_statement -> expression SEMI\n");
  }
#line 2871 "y.tab.c" /* yacc.c:1646  */
    break;

  case 121:
#line 597 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "compound_statement -> OPEN_CURLY CLOSE_CURLY\n");
  }
#line 2879 "y.tab.c" /* yacc.c:1646  */
    break;

  case 122:
#line 601 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "compound_statement -> OPEN_CURLY statement_list CLOSE_CURLY\n");
  }
#line 2887 "y.tab.c" /* yacc.c:1646  */
    break;

  case 123:
#line 605 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "compound_statement -> OPEN_CURLY declaration_list CLOSE_CURLY\n");
  }
#line 2895 "y.tab.c" /* yacc.c:1646  */
    break;

  case 124:
#line 609 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "compound_statement -> OPEN_CURLY declaration_list statement_list CLOSE_CURLY\n");
  }
#line 2903 "y.tab.c" /* yacc.c:1646  */
    break;

  case 125:
#line 615 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement_list -> statement\n");
  }
#line 2911 "y.tab.c" /* yacc.c:1646  */
    break;

  case 126:
#line 619 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "statement_list -> statement_list statement\n");
  }
#line 2919 "y.tab.c" /* yacc.c:1646  */
    break;

  case 127:
#line 625 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "selection_statement -> IF OPEN_PAREN expression CLOSE_PAREN statement\n");
  }
#line 2927 "y.tab.c" /* yacc.c:1646  */
    break;

  case 128:
#line 629 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "selection_statement -> IF OPEN_PAREN expression CLOSE_PAREN statement ELSE statement\n");
  }
#line 2935 "y.tab.c" /* yacc.c:1646  */
    break;

  case 129:
#line 633 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "selection_statement -> SWITCH OPEN_PAREN expression CLOSE_PAREN statement\n");
  }
#line 2943 "y.tab.c" /* yacc.c:1646  */
    break;

  case 130:
#line 639 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> WHILE OPEN_PAREN expression CLOSE_PAREN statement\n");
  }
#line 2951 "y.tab.c" /* yacc.c:1646  */
    break;

  case 131:
#line 643 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> DO statement WHILE OPEN_PAREN expression CLOSE_PAREN SEMI\n");
  }
#line 2959 "y.tab.c" /* yacc.c:1646  */
    break;

  case 132:
#line 647 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN SEMI SEMI CLOSE_PAREN statement\n");
  }
#line 2967 "y.tab.c" /* yacc.c:1646  */
    break;

  case 133:
#line 651 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN SEMI SEMI expression CLOSE_PAREN statement\n");
  }
#line 2975 "y.tab.c" /* yacc.c:1646  */
    break;

  case 134:
#line 655 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN SEMI expression SEMI CLOSE_PAREN statement\n");
  }
#line 2983 "y.tab.c" /* yacc.c:1646  */
    break;

  case 135:
#line 659 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN SEMI expression SEMI expression CLOSE_PAREN statement\n");
  }
#line 2991 "y.tab.c" /* yacc.c:1646  */
    break;

  case 136:
#line 663 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN expression SEMI SEMI CLOSE_PAREN statement\n");
  }
#line 2999 "y.tab.c" /* yacc.c:1646  */
    break;

  case 137:
#line 667 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN expression SEMI SEMI expression CLOSE_PAREN statement\n");
  }
#line 3007 "y.tab.c" /* yacc.c:1646  */
    break;

  case 138:
#line 671 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN expression SEMI expression SEMI CLOSE_PAREN statement\n");
  }
#line 3015 "y.tab.c" /* yacc.c:1646  */
    break;

  case 139:
#line 675 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "iteration_statement -> FOR OPEN_PAREN expression SEMI expression SEMI expression CLOSE_PAREN statement\n");
  }
#line 3023 "y.tab.c" /* yacc.c:1646  */
    break;

  case 140:
#line 681 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "jump_statement -> GOTO identifier SEMI\n");
  }
#line 3031 "y.tab.c" /* yacc.c:1646  */
    break;

  case 141:
#line 685 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "jump_statement -> CONTINUE SEMI\n");
  }
#line 3039 "y.tab.c" /* yacc.c:1646  */
    break;

  case 142:
#line 689 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "jump_statement -> BREAK SEMI\n");
  }
#line 3047 "y.tab.c" /* yacc.c:1646  */
    break;

  case 143:
#line 693 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "jump_statement -> RETURN SEMI\n");
  }
#line 3055 "y.tab.c" /* yacc.c:1646  */
    break;

  case 144:
#line 697 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "jump_statement -> RETURN expression SEMI\n");
  }
#line 3063 "y.tab.c" /* yacc.c:1646  */
    break;

  case 145:
#line 703 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "expression -> assignment_expression\n");
  }
#line 3071 "y.tab.c" /* yacc.c:1646  */
    break;

  case 146:
#line 707 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "expression -> expression COMMA assignment_expression\n");
  }
#line 3079 "y.tab.c" /* yacc.c:1646  */
    break;

  case 147:
#line 713 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_expression -> conditional_expression\n");
  }
#line 3087 "y.tab.c" /* yacc.c:1646  */
    break;

  case 148:
#line 717 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_expression -> unary_expression assignment_operator assignment_expression\n");
  }
#line 3095 "y.tab.c" /* yacc.c:1646  */
    break;

  case 149:
#line 723 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> EQUAL\n");
  }
#line 3103 "y.tab.c" /* yacc.c:1646  */
    break;

  case 150:
#line 727 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> MUL_ASSIGN\n");
  }
#line 3111 "y.tab.c" /* yacc.c:1646  */
    break;

  case 151:
#line 731 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> DIV_ASSIGN\n");
  }
#line 3119 "y.tab.c" /* yacc.c:1646  */
    break;

  case 152:
#line 735 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> MOD_ASSIGN\n");
  }
#line 3127 "y.tab.c" /* yacc.c:1646  */
    break;

  case 153:
#line 739 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> ADD_ASSIGN\n");
  }
#line 3135 "y.tab.c" /* yacc.c:1646  */
    break;

  case 154:
#line 743 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> SUB_ASSIGN\n");
  }
#line 3143 "y.tab.c" /* yacc.c:1646  */
    break;

  case 155:
#line 747 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> LEFT_ASSIGN\n");
  }
#line 3151 "y.tab.c" /* yacc.c:1646  */
    break;

  case 156:
#line 751 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> RIGHT_ASSIGN\n");
  }
#line 3159 "y.tab.c" /* yacc.c:1646  */
    break;

  case 157:
#line 755 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> AND_ASSIGN\n");
  }
#line 3167 "y.tab.c" /* yacc.c:1646  */
    break;

  case 158:
#line 759 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> XOR_ASSIGN\n");
  }
#line 3175 "y.tab.c" /* yacc.c:1646  */
    break;

  case 159:
#line 763 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "assignment_operator -> OR_ASSIGN\n");
  }
#line 3183 "y.tab.c" /* yacc.c:1646  */
    break;

  case 160:
#line 769 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "conditional_expression -> logical_or_expression\n");
  }
#line 3191 "y.tab.c" /* yacc.c:1646  */
    break;

  case 161:
#line 773 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "conditional_expression -> logical_or_expression Q_MARK expression COLON conditional_expression\n");
  }
#line 3199 "y.tab.c" /* yacc.c:1646  */
    break;

  case 162:
#line 779 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "constant_expression -> conditional_expression\n");
  }
#line 3207 "y.tab.c" /* yacc.c:1646  */
    break;

  case 163:
#line 785 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "logical_or_expression -> logical_and_expression\n");
  }
#line 3215 "y.tab.c" /* yacc.c:1646  */
    break;

  case 164:
#line 789 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "logical_or_expression -> logical_or_expression OR_OP logical_and_expression\n");
  }
#line 3223 "y.tab.c" /* yacc.c:1646  */
    break;

  case 165:
#line 795 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "logical_and_expression -> inclusive_or_expression\n");
  }
#line 3231 "y.tab.c" /* yacc.c:1646  */
    break;

  case 166:
#line 799 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "logical_and_expression -> logical_and_expression AND_OP inclusive_or_expression\n");
  }
#line 3239 "y.tab.c" /* yacc.c:1646  */
    break;

  case 167:
#line 805 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "inclusive_or_expression -> exclusive_or_expression\n");
  }
#line 3247 "y.tab.c" /* yacc.c:1646  */
    break;

  case 168:
#line 809 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "inclusive_or_expression -> inclusive_or_expression OR exclusive_or_expression\n");
  }
#line 3255 "y.tab.c" /* yacc.c:1646  */
    break;

  case 169:
#line 815 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "exclusive_or_expression -> and_expression\n");
  }
#line 3263 "y.tab.c" /* yacc.c:1646  */
    break;

  case 170:
#line 819 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "exclusive_or_expression -> exclusive_or_expression XOR and_expression\n");
  }
#line 3271 "y.tab.c" /* yacc.c:1646  */
    break;

  case 171:
#line 825 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "and_expression -> equality_expression\n");
  }
#line 3279 "y.tab.c" /* yacc.c:1646  */
    break;

  case 172:
#line 829 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "and_expression -> and_expression AND equality_expression\n");
  }
#line 3287 "y.tab.c" /* yacc.c:1646  */
    break;

  case 173:
#line 835 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "equality_expression -> relational_expression\n");
  }
#line 3295 "y.tab.c" /* yacc.c:1646  */
    break;

  case 174:
#line 839 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "equality_expression -> equality_expression EQ_OP relational_expression\n");
  }
#line 3303 "y.tab.c" /* yacc.c:1646  */
    break;

  case 175:
#line 843 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "equality_expression -> equality_expression NE_OP relational_expression\n");
  }
#line 3311 "y.tab.c" /* yacc.c:1646  */
    break;

  case 176:
#line 849 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "relational_expression -> shift_expression\n");
  }
#line 3319 "y.tab.c" /* yacc.c:1646  */
    break;

  case 177:
#line 853 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "relational_expression -> relational_expression LE shift_expression\n");
  }
#line 3327 "y.tab.c" /* yacc.c:1646  */
    break;

  case 178:
#line 857 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "relational_expression -> relational_expression GE shift_expression\n");
  }
#line 3335 "y.tab.c" /* yacc.c:1646  */
    break;

  case 179:
#line 861 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "relational_expression -> relational_expression LE_OP shift_expression\n");
  }
#line 3343 "y.tab.c" /* yacc.c:1646  */
    break;

  case 180:
#line 865 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "relational_expression -> relational_expression GE_OP shift_expression\n");
  }
#line 3351 "y.tab.c" /* yacc.c:1646  */
    break;

  case 181:
#line 871 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "shift_expression -> additive_expression\n");
  }
#line 3359 "y.tab.c" /* yacc.c:1646  */
    break;

  case 182:
#line 875 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "shift_expression -> shift_expression LEFT_OP additive_expression\n");
  }
#line 3367 "y.tab.c" /* yacc.c:1646  */
    break;

  case 183:
#line 879 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "shift_expression -> shift_expression RIGHT_OP additive_expression\n");
  }
#line 3375 "y.tab.c" /* yacc.c:1646  */
    break;

  case 184:
#line 885 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "additive_expression -> multiplicative_expression\n");
  }
#line 3383 "y.tab.c" /* yacc.c:1646  */
    break;

  case 185:
#line 889 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "additive_expression -> additive_expression PLUS multiplicative_expression\n");
  }
#line 3391 "y.tab.c" /* yacc.c:1646  */
    break;

  case 186:
#line 893 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "additive_expression -> additive_expression MINUS multiplicative_expression\n");
  }
#line 3399 "y.tab.c" /* yacc.c:1646  */
    break;

  case 187:
#line 899 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "multiplicative_expression -> cast_expression\n");
  }
#line 3407 "y.tab.c" /* yacc.c:1646  */
    break;

  case 188:
#line 903 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "multiplicative_expression -> multiplicative_expression MUL cast_expression\n");
  }
#line 3415 "y.tab.c" /* yacc.c:1646  */
    break;

  case 189:
#line 907 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "multiplicative_expression -> multiplicative_expression DIV cast_expression\n");
  }
#line 3423 "y.tab.c" /* yacc.c:1646  */
    break;

  case 190:
#line 911 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "multiplicative_expression -> multiplicative_expression MOD cast_expression\n");
  }
#line 3431 "y.tab.c" /* yacc.c:1646  */
    break;

  case 191:
#line 917 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "cast_expression -> unary_expression\n");
  }
#line 3439 "y.tab.c" /* yacc.c:1646  */
    break;

  case 192:
#line 921 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "cast_expression -> OPEN_PAREN type_name CLOSE_PAREN cast_expression\n");
  }
#line 3447 "y.tab.c" /* yacc.c:1646  */
    break;

  case 193:
#line 927 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_expression -> postfix_expression\n");
  }
#line 3455 "y.tab.c" /* yacc.c:1646  */
    break;

  case 194:
#line 931 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_expression -> INC_OP unary_expression\n");
  }
#line 3463 "y.tab.c" /* yacc.c:1646  */
    break;

  case 195:
#line 935 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_expression -> DEC_OP unary_expression\n");
  }
#line 3471 "y.tab.c" /* yacc.c:1646  */
    break;

  case 196:
#line 939 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_expression -> unary_operator cast_expression\n");
  }
#line 3479 "y.tab.c" /* yacc.c:1646  */
    break;

  case 197:
#line 943 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_expression -> SIZEOF unary_expression\n");
  }
#line 3487 "y.tab.c" /* yacc.c:1646  */
    break;

  case 198:
#line 947 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_expression -> SIZEOF OPEN_PAREN type_name CLOSE_PAREN\n");
  }
#line 3495 "y.tab.c" /* yacc.c:1646  */
    break;

  case 199:
#line 953 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_operator -> AND\n");
  }
#line 3503 "y.tab.c" /* yacc.c:1646  */
    break;

  case 200:
#line 957 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_operator -> MUL\n");
  }
#line 3511 "y.tab.c" /* yacc.c:1646  */
    break;

  case 201:
#line 961 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_operator -> PLUS\n");
  }
#line 3519 "y.tab.c" /* yacc.c:1646  */
    break;

  case 202:
#line 965 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_operator -> MINUS\n");
  }
#line 3527 "y.tab.c" /* yacc.c:1646  */
    break;

  case 203:
#line 969 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_operator -> TILDE\n");
  }
#line 3535 "y.tab.c" /* yacc.c:1646  */
    break;

  case 204:
#line 973 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "unary_operator -> NOT\n");
  }
#line 3543 "y.tab.c" /* yacc.c:1646  */
    break;

  case 205:
#line 979 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> primary_expression\n");
  }
#line 3551 "y.tab.c" /* yacc.c:1646  */
    break;

  case 206:
#line 983 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression OPEN_SQUARE expression CLOSE_SQUARE\n");
  }
#line 3559 "y.tab.c" /* yacc.c:1646  */
    break;

  case 207:
#line 987 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression OPEN_PAREN CLOSE_PAREN\n");
  }
#line 3567 "y.tab.c" /* yacc.c:1646  */
    break;

  case 208:
#line 991 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression OPEN_PAREN argument_expression_list CLOSE_PAREN\n");
  }
#line 3575 "y.tab.c" /* yacc.c:1646  */
    break;

  case 209:
#line 995 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression DOT identifier\n");
  }
#line 3583 "y.tab.c" /* yacc.c:1646  */
    break;

  case 210:
#line 999 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression PTR_OP identifier\n");
  }
#line 3591 "y.tab.c" /* yacc.c:1646  */
    break;

  case 211:
#line 1003 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression INC_OP\n");
  }
#line 3599 "y.tab.c" /* yacc.c:1646  */
    break;

  case 212:
#line 1007 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "postfix_expression -> postfix_expression DEC_OP\n");
  }
#line 3607 "y.tab.c" /* yacc.c:1646  */
    break;

  case 213:
#line 1013 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "primary_expression -> identifier\n");
  }
#line 3615 "y.tab.c" /* yacc.c:1646  */
    break;

  case 214:
#line 1017 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "primary_expression -> constant\n");
  }
#line 3623 "y.tab.c" /* yacc.c:1646  */
    break;

  case 215:
#line 1021 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "primary_expression -> string\n");
  }
#line 3631 "y.tab.c" /* yacc.c:1646  */
    break;

  case 216:
#line 1025 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "primary_expression -> OPEN_PAREN expression CLOSE_PAREN\n");
  }
#line 3639 "y.tab.c" /* yacc.c:1646  */
    break;

  case 217:
#line 1031 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "argument_expression_list -> assignment_expression\n");
  }
#line 3647 "y.tab.c" /* yacc.c:1646  */
    break;

  case 218:
#line 1035 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "argument_expression_list -> argument_expression_list COMMA assignment_expression\n");
  }
#line 3655 "y.tab.c" /* yacc.c:1646  */
    break;

  case 219:
#line 1041 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "constant -> INTEGER_CONSTANT\n");
  }
#line 3663 "y.tab.c" /* yacc.c:1646  */
    break;

  case 220:
#line 1045 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "constant -> CHARACTER_CONSTANT\n");
  }
#line 3671 "y.tab.c" /* yacc.c:1646  */
    break;

  case 221:
#line 1049 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "constant -> FLOATING_CONSTANT\n");
  }
#line 3679 "y.tab.c" /* yacc.c:1646  */
    break;

  case 222:
#line 1053 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "constant -> ENUMERATION_CONSTANT\n");
  }
#line 3687 "y.tab.c" /* yacc.c:1646  */
    break;

  case 223:
#line 1059 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "string -> STRING_LITERAL\n");
  }
#line 3695 "y.tab.c" /* yacc.c:1646  */
    break;

  case 224:
#line 1065 "jstc_parser.yacc" /* yacc.c:1646  */
    {
    debug_log(g_parser_debug_level, PARSER_DEBUG_STREAM, "identifier -> IDENTIFIER\n");
  }
#line 3703 "y.tab.c" /* yacc.c:1646  */
    break;


#line 3707 "y.tab.c" /* yacc.c:1646  */
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 1070 "jstc_parser.yacc" /* yacc.c:1906  */



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

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

import unittest
import itertools
from compiler.compiler_state import CompilerState
from scanning.clexer import Lexer


class TestLexer(unittest.TestCase):

    SIMPLE_MAIN_TOKEN_TYPES = ['INT', 'ID', 'LPAREN', 'RPAREN', 'LBRACE', 'RETURN', 'ICONST', 'SEMI', 'RBRACE']

    def setUp(self):
        self.compiler_state = CompilerState()
        self.lexer = Lexer(compiler_state=self.compiler_state)

    def tearDown(self):
        self.lexer = None
        self.compiler_state = None

    def test_plain_main(self):
        data = """int main() {return 0;}"""
        self.compare_token_output(data, expected_token_types=TestLexer.SIMPLE_MAIN_TOKEN_TYPES)

    def test_regular_comments_get_eaten(self):
        data = """
            // this is a comment
            int main() {return 0;}
        """
        self.compare_token_output(data, expected_token_types=TestLexer.SIMPLE_MAIN_TOKEN_TYPES)

    def test_regular_comments_after_code_get_eaten(self):
        data = """
            int main() {// this is a comment
              return 0;
            }
        """
        self.compare_token_output(data, expected_token_types=TestLexer.SIMPLE_MAIN_TOKEN_TYPES)

    def test_block_comments_get_eaten(self):
        data = """
            /* This is a block comment */
            int main() {return 0;}
        """
        self.compare_token_output(data, expected_token_types=TestLexer.SIMPLE_MAIN_TOKEN_TYPES)

    def test_block_comments_within_code_get_eaten(self):
        data = """int main(/* This is a block comment */) {return 0;}"""
        self.compare_token_output(data, expected_token_types=TestLexer.SIMPLE_MAIN_TOKEN_TYPES)

    def test_mulitiline_block_comments_get_eaten(self):
        data = """
        int main() {
          /**
           * Input: None
           * Returns: Error status of program execution.
           */
          return 0;
        }"""
        self.compare_token_output(data, expected_token_types=TestLexer.SIMPLE_MAIN_TOKEN_TYPES)

    def test_declare_var(self):
        data = """
            int main() {
                int i = 0;
                return 0;
            }
            """
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
        self.assertTrue(True, 'No exceptions = Lexer successfully parsed.')

    def test_illegal_character(self):
        with self.assertRaises(Exception):
            data = """
            int main() {
                int i = 0;
                char 사랑 = 4;
                return 0;
            }
            """
            self.lexer.input(data)
            while True:
                tok = self.lexer.token()
                if not tok:
                    break

    def test_declare_global_constant(self):
        data = """
        const int GLOBAL_CONSTANT = 5;

        int main() {
          return 0;
        }
        """
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
        self.assertTrue(True, 'No exceptions = Lexer successfully parsed.')

    def test_declare_array(self):
        data = """
        int main() {
          int my_array[10];
          return 0;
        }
        """
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
        self.assertTrue(True, 'No exceptions = Lexer successfully parsed.')

    def test_block_comments(self):
        data = """
        /* this is a comment */
        int main() {

          int i = 0;

          /* this is another comment */
          return 0;
        }
        """
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
        self.assertTrue(True, 'No exceptions = Lexer successfully parsed.')

    def test_const_tokens(self):
        data = """
            int main() {
                int i = 0;
                int j = 5.6;
                printf("STRINGCONSTTT");
                char f = 'k';
                return 0;
            }
            """
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
        self.assertTrue(True, 'No exceptions = Lexer successfully parsed.')

    def test_declare_and_call_function(self):
        data = """
            int do_stuff(char c);

            int main() {
              do_stuff('f');
              return 0;
            }

            int do_stuff(char c) {
                return c + c;
            }
        """
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
        self.assertTrue(True, 'No exceptions = Lexer successfully parsed.')

    def test_bang_bang_S(self):
        data = """
            int do_stuff(char c);

            int main() {
              do_stuff('f');
              return 0;
            }

            int do_stuff(char c) {
                return c + c;
            }
        """
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
        self.assertTrue(True, 'No exceptions = Lexer successfully parsed.')

    def test_declare_struct(self):
        data = """
            struct Pixel {
                char r;
                char g;
                char b;
            };

            int main() {
              return 0;
            }
        """
        expected_token_types = ['STRUCT', 'ID', 'LBRACE', 'CHAR', 'ID', 'SEMI', 'CHAR', 'ID', 'SEMI', 'CHAR', 'ID',
                                'SEMI', 'RBRACE', 'SEMI', 'INT', 'ID', 'LPAREN', 'RPAREN', 'LBRACE', 'RETURN', 'ICONST',
                                'SEMI', 'RBRACE']

        self.compare_token_output(data, expected_token_types)

    def test_token_symbols(self):
        data = """
        +,-,*,/,%,|,&,~,^,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=
        =, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=
        ++,--
        ->
        ?
        () [] {} , . ; :
        ...
        """
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
        self.assertTrue(True, 'No exceptions = Lexer successfully parsed.')

    def test_reserved_words(self):
        data = """
        auto
        break
        case
        char
        const
        continue
        default
        do
        double
        else
        enum
        extern
        float
        for
        goto
        if
        int
        long
        register
        return
        short
        signed
        sizeof
        static
        struct
        switch
        typedef
        union
        unsigned
        void
        volatile
        while
        """
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
        self.assertTrue(True, 'No exceptions = Lexer successfully parsed.')

    def test_declare_function_pointer_typedef(self):
        data = """
        typedef int (*add_callback)(int a, int b);

        int add_two(int a, int b, add_callback callback);

        int normal_add(int a, int b);
        int weird_add(int a, int b);

        int main() {
          int x;
          int y;

          x = add_two(1, 2, normal_add);
          y = add_two(1, 2, weird_add);

          return 0;
        }

        int add_two(int a, int b, add_callback callback) {
            return callback(a, b);
        }

        int normal_add(int a, int b) {
            return a + b;
        }

        int weird_add(int a, int b) {
            return (a + b) % 4;
        }
        """
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
        self.assertTrue(True, 'No exceptions = Lexer successfully parsed.')

    def test_int_verify_no_overflow(self):
        self.assertFalse(Lexer.string_to_int_fails("4"), "4 should be acceptable")

    def test_int_verify_overflow(self):
        self.assertTrue(Lexer.string_to_int_fails("9999999999999999999999999999999999999999"),
                        "That should should overflow")

    def test_float_acceptable(self):
        self.assertTrue(Lexer.string_to_float_fails('1.123'), "1.23 is an acceptable float")

    def test_float_unacceptable(self):
        self.assertFalse(Lexer.string_to_float_fails('1.8E+308'), "'1.8E+308' is too big")

    def compare_token_output(self, data, expected_token_types):
        self.lexer.input(data)

        for given, expected in itertools.zip_longest(self.lexer.lexer, expected_token_types):
            self.assertEqual(given.type, expected)


if __name__ == '__main__':
    unittest.main()

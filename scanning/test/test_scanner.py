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
from scanning.clexer import Lexer


class TestLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer()

    def tearDown(self):
         self.lexer = None

    def test_int_verify_no_overflow(self):
        self.assertFalse(Lexer.does_int_overflow(int("4"), 64, False), "4 should be acceptable")

    def test_int_verify_overflow(self):
        self.assertTrue(Lexer.does_int_overflow(int("9999999999999999999999999999999999999999"), 64, False), "That should should overflow")

    def test_float_acceptable(self):
        self.assertTrue(Lexer.float_is_acceptable('1.123'), "1.23 is an acceptable float")

    def test_float_unacceptable(self):
        self.assertFalse(Lexer.float_is_acceptable('1.8E+308'), "'1.8E+308' is too big")

    def test_plain_main(self):
        data = """int main() {return 0;}"""
        self.lexer.input(data)
        while True:
          tok = self.lexer.token()
          if not tok:
            break
        self.assertTrue(True, 'No exceptions = Lexer successfully parsed.')

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
              struct Pixel pixel;
              pixel.r = 255;
              pixel.g = 0;
              pixel.b = 0;

              return 0;
            }
        """
        self.lexer.input(data)
        while True:
          tok = self.lexer.token()
          if not tok:
            break
        self.assertTrue(True, 'No exceptions = Lexer successfully parsed.')

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

    def test_token_words(self):
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


if __name__ == '__main__':
    unittest.main()

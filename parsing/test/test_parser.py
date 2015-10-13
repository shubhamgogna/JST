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
import unittest
import time
from loggers.parser_logger import ParserLogger
from parsing.cparser import Parser
from scanning.clexer import Lexer


class TestParser(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer()
        self.parser = Parser(self.lexer)

    def tearDown(self):
        self.parser.teardown()
        self.parser = None
        self.lexer = None

    def test_plain_main(self):
        data = """int main() {return 0;}"""
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_malformed_main_fails(self):
        with self.assertRaises(Exception):
            data = 'badmain(] {return 0;}'
            self.parser.parse(data)

    def test_declare_var(self):
        data = """
            int main() {
                int i = 0;
                return 0;
            }
            """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_global_constant(self):
        data = """
        const int GLOBAL_CONSTANT = 5;

        int main() {
          return 0;
        }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_array(self):
        data = """
        int main() {
          int my_array[10];
          return 0;
        }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

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
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_struct(self):
        self.parser.logger.add_switch(ParserLogger.PRODUCTION)

        data =  """
            int global;

            // a comment

            struct Pixel {
                char r;
                // char g;
                // char b;
            };

            int main() {
              struct Pixel pixel;
              pixel.r = 255;
              // pixel.g = 0;
              // pixel.b = 0;

              return 0;
            }
        """

        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

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
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')




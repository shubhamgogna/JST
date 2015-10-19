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
from compiler.compiler_state import CompilerState
from loggers.logger import Logger
from parsing.cparser import Parser
from scanning.clexer import Lexer


class TestParser(unittest.TestCase):
    def setUp(self):
        self.debug = True

        self.compiler_state = CompilerState()
        self.lexer = Lexer(compiler_state=self.compiler_state)
        self.parser = Parser(compiler_state=self.compiler_state, lexer=self.lexer)
        self.parser.logger.add_switch(Logger.TOKEN)

    def tearDown(self):
        self.parser.logger.remove_switch(Logger.TOKEN)
        self.parser.teardown()
        self.parser = None
        self.lexer = None
        self.compiler_state = None

    def test_plain_main(self):
        data = """int main() {return 0;}"""
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_primitive_variable(self):
        data = """
            int main() {
                int i;
                return 0;
            }
            """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_and_assign_primitive_variable(self):
        data = """
            int main() {
                int i = 5;
                return 0;
            }
            """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_multiple_primitive_variable(self):
        # self.enable_parser_debugging()
        data = """
            int main() {
                int i, j, k;

                i = 0;
                !!S
                return 0;
            }
            """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_modify_primitive_variable(self):
        self.parser.logger.add_switch(Logger.PRODUCTION)
        self.parser.logger.add_switch(Logger.INFO)

        data = """
            int main() {
                int i = 0;
                i += 5;
                return 0;
            }
            """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_pointer_variable(self):
        self.enable_parser_debugging()
        data = """
            int main() {
                int* i;
                i = 0;
                !!S
                return 0;
            }
            """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_deep_pointer_variable(self):
        data = """
            int main() {
                int*** i;
                return 0;
            }
            """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_global_constant(self):
        data = """
        const int GLOBAL_CONSTANT = 5;

        int main() {
          int i = GLOBAL_CONSTANT;
          return 0;
        }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_typedef(self):
        self.enable_parser_debugging()
        data = """
        typedef int GlorifiedInt;

        int main() {
          return 0;
        }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_typedef_and_use_typedef_in_variable_declaration(self):
        self.enable_parser_debugging()

        data = """
        typedef int GlorifiedInt;

        int main() {
          GlorifiedInt i = 3;
          return 0;
        }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_while_loop(self):
        data = """
        int main() {
          while (1) {}
          return 0;
        }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_for_loop(self):
        self.enable_parser_debugging()
        data = """
        int main() {
          int i;
          for (i = 0; i < 3; i++) {}

          return 0;
        }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_do_while_loop(self):
        data = """
        int main() {
          int i = 1;
          do {i++;} while(i);
          return 0;
        }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_array(self):
        self.enable_parser_debugging()
        data = """
        int main() {
          int my_array[10];
          return 0;
        }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_array_with_constant_expression_in_subscript(self):
        data = """
        int main() {
          int my_array[5 + 5];
          int i;
          !!S
          return 0;
        }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_access_array(self):
        data = """
        int main() {
          int i = 0;
          int my_array[10];

          int first_element = my_array[0];
          int some_other_element = my_array[i];

          return 0;
        }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_function(self):
        data = """
            int do_stuff(char c);

            int main() {
              return 0;
            }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_function_implementation(self):
        data = """
            int do_stuff(char c) {
                return c + c;
            }

            int main() {
              return 0;
            }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_call_function(self):
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

    def test_declare_string_literal_char_star(self):
        data = """
            char* literal_string = "hello there";

            int main() {
              char array_string[] = "hey";
              return 0;
            }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_declare_segmented_string_literal(self):
        print('segmented')
        data = """
            char* literal_string = "hello "
                                   "world";

            int main() {
              char array_string[] = "hey";
              return 0;
            }
        """
        self.parser.parse(data)
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

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
              pixel.g = 255;
              pixel.b = 255;

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

    # TODO: don't put a lot of emphasis on bad cases until things are strong with the good cases
    def test_malformed_main_fails(self):
        with self.assertRaises(Exception):
            data = 'badmain(] {return 0;}'
            self.parser.parse(data)

    def enable_parser_debugging(self):
        if self.debug:
            self.parser.logger.add_switch(Logger.PRODUCTION)
            self.parser.logger.add_switch(Logger.INFO)

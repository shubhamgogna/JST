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
        # self.parser.logger.add_switch(Logger.TOKEN)

    def tearDown(self):
        # self.parser.logger.remove_switch(Logger.TOKEN)
        self.parser.teardown()
        self.parser = None
        self.lexer = None
        self.compiler_state = None

    def test_plain_main(self):
        self.enable_parser_debugging()

        data = """int main() {return 0;} !!C"""
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        print(symbol_table_clone)

        self.check_correct_element(symbol_table_clone, 'main', 0, 'int main()')

    def test_declare_primitive_variable(self):
        self.enable_parser_debugging()

        data = """
            int main() {
                int i;
                !!C
                return 0;
            }
            """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'i', 1, 'int i')


    def test_declare_and_assign_primitive_variable(self):
        data = """
            int main() {
                int i = 5;
                !!C
                return 0;
            }
            """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'i', 1, 'int i')


    def test_declare_multiple_primitive_variable(self):
        # self.enable_parser_debugging()
        data = """
            int main() {
                int i, j, k;

                i = 0;
                !!C
                return 0;
            }
            """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'i', 1, 'int i')
        self.check_correct_element(symbol_table_clone, 'j', 1, 'int j')
        self.check_correct_element(symbol_table_clone, 'k', 1, 'int k')

    def test_modify_primitive_variable(self):
        self.enable_parser_debugging()

        data = """
            int main() {
                int i = 0;
                i += 5;
                !!C
                return 0;
            }
            """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'i', 1, 'int i')

    def test_declare_pointer_variable(self):
        self.enable_parser_debugging()
        data = """
            int main() {
                int* i;
                i = 0;
                !!C
                return 0;
            }
            """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'i', 1, 'int* i')

    def test_declare_deep_pointer_variable(self):
        data = """
            int main() {
                int*** i;
                !!C
                return 0;
            }
            """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'i', 1, 'int*** i')

    def test_declare_global_constant(self):
        data = """
        const int GLOBAL_CONSTANT = 5;

        int main() {
          int i = GLOBAL_CONSTANT;
          !!C
          return 0;
        }
        """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'GLOBAL_CONSTANT', 0, 'const int GLOBAL_CONSTANT')
        self.check_correct_element(symbol_table_clone, 'i', 1, 'int i')

    # def test_declare_typedef(self):
    #     self.enable_parser_debugging()
    #     data = """
    #     typedef int GlorifiedInt;
    #     !!C
    #
    #     int main() {
    #       return 0;
    #     }
    #     """
    #     self.parser.parse(data)
    #     symbol_table_clone = self.compiler_state.cloned_tables[0]
    #
    #     # TODO: How are we handling typedefs?
    #     self.check_correct_element(symbol_table_clone, 'GlorifiedInt', 0, 'typedef int GlorifiedInt')

    # def test_declare_typedef_and_use_typedef_in_variable_declaration(self):
    #     self.enable_parser_debugging()
    #
    #     data = """
    #     typedef int GlorifiedInt;
    #
    #     int main() {
    #       GlorifiedInt i = 3;
    #       return 0;
    #       !!C
    #     }
    #     """
    #     self.parser.parse(data)
    #     symbol_table_clone = self.compiler_state.cloned_tables[0]
    #
    #     # TODO: How are we handling typedefs?
    #     self.check_correct_element(symbol_table_clone, 'GlorifiedInt', 0, 'typedef int GlorifiedInt')
    #     self.check_correct_element(symbol_table_clone, 'i', 1, 'GlorifiedInt')

    def test_while_loop(self):
        data = """
        int main() {
          while (1) {}
          return 0;
        }
        !!C
        """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]
        print('hi', symbol_table_clone)

        self.check_correct_element(symbol_table_clone, 'main', 0, 'int main()')

    def test_for_loop(self):
        self.enable_parser_debugging()
        data = """
        int main() {
          int i;
          for (i = 0; i < 3; i++) {}
          !!C
          return 0;
        }
        """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'i', 1, 'int i')

    def test_do_while_loop(self):
        data = """
        int main() {
          int i = 1;
          do {i++;} while(i);
          !!C
          return 0;
        }
        """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'i', 1, 'int i')

    def test_declare_array(self):
        self.enable_parser_debugging()
        data = """
        int main() {
          int my_array[10];
          !!C
          return 0;
        }
        """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'my_array', 1, 'int my_array[10]')

    def test_declare_array_with_constant_expression_in_subscript(self):
        data = """
        int main() {
          int my_array[5 + 5];
          int i;
          !!C
          return 0;
        }
        """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'my_array', 1, 'int my_array[10]')

    def test_access_array(self):
        self.enable_parser_debugging()
        data = """
        int main() {
          int i = 0;
          int my_array[10];

          int first_element = my_array[0];
          int some_other_element = my_array[i];

          !!C
          return 0;
        }
        """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        print(symbol_table_clone)

        self.check_correct_element(symbol_table_clone, 'i', 1, 'int i')
        self.check_correct_element(symbol_table_clone, 'my_array', 1, 'int my_array[10]')
        self.check_correct_element(symbol_table_clone, 'first_element', 1, 'int first_element')
        self.check_correct_element(symbol_table_clone, 'some_other_element', 1, 'int some_other_element')

    def test_declare_function(self):
        data = """
            int do_stuff(char c);
            !!C

            int main() {
              return 0;
            }
        """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'do_stuff', 0, 'int do_stuff(char c)')

    def test_declare_function_implementation(self):
        data = """
            int do_stuff(char c) {
                return c + c;
            }
            !!C

            int main() {
              return 0;
            }
        """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'do_stuff', 0, 'int do_stuff(char c)')

    def test_call_function(self):
        self.enable_parser_debugging()
        data = """
            int do_stuff(char c);
            !!C

            int main() {
              do_stuff('f');

              return 0;
            }

            int do_stuff(char c) {
                return c + c;
                !!C
            }
        """
        self.parser.parse(data)
        symbol_table_clone_inner = self.compiler_state.cloned_tables[0]
        symbol_table_clone_outer = self.compiler_state.cloned_tables[1]

        print(symbol_table_clone_outer)

        self.check_correct_element(symbol_table_clone_inner, 'do_stuff', 0, 'int do_stuff(char c)')
        self.check_correct_element(symbol_table_clone_outer, 'c', 1, 'char c')

    def test_declare_string_literal_char_star(self):
        self.enable_parser_debugging()
        data = """
            char* literal_string = "hello there";
            !!C

            int main() {
              return 0;
            }
        """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'literal_string', 0, 'char* literal_string')

    def test_declare_string_as_array(self):
        self.enable_parser_debugging()
        data = """
            int main() {
              char array_string[] = "hey";
              !!C
              return 0;
            }
        """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'array_string', 1, 'char array_string[]')

    def test_declare_segmented_string_literal(self):
        print('segmented')
        data = """
            char* literal_string = "hello "
                                   "world";
            !!C
            int main() {
              return 0;
            }
        """
        self.parser.parse(data)
        symbol_table_clone = self.compiler_state.cloned_tables[0]

        self.check_correct_element(symbol_table_clone, 'literal_string', 0, 'char* literal_string')

    # def test_declare_struct(self):
    #     data = """
    #         !!C
    #         struct Pixel {
    #             char r;
    #             char g;
    #             char b;
    #             !!C
    #         };
    #
    #         int main() {
    #           struct Pixel pixel;
    #           pixel.r = 255;
    #           pixel.g = 255;
    #           pixel.b = 255;
    #           !!C
    #           return 0;
    #         }
    #     """
    #
    #     self.parser.parse(data)
    #     symbol_table_clone = self.compiler_state.cloned_tables[0]
    #
    #     # TODO: How are we handling structs?
    #     self.check_correct_element(symbol_table_clone, 'Pixel', 0, 'struct Pixel')
    #     self.check_correct_element(symbol_table_clone, 'r', 1, 'char r')
    #     self.check_correct_element(symbol_table_clone, 'g', 1, 'char g')
    #     self.check_correct_element(symbol_table_clone, 'b', 1, 'char b')
    #     self.check_correct_element(symbol_table_clone, 'pixel', 1, 'struct Pixel pixel')
    #
    #
    # def test_declare_function_pointer_typedef(self):
    #     data = """
    #     typedef int (*add_callback)(int a, int b);
    #
    #     int add_two(int a, int b, add_callback callback);
    #
    #     int normal_add(int a, int b);
    #     int weird_add(int a, int b);
    #
    #     int main() {
    #       int x;
    #       int y;
    #
    #       x = add_two(1, 2, normal_add);
    #       y = add_two(1, 2, weird_add);
    #
    #       !!C
    #       return 0;
    #     }
    #
    #     int add_two(int a, int b, add_callback callback) {
    #         return callback(a, b);
    #     }
    #
    #     int normal_add(int a, int b) {
    #         return a + b;
    #     }
    #
    #     int weird_add(int a, int b) {
    #         return (a + b) % 4;
    #     }
    #     """
    #     self.parser.parse(data)
    #     symbol_table_clone = self.compiler_state.cloned_tables[0]
    #
    #     # TODO: Function Pointers??
    #     self.check_correct_element(symbol_table_clone, 'x', 1, 'int x')


    def test_bubble_sort(self):
        data = """
            // function prototypes
            void print( int* list, int size);
            void bubbleSort(int* list, int size);

            // main
            int main() {
               // initialize vars
               int* list = (int*)malloc(10);
               int i;
               srand(time(NULL));

               // create list
               for(i =0; i<10;i++)
                  {
                   list[i] = rand() % 10 + 1; 
                  }
               print(list, 10);

               // bubble sort
               bubbleSort( list, 10 );

               printf( "Sorted " );
               print(list, 10);

               !!C

               // return
               return 0;

            }


            // fxn imp
            void bubbleSort(int* list, int size){
               // initialize vars
               int i,j;
               int temp;
               int swapped;
               
               // loop through list
               for( i = 0; i < size; i++)
                  {

                  // swapped is false
                  swapped = 0;

                  // loop through list
                  for( j = 0; j < size - 1; j++)
                     {
                     // if smaller, swap
                     if( list[j+1] < list[j])
                        {
                        temp = list[j];
                        list[j] = list[j+1];
                        list[j+1] = temp;
                        swapped = 1;
                        }
                     }
                  // if swapped is false, break
                  if( swapped == 0)
                     {         
                     break;
                     }   
                  }

               }

            void print( int* list, int size ){
               int i;
               printf("List is: ");

               for(i =0; i < size; i++)
                  {
                  printf( "%d ", list[i] );
                  }
               printf("\n");
               }
        """
        self.parser.parse(data)
        #symbol_table_clone = self.compiler_state.cloned_tables[0]

        # TODO: Determine what scopes we want to test here
        #self.check_correct_element(symbol_table_clone, '', 1, '')
        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')


    def test_recursive_factorial(self):
        data = """
            long int recur_Fact( int number);

            int main() {
              int number;
              long int fact;

              printf( "Enter number to get factorial of: ");
              scanf( "%d", &number );

              fact = recur_Fact(number);

              printf("Factorial of %d is:  %ld\n", number, fact);

              return 0;
            }

            long int recur_Fact( int number) {
              // base case
              if( number <= 0)
                return 1;

              // recursive case
              else if( number > 1 ) {
                return number*recur_Fact(number-1);    
              }
            }
        """
        self.parser.parse(data)
        #symbol_table_clone = self.compiler_state.cloned_tables[0]

        # TODO: Determine what scopes we want to test here
        #self.check_correct_element(symbol_table_clone, '', 1, '')

        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')

    def test_iterative_factorial(self):
        data = """
            long int iter_Fact( int number);

            int main() {
              int number;
              long int fact;

              printf( "Enter number to get factorial of: ");
              scanf( "%d", &number );

              fact = iter_Fact(number);

              printf( "Factorial of %d is:  %ld \n", number, fact);

              return 0;
            }

            long int iter_Fact( int number) {
              int i;
              long int fact = 1;

              if( i < 0){
                return 1;
              }

              for( i = number; i > 0; i --) {
                fact = fact*i;
              }
              return fact;
            }
        """
        self.parser.parse(data)
        #symbol_table_clone = self.compiler_state.cloned_tables[0]

        # TODO: Determine what scopes we want to test here
        #self.check_correct_element(symbol_table_clone, '', 1, '')

        self.assertTrue(True, 'No exceptions = Parser successfully parsed.')



    # TODO: don't put a lot of emphasis on bad cases until things are strong with the good cases
    def test_malformed_main_fails(self):
        with self.assertRaises(Exception):
            data = 'badmain(] {return 0;}'
            self.parser.parse(data)

    def enable_parser_debugging(self):
        if self.debug:
            self.parser.prod_logger.add_switch(Logger.PRODUCTION)
            self.parser.prod_logger.add_switch(Logger.INFO)


    def check_correct_element(self, symbol_table_clone, check_value, check_scope, check_string):
        found_symbol, in_scope = symbol_table_clone.find(check_value)
        self.assertEqual(in_scope, check_scope)
        self.assertEquals(check_string, str(found_symbol))


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


#~~~
# The purpose of this file is to have the plainest possible test cases for presentation purposes. This file should
# not have experimental or correctness verification tests, but rather succinct, clean test cases or well-thought out
# multi-feature tests that are directly intended for demonstration of the compiler's capabilities.
#
# Unlike other files, this file should not produce anything other than what will end up in a MIPS file.
#~~~


import unittest
import compiler.compiler_state as compiler
import mips.generation as generation

import loggers.logger as log


class TestFullRunAssemblyGeneration(unittest.TestCase):
    def setUp(self):
        self.compiler_state = compiler.CompilerState(print_productions=False)
        self.enable_debug(False)

        self.generator = generation.MipsGenerator(self.compiler_state, inject_source = False, inject_3ac=False)

    def tearDown(self):
        self.compiler_state.teardown()
        self.compiler_state = None

    def enable_debug(self, enable, productions=True, source=False):
        if enable:
            prod_logger = self.compiler_state.get_parser_logger()

            prod_logger.add_switch(log.Logger.INFO)
            if productions:
                prod_logger.add_switch(log.Logger.PRODUCTION)

            if source:
                prod_logger.add_switch(log.Logger.SOURCE)

    def test_plain_main(self):
        data = """
            int main() {
                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        source_tac = ast.to_3ac()

        self.generator.load(source_tac)
        self.generator.translate_tac_to_mips()
        print(self.generator.dumps())

    def test_local_variable_declaration_and_assignment(self):
        data = """
            int main() {
                int local_variable;

                // print the garbage that will be in the variable
                print_int(local_variable);

                // perform an assignment and print to show that the
                // value was assigned
                local_variable = 123;
                print_int(local_variable);

                // assign another value to show that it can be overwritten
                local_variable = 126;
                print_int(local_variable);

                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        source_tac = ast.to_3ac()

        self.generator.load(source_tac)
        self.generator.translate_tac_to_mips()
        print(self.generator.dumps())

    def test_local_variable_addition(self):
        data = """
            int main() {
                int local_variable = 1;
                int other_variable = 2;
                int la = 5;

                // print the values that will be in the variables
                print_int(local_variable);
                print_int(other_variable);

                // perform the addition
                print_int(local_variable + other_variable);
                la = local_variable + other_variable;
                print_int(la);

                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        source_tac = ast.to_3ac()

        # i = 0;
        # for item in source_tac:
        #     if i% 3 == 0:
        #         print('\n')
        #     print(item)
        #
        # print('\n\n\n\n')

        self.generator.load(source_tac)
        self.generator.translate_tac_to_mips()
        print(self.generator.dumps())


    def test_global_variables_declaration_and_assignement(self):
        data = """
            const int GLOBAL_CONST = 4;
            int GLOBAL_VAR = 2;

            int main() {

                // print the values that will be in the variables
                print_int(GLOBAL_CONST);
                print_int(GLOBAL_VAR);

                // perform the assignment
                GLOBAL_VAR = GLOBAL_CONST;
                print_int(GLOBAL_VAR);

                return 0;
            }


            """
        ast = self.compiler_state.parse(data)
        source_tac = ast.to_3ac()

        #TODO: Take out debug after fixing test case issues
        print(source_tac, 'asdfsadf')

        self.generator.load(source_tac)
        self.generator.translate_tac_to_mips()
        print(self.generator.dumps())


    def test_if_elif_else(self):
        data = """
            int main() {

                int i = 0;

                // FizzBuzz
                for( i = 1; i <= 30; i++) {
                   //FizzBuzz
                   if( i % 3 == 0){

                        //FizzBuzz
                        if( i % 5 == 0 ){

                            //print_char('f');
                            //print_char('b');
                            print_int(35);
                        }

                        //Fizz
                        else {
                           //print_char('f');
                            print_int(3);
                        }

                   }
                   // Buzz
                   else if( i % 5 == 0) {
                       //print_char('b');
                       print_int(5);

                   }
                   // Number
                   else{
                       print_int(i);
                   }
                }

                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        source_tac = ast.to_3ac()

        self.generator.load(source_tac)
        self.generator.translate_tac_to_mips()
        print(self.generator.dumps())

    def test_all_three_loop_types(self):
        data = """
            int main() {

                int i = 0;
                int j = 10;
                int k = 15;
                int l = 20;



                // test while loops
                while( i < 5){
                    print_int(i);
                    i++;
                }

                // test do while loops

                // test for loops

                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        source_tac = ast.to_3ac()

        self.generator.load(source_tac)
        self.generator.translate_tac_to_mips()
        print(self.generator.dumps())


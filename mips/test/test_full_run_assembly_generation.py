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

                // print the garbage that will be in the variable
                print_int(local_variable);
                print_int(other_variable);

                // perform the addition
                print_int(local_variable + other_variable);

                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        source_tac = ast.to_3ac()

        self.generator.load(source_tac)
        self.generator.translate_tac_to_mips()
        print(self.generator.dumps())
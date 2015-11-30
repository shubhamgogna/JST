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

import mips.generation
from compiler.compiler_state import CompilerState
from loggers.logger import Logger


class TestMipsGenerator(unittest.TestCase):
    def setUp(self):
        self.compiler_state = CompilerState(print_productions=True)
        self.enable_debug(False)

        self.generator = mips.generation.MipsGenerator(self.compiler_state)

    def tearDown(self):
        self.compiler_state.teardown()
        self.compiler_state = None

    def enable_debug(self, enable, productions=True, source=False):
        if enable:
            prod_logger = self.compiler_state.get_parser_logger()

            prod_logger.add_switch(Logger.INFO)
            if productions:
                prod_logger.add_switch(Logger.PRODUCTION)

            if source:
                prod_logger.add_switch(Logger.SOURCE)

    def test_plain_main(self):
        data = """
            int main()
            {
                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        source_tac = ast.to_3ac()

        self.generator.load(source_tac)
        self.generator.translate_tac_to_mips()
        print(self.generator.dumps())

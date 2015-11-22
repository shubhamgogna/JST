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
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from compiler.compiler_state import CompilerState
from loggers.logger import Logger


class TestTac(unittest.TestCase):

    def setUp(self):
        self.compiler_state = CompilerState()
        self.enable_debug(False)

    def tearDown(self):
        self.compiler_state.teardown()
        self.compiler_state = None

    def enable_debug(self, enable, productions=False, source=False):
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
        # print(ast.to_graph_viz_str())


    def test_simple_assignment(self):
        data = """
            int main()
            {
                int i = 0;
                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        # print(ast.to_graph_viz_str())

    def test_constant_expression(self):
        data = """
            int main()
            {
                int i, a, b;
                i = a + b;
                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        # print(ast.to_graph_viz_str())

    def test_explicit_cast(self):
        data = """
            int main()
            {
                int i = (int) 4.2;
                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        # print(ast.to_graph_viz_str())


    def test_if_elif_else(self):
        data = """
            int main()
            {
                int i;
                if (i == 5)
                {
                    i = 6;
                }
                else if(i == 6)
                {
                    i = 7;
                }
                else
                {
                    i = 5;
                }
            }
            """
        ast = self.compiler_state.parse(data)
        # print(ast.to_graph_viz_str())

    def test_while_loop(self):
        data = """
            int main()
            {
                int i;
                while(i < 5){}
            }
            """
        ast = self.compiler_state.parse(data)
        # print(ast.to_graph_viz_str())

    def test_array_access(self):
        data = """
            int main()
            {
                int a[2][2];
                a[0][0] = a[1][1];
                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        # print(ast.to_graph_viz_str())

    def test_array_initializers(self):
        data = """
            int main()
            {
                int a[5] = {1,2,3,4,5};
                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        # print(ast.to_graph_viz_str())

    def test_function_with_param(self):
        data = """
            int foo( int a, int b, int c);

            int main()
            {
                int i = foo(1,2,3);
                return 0;
            }

            int foo( int a, int b, int c)
            {
                return 1;
            }
            """
        ast = self.compiler_state.parse(data)
        # print(ast.to_graph_viz_str())

    def test_for_loop(self):
        data = """
            int main()
            {
                int i = 0;
                for(i=0;i<3;i++)
                    {
                    /* pass */
                    }
                return 0;
            }
            """
        ast = self.compiler_state.parse(data)
        # print(ast.to_graph_viz_str())

    def test_do_while_loop(self):
        data = """
            int main()
            {
                int i;
                do {} while (i > 10);
            }
            """
        ast = self.compiler_state.parse(data)
        # print(ast.to_graph_viz_str())

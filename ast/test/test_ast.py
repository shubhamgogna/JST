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
from parsing.cparser import Parser
from scanning.clexer import Lexer


class TestAst(unittest.TestCase):

    def setUp(self):
        self.debug = True

        self.compiler_state = CompilerState()
        self.lexer = Lexer(compiler_state=self.compiler_state)
        self.parser = Parser(compiler_state=self.compiler_state, lexer=self.lexer)

        self.enable_debug()

    def tearDown(self):
        self.parser.teardown()
        self.parser = None
        self.lexer = None
        self.compiler_state = None

    def enable_debug(self, productions=True, source=True):
        if self.debug:
            self.parser.prod_logger.add_switch(Logger.INFO)
            if productions:
                self.parser.prod_logger.add_switch(Logger.PRODUCTION)

            if source:
                self.parser.prod_logger.add_switch(Logger.SOURCE)

    def test_empty_file(self):
        data = ""
        ast = self.parser.parse(data)
        print(ast)

    def test_plain_main(self):
        data = "int main() {return 0;}"
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_simple_variable_declaration(self):
        data = """
            int main() {int i;}
            """
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_const_declaration(self):
        data = """
            int main() {const int i;}
            """
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_array_declaration(self):
        data = """
            int main() {int i[5];}
            """
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_2d_array_declaration(self):
        data = """
            int main() {int i[5][7];}
            """
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_lone_if(self):
        data = ''\
            'int main() {\n' \
            '  //int i;\n'\
            '  if (/*i ==*/ 5) {\n'\
            '    //i = 6;\n'\
            '  }\n' \
            '}\n'\
            ''
        ast = self.parser.parse(data)
        print(ast.children[0])
        print(ast.children[0].children)
        print(ast, type(ast))
        print(ast.to_graph_viz_str())


    def test_if_else(self):
        data = ''\
            'int main() {\n' \
            '  //int i;\n'\
            '  if (/*i ==*/ 5) {\n'\
            '    //i = 6;\n'\
            '  } else {\n'\
            '    //i = 5;\n' \
            '  }\n' \
            '}\n'\
            ''
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_if_elif_else(self):
        data = ''\
            'int main() {\n' \
            '  //int i;\n'\
            '  if (/*i ==*/ 5) {\n'\
            '    //i = 6;\n'\
            '  } else if (/*i ==*/ 6) {\n' \
            '    //i = 7;\n' \
            '  } else {\n'\
            '    //i = 5;\n' \
            '  }\n' \
            '}\n'\
            ''
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())


    def test_simple_assign_const(self):
        # self.enable_debug()

        data = '''
            int main()
            {
            int g;
            g = 5;
            }
            '''
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_simple_assign_var(self):
        # self.enable_debug()

        data = """
            int main()
            {
            int g;
            int G;

            g = 5;
            G = g;
            }
            """

        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_array_simple_assign(self):
        # self.enable_debug()

        data = '''
            int main()
            {
            int a[10];
            a[1] = 4;
            }
            '''

        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_array_simple_access(self):
        self.enable_debug()

        data = '''
            int main()
            {
            int g;
            int a[10];
            a[1] = 4;
            g = a[1];
            }
            '''

        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_array_access_const_expr(self):
        # self.enable_debug()

        data = '''
            int main()
            {
            int g;
            int a[10];
            a[6] = 4;
            g = a[5 + 1];
            }
            '''

        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_array_access_var_expr(self):
        # self.enable_debug()

        data = '''
            int main()
            {
            int g;
            int a[10];
            a[1] = 4;
            g = a[1];
            g = a[g + 1];
            }

            '''

        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_array_twodim(self):
        # self.enable_debug()

        data = '''
            int main()
            {
            int b[10][10];
            b[1][1] = 5;
            }

            '''

        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_for_loop_1(self):
        data = """
            int main()
            {
                int i;
                for(i = 0; ;) {}
            }
            """
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_for_loop_2(self):
        data = """
            int main()
            {
                int i;
                for(i = 0; ; i++) {}
            }
            """
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_for_loop_3(self):
        data = """
            int main()
            {
                int i;
                for(i = 0; i < 1; i++) {}
            }
            """
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_function_decl_top_impl_bottom(self):
        self.enable_debug()

        data = """
            int do_stuff();

            int do_stuff()
            {
                return 5;
            }
            """

        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_function_decl_top_impl_bottom_call_middle(self):
        self.enable_debug()

        data = """
            int do_stuff();

            int main()
            {
                return do_stuff();
            }

            int do_stuff()
            {
                return 5;
            }
            """

        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_function_parameters(self):
        self.enable_debug()

        data = """
            int do_stuff(int* ret, int x)
            {
                *ret = x + x;
                return 5;
            }

            int main()
            {
                return do_stuff();
            }
            """

        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_function_def_on_top(self):
        data = """
            // definition on top
            int do_stuff() {
                return 5;
            }
            """
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_function_def_on_top_call(self):
        data = """
            int do_stuff()
            {
                return 5;
            }

            int main()
            {
                return do_stuff();
            }
            """
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())

    def test_declare_const_and_var_types(self):
        data = '''
            int main(){

                const int i;
                float j;
                char k;
                
            }
            '''
        ast = self.parser.parse(data)
        print(ast.to_graph_viz_str())
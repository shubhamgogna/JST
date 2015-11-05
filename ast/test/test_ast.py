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


    def enable_debug(self, productions=True, source=False):
        if self.debug:
            self.parser.prod_logger.add_switch(Logger.INFO)
            if productions:
                self.parser.prod_logger.add_switch(Logger.PRODUCTION)

            if source:
                self.parser.prod_logger.add_switch(Logger.SOURCE)

    def test_empty_file(self):

        i = LABEL_COUNTER.get()
        print(i)

        data = ""
        ast = self.parser.parse(data)
        print(ast)

    def test_plain_main(self):
        data = "int main() {return 0;}"
        ast = self.parser.parse(data)

        print(ast)


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
        print(ast, type(ast))
        print(ast.to_graph_viz_str())
        print(ast.children)


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

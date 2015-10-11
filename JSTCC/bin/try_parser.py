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

from parsing.calcparser import CalcParser
from parsing.cparser import Parser
from scanning.clexer import Lexer
from scanning.calclexer import CalcLexer


def main():

    p = Parser(Lexer())
    result = p.parse("int main() {return 0;}")
    print(result)

    lexer = CalcLexer()
    parser = CalcParser(lexer)

    while True:
       try:
           s = input('calc > ')
       except EOFError:
           break
       if not s: continue
       result = parser.parse(s)
       print(result)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

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

import sys

import argparse
from parsing.cparser import Parser
from scanning.clexer import Lexer


dummy_data = """int main() {int i; !!S return 0;}"""

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input", type=str, help="The C program code file to compile.")
    arg_parser.add_argument("-o", "--outfile", type=str, default='',
                            help="The name of the file output file. Defaults to $(TODO).")
    arg_parser.add_argument("-s", "--scandebug", type=int, choices=[0, 1], default=0,
                            help="The debug level for the scanner.")
    arg_parser.add_argument("-p", "--parsedebug", type=int, choices=[0, 1], default=0,
                            help="The debug level for the parser.")
    arg_parser.add_argument("-w", "--warnlevel", type=int, choices=[0, 1], default=0,
                            help="The debug level for the parser.")
    args = arg_parser.parse_args()

    print(args)


    data = dummy_data

    parser = Parser(lexer=Lexer())
    parser.parse(data)

    parser.teardown()

if __name__ == '__main__':
    main()
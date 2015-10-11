# This file is part of $(PROJECT_NAME).

# $(PROJECT_NAME) is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# $(PROJECT_NAME) is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
import sys

from parsing.cparser import Parser
from scanning.calclexer import CalcLexer


class Thing(object):
    def __init__(self):
        self.out = sys.stdout

    def sound_off(self):
        self.out.write("Sound off!\n")

    def tear_down(self):
        if self.out is not sys.stdout:
            self.out.close()

        self.out.write('Still open!\n')

        self.out = None


def main():
    t = Thing()
    t.sound_off()
    t.tear_down()

if __name__ == '__main__':
    main()
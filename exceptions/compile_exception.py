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


class CompileException(Exception):
    def __init__(self, message, line_num, token_col, source_line):
        self.message = message
        self.line_num = line_num
        self.token_col = token_col
        self.source_line = source_line

    def __str__(self):
        return "{}\n  Line {}, Column {}\n  Source: {}".\
            format(self.message, self.line_num, self.token_col, self.source_line)

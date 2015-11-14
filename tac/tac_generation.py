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

import tac.instructions as instructions

class TacInstruction(object):
    NULL = None

    def __init__(self, instruction:str, dest:str=NULL, src1:str=NULL, src2:str=NULL):
        self.instruction = instruction
        self.dest = dest
        self.src1 = src1
        self.src2 = src2

    def __str__(self):
        """
        __str__ is supposed to be "human readable, so this method will produce a more concise string that will fit in
        the terminal better for debugging.
        """
        if self.instruction == instructions.COMMENT:
            return '{}: {}'.format(instructions.COMMENT, self.dest)
        else:
            return '{}, {}, {}, {}'.format(self.instruction, self.dest, self.src1, self.src2)

    def __repr__(self):
        """
        __repr__ is supposed to be "unambiguous," but it gets called on all contained objects when you stringify a
        container, so this will be the method that produces the fixed field format string representing the instruction.
        """

        if self.instruction == instructions.COMMENT:
            return '# ' + self.dest
        elif self.instruction == instructions.LABEL:
            return self.dest + ':'
        else:
            return 'implement me!'


def add(result, left_operand, right_operand):
    return TacInstruction(instructions.ADD, result, left_operand, right_operand)

def label(label_name):
    return TacInstruction(instructions.LABEL, label_name)

def comment(text):
    return TacInstruction(instructions.COMMENT, text)
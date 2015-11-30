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


def offset_from_label(label, offset):
    return '{} + {}'.format(label, offset)


class MipsInstruction(object):
    NULL = None

    def __init__(self, instruction: str, slot_0: str = NULL, slot_1: str = NULL, slot_2: str = NULL):
        self.instruction = instruction
        self.slot_0 = slot_0
        self.slot_1 = slot_1
        self.slot_2 = slot_2

    def __str__(self):
        return repr(self)

    def __repr__(self):
        """
        __repr__ is supposed to be "unambiguous," but it gets called on all contained objects when you stringify a
        container, so this will be the method that produces the fixed field format string representing the instruction.
        """
        ret = ''
        if self.instruction:  # TODO: fill in with custom logic for "non-instructions" like comment
            ret = '{:<15} {:<15}, {:<15}, {:<15}'.format(self.instruction,
                                                         self.slot_0 if self.slot_0 is not MipsInstruction.NULL else '-',
                                                         self.slot_1 if self.slot_1 is not MipsInstruction.NULL else '-',
                                                         self.slot_2 if self.slot_2 is not MipsInstruction.NULL else '-')

        return ret

    def __eq__(self, other):
        return self.instruction == other.instruction and self.slot_0 == other.slot_0 and self.slot_1 == other.slot_1 and \
               self.slot_2 == other.slot_2



#
# ADMINISTRATIVE
#
class COMMENT(MipsInstruction):
    def __init__(self, text):
        super(COMMENT, self).__init__(instruction='comment', slot_0=text)

class SOURCE(MipsInstruction):
    def __init__(self, start_line, end_line):
        super(SOURCE, self).__init__(instruction='source', slot_0=start_line, slot_1=end_line)

class TAC(MipsInstruction):
    def __init__(self, tac_str):
        super(TAC, self).__init__(instruction='comment', slot_0=tac_str)



#
# MEMORY
#
li = 'li'
lw = 'lw'
sw = 'sw'
la = 'la'


class LI(MipsInstruction):
    def __init__(self, register, immediate):
        super(LI, self).__init__(lw, register, immediate)


class LW(MipsInstruction):
    def __init__(self, register, memory_address):
        super(LW, self).__init__(lw, register, memory_address)


class SW(MipsInstruction):
    def __init__(self, register, memory_address):
        super(SW, self).__init__(lw, register, memory_address)


class LA(MipsInstruction):
    def __init__(self, register, memory_address):
        super(LA, self).__init__(lw, register, memory_address)


#
# MATH
#
add = 'add'


class ADD(MipsInstruction):
    def __init__(self, sum, addend, augend):
        super(ADD, self).__init__(add, sum, addend, augend)


#
# if __name__ == '__main__':
#     l = LW('$t0', '0x10010000')
#     print(l)

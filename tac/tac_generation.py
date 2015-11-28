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


# Special Registers
ZERO = '$zero'
FP = '$FP'
SP = '$SP'
RA = '$RA'
V0 = '$v0'


class TacInstruction(object):
    NULL = None

    def __init__(self, instruction: str, dest: str = NULL, src1: str = NULL, src2: str = NULL):
        self.instruction = instruction
        self.dest = dest
        self.src1 = src1
        self.src2 = src2

    def __str__(self):
        """
        __str__ is supposed to be "human readable, so this method will produce a more concise string that will fit in
        the terminal better for debugging.
        """
        ret = ''
        if self.instruction == instructions.COMMENT:
            ret = '{}: {}'.format(instructions.COMMENT, self.dest)
        else:
            ret = '{}, {}, {}, {}'.format(self.instruction, self.dest, self.src1, self.src2)

        # return ret
        return repr(self)

    def __repr__(self):
        """
        __repr__ is supposed to be "unambiguous," but it gets called on all contained objects when you stringify a
        container, so this will be the method that produces the fixed field format string representing the instruction.
        """
        ret = ''
        if self.instruction == instructions.COMMENT:
            ret = '# ' + self.dest
        elif self.instruction == instructions.LABEL:
            ret = self.dest + ':'
        elif self.instruction in (instructions.TEXT, instructions.DATA):
            ret = '.' + self.instruction.lower()
        else:
            ret = '{:<15}, {:<15}, {:<15}, {:<15}'.format(self.instruction,
                                                          self.dest if self.dest is not TacInstruction.NULL else '-',
                                                          self.src1 if self.src1 is not TacInstruction.NULL else '-',
                                                          self.src2 if self.src2 is not TacInstruction.NULL else '-')

        return ret

    @classmethod
    def from_str(cls, tac_str):
        # TODO: consider improving so that the special case instructions can work too, instead of the standard format
        # TODO: ones

        parts = tac_str.split(',')

        return cls(instruction=parts[0].trim(), dest=parts[1].trim() if parts[1] != '-' else TacInstruction.NULL,
                   src1=parts[2].trim() if parts[2] != '-' else TacInstruction.NULL,
                   src2=parts[3].trim() if parts[3] != '-' else TacInstruction.NULL)


#
# THE ALMIGHTY DUP
#
def DUP(clone, original):
    """
    args:
        clone
        original

    function:
        Clones the original value into a new temporary register. The temporaries will be mapped into a register
        allocation scheme later.
    """
    return TacInstruction(instructions.DUP, clone, original)


#
# THE ALMIGHTY SOURCE
#
def SOURCE(line_start, line_end):
    """
    args:
        start_line

    function:
        Instruction that gets filtered in the output and converted to the actual source from the program.
    """
    return TacInstruction(instructions.SOURCE, line_start, line_end)


#
# PROGRAM SECTIONS
#
def DATA():
    return TacInstruction(instructions.DATA)


def TEXT():
    return TacInstruction(instructions.TEXT)


#
# MATH
#
def ADD(sum, augend, addend):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.ADD, sum, augend, addend)


def SUB(difference, minuend, subtrahend):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.SUB, difference, minuend, subtrahend)


def MUL(product, multiplicand, multiplier):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.MUL, product, multiplicand, multiplier)


def DIV(quotient, dividend, divisor):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.DIV, quotient, dividend, divisor)


def MOD(remainder, dividend, divisor):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.MOD, remainder, dividend, divisor)


def NEG(result, operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.NEG, result, operand)


def ADDI(sum, augend, addend):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.ADDI, sum, augend, addend)


def SUBI(difference, minuend, subtrahend):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.SUBI, difference, minuend, subtrahend)


def MULI(product, multiplicand, multiplier):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.MULI, product, multiplicand, multiplier)


def DIVI(quotient, dividend, divisor):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.DIVI, quotient, dividend, divisor)


def ADDU(sum, augend, addend):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.ADDU, sum, augend, addend)


def SUBU(difference, minuend, subtrahend):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.SUBU, difference, minuend, subtrahend)


def MULU(product, multiplicand, multiplier):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.MULU, product, multiplicand, multiplier)


def DIVU(quotient, dividend, divisor):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.DIVU, quotient, dividend, divisor)


def MODU(remainder, dividend, divisor):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.MODU, remainder, dividend, divisor)


def NEGU(result, operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.NEGU, result, operand)


def ADDIU(sum, augend, addend):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.ADDIU, sum, augend, addend)


def SUBIU(difference, minuend, subtrahend):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.SUBIU, difference, minuend, subtrahend)


def MULIU(product, multiplicand, multiplier):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.MULIU, product, multiplicand, multiplier)


def DIVIU(quotient, dividend, divisor):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.DIVIU, quotient, dividend, divisor)


def ADDS(sum, augend, addend):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.ADDS, sum, augend, addend)


def SUBS(difference, minuend, subtrahend):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.SUBS, difference, minuend, subtrahend)


def MULS(product, multiplicand, multiplier):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.MULS, product, multiplicand, multiplier)


def DIVS(quotient, dividend, divisor):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.DIVS, quotient, dividend, divisor)


def NEGS(result, operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.NEGS, result, operand)


#
# LOGICAL
#
def LAND(result, left_operand, right_operand):
    return TacInstruction(instructions.LAND, result, left_operand, right_operand)


def LOR(result, left_operand, right_operand):
    return TacInstruction(instructions.LOR, result, left_operand, right_operand)


def NOT(result, operand):
    return TacInstruction(instructions.NOT, result, operand)


def EQ(result, left_operand, right_operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.EQ, result, left_operand, right_operand)


def NE(result, left_operand, right_operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.NE, result, left_operand, right_operand)


def GT(result, left_operand, right_operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.GT, result, left_operand, right_operand)


def GE(result, left_operand, right_operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.GE, result, left_operand, right_operand)


def LT(result, left_operand, right_operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.LT, result, left_operand, right_operand)


def LE(result, left_operand, right_operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.LE, result, left_operand, right_operand)


#
# CASTING
#
def CVTWS(result, operand):
    return TacInstruction(instructions.CVTWS, result, operand)


def CVTSW(result, operand):
    return TacInstruction(instructions.CVTSW, result, operand)


#
# ASSIGNMENT
#
def ASSIGN(result, lvalue, rvalue):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.ASSIGN, result, lvalue, rvalue)


#
# Memory Access
#
def LW(result, address):
    return TacInstruction(instructions.LW, result, address)


def SW(result, address):
    return TacInstruction(instructions.SW, result, address)


def LA(result, address):
    return TacInstruction(instructions.LA, result, address)


#
# PROGRAM FLOW
#
def LABEL(label_name):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.LABEL, label_name)


def JAL(label):
    return TacInstruction(instructions.JAL, label)


def JR(register):
    return TacInstruction(instructions.JR, register)


def BR(label_name):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.BR, label_name)


def BREQ(label_name, left_operand, right_operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.BREQ, label_name, left_operand, right_operand)


def BRNE(label_name, left_operand, right_operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.BRNE, label_name, left_operand, right_operand)


def BRLT(label_name, left_operand, right_operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.BRLT, label_name, left_operand, right_operand)


def BRLE(label_name, left_operand, right_operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.BRLE, label_name, left_operand, right_operand)


def BRGT(label_name, left_operand, right_operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.BRGT, label_name, left_operand, right_operand)


def BRGE(label_name, left_operand, right_operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.BRGE, label_name, left_operand, right_operand)


def HALT():
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.HALT)


#
# PROCEDURE/FUNCTION
#
def ARGS(argc):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.ARGS, argc)


def REFOUT(arg):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.REFOUT, arg)


def VALOUT(arg):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.VALOUT, arg)


# CALL and LLAC will be defined as macros in the actual MIPS
def CALL(function_name, size):
    """
    args:
        function_name: the label of the function definition
        size: the size of the portion of the activation frame to be dedicated to argument and parameter values
    function:

    """
    return TacInstruction(instructions.CALL, function_name, size)


def LLAC(size):
    """
    args:
        function_name: the label of the function definition
        size: the size of the portion of the activation frame to be dedicated to argument and parameter values
    function:

    """
    return TacInstruction(instructions.LLAC, size)


def PROCENTRY(op1, op2, op3):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.PROCENTRY, op1, op2, op3)


def ENDPROC():
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.ENDPROC)


def RETURN(rvalue='$zero'):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.RETURN, rvalue)


#
# MISCELLANEOUS
#
def BOUND(test, lower, upper):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.BOUND, test, lower, upper)


def ADDR(target):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.ADDR, target)


def GLOBAL(target, mem_size):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.GLOBAL, target, mem_size)


def STRING(data, label):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.STRING, data, label)


def COMMENT(text):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.COMMENT, text)


def create_offset_reference(offset, register):
    return '{}({})'.format(offset, register)

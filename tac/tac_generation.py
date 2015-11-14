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

        return ret

    def __repr__(self):
        """
        __repr__ is supposed to be "unambiguous," but it gets called on all contained objects when you stringify a
        container, so this will be the method that produces the fixed field format string representing the instruction.
        """
        ret = ''
        if self.instruction == instructions.COMMENT:
            ret = '# ' + self.dest
        elif self.instruction == instructions.LABEL:
            ret =  self.dest + ':'
        else:
            ret = '{:<15}, {:<15}, {:<15}, {:<15}'.format(self.instruction,
                                                           self.dest if self.dest is not TacInstruction.NULL else '-',
                                                           self.src1 if self.src1 is not TacInstruction.NULL else '-',
                                                           self.src2 if self.src2 is not TacInstruction.NULL else '-')

        return ret + '\n'
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
    return TacInstruction(instructions.SUB, quotient, dividend, divisor)

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

#
# LOGICAL
#

def NOT(result, operand):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
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

def CALL(function_name):
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.CALL, function_name)

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

def RETURN():
    """
    args:
        sum: the register where the addition result is stored.
        augend: the left operand of the addition.
        addend: the right operand of the addition.

    function:
        Performs basic addition.
    """
    return TacInstruction(instructions.RETURN)

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

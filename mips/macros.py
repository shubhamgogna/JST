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

import mips.registers as mr
import mips.instructions as mi


class Macro(object):
    def __init__(self, name, args=None, body=None):
        self.name = name
        self.args = args if args else []
        self.body = body if body else []

    def definition(self):
        return [mi.BEGIN_MACRO(self.name, self.args)] + self.body + [mi.END_MACRO()]

    def call(self, *args):
        return mi.CALL_MACRO(self.name, args)


__T_REGISTERS = (mr.T0, mr.T1, mr.T2, mr.T3, mr.T4, mr.T5, mr.T6, mr.T7, mr.T8, mr.T9)


__save_register_macro_instructions = []
for __temp_register in __T_REGISTERS:
    __save_register_macro_instructions.append(mi.SUBIU(mr.SP, mr.SP, mr.WORD_SIZE))
    __save_register_macro_instructions.append(mi.SW(__temp_register, mi.offset_register_immediate(mr.SP)))
SAVE_REGISTER_MACRO = Macro(name='SAVE_T_REGISTERS', args=None, body=__save_register_macro_instructions)


__restore_register_macro_instructions = []
for __temp_register in __T_REGISTERS:
    __restore_register_macro_instructions.append(mi.LW(__temp_register, mi.offset_register_immediate(mr.SP)))
    __restore_register_macro_instructions.append(mi.ADDIU(mr.SP, mr.SP, mr.WORD_SIZE))
RESTORE_REGISTER_MACRO = Macro(name='RESTORE_T_REGISTERS', args=None, body=__restore_register_macro_instructions)


__function_prologue_body = [
    mi.COMMENT("push $ra"),
    mi.SUBIU(mr.SP, mr.SP, mr.WORD_SIZE),
    mi.SW(mr.RA, mi.offset_register_immediate(mr.SP)),
    mi.COMMENT("push the caller's $fp"),
    mi.SUBIU(mr.SP, mr.SP, mr.WORD_SIZE),
    mi.SW(mr.FP, mi.offset_register_immediate(mr.SP)),
    mi.COMMENT("push the $s* registers (we might not use those in this way)"),
    mi.COMMENT("initialize the new frame pointer $fp = $sp - space for variables"),
    mi.LI(mr.A0, mr.WORD_SIZE),
    mi.MULU(mr.A1, mr.A0, mi.macro_arg('variable_size')),
    mi.SUB(mr.FP, mr.SP, mr.A1),
    mi.COMMENT("set $sp = $fp (this might allow us to spill registers to the stack, maybe)"),
    mi.ADD(mr.SP, mr.FP, mr.ZERO)
]
FUNCTION_PROLOGUE_MACRO = Macro(name='FUNCTION_PROLOGUE',
                                args=['variable_size'],
                                body=__function_prologue_body)


__function_epilogue_body = [
    mi.COMMENT("deallocate stack memory by setting $sp = $fp + space for variables"),
    mi.LI(mr.A0, mr.WORD_SIZE),
    mi.MULU(mr.A1, mr.A0, mi.macro_arg('variable_size')),
    mi.ADD(mr.SP, mr.FP, mr.A1),
    mi.COMMENT("recover the $s* registers (we might not use those in this way)"),
    mi.COMMENT("recover the caller's $fp"),
    mi.LW(mr.FP, mi.offset_register_immediate(mr.SP)),
    mi.ADDIU(mr.SP, mr.SP, mr.WORD_SIZE),
    mi.COMMENT("recover $ra"),
    mi.LW(mr.RA, mi.offset_register_immediate(mr.SP)),
    mi.ADDIU(mr.SP, mr.SP, mr.WORD_SIZE),
    mi.COMMENT("jump back to the caller"),
    mi.JR(mr.RA)
]
FUNCTION_EPILOGUE_MACRO = Macro(name='FUNCTION_EPILOGUE',
                                args=['variable_size'],
                                body=None)

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
import sys
import mips.register_management as mrm
import mips.registers as mr
import mips.instructions as mi
from tac.tac_generation import TacInstruction
import tac.tac_generation as tac_gen
import tac.instructions as taci
import mips.macros as mm


WORD_SIZE = 4

DEFAULT_TEMPROARY_REGISTER_SET = (mr.T0, mr.T1, mr.T2, mr.T3, mr.T4, mr.T5, mr.T6, mr.T7, mr.T8, mr.T9)

DEFAULT_SPILL_MEMORY_LABEL = 'SPILL_MEMORY'
DEFUALT_SPILL_MEMORY_SIZE = 128  # bytes



class MipsGenerator(object):
    """ An object to drive translation from 3AC to MIPS.

    This object conducts the translation from 3AC to MIPS and contains the results within itself.
    """

    def __init__(self, compiler_state=None, temporary_registers=DEFAULT_TEMPROARY_REGISTER_SET,
                 spill_mem_label=DEFAULT_SPILL_MEMORY_LABEL, spill_mem_size=DEFUALT_SPILL_MEMORY_SIZE):
        """ The constructor.

        Constructs the MipsGenerator object.

        :param compiler_state: Contains any parameters required for the execution of the compiler program.
        :param temporary_registers: A set of the registers that are allowed to be used as temporaries.
        :param spill_mem_label: The label to use in the generated MIPS to allocate register spilling memory.
        :param spill_mem_size: The amount of memory to make available for register spilling.
        :return: A constructed MipsGenerator.
        """

        self.compiler_state = compiler_state

        self.source_tac = []
        self.mips_output = []
        self.register_table = mrm.RegisterUseTable(temporary_registers, spill_mem_label, spill_mem_size)

    def load(self, source_tac):
        """ Supply the 3AC the generator should use to generate MIPS assembly code from.

        :param source_tac: An iterable of 3AC items to translate from.
        :return: None.
        """
        self.source_tac = source_tac

    def dumps(self):
        """ Dump the generated MIPS code to a string.

        Iterates over all generated MIPS code and produces a single string with one MIPS instruction (or
        source/comment/original 3AC item) per line. The lines are separated by new-lines.

        :return: The constructed string with one MIPS instruction per line.
        """
        return '\n'.join([str(mips_instruction) for mips_instruction in self.mips_output])

    def dump(self, file_name=None):
        """ Dumps the generated MIPS to a file.

        Uses dumps() internally.

        :param file_name: The name of the file to dump the generated code to. Defaults to the stdout.
        :return: None.
        """
        file = None
        if file_name:
            file = open(file_name)
        else:
            file = sys.stdout

        file.write(self.dumps())

        if file_name:
            file.close()

    def translate_tac_to_mips(self):
        """ Iterates over the set source 3AC and generates new MIPS code.

        This function iterates over the given 3AC and produces MIPS that is stored internally. This method is
        essentially a poor man's parser that calls methods for each type of 3AC as appropriate.

        :return: None.
        """

        self.mips_output.extend(mm.SAVE_REGISTER_MACRO.definition())
        self.mips_output.extend(mm.RESTORE_REGISTER_MACRO.definition())
        self.mips_output.extend(mm.CALLEE_FUNCTION_PROLOGUE_MACRO.definition())
        self.mips_output.extend(mm.CALLEE_FUNCTION_EPILOGUE_MACRO.definition())

        for instruction in self.source_tac:
            assert (isinstance(instruction, TacInstruction))
            if instruction.instruction == taci.SOURCE:
                self._source(instruction)
            elif instruction.instruction == taci.COMMENT:
                self._comment(instruction)
            else:
                self.mips_output.append(mi.TAC(str(instruction)))  # TODO: make it configurable to disable this

                if instruction.instruction == taci.DATA:
                    self._data_section(instruction)

                elif instruction.instruction == taci.TEXT:
                    self._text_section(instruction)

                elif instruction.instruction == taci.LABEL:
                    self._label(instruction)

                elif instruction.instruction == taci.KICK:
                    self._kick(instruction)

                elif instruction.instruction == taci.CALL_PROC:
                    self._call_procedure(instruction)

                elif instruction.instruction == taci.BEGIN_PROC:

                    pass

                    self._begin_procedure(instruction)

                elif instruction.instruction == taci.END_PROC:

                    pass

                    self._end_procedure(instruction)

                elif instruction.instruction == taci.LI:
                    self._load_immediate(instruction)

                elif instruction.instruction == taci.LOAD:
                    self._load(instruction)

                elif instruction.instruction == taci.LA:
                    self._load_address(instruction)

                elif instruction.instruction == taci.STORE:
                    self._store(instruction)

                elif instruction.instruction == taci.BR:
                    self._branch(instruction)

                elif instruction.instruction == taci.BRNE:
                    self._branch_not_equal(instruction)

                # elif instruction.instruction == taci.ASSIGN:
                #     self._assign(instruction)

                elif instruction.instruction == taci.JR:
                    self._jump_to_register_value(instruction)

                elif instruction.instruction == taci.ADDIU:
                    self._add_immediate_unsigned(instruction)

                elif instruction.instruction == taci.ADDU:
                    self._add_unsigned(instruction)

                elif instruction.instruction == taci.ADD:
                    self._add(instruction)

                elif instruction.instruction == taci.MULIU:
                    self._multiply_unsigned(instruction)

                elif instruction.instruction == taci.EQ:
                    self._equality(instruction)

                elif instruction.instruction == taci.LT:
                    self._less_than(instruction)

                elif instruction.instruction == taci.GT:
                    self._greater_than(instruction)

                elif instruction.instruction == taci.BOUND:
                    self._bound(instruction)

                elif instruction.instruction == taci.RETURN:
                    self._return(instruction)


                # elif instruction.instruction == taci.LT:

                else:
                    raise NotImplementedError("{} 3AC -> MIPS is not implemented!".format(instruction.instruction))

    def _source(self, t):
        self.mips_output.append(mi.SOURCE(start_line=t.dest, end_line=t.src1))

    def _comment(self, t):
        self.mips_output.append(mi.COMMENT(text=t.dest))

    def _data_section(self, t):
        self.mips_output.append(mi.DATA())

    def _text_section(self, t):
        self.mips_output.append(mi.TEXT())

    def _label(self, t):
        self.mips_output.append(mi.LABEL(t.dest))

    def _kick(self, instruction):
        self.register_table.release(instruction.dest)

    def _call_procedure(self, t):
        # push the temporary registers on the stack
        self.mips_output.append(mm.SAVE_REGISTER_MACRO.call())

        # load the argument registers
        # (likely unnecessary since we have decided to include arguments in our frame)

        # jump and link to the procedure
        self.mips_output.append(mi.JAL(t.dest))

        # retake the registers that were stored after the call
        self.mips_output.append(mm.RESTORE_REGISTER_MACRO.call())

    def _begin_procedure(self, t):
        # raise NotImplementedError
        pass

    def _end_procedure(self, t):
        # raise NotImplementedError()
        pass

    def _return(self, t):
        result = self.register_table.acquire(t.dest)
        self.mips_output.extend(result['code'])
        register = result['register']
        self.mips_output.append(mi.ADD(mr.V0, register, mr.ZERO))

        # TODO: the parameter needs to be the size of the function's variables
        self.mips_output.append(mm.CALLEE_FUNCTION_EPILOGUE_MACRO.call(mr.ZERO))

    def _load_immediate(self, t):
        result = self.register_table.acquire(t.dest)
        self.mips_output.extend(result['code'])
        self.mips_output.append(mi.LI(result['register'], t.src1))

    def _load(self, t):
        result = self.register_table.acquire(t.dest)
        self.mips_output.extend(result['code'])
        dest_register = result['register']

        if t.src2 is 1:
            self.mips_output.append(mi.LB(dest_register, t.src1))
        elif t.src2 is 2:
            self.mips_output.append(mi.LHW(dest_register, t.src1))
        elif t.src2 is 4:
            self.mips_output.append(mi.LW(dest_register, t.src1))

    def _store(self, t):
        # TODO: ensure that the address is handled for all of the variants
        # ($t2), 100($t2), 100, label, label + immediate, label($t2), label + immediate($t2)
        content_reg = self.register_table.acquire(t.dest)
        address_reg = self.register_table.acquire(t.src1)

        self.mips_output.append(content_reg['code'])
        self.mips_output.append(address_reg['code'])

        # Content and then address
        if t.src2 is 1:

            self.mips_output.append(mi.SB(content_reg['register'], address_reg['register']))
        elif t.src2 is 2:
            self.mips_output.append(mi.SHW(content_reg['register'], address_reg['register']))
        elif t.src2 is 4:
            self.mips_output.append(mi.SW(content_reg['register'], address_reg['register']))

    def _load_address(self, t):
        result = self.register_table.acquire(t.dest)
        self.mips_output.extend(result['code'])
        dest_register = result['register']

        self.mips_output.append(mi.LA(dest_register, t.src1))
    #
    # def _assign(self, t):
    #     dest_register = None
    #     src1_register = None
    #
    #     result = self.register_table.acquire(t.src1)
    #     self.mips_output.extend(result['code'])
    #     dest_register = result['register']
    #
    #     if t.src1 not in tac_gen.CONSTANT_REGISTERS:
    #         result = self.register_table.acquire(t.src2)
    #         self.mips_output.extend(result['code'])
    #         src1_register = result['register']
    #     else:
    #         src1_register = self.tac_special_register_to_mips(t.src2)
    #
    #     self.mips_output.append(mi.SW(dest_register, src1_register))


    def _add_immediate_unsigned(self, t):
        dest_register = None
        src1_register = None
        src2_register = None

        result = self.register_table.acquire(t.dest)
        self.mips_output.extend(result['code'])
        dest_register = result['register']

        if t.src1 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src1)
            self.mips_output.extend(result['code'])
            src1_register = result['register']
        else:
            src1_register = self.tac_special_register_to_mips(t.src1)

        # if t.src2 in tac_gen.CONSTANT_REGISTERS:
        #     result = self.register_table.acquire(t.src2)
        #     self.mips_output.extend(result['code'])
        #     src2_register = result['register']

        self.mips_output.append(mi.ADDIU(dest_register, src1_register, t.src2))

    def _add_unsigned(self, t):
        dest_register = None
        src1_register = None
        src2_register = None

        result = self.register_table.acquire(t.dest)
        self.mips_output.extend(result['code'])
        dest_register = result['register']

        if t.src1 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src1)
            self.mips_output.extend(result['code'])
            src1_register = result['register']
        else:
            src1_register = self.tac_special_register_to_mips(t.src1)

        if t.src2 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src2)
            self.mips_output.extend(result['code'])
            src2_register = result['register']
        else:
            src2_register = self.tac_special_register_to_mips(t.src2)

        self.mips_output.append(mi.ADDU(dest_register, src1_register, src2_register))

    def _add(self, t):
        dest_register = None
        src1_register = None
        src2_register = None

        result = self.register_table.acquire(t.dest)
        self.mips_output.extend(result['code'])
        dest_register = result['register']

        if t.src1 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src1)
            self.mips_output.extend(result['code'])
            src1_register = result['register']
        else:
            src1_register = self.tac_special_register_to_mips(t.src1)

        if t.src2 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src2)
            self.mips_output.extend(result['code'])
            src2_register = result['register']
        else:
            src2_register = self.tac_special_register_to_mips(t.src2)

        self.mips_output.append(mi.ADD(dest_register, src1_register, src2_register))

    def _multiply_unsigned(self, t):
        dest_register = None
        src1_register = None
        src2_register = None

        result = self.register_table.acquire(t.dest)
        self.mips_output.extend(result['code'])
        dest_register = result['register']

        if t.src1 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src1)
            self.mips_output.extend(result['code'])
            src1_register = result['register']
        else:
            src1_register = self.tac_special_register_to_mips(t.src1)

        if t.src2 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src2)
            self.mips_output.extend(result['code'])
            src2_register = result['register']
        else:
            src2_register = self.tac_special_register_to_mips(t.src2)

        self.mips_output.append(mi.MULU(dest_register, src1_register, src2_register))


    def _equality(self, t):
        dest_register = None
        src1_register = None
        src2_register = None

        result = self.register_table.acquire(t.dest)
        self.mips_output.extend(result['code'])
        dest_register = result['register']

        if t.src1 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src1)
            self.mips_output.extend(result['code'])
            src1_register = result['register']
        else:
            src1_register = self.tac_special_register_to_mips(t.src1)

        if t.src2 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src2)
            self.mips_output.extend(result['code'])
            src2_register = result['register']
        else:
            src2_register = self.tac_special_register_to_mips(t.src2)

        self.mips_output.append(mi.SEQ(dest_register, src1_register, src2_register))

    def _less_than(self, t):
        dest_register = None
        src1_register = None
        src2_register = None

        result = self.register_table.acquire(t.dest)
        self.mips_output.extend(result['code'])
        dest_register = result['register']

        if t.src1 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src1)
            self.mips_output.extend(result['code'])
            src1_register = result['register']
        else:
            src1_register = self.tac_special_register_to_mips(t.src1)

        if t.src2 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src2)
            self.mips_output.extend(result['code'])
            src2_register = result['register']
        else:
            src2_register = self.tac_special_register_to_mips(t.src2)

        self.mips_output.append(mi.SLT(dest_register, src1_register, src2_register))

    def _greater_than(self, t):
        dest_register = None
        src1_register = None
        src2_register = None

        result = self.register_table.acquire(t.dest)
        self.mips_output.extend(result['code'])
        dest_register = result['register']

        if t.src1 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src1)
            self.mips_output.extend(result['code'])
            src1_register = result['register']
        else:
            src1_register = self.tac_special_register_to_mips(t.src1)

        if t.src2 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src2)
            self.mips_output.extend(result['code'])
            src2_register = result['register']
        else:
            src2_register = self.tac_special_register_to_mips(t.src2)

        self.mips_output.append(mi.SGT(dest_register, src1_register, src2_register))

    def _bound(self, t):
        dest_register = None
        src1_register = None
        src2_register = None

        result = self.register_table.acquire(t.dest)
        self.mips_output.extend(result['code'])
        dest_register = result['register']

        if t.src1 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src1)
            self.mips_output.extend(result['code'])
            src1_register = result['register']
        else:
            src1_register = self.tac_special_register_to_mips(t.src1)

        if t.src2 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src2)
            self.mips_output.extend(result['code'])
            src2_register = result['register']
        else:
            src2_register = self.tac_special_register_to_mips(t.src2)

        self.mips_output.append(mi.TLT(dest_register, src1_register))
        self.mips_output.append(mi.TGE(dest_register, src2_register))



    def _branch(self, t):
        self.mips_output.append(mi.J(t.dest))

    def _branch_not_equal(self, t):
        dest_register = None
        src1_register = None
        src2_register = None

        # result = self.register_table.acquire(t.dest)
        # self.mips_output.extend(result['code'])
        # dest_register = result['register']

        if t.src1 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src1)
            self.mips_output.extend(result['code'])
            src1_register = result['register']
        else:
            src1_register = self.tac_special_register_to_mips(t.src1)

        if t.src2 not in tac_gen.CONSTANT_REGISTERS:
            result = self.register_table.acquire(t.src2)
            self.mips_output.extend(result['code'])
            src2_register = result['register']
        else:
            src2_register = self.tac_special_register_to_mips(t.src2)

        self.mips_output.append(mi.BNE(t.dest, src1_register, src2_register))


    def _jump_to_register_value(self, t):
        # result = self.register_table.acquire(t.dest)
        # self.mips_output.extend(result['code'])
        self.mips_output.append(mi.JR((t.dest).lower()))


    @staticmethod
    def tac_special_register_to_mips(tac_register):
        if tac_register == tac_gen.ZERO:
            return mr.ZERO

        elif tac_register == tac_gen.GP:
            return mr.GP

        elif tac_register == tac_gen.FP:
            return mr.FP

        elif tac_register == tac_gen.SP:
            return mr.SP

        elif tac_register == tac_gen.RA:
            return mr.RA

        elif tac_register == tac_gen.V0:
            return mr.V0

        else:
            raise Exception('No MIPS equivalent for 3AC register {}'.format(tac_register))

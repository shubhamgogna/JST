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
import tac.instructions as taci


DEFAULT_TEMPROARY_REGISTER_SET = {mr.T0, mr.T1, mr.T2, mr.T3, mr.T4, mr.T5, mr.T6, mr.T7, mr.T8, mr.T9}

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
        for instruction in self.source_tac:
            assert (isinstance(instruction, TacInstruction))
            if instruction.instruction == taci.SOURCE:
                self.source(instruction)
            elif instruction.instruction == taci.COMMENT:
                self.comment(instruction)
            else:
                self.mips_output.append(mi.TAC(str(instruction)))

                if instruction.instruction == taci.LW:
                    self.load_word(instruction)

    def source(self, t):
        self.mips_output.append(mi.SOURCE(start_line=t.dest, end_line=t.src1))

    def comment(self, t):
        self.mips_output.append(mi.COMMENT(text=t.dest))

    def load_word(self, t):
        # do a register/argument check

        # generate the mips code

        raise NotImplementedError()

    def load_address(self, t):
        raise NotImplementedError()

        # one of these methods for every 3AC instruction we made

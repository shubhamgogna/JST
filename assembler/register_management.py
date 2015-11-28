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

import itertools
import pylru
import assembler.mips_instructions as assembler


class OutOfSpillMemoryException(Exception):
    pass


class MipsRegisterUseTable(object):
    """ A class for doing the book-keeping of physical register allocation.

    Handles stuff.
    """

    def __init__(self, available_registers, spill_memory_base_label, spill_memory_size, word_size=4):
        """

        :param working_register:
        :param available_registers:
        :param spill_memory_size:
        :word_size:
        :return:
        """

        self.spill_mem_base_label = spill_memory_base_label
        self.spill_mem_size = spill_memory_size

        self.available_registers = list(reversed(available_registers))
        self.available_spill_memory_words = list(reversed(range(0, spill_memory_size, word_size)))

        self.lru_cache = pylru.lrucache(size=len(available_registers), callback=self._spill)
        self.spilled_registers = {}

        self._spill_code = []
        self._freed_physical_register = None

    def acquire(self, pseudo_register):
        """ Returns a physical register's name and the assembly required to properly use the register

        Will return a physical register name for use, even if registers must be spilled into memory. Also composes the
        instructions necessary to make use of the register. Everything is returned as a dictionary containing 'register'
        and 'code' keys.

        :param pseudo_register:
        :return:
        """

        physical_register = None
        code = []

        if pseudo_register in self.lru_cache:
            physical_register = self.lru_cache[pseudo_register]

        elif pseudo_register in self.spilled_registers:
            physical_register, code = self._recover(pseudo_register)

        elif self.available_registers:
            physical_register = self.available_registers.pop()
            self.lru_cache[pseudo_register] = physical_register

        else:  # there are no available registers, so force a spill
            self.lru_cache[pseudo_register] = None
            physical_register = self._freed_physical_register
            self.lru_cache[pseudo_register] = physical_register
            code = self._spill_code

        return {'register': physical_register, 'code': code}

    def release(self, pseudo_register):
        """ Releases any resources held for a pseudo/temporary register (physical register, memory).

        :param pseudo_register:
        :return:
        """

        if pseudo_register in self.lru_cache:
            self.available_registers.append(self.lru_cache[pseudo_register])
            del self.lru_cache[pseudo_register]

        elif pseudo_register in self.spilled_registers:
            self.available_spill_memory_words.append(self.spilled_registers.pop(pseudo_register))

        else:  # if there is no record of the pseudo-register, there is nothing to do
            pass

    def release_all(self):
        """ Releases all resources (physical registers, memory) for future use.

        :return:
        """
        for pseudo_register in itertools.chain(list(self.lru_cache.keys()), list(self.spilled_registers.keys())):
            self.release(pseudo_register)

    def _spill(self, pseudo_register, physical_register):
        """ Handles all of the logic for spilling the contents of a physical register into memory.

        :param pseudo_register:
        :physical_register:
        :return:
        """

        self._spill_code = []
        self._freed_physical_register = physical_register

        if not self.available_spill_memory_words:
            raise OutOfSpillMemoryException()

        spill_offset = self.available_spill_memory_words.pop()

        self.spilled_registers[pseudo_register] = spill_offset

        self._spill_code = [
            assembler.SW(physical_register, assembler.offset_from_label(self.spill_mem_base_label, spill_offset))]

    def _recover(self, pseudo_register):
        """ Handles the logic for reversing the spilling of a register.

        :param pseudo_register:
        :return:
        """

        spill_offset = self.spilled_registers.pop(pseudo_register)
        physical_register = None
        code = []

        if self.available_registers:
            physical_register = self.available_registers.pop()
            self.lru_cache[pseudo_register] = physical_register
        else:
            self.lru_cache[pseudo_register] = None
            physical_register = self._freed_physical_register

            code.extend(self._spill_code)

            self.lru_cache[pseudo_register] = physical_register

            code.append(
                assembler.LW(physical_register, assembler.offset_from_label(self.spill_mem_base_label, spill_offset)))

        self.available_spill_memory_words.append(spill_offset)

        return physical_register, code

    def __str__(self):

        lru_cache_str = '{' + ', '.join([str(item[0] +': ' + str(item[1])) for item in self.lru_cache.items()]) + '}'

        ret = 'lru cache:             {}\n' \
              'spilled registers:     {}\n' \
              'available registers:   {}\n' \
              'available spill words: {}'.format(lru_cache_str, self.spilled_registers, self.available_registers,
                                                 len(self.available_spill_memory_words))


        return ret

    def __repr__(self):
        return str(self)

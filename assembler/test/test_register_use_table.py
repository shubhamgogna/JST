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

import unittest
import assembler.mips_registers as mips
import assembler.mips_instructions as assembler
from assembler.register_management import MipsRegisterUseTable, OutOfSpillMemoryException
from ticket_counting.ticket_counters import INT_REGISTER_TICKETS


SPILL = 'spill'

class TestRegisterUseTable(unittest.TestCase):
    """
    PLEASE NOTE: The tests rely heavily on the setUp() function. In order to make it easy to evaluate the tests, the
                 register_use_table was set up to use a very small set of registers and spill memory. Should these
                 parameters be modified, all of the tests should be revisited to ensure they are performing their
                 tests correctly.
    """
    def setUp(self):
        registers_to_use = (mips.T0, mips.T1)

        self.register_use_table = MipsRegisterUseTable(registers_to_use, SPILL, 8)

    def tearDown(self):
        pass

    def test_single_register_use(self):

        pseudo_register = INT_REGISTER_TICKETS.get()

        self.assertFalse(pseudo_register in self.register_use_table.lru_cache)

        result = self.register_use_table.acquire(pseudo_register)

        expected_result = {'register': mips.T0, 'code': []}
        self.assertEqual(expected_result, result, 'register $t0 should have been returned and no code required')

        # since no spilling occurred, we should get the same register back with no code needed
        result = self.register_use_table.acquire(pseudo_register)
        self.assertEqual(expected_result, result, 'register $t0 should have been returned and no code required')

        self.register_use_table.release(pseudo_register)
        self.assertFalse(pseudo_register in self.register_use_table.lru_cache)
        self.assertSequenceEqual([mips.T1, mips.T0], self.register_use_table.available_registers)

    def test_register_spill(self):
        pseudo_registers = [INT_REGISTER_TICKETS.get() for _ in range(0, 3)]

        self.register_use_table.acquire(pseudo_registers[0])
        self.register_use_table.acquire(pseudo_registers[1])

        self.assertSequenceEqual([], self.register_use_table.available_registers, 'the registers should be used up')

        expected_result = {'register': mips.T0, 'code': [assembler.SW(mips.T0, assembler.offset_from_label(SPILL, 0))]}
        result = self.register_use_table.acquire(pseudo_registers[2])
        self.assertEqual(expected_result, result)

    def test_spill_recovery(self):
        pseudo_registers = [INT_REGISTER_TICKETS.get() for _ in range(0, 3)]

        self.register_use_table.acquire(pseudo_registers[0])
        self.register_use_table.acquire(pseudo_registers[1])

        self.assertSequenceEqual([], self.register_use_table.available_registers, 'the registers should be used up')

        expected_result = {'register': mips.T0, 'code': [assembler.SW(mips.T0, assembler.offset_from_label(SPILL, 0))]}
        result = self.register_use_table.acquire(pseudo_registers[2])
        self.assertEqual(expected_result, result)

        # recovering a spilled register's value from memory should not only get the register, but also provide the
        # assembler code that swaps the values for the temporaries using the spill memory
        expected_result = {
            'register': mips.T1,
            'code': [
                assembler.SW(mips.T1, assembler.offset_from_label(SPILL, 4)),
                assembler.LW(mips.T1, assembler.offset_from_label(SPILL, 0))
            ]
        }
        result = self.register_use_table.acquire(pseudo_registers[0])
        self.assertEqual(expected_result, result)

    def test_overrun_of_spill_memory_fails(self):
        with self.assertRaises(OutOfSpillMemoryException):
            # 5 is precisely enough to run out of spill memory
            pseudo_registers = [INT_REGISTER_TICKETS.get() for _ in range(0,5)]
            for pseudo_register in pseudo_registers:
                self.register_use_table.acquire(pseudo_register)

    def test_multiple_spills(self):
        self.fail()

    def test_multiple_recoveries(self):
        self.fail()

    def test_release_one_register(self):
        self.fail()

    def test_release_all_registers(self):
        self.fail()

    def test_double_register_use(self):
        self.fail("We aren't supporting two registers for double word purposes yet, cuz it's hard.")

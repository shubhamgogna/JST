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

import unittest
from symbol_table.symbol import Symbol
from symbol_table.symbol_table import SymbolTable


class TestSymbolTable(unittest.TestCase):

    def setUp(self):
        self.sym = SymbolTable()

    def tearDown(self):
        self.sym = None

    def test_insert(self):
        self.assertTrue(self.sym.insert(Symbol('A')) == 'SUCCESS')
        self.assertTrue(self.sym.insert(Symbol('B')) == 'SUCCESS')
        self.assertTrue(self.sym.insert(Symbol('C')) == 'SUCCESS')

    def test_find_same_scope(self):
        self.assertTrue(self.sym.insert(Symbol('A')) == 'SUCCESS')
        self.assertTrue(self.sym.find('A') != None)

    def test_find_diff_scope(self):
        self.sym.insert(Symbol('A'))
        self.sym.push()
        self.sym.insert(Symbol('B'))
        self.assertTrue(self.sym.find('A') != None)

    def test_shadowed_symbol(self):
        self.assertTrue(self.sym.insert(Symbol('A')) == 'SUCCESS')
        self.sym.push()
        self.assertTrue(self.sym.insert(Symbol('A')) == 'SHADOWED')

    def test_exisiting_symbol(self):
        self.assertTrue(self.sym.insert(Symbol('A')) == 'SUCCESS')
        self.assertTrue(self.sym.insert(Symbol('A')) == 'EXISTS')

    def test_push_and_pop(self):
        self.sym.insert(Symbol('A'))
        self.assertTrue(self.sym.size() == 1)
        self.sym.push()

        self.sym.insert(Symbol('B'))
        self.assertTrue(self.sym.size() == 2)

        self.sym.pop()
        self.assertTrue(self.sym.size() == 1)

        self.sym.pop()
        self.assertTrue(self.sym.size() == 0)

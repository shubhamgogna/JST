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
from symbol_table.scope import Scope
from symbol_table.symbol import Symbol


class TestScope(unittest.TestCase):
    def setUp(self):
        self.scope = Scope()

    def tearDown(self):
        self.scope = None

    def test_insert(self):
        self.assertTrue(self.scope.insert(Symbol('A')) == Scope.INSERT_SUCCESS)
        self.assertTrue(self.scope.insert(Symbol('A')) == Scope.INSERT_REDECL)
        self.assertTrue(self.scope.insert(Symbol('B')) == Scope.INSERT_SUCCESS)

    def test_find(self):
        self.scope.insert(Symbol('A'))
        found = self.scope.find('A')
        self.assertTrue(found is not None)
        self.assertTrue(found.identifier is 'A')
        self.assertTrue(type(found) is Symbol)

    def test_size(self):
        self.assertTrue(self.scope.size() == 0)
        self.scope.insert(Symbol('A'))
        self.assertTrue(self.scope.size() == 1)

    def test_clone(self):
        self.scope.insert(Symbol('A'))
        self.scope.insert(Symbol('B'))

        clone = self.scope.clone()
        self.assertTrue(self.scope.find('A') is not clone.find('A'))
        self.assertTrue(self.scope.find('B') is not clone.find('B'))

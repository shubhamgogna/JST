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
from symbol_table.symbol import Symbol, TypeDeclaration


class TestSymbol(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_str(self):
        type = TypeDeclaration()
        type.add_type_specifier('int')
        symbol = Symbol(identifier='my_variable')
        symbol.type = type

        s = str(symbol)

        self.assertEqual(s, "int my_variable")

    # not sure what we should test, but I think this might be an example of how to start
    def test_add_args_makes_function(self):
        symbol = Symbol(identifier='my_function')
        symbol.add_arguments([])

        self.assertTrue(symbol.is_function, 'Adding arguments should make the symbol into a function')

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
from symbol_table.symbol import Symbol, TypeDeclaration, FunctionSymbol


class TestSymbol(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_variable_str(self):
        type = TypeDeclaration()
        type.add_type_specifier('int')
        symbol = Symbol(identifier='my_variable')
        symbol.type = type

        s = str(symbol)

        self.assertEqual(s, "int my_variable")

    def test_function_str(self):
        # TODO: with the introduction of the FunctionSymbol, we might be throwing out this test, so it's ok if it fails
        type = TypeDeclaration()
        type.add_type_specifier('int')
        symbol = FunctionSymbol(identifier='my_function', lineno=0)
        symbol.type = type

        parameter_1 = Symbol(identifier='parameter_1')
        p_1_type = TypeDeclaration()
        p_1_type.add_type_specifier('int')
        parameter_1.type = p_1_type

        parameter_2 = Symbol(identifier='parameter_2')
        p_2_type = TypeDeclaration()
        p_2_type.add_type_specifier('char')
        parameter_2.type = p_2_type


        parameters = [parameter_1, parameter_2]
        symbol.add_named_parameters(parameters)

        s = str(symbol)

        self.assertEqual("int my_function(int parameter_1, char parameter_2)", s)

    # not sure what we should test, but I think this might be an example of how to start
    def test_add_args_makes_function(self):
        symbol = Symbol(identifier='my_function')
        symbol.add_parameters([])

        self.assertTrue(symbol.is_function, 'Adding arguments should make the symbol into a function')

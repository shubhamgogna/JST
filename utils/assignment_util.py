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

from symbol_table.symbol import FunctionSymbol, VariableSymbol
from ast.ast_nodes import Constant, SymbolNode, FunctionCall, BinaryOperator


class AssignmentUtil(object):
    @staticmethod
    def can_assign(left, right):
        if isinstance(left, Constant) or (isinstance(left, SymbolNode) and left.symbol.immutable):
            print(left.symbol.decl_type)
            return 1, 'Constants cannot be reassigned.'

        if isinstance(left, SymbolNode) and isinstance(left.symbol, FunctionSymbol):
            return 1, 'Assignment operators are invalid for functions.'

        if isinstance(left, SymbolNode) and isinstance(left.symbol, VariableSymbol):
            left_type = left.symbol.get_type_str()

            if isinstance(right, SymbolNode) and isinstance(right.symbol, VariableSymbol):
                right_type = right.symbol.get_type_str()

                if left_type == right_type:
                    return None, ''
                # TODO Implicit conversion
                else:
                    return 3, 'Right type ({}) does not match left type ({}).'.format(right_type, left_type)

            elif isinstance(right, Constant):

                if left_type == right.type:
                    return None, ''
                # TODO Implicit conversion
                else:
                    return 3, 'Right type ({}) does not match left type ({}).'.format(right.type, left_type)

            elif isinstance(right, FunctionCall):
                # TODO Figure out how to get return type info from function call
                return None, 'TODO'

            elif isinstance(right, BinaryOperator):
                # TODO Figure out how to get return type info from function call
                return None, 'TODO'

            else:
                return 3, 'Unknown type of right-hand side.'

        return 1, 'Unknown type of left-hand side.'

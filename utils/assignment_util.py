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
    integral_types = {
        'char': 8,
        'short': 16,
        'short int': 16,
        'int': 16,
        'long': 32,
        'long int': 32,
        'long long': 64,
        'long long int': 64
    }

    floating_types = {
        'float': 32,
        'double': 64,
        'long double': 80  # Depends on platform
    }

    @staticmethod
    def can_assign(left, right):
        # This is a workaround that allows this function to be used to check function parameters
        # It will likely go away eventually
        if isinstance(left, (VariableSymbol, FunctionSymbol)):
            left = SymbolNode(left)
        if isinstance(right, (VariableSymbol, FunctionSymbol)):
            right = SymbolNode(right)

        if isinstance(left, Constant) or (isinstance(left, SymbolNode) and left.symbol.immutable):
            print(left.symbol.decl_type)
            return 1, 'Constants cannot be reassigned.'

        if isinstance(left, SymbolNode) and isinstance(left.symbol, FunctionSymbol):
            return 1, 'Assignment operators are invalid for functions.'

        if isinstance(left, SymbolNode) and isinstance(left.symbol, VariableSymbol):
            left_type = left.symbol.get_type_tuple()

            if isinstance(right, SymbolNode) and isinstance(right.symbol, VariableSymbol):
                right_type = right.symbol.get_type_tuple()

                # VariableSymbol
                # 0 = signed/unsigned/None, 1 = type declaration, 2 = array dims, 3 = pointers
                if left_type[2] == right_type[2] and left_type[3] == right_type[3]:

                    if left_type[0] == right_type[0] and left_type[1] == right_type[1]:
                        return None, ''
                    elif AssignmentUtil.can_cast_implicit(left_type[1], right_type[1]):
                        return None, ''
                else:
                    return 3, 'Right type ({}) does not match left type ({}).'.format(
                        ' '.join(right_type).strip(), ' '.join(left_type).strip())

            elif isinstance(right, Constant):

                # VariableSymbol
                # 0 = signed/unsigned/None, 1 = type declaration, 2 = array dims, 3 = pointers
                # Constant
                # 0 = signed/unsigned/None, 1 = type declaration
                if left_type[0] == right.type[0] and left_type[1] == right.type[1]:
                    return None, ''
                elif AssignmentUtil.can_cast_implicit(left_type[1], right.type[1]):
                    return None, ''
                else:
                    return 3, 'Right type ({}) does not match left type ({}).'.format(
                        ' '.join(right.type).strip(), ' '.join(left_type).strip())

            elif isinstance(right, FunctionCall):
                right_type = right.function_symbol.get_type_tuple()

                # VariableSymbol
                # 0 = signed/unsigned/None, 1 = type declaration, 2 = array dims, 3 = pointers
                # FunctionSymbol
                # 0 = signed/unsigned/None, 1 = type declaration
                if left_type[0] == right_type[0] and left_type[1] == right_type[1]:
                    return None, ''
                elif AssignmentUtil.can_cast_implicit(left_type[1], right_type[1]):
                    return None, ''
                else:
                    return 3, 'Right type ({}) does not match left type ({}).'.format(
                        ' '.join(right_type).strip(), ' '.join(left_type).strip())

            elif isinstance(right, BinaryOperator):
                # TODO Figure out how to get return type info from function call
                return 3, 'TODO: BinaryOperator in AssignmentUtil'

            # TODO Array references
            else:
                return 3, 'Unknown node on right-hand side. ({})'.format(type(right))

        return 1, 'Unknown node on left-hand side. ({})'.format(type(left))

    @staticmethod
    def can_cast_implicit(left_type, right_type):
        if left_type in AssignmentUtil.integral_types and right_type in AssignmentUtil.integral_types:
            return AssignmentUtil.integral_types[left_type] > AssignmentUtil.integral_types[right_type]
        elif left_type in AssignmentUtil.floating_types and right_type in AssignmentUtil.floating_types:
            return AssignmentUtil.floating_types[left_type] > AssignmentUtil.floating_types[right_type]

        return False

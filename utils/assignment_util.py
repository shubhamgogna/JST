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
from ast.ast_nodes import Constant, FunctionCall, BinaryOperator, Assignment, SymbolNode, ArrayReference, \
    TypeDeclaration


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

    # Compares TypeDeclarations for equality or implicit conversion.
    #
    # @param param_left  TypeDeclaration
    # @param param_right TypeDeclaration
    #
    # @return Tuple (bad_token_num, error_message)
    @staticmethod
    def can_assign(param_left, param_right):
        left = AssignmentUtil.get_type_decl(param_left)
        right = AssignmentUtil.get_type_decl(param_right)
        print(left, right)

        if not left:
            return 1, 'Unknown type {}. Failed to check if assignment is valid.'.format(type(left))
        if not right:
            return 3, 'Unknown type {}. Failed to check if assignment is valid.'.format(type(right))

        if left.is_const:
            return 1, 'Constants and constant type variables cannot be reassigned.'

        left_specifiers = ' '.join(left.type_specifiers)
        right_specifiers = ' '.join(right.type_specifiers)

        if (left.type_sign == right.type_sign and left_specifiers == right_specifiers) or \
                AssignmentUtil.can_implicit_cast(left_specifiers, right_specifiers):
            return None, None
        else:
            return 3, 'Right type ({}) does not match left type ({}).'.format(
                (left.type_sign + ' ' if left.type_sign else '') + left_specifiers,
                (right.type_sign + ' ' if right.type_sign else '') + right_specifiers)

    @staticmethod
    def get_type_decl(source):
        if isinstance(source, TypeDeclaration):
            return source

        if isinstance(source, Constant):
            return source.type

        if isinstance(source, (VariableSymbol, FunctionSymbol)):
            return source.decl_type

        if isinstance(source, SymbolNode):
            return AssignmentUtil.get_type_decl(source.symbol)

        if isinstance(source, Assignment):
            return AssignmentUtil.get_type_decl(source.lvalue)

        if isinstance(source, FunctionCall):
            return AssignmentUtil.get_type_decl(source.function_symbol)

        if isinstance(source, ArrayReference):
            return AssignmentUtil.get_type_decl(source.symbol)

        if isinstance(source, BinaryOperator):
            raise NotImplemented('Checking BinaryOperator is not supported yet in AssignmentUtil')

        return None

    @staticmethod
    def can_implicit_cast(left_type, right_type):
        if left_type in AssignmentUtil.integral_types and right_type in AssignmentUtil.integral_types:
            return AssignmentUtil.integral_types[left_type] > AssignmentUtil.integral_types[right_type]
        elif left_type in AssignmentUtil.floating_types and right_type in AssignmentUtil.floating_types:
            return AssignmentUtil.floating_types[left_type] > AssignmentUtil.floating_types[right_type]

        return False

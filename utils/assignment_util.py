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
from ast.ast_nodes import Constant, FunctionCall, BinaryOperator, Assignment, SymbolNode, ArrayReference
from utils import type_utils


class AssignmentUtil(object):
    integral_types = {'char': 8, 'short': 16, 'short int': 16, 'int': 16, 'long': 32, 'long int': 32, 'long long': 64,
                      'long long int': 64}

    floating_types = {'float': 32, 'double': 64, 'long double': 80}  # Depends on platform}

    # Compares TypeDeclarations for equality or implicit conversion.
    #
    # @param param_left  TypeDeclaration
    # @param param_right TypeDeclaration
    #
    # @return Tuple (bad_token_num, error_message)
    @staticmethod
    def can_assign(param_left, param_right):
        left = param_left.get_resulting_type()
        right = param_right.get_resulting_type()

        if param_left.immutable:
            return 1, 'Constants and constant type variables cannot be reassigned.'

        if (type_utils.is_primitive_type(left) and type_utils.is_primitive_type(right)) or \
                (type_utils.is_pointer_type(left) and type_utils.is_integral_type(right)):  # we can extend this later
            return None, None

        # if not left:
        #     return 1, 'Unknown type {}. Failed to check if assignment is valid.'.format(type(left))
        # if not right:
        #     return 3, 'Unknown type {}. Failed to check if assignment is valid.'.format(type(right))

        # if (left.type_sign == right.type_sign and left_specifiers == right_specifiers) or \
        #         AssignmentUtil.can_implicit_cast(left_specifiers, right_specifiers):
        #     return None, None
        else:
            return 3, 'Right type ({}) does not match left type ({}).'.format(left, right)

    @staticmethod
    def get_type_declaration(source):
        raise NotImplementedError(
            'We are abandoning this method. It will be unnecessary since we are unpacking TypeDeclarations.')

        # if isinstance(source, TypeDeclaration):
        #     return source
        #
        # if isinstance(source, Constant):
        #     return source.type_declaration
        #
        # if isinstance(source, (VariableSymbol, FunctionSymbol)):
        #     return source.type_declaration
        #
        # if isinstance(source, SymbolNode):
        #     return AssignmentUtil.get_type_declaration(source.symbol)
        #
        # if isinstance(source, Assignment):
        #     return AssignmentUtil.get_type_declaration(source.lvalue)
        #
        # if isinstance(source, FunctionCall):
        #     return AssignmentUtil.get_type_declaration(source.function_symbol)
        #
        # if isinstance(source, ArrayReference):
        #     return AssignmentUtil.get_type_declaration(source.symbol)
        #
        # if isinstance(source, BinaryOperator):
        #     resulting_type, _ = source.get_resulting_type()
        #     type_declaration = TypeDeclaration()
        #     specifiers = resulting_type.split(' ')
        #     for specifier in specifiers:
        #         type_declaration.add_type_specifier(specifier)
        #     return type_declaration
        #
        # return None

    @staticmethod
    def can_implicit_cast(left_type, right_type):
        if left_type in AssignmentUtil.integral_types and right_type in AssignmentUtil.integral_types:
            return AssignmentUtil.integral_types[left_type] > AssignmentUtil.integral_types[right_type]
        elif left_type in AssignmentUtil.floating_types and right_type in AssignmentUtil.floating_types:
            return AssignmentUtil.floating_types[left_type] > AssignmentUtil.floating_types[right_type]

        return False

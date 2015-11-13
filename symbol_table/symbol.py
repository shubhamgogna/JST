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

import copy
import itertools
import utils
from ast.ast_nodes import SymbolNode, Constant, BinaryOperator


class Symbol(object):
    def __init__(self, identifier, lineno, column):
        self.identifier = identifier
        self.lineno = lineno
        self.column = column

        # type(decl_type) is TypeDeclaration
        self.decl_type = None
        self.finalized = False

    def clone(self):
        # TODO Verify this is actually a deepcopy
        return copy.deepcopy(self)


class VariableSymbol(Symbol):
    def __init__(self, identifier, lineno, column):
        super(VariableSymbol, self).__init__(identifier, lineno, column)
        self.array_dims = []
        self.pointer_modifiers = []

    @property
    def immutable(self):
        return 'const' in self.decl_type.type_qualifiers

    def add_pointer_level(self, pointer_declarations):
        self.pointer_modifiers.extend(pointer_declarations)

    def add_array_dimension(self, dimension):
        self.array_dims.append(dimension)

    # Basically the same as __str__ but doesn't include the identifier
    def to_abstract_str(self):
        pointer_str = '*' * len(self.pointer_modifiers)
        decl_str = str(self.decl_type) if self.decl_type else 'void'

        array_str = ''
        for dim in self.array_dims:
            array_str += '[{}]'.format(dim if dim else '')

        return '{}{}{}'.format(decl_str, pointer_str, array_str)

    # TODO I just threw this together. I should go back and fix it. - Shubham
    def get_type_tuple(self):
        pointer_str = '*' * len(self.pointer_modifiers)
        array_str = ''

        for dim in self.array_dims:
            array_str += '[{}]'.format(dim if dim else '')

        return self.decl_type.type_sign, ' '.join(self.decl_type.type_specifiers), pointer_str, array_str

    def __str__(self):
        if self.identifier == '':  # a case like when the symbol is part of a function signature
            self_str = self.to_abstract_str()
        else:
            pointer_str = len(self.pointer_modifiers) * '*' if len(self.pointer_modifiers) > 0 else ''
            type_str = '{}{}'.format(self.decl_type if self.decl_type else 'void', pointer_str)
            array_str = ''
            for dim in self.array_dims:
                array_str += '[{}]'.format(dim if dim else '')

            self_str = '{} {}{}'.format(type_str, self.identifier, array_str)

        return self_str

    def __repr__(self):
        return str(self)


class FunctionSymbol(Symbol):

    def __init__(self, identifier, lineno, column):
        super(FunctionSymbol, self).__init__(identifier, lineno, column)
        # Defines what parameters this function takes
        # It is a list of VariableSymbols that may or may not have identifiers
        self.named_parameters = []

    def parameter_types_match(self, parameter_type_list):
        for signature_symbol, parameter_symbol in itertools.zip_longest(self.named_parameters, parameter_type_list):
            if signature_symbol.to_abstract_str() != parameter_symbol.to_abstract_str():
                return False
        return True

    def set_named_parameters(self, parameter_type_list):
        if self.finalized:
            raise Exception('Attempted redefinition of function {}.'.format(self.identifier))
        self.named_parameters = parameter_type_list

    def arguments_match_parameter_types(self, argument_list):
        if len(self.named_parameters) != len(argument_list):
            return False, 'Argument count does not match required count for function call.'

        if len(argument_list) is 0 and len(self.named_parameters) is 0:
            return True, None

        for parameter, argument in itertools.zip_longest(self.named_parameters, argument_list):

            if isinstance(argument, SymbolNode):
                error_side, message = utils.assignment_util.AssignmentUtil.can_assign(parameter, argument.symbol)
            else:
                error_side, message = utils.assignment_util.AssignmentUtil.can_assign(parameter, argument)

            if error_side is not None:
                raise Exception(message)

        return True, None

    # TODO I just threw this together. I should go back and fix it. - Shubham
    def get_type_tuple(self):
        return self.decl_type.type_sign, ' '.join(self.decl_type.type_specifiers), '', ''

    def __str__(self):
        decl_str = str(self.decl_type) if self.decl_type else 'void'
        args_as_strings = ''

        if self.named_parameters:
            args_as_strings = ', '.join([str(symbol) for symbol in self.named_parameters])

        return '{} {}({})'.format(decl_str, self.identifier, args_as_strings)

    def __repr__(self):
        return str(self)

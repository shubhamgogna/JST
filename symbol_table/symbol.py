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

from ast.ast_nodes import SymbolNode
from utils import type_utils


class Symbol(object):

    def __init__(self, identifier, lineno, column):
        self.identifier = identifier
        self.lineno = lineno
        self.column = column

        self.global_memory_location = None
        self.activation_frame_offset = None

        self.finalized = False

    def clone(self):
        # TODO Verify this is actually a deepcopy
        return copy.deepcopy(self)


class VariableSymbol(Symbol):

    def __init__(self, identifier, lineno, column):
        super(VariableSymbol, self).__init__(identifier, lineno, column)

        # In GCC, qualifiers and classes are idempotent
        self.storage_classes = set()
        self.type_qualifiers = set()
        self.type_specifiers = ''

        self.value = None
        self.is_parameter = False

    def finalize(self):
        # TODO:
        # check the type specifiers for correctness
        # check the pointers for correctness
        # check the array dims for correctness
        # allocate the memory space
        self.finalized = True

    @property
    def immutable(self):
        return type_utils.CONST in self.type_qualifiers

    def get_type_str(self):
        return self.type_specifiers

    def add_type_declaration(self, type_declaration):
        self.storage_classes = type_declaration.storage_classes
        self.type_qualifiers = type_declaration.type_qualifiers
        self.type_specifiers = ' '.join(type_declaration.type_specifiers)

    def get_resulting_type(self):
        return self.get_type_str()

    def size_in_bytes(self):
        return type_utils.type_size_in_bytes(self.type_specifiers)

    def __str__(self):
        if self.is_parameter:
            return self.get_type_str()
        else:
            return '{} {}'.format(self.type_specifiers, self.identifier)

    def __repr__(self):
        return str(self)


class PointerSymbol(Symbol):

    def __init__(self, identifier, lineno, column):
        super(PointerSymbol, self).__init__(identifier, lineno, column)
        self.dimensions = []

        # In GCC, qualifiers and classes are idempotent
        self.storage_classes = set()
        self.type_qualifiers = set()
        self.type_specifiers = ''

        self.value = None
        self.is_parameter = False

    @property
    def immutable(self):
        return type_utils.CONST in self.type_qualifiers

    @property
    def is_array(self):
        for dim in self.dimensions:
            if dim is None:
                return False
        return True

    @property
    def is_pointer(self):
        return not self.is_array

    def get_type_str(self):
        return self.type_specifiers

    def add_type_declaration(self, type_declaration):
        self.storage_classes = type_declaration.storage_classes
        self.type_qualifiers = type_declaration.type_qualifiers
        self.type_specifiers = ' '.join(type_declaration.type_specifiers)

    def add_dimension(self, qualifiers, size=None):
        self.dimensions.append((qualifiers, size))

    def size_in_bytes(self):
        if self.is_pointer:
            # MIPS uses 4 bytes for a word (pointers are the size of a word)
            return 4
        else:
            multiplier = 1
            for dim in self.dimensions:
                multiplier *= dim

            return multiplier * type_utils.type_size_in_bytes(self.type_specifiers)

    def __str__(self):
        if self.is_parameter:
            return self.get_type_str()
        elif self.is_array:
            dim_str = '[' + ']['.join([size for (x, size) in self.dimensions]) + ']'
            return '{} {}{}'.format(self.type_specifiers, self.identifier, dim_str)
        else:
            return '{} {}{}'.format(self.type_specifiers, self.identifier, '*' * len(self.dimensions))


class FunctionSymbol(Symbol):

    def __init__(self, identifier, lineno, column):
        super(FunctionSymbol, self).__init__(identifier, lineno, column)
        # Defines what parameters this function takes
        # It is a list of VariableSymbols that may or may not have identifiers
        self.named_parameters = []

        self.return_type_pointer_modifiers = []
        self.return_type_specifiers = ''

        self.activation_frame_size = 0  # the variables and params, doesn't count stored registers

    @classmethod
    def from_variable_symbol(cls, variable_symbol):
        if not isinstance(variable_symbol, VariableSymbol):
            raise Exception("Can't construct a FunctionSymbol from something that isn't a VariableSymbol")
        return FunctionSymbol(variable_symbol.identifier, variable_symbol.lineno, variable_symbol.column)

    def parameter_types_match(self, parameter_type_list):
        for signature_symbol, parameter_symbol in itertools.zip_longest(self.named_parameters, parameter_type_list):
            if signature_symbol.to_abstract_str() != parameter_symbol.to_abstract_str():
                return False
        return True

    def add_return_type_declaration(self, type_declaration):
        self.return_type_specifiers = ' '.join(type_declaration.type_specifiers)

    def set_named_parameters(self, parameter_type_list):
        if self.finalized:
            raise Exception('Attempted redefinition of function {}.'.format(self.identifier))
        self.named_parameters = parameter_type_list

        for named_parameter in self.named_parameters:
            named_parameter.is_parameter = True

    def arguments_match_parameter_types(self, argument_list):
        if len(self.named_parameters) != len(argument_list):
            return False, 'Argument count does not match required count for function call.'

        if len(argument_list) is 0 and len(self.named_parameters) is 0:
            return True, None

        for parameter, argument in itertools.zip_longest(self.named_parameters, argument_list):

            if isinstance(argument, SymbolNode):
                cast_result, message = type_utils.can_assign(parameter.get_resulting_type(), argument.symbol.get_resulting_type())
            else:
                cast_result, message = type_utils.can_assign(parameter.get_resulting_type(), argument.get_resulting_type())

            if cast_result == type_utils.INCOMPATIBLE_TYPES:
                raise Exception(message)

        return True, None

    def get_resulting_type(self):
        return self.return_type_specifiers

    def __str__(self):
        decl_str = str(self.return_type_specifiers) if self.return_type_specifiers != '' else 'void'
        args_as_strings = ''

        if self.named_parameters:
            args_as_strings = ', '.join([str(symbol) for symbol in self.named_parameters])

        return '{} {}({})'.format(decl_str, self.identifier, args_as_strings)

    def __repr__(self):
        return str(self)


class TypeDeclaration(object):
    """
    Not sure if this should remain an AST node, but rather an info collection class that gets disassembled and
    absorbed by the Symbol this contributes to.
    """

    def __init__(self, **kwargs):
        # In GCC, storage classes are idempotent (but there can only be one of each)
        self.storage_classes = set()
        # In GCC, qualifiers are idempotent
        self.type_qualifiers = set()
        # List allows for things like 'long long' and 'long double'
        self.type_specifiers = []
        # Indicated if the type is signed/unsigned
        # None = sign not applicable
        self.type_sign = None

    def add_all_from(self, other_type_declaration):
        # TODO: error checking?
        self.type_specifiers.extend(other_type_declaration.type_specifiers)
        self.type_qualifiers.update(other_type_declaration.type_qualifiers)
        self.storage_classes.update(other_type_declaration.storage_classes)

    def name_arg(self):
        joined = [self.type_sign if self.type_sign else '',
                  ' '.join(self.storage_classes),
                  ' '.join(self.type_qualifiers),
                  ' '.join(self.type_specifiers)]
        return ' '.join([i for i in joined if i is not ''])

    def add_storage_class(self, storage_class_specifier):
        if storage_class_specifier in self.storage_classes:
            raise Exception('Duplication of storage class specifier "{}".'.format(storage_class_specifier))
        self.storage_classes.add(storage_class_specifier)

    def add_type_qualifier(self, type_qualifier):
        self.type_qualifiers.add(type_qualifier)

    def add_type_specifier(self, specifier):
        if specifier == 'unsigned' or specifier == 'signed':
            if self.type_sign is not None:
                raise Exception('Multiple signed/unsigned specifiers not allowed.')
            else:
                self.type_sign = specifier
        else:
            self.type_specifiers.insert(0, specifier)

    def get_type_str(self):
        return (self.type_sign + ' ' if self.type_sign else '') + ' '.join(self.type_specifiers)

    def sizeof(self):
        return type_utils.get_bit_size(self) / 4  # divide by 4 for bytes

    @property
    def immutable(self):
        return 'const' in self.type_qualifiers

    def __str__(self):
        joined = [self.type_sign if self.type_sign else '',
                  ' '.join(self.storage_classes),
                  ' '.join(self.type_qualifiers),
                  ' '.join(self.type_specifiers) if self.type_specifiers else 'Unknown']
        return ' '.join([i for i in joined if i is not ''])

    def __repr__(self):
        return str(self)

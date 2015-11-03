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


class Symbol(object):
    EMPTY_ARRAY_DIM = -1

    def __init__(self, identifier, lineno=-1, column_no=0, type=None):
        self.finalized = False
        self.symbol_class = None
        self.identifier = identifier
        self.type = None  # TypeDeclaration
        self.pointer_modifiers = []
        self.array_dims = []
        self.storage_specifiers = []  # auto, static, extern, etc.
        self.type_qualifier = None  # const, volatile
        self.struct_members = {}
        self.union_members = {}
        self.enum_members = {}
        self.parameters = []
        self.is_struct = False
        self.is_enum = False
        self.is_function = False

    def set_pointer_modifiers(self, pointer_declarations=None):
        self.pointer_modifiers = pointer_declarations

    # Basically the same as __str__ but doesn't include the identifier
    def to_abstract_str(self):
        pointer_str = len(self.pointer_modifiers) * '*' if len(self.pointer_modifiers) > 0 else ''
        type_str = '{}{}'.format(self.type if self.type else 'void', pointer_str)

        array_str = ''
        for dim in self.array_dims:
            array_str += '[{}]'.format(dim if dim is not None else '')

        return '{}{}'.format(type_str, array_str)

    def __str__(self):
        # TODO: lots...

        self_str = ''

        if self.identifier == '':  # a case like when the symbol is part of a function signature
            self_str = self.to_abstract_str()
        else:
            pointer_str = len(self.pointer_modifiers) * '*' if len(self.pointer_modifiers) > 0 else ''
            type_str = '{}{}'.format(self.type if self.type else 'void', pointer_str)
            array_str = ''
            for dim in self.array_dims:
                array_str += '[{}]'.format(dim if dim is not None else '')

            self_str = '{} {}{}'.format(type_str, self.identifier, array_str)

        return self_str

    def __repr__(self):
        return str(self)

    def clone(self):
        return copy.deepcopy(self)


class VariableSymbol(Symbol):
    def __init__(self, identifier, lineno=-1, column_no=0):
        super(VariableSymbol, self).__init__(identifier, lineno, column_no)

    # Sets the array dimensions for the VariableSymbol.
    #
    # @param dimensions List of integers (optionally with None in the last element)
    def set_array_dimensions(self, dimensions):
        if dimensions is None:
            self.array_dims = None
        elif type(dimensions) is list:
            self.array_dims = dimensions    # TODO Deepcopy?
        else:
            raise ValueError('Dimensions must be a list of integers.')

    @property
    def immutable(self):
        return 'const' in self.type.qualifiers


class FunctionSymbol(Symbol):
    def __init__(self, identifier, lineno):
        super(FunctionSymbol, self).__init__(identifier, lineno)

        self.return_type = None
        self.signature = []
        self.named_parameters = []

    def set_signature(self, parameters):
        if self.finalized:
            raise Exception('Error: redefinition of function {}. (TODO replace with CompileException)'
                            .format(self.identifier))

        self.signature.extend(parameters)

    def parameter_types_match(self, parameter_type_list):
        for signature_symbol, parameter_symbol in itertools.zip_longest(self.signature, parameter_type_list):
            if signature_symbol.to_abstract_str() != parameter_symbol.to_abstract_str():
                return False
        return True

    def add_named_parameters(self, paramter_type_list):
        if self.finalized:
            raise Exception('Error: redefinition of function {}. (TODO replace with CompileException)'
                            .format(self.identifier))

        self.named_parameters.extend(paramter_type_list)

    def arguments_match_parameter_types(self, argument_list):
        for signature_symbol, argument in itertools.zip_longest(self.signature, argument_list):
            arg_type_str = ''
            if isinstance(argument, Symbol):
                arg_type_str = argument.to_abstract_str()
            elif isinstance(argument, ConstantValue):
                arg_type_str = argument.type
            else:
                raise Exception('Debug: did I forget a class-type?')

            if signature_symbol.to_abstract_str() != arg_type_str:
                # TODO: make sure that we can match types that are different but still compatible (Ex: char and int)
                return False

        return True


    def __str__(self):
        pointer_str = len(self.pointer_modifiers) * '*' if len(self.pointer_modifiers) > 0 else ''
        type_str = '{}{}'.format(self.type, pointer_str)

        args_as_strings = []

        if self.named_parameters:
            args_as_strings = [str(symbol) for symbol in self.named_parameters]
        elif self.signature:
            args_as_strings = [symbol.to_abstract_str() for symbol in self.signature]

        arg_list_string = ', '.join(args_as_strings) if args_as_strings else ''

        return '{} {}({})'.format(type_str, self.identifier, arg_list_string)

    def __repr__(self):
        return str(self)


class ConstantValue(object):
    INTEGER = 'int'
    FLOAT = 'float'

    def __init__(self, value=0, type=INTEGER):
        self.value = value
        self.type = type


###############################################################################
# Declaration Classes Below
###############################################################################


class TypeDeclaration(object):
    FLOAT_TYPES = {'float', 'double'}
    INT_TYPES = {'char', 'short', 'int'}

    def __init__(self):
        # Storage class items cannot be repeated + any order
        self.storage_classes = set() # TODO convert to set
        # Type qualifiers can be repeated + any order
        self.type_qualifiers = set()
        # Type specifiers can have special meanings in cases
        # such as 'unsigned int' or 'long double'
        self.type_specifiers = []

    def add_storage_class(self, storage_class_specifier):
        if storage_class_specifier in self.storage_classes:
            raise ValueError('Duplicate storage class specifier "{}".'.format(storage_class_specifier))
        else:
            self.storage_classes.add(storage_class_specifier)

    def add_qualifier(self, type_qualifier):
        self.type_qualifiers.add(type_qualifier)

    def add_type_specifier(self, specifier):
        self.type_specifiers.append(specifier)

        result = self.__validate_type_specifiers()
        if result[0] is False:
            raise ValueError(result[1])

    def __str__(self):
        storage_class_str = ' '.join(self.storage_classes) + ' ' if self.storage_classes else ''
        qualifier_str = ' '.join(self.type_qualifiers) + ' ' if self.type_qualifiers else ''
        specifier_str = ' '.join(self.type_specifiers) if self.type_specifiers else 'UNKNOWN'

        return '{}{}{}'.format(storage_class_str, qualifier_str, specifier_str)

    def __repr__(self):
        return str(self)

    def __validate_type_specifiers(self):
        cloned = [specifier for specifier in self.type_specifiers]
        contains_unsigned, contains_signed = False, False
        while 'unsigned' in cloned:
            cloned.remove('unsigned')
            contains_unsigned = True
        while 'signed' in cloned:
            cloned.remove('signed')
            contains_signed = True

        if len(cloned) is 0:
            return True, None
        elif len(cloned) is 1:
            if (contains_unsigned or contains_signed) and (cloned[0] == 'float' or cloned[0] == 'double'):
                return False, 'Floats or doubles cannot be (un)signed.'
            else:
                return True, None
        else:
            joined = ' '.join(cloned)
            if joined == 'long long' or joined == 'long double':
                return True, None
            else:
                return False, 'Invalid combination of types.'

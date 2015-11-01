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

###############################################################################
# File Description: Class for representing the various forms an identifier
# in code can have, such as a variable, function, typedef, etc.
###############################################################################

import copy
import itertools


class Symbol(object):
    VARIABLE = 'VARIABLE'
    FUNCTION = 'FUNCTION'
    TYPEDEF = 'TYPEDEF'
    ENUM = 'ENUM'
    STRUCT = 'STRUCT'
    UNION = 'UNION'

    EMPTY_ARRAY_DIM = -1

    def __init__(self, identifier, lineno=-1, colomn_no=0, type=None, ):
        self.finalized = False
        self.symbol_class = None
        self.type = None  # TypeDeclaration
        self.identifier = identifier
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


    def add_pointer_level(self, pointer_declarations):
        self.pointer_modifiers.extend(pointer_declarations)

    def add_array_dimension(self, dimension):
        if (dimension is Symbol.EMPTY_ARRAY_DIM and self.array_dims and self.array_dims[-1] is Symbol.EMPTY_ARRAY_DIM) \
                or (dimension is not Symbol.EMPTY_ARRAY_DIM and dimension < 0):
            raise Exception("Invalid array dimension ({}) when {} already specified".format(dimension, self.array_dims))

        self.array_dims.append(dimension)


    def add_parameters(self, parameters):
        self.is_function = True
        if parameters:
            self.parameters.extend(parameters)

    def add_compound_statements(self, compound_statements):
        pass

    def get_symbol_class(self):
        # others might refer to this as Node Type
        if self.symbol_class:
            return self.symbol_class
        elif self.is_function or self.parameters:
            return Symbol.FUNCTION
        # TODO: if we are feeling frisky, we can do the harder stuff
        # elif self.struct_members:
        #     return  Symbol.STRUCT
        # elif self.union_members:
        #     return Symbol.UNION
        # elif self.enum_members:
        #     return Symbol.ENUM
        # elif self.is_typedef:
        #    pass
        else:
            return Symbol.VARIABLE

    def set_as_variable(self, type_declaration):
        self.symbol_class = Symbol.VARIABLE
        self.type = type_declaration

    def set_as_function(self, type_declaration, parameter_list, compound_statements):
        self.type = Symbol.FUNCTION
        self.type = type_declaration
        self.add_parameters(parameter_list)
        self.add_compound_statements(compound_statements)

    ## Basically the same as __str__ but doesn't include the identifier
    def to_abstract_str(self):
        pointer_str = len(self.pointer_modifiers) * '*' if len(self.pointer_modifiers) > 0 else ''
        type_str = '{}{}'.format(self.type if self.type else 'void', pointer_str)

        array_str = ''
        for dim in self.array_dims:
            array_str += '[{}]'.format(dim if dim is not Symbol.EMPTY_ARRAY_DIM else '')

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
                array_str += '[{}]'.format(dim if dim is not Symbol.EMPTY_ARRAY_DIM else '')

            self_str = '{} {}{}'.format(type_str, self.identifier, array_str)

        return self_str

    def __repr__(self):
        return str(self)

    def clone(self):
        return copy.deepcopy(self)


class TypeDeclaration(object):
    FLOAT_TYPES = {'float', 'double'}
    INT_TYPES = {'char', 'short', 'int'}

    def __init__(self):
        self.storage_class = []
        self.qualifiers = set()  # in gcc, type qualifiers are idempotent
        self.type_specifier = []  # being a list allows for things like 'unsigned int', 'long double'

    def add_storage_class(self, storage_class_specifier):
        if storage_class_specifier in self.storage_class:
            raise Exception('Duplication of storage class specifier "{}".'.format(storage_class_specifier))

        self.storage_class.append(storage_class_specifier)

    def add_qualifier(self, type_qualifier):
        self.qualifiers.add(type_qualifier)

    def add_type_specifier(self, specifier):

        if (specifier is 'long' and 2 <= self.type_specifier.count('long')) or specifier in self.type_specifier:
            raise Exception('Too many instances of type specifier "{}" in type declaration'.format(specifier))

        self.type_specifier.append(specifier)

        # TODO: check for unsigned along with float types and such

    def __str__(self):
        storage_class_str = ' '.join(self.storage_class) + ' ' if self.storage_class else ''
        qualifier_str = ' '.join(self.qualifiers) + ' ' if self.qualifiers else ''
        specifier_str = ' '.join(self.type_specifier) if self.type_specifier else 'UNKNOWN'

        return '{}{}{}'.format(storage_class_str, qualifier_str, specifier_str)

    def __repr__(self):
        return str(self)


class PointerDeclaration(object):
    def __init__(self):
        self.qualifiers = []

    def add_qualifiers(self, qualifiers):
        pass


class ConstantValue(object):
    INTEGER = 'int'
    FLOAT = 'float'

    def __init__(self, value=0, type=INTEGER):
        self.value = value
        self.type = type





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



class NewSymbol(object):
    VARIABLE = 'VARIABLE'
    FUNCTION = 'FUNCTION'
    TYPEDEF = 'TYPEDEF'
    ENUM = 'ENUM'
    STRUCT = 'STRUCT'
    UNION = 'UNION'

    def __init__(self, identifier=''):
        # Used to identify the symbol
        self.identifier = identifier

        # Determines if Symbol is not defined (None),
        # VARIABLE, FUNCTION, TYPEDEF, ENUM, STRUCT, or UNION
        self.type = None

        # TODO Eventually need to store more information about Symbol
        # TODO Example: Variables have a variable-type ('x' can be a variable-type of 'int')
        self.decl_specifiers = None

        self.parameter_type_list = None
        self.compound_statements = None

    def set_as_variable(self, decl_specifiers):
        self.type = Symbol.VARIABLE
        self.decl_specifiers = decl_specifiers

    def set_as_function(self, decl_specifiers, parameter_type_list, compound_statements):
        self.type = Symbol.FUNCTION
        # decl_specifiers is the function's return type
        self.decl_specifiers = decl_specifiers
        self.parameter_type_list = parameter_type_list
        self.compound_statements = compound_statements

    def __repr__(self):
        prefix = self.identifier + ' ' + str(self.type)

        if self.type is Symbol.VARIABLE:
            return "%s (%s)" % (prefix, str(self.decl_specifiers))
        elif self.type is Symbol.FUNCTION:
            lst = []
            if self.parameter_type_list is not None:
                for item in self.parameter_type_list:
                    lst.append(item)
            return "%s (%s) (%s)" % (prefix, str(self.decl_specifiers), ' '.join(lst))
        else:
            return prefix

    def clone(self):
        result = Symbol(self.identifier)
        result.type = self.type
        # TODO This is not a deep copy!
        result.decl_specifiers = self.decl_specifiers
        result.parameter_type_list = self.parameter_type_list
        result.compound_statements = self.compound_statements
        return result



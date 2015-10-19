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

class Symbol(object):
    EMPTY_ARRAY_DIM = -1

    def __init__(self, identifier='', type=None):
        self.type = None  # TypeDeclaration
        self.identifier = identifier
        self.pointer_modifiers = []
        self.array_dims = []
        self.storage_specifiers = []  # auto, static, extern, etc.
        self.type_qualifier = None  # const, volatile
        self.parameters = []
        self.is_struct = False
        self.is_enum = False
        self.is_function = False

    def __str__(self):
        # TODO: lots...

        if self.is_function:
            return 'function: {} {}({})'.format(self.type, self.name, self.parameters, self.type)
        else:
            pointer_str = len(self.pointer_modifiers) * '*' if len(self.pointer_modifiers) > 0 else ''
            array_str = ''
            for dim in self.array_dims:
                array_str += '[{}]'.format(dim if dim is not Symbol.EMPTY_ARRAY_DIM else '')

            return '{}{} {}{}'.format(self.type, pointer_str, self.identifier, array_str)

    def __repr__(self):
        return str(self)

    def add_storage_specifier(self, specifier):
        pass

    def add_type_qualifier(self, qualifier):
        pass

    def add_pointer_level(self, pointer_declarations):
        self.pointer_modifiers.extend(pointer_declarations)

    def add_array_dimension(self, dimension):
        if (dimension is Symbol.EMPTY_ARRAY_DIM and self.array_dims and self.array_dims[-1] is Symbol.EMPTY_ARRAY_DIM) \
                or (dimension is not Symbol.EMPTY_ARRAY_DIM and dimension < 0):
            raise Exception("Invalid array dimension ({}) when {} already specified".format(dimension, self.array_dims))

        self.array_dims.append(dimension)

    def add_struct_members(self, members):
        pass

    def add_union_members(self, members):
        pass

    def add_enum_members(self, members):
        pass

    def add_arguments(self, arguments):
        self.is_function = True
        pass


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


class PointerDeclaration(object):
    def __init__(self):
        self.qualifiers = []

    def add_qualifiers(self):
        pass
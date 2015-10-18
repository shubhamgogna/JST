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
    EMPTY_ARRAY_DiM = -1

    def __init__(self, identifier='', type=None):
        self.type = ''  # int, float, etc.
        self.identifier = identifier
        self.pointer_level = 0
        self.array_dims = []
        self.storage_specifiers = []  # auto, static, extern, etc.
        self.type_qualifier = None    # const, volatile
        self.parameters = []
        self.is_struct = False
        self.is_enum = False
        self.is_function = False

    def __str__(self):
        # TODO: lots...

        if self.is_function:
            return 'function: {} {}({})'.format(self.type, self.name, self.parameters, self.type)
        else:
            pointer_str = self.pointer_level * '*'
            array_str = ''
            for dim in self.array_dims:
                array_str += '[{}]'.format(dim if dim is not Symbol.EMPTY_ARRAY_DiM else '')

            return '{}{} {}{}'.format(self.type, pointer_str, self.identifier, array_str)

    def __repr__(self):
        return str(self)

    def add_storage_specifier(self, specifier):
        pass

    def add_type_qualifier(self, qualifier):
        pass

    def add_to_pointer_level(self, addition):
        pass

    def add_struct_members(self, members):
        pass

    def add_union_members(self, members):
        pass

    def add_enum_members(self, members):
        pass

    def add_arguments(self, arguments):
        self.is_function = True
        pass


class FunctionSymbol(Symbol):
    def __int__(self, identifier, type=None):
        super(FunctionSymbol, self).__init__(identifier, type)
        self.arguments = []


class ConstantSymbol(Symbol):
    def __int__(self, identifier, value, type=None):
        super(ConstantSymbol, self).__init__(identifier, type)
        self.value = value

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
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

from symbol_table.symbol import Symbol


class SymbolBuilder(object):
    """A placeholder so I can continue working."""

    def __init__(self, type_qualifier=list(), storage_specifiers=list(), pointer_count=0, type=None, identifier=None,
                 array_dims=list(), is_struct=False, struct_members=list(), is_enum=False, enum_members=list(),
                 is_function=False, arguments=list(), is_constant_literal=False, literal_value=None):

        self.type_qualifier = type_qualifier  # const, volatile
        self.storage_specifiers = storage_specifiers  # auto, static, extern, etc.
        self.pointer_count = pointer_count
        self.type = type  # int, float, etc.
        self.identifier = identifier
        self.array_dims = array_dims

        self.is_struct = is_struct
        self.struct_members = struct_members

        self.is_enum = is_enum
        self.enum_members = enum_members

        self.is_function = is_function
        self.arguments = arguments

        self.is_constant_literal = is_constant_literal
        self.literal_value = literal_value

    def combine(self, other_builder):
        # TODO: add sanity checks for fields that can't or shouldn't be combined
        self.type_qualifier.extend(other_builder.type_qualifier)
        self.storage_specifiers.extend(other_builder.storage_specifiers)
        self.pointer_count += other_builder.pointer_count
        if self.type is None:
            self.type = other_builder.type
        self.array_dims.extend(other_builder.array_dims)
        self.is_function |= other_builder.is_function
        self.arguments.extend(other_builder.arguments)

        # probably won't need to do anything for literal constants, object should be immutable at that point

        return self

    def add_member(self, new_member):
        self.is_struct = True  # if it has an argument, it must be a struct
        self.struct_members.append(new_member)
        return self

    def add_enum_member(self, new_member):
        self.is_enum = True  # if it has an argument, it must be an enum
        self.enum_members.append(new_member)
        return self

    def add_argument(self, new_arg_symbol):
        self.is_function = True  # if it has an argument, it must be a function
        self.arguments.append(new_arg_symbol)
        return self

    def build(self):
        return Symbol(self.identifier)



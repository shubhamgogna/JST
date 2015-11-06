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
from utils.primitive_types import Type


class TypeCheck(object):

    @staticmethod
    def type_specifier_is_acceptable(type_specifiers):
        if type_specifiers.count(Type.LONG) > 2:
            raise Exception('Type "long long long" is too long for jstcc')

        if (Type.SIGNED in type_specifiers or Type.UNSIGNED in type_specifiers) and (
                Type.FLOAT in type_specifiers or Type.DOUBLE in type_specifiers):
            raise Exception(
                'Floating point types are implicitly signed, declaring them to be signed or unsigned is silly.')

        if (type_specifiers.count(Type.FLOAT) + type_specifiers.count(Type.DOUBLE)) > 1:
            raise Exception('Floating point specifiers can only be used once in a declaration.')

    @staticmethod
    def get_bit_size(type):
        # TODO implement me!
        return 4



class ArrayDimensionCheck(object):
    @staticmethod
    def array_dimensions_are_acceptable(array_dims):
        pass
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


class TypeDeclarationUtil(object):
    valid_primative_types = {
        'char': 8,
        'short': 16,
        'short int': 16,
        'int': 16,
        'long': 16,
        'long int': 32,
        'long long': 64,
        'long long int': 64,
        'float': 32,
        'double': 64,
        'long double': 80  # Depends on platform
    }

    integral_types = (
        'char',
        'short',
        'short int',
        'int',
        'long',
        'long int',
        'long long',
        'long long int'
    )

    floating_types = (
        'float',
        'double',
        'long double'  # Depends on platform
    )

    @staticmethod
    def is_valid(declaration):
        type_str = declaration.get_type_str()

        if type_str in TypeDeclarationUtil.valid_primative_types:
            if type_str in TypeDeclarationUtil.integral_types:
                if declaration.type_sign is None:
                    # Default is a signed value
                    declaration.type_sign = 'signed'
            else:
                if declaration.type_sign is not None:
                    return False, 'Floating point values cannot be specified as signed/unsigned.'
            return True, None
        else:
            return False, 'Invalid or unknown type ({}).'.format(type_str)

    @staticmethod
    def get_bit_size(declaration):
        type_str = declaration.get_type_str()

        if type_str in TypeDeclarationUtil.valid_primative_types:
            return TypeDeclarationUtil.valid_primative_types[type_str]
        else:
            raise Exception('Invalid or unknown type ({}).'.format(type_str))

    @staticmethod
    def is_integral_type(declaration):
        return declaration.get_type_str() in TypeDeclarationUtil.integral_types

    @staticmethod
    def is_floating_type(declaration):
        return declaration.get_type_str() in TypeDeclarationUtil.floating_types

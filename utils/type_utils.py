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

VALID_PRIMITIVE_TYPES = {'void': 0, 'char': 8, 'short': 16, 'short int': 16, 'int': 16, 'long': 16, 'long int': 32,
    'long long': 64, 'long long int': 64, 'float': 32, 'double': 64, 'long double': 80  # Depends on platform
    }

INTEGRAL_TYPES = ('char', 'short', 'short int', 'int', 'long', 'long int', 'long long', 'long long int')

FLOATING_POINT_TYPES = ('float', 'double', 'long double'  # Depends on platform
                        )

CAST_UP = "CAST_RESULT_UP"
CAST_DOWN = 'CAST_RESULT_DOWN'
CAST_UNAFFECTED = 'CAST_RESULT_UNAFFECTED'


def is_valid_type(declaration):
    type_str = declaration.get_type_str()

    if type_str in VALID_PRIMITIVE_TYPES:
        if type_str in INTEGRAL_TYPES:
            if declaration.type_sign is None:
                # Default is a signed value
                declaration.type_sign = 'signed'
        else:
            if declaration.type_sign is not None:
                return False, 'Floating point values cannot be specified as signed/unsigned.'
        return True, None
    else:
        return False, 'Invalid or unknown type ({}).'.format(type_str)


def get_bit_size(declaration):
    type_str = declaration.get_type_str()

    if type_str in VALID_PRIMITIVE_TYPES:
        return VALID_PRIMITIVE_TYPES[type_str]
    else:
        raise Exception('Invalid or unknown type ({}).'.format(type_str))


def is_integral_type(type_declaration_str):
    return type_declaration_str.get_type_str() in INTEGRAL_TYPES

def is_floating_type(declaration):
    return declaration.get_type_str() in FLOATING_POINT_TYPES


def get_promoted_type(one_type, other_type):
    if one_type == other_type:
        return one_type, CAST_UNAFFECTED
    elif is_integral_type(one_type) and is_integral_type(other_type) or \
         is_floating_type(one_type) and is_floating_type(other_type):

        return one_type if VALID_PRIMITIVE_TYPES[one_type] > VALID_PRIMITIVE_TYPES[other_type] else other_type, CAST_UP
    elif is_floating_type(one_type):
        return one_type, CAST_UP
    else:
        return other_type, CAST_UP


def cast_as_required_type(required_type, given_type):
    if required_type == given_type or required_type > given_type:
        return CAST_UNAFFECTED
    elif required_type < given_type:
        # TODO: in 3AC we will have to smash the given value down ot fit the required type
        # example, if 256 needs to be stored as a char, return 0
        #             257     ""                          ""   1
        # the process is likely as simple as just keeping the lower bits of the given value (at least for ints, not
        # sure about floats)
        return CAST_DOWN


class Type(object):
    """
    Not really used in earnest, still lingering in a few places in the code.
    """
    CHAR = 'char'
    SHORT = 'short'
    INT = 'int'
    LONG = 'long'
    SIGNED = 'signed'
    UNSIGNED = 'unsigned'
    FLOAT = 'float'
    DOUBLE = 'double'


class TypeCheck(object):

    @staticmethod
    def type_specifier_is_acceptable(type_specifiers):
        '''
        This method is currently unused; it has been placed on hold in favor of the simpler "look the type up in an
        enumeration of all valid types" approach to validation.
        '''
        if type_specifiers.count(Type.LONG) > 2:
            raise Exception('Type "long long long" is too long for jstcc')

        if (Type.SIGNED in type_specifiers or Type.UNSIGNED in type_specifiers) and (
                Type.FLOAT in type_specifiers or Type.DOUBLE in type_specifiers):
            raise Exception(
                'Floating point types are implicitly signed, declaring them to be signed or unsigned is silly.')

        if (type_specifiers.count(Type.FLOAT) + type_specifiers.count(Type.DOUBLE)) > 1:
            raise Exception('Floating point specifiers can only be used once in a declaration.')

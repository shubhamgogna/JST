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


#
# TODO: WARNING: NOTHING HAS BEEN DONE HERE TO HANDLE POINTER TYPES, WHICH WE MAY WANT TO DO.
#
import re


VOID = 'void'
CHAR = 'char'
SIGNED_CHAR = 'signed char'
UNSIGNED_CHAR = 'unsigned char'
SHORT = 'short'
SHORT_INT = 'short int'
SIGNED_SHORT = 'signed short'
SIGNED_SHORT_INT = 'signed short int'
UNSIGNED_SHORT = 'unsigned short'
UNSIGNED_SHORT_INT = 'unsigned short int'
INT = 'int'
SIGNED = 'signed'
SIGNED_INT = 'signed int'
UNSIGNED = 'unsigned'
UNSIGNED_INT = 'unsigned int'
LONG = 'long'
LONG_INT = 'long int'
SIGNED_LONG = 'signed long'
SIGNED_LONG_INT = 'signed long int'
UNSIGNED_LONG = 'unsigned long'
UNSIGNED_LONG_INT = 'unsigned long int'
LONG_LONG = 'long long'
LONG_LONG_INT = 'long long int'
SIGNED_LONG_LONG = 'signed long long'
SIGNED_LONG_LONG_INT = 'signed long long int'
UNSIGNED_LONG_LONG = 'unsigned long long'
UNSIGNED_LONG_LONG_INT = 'unsigned long long int'
FLOAT = 'float'
DOUBLE = 'double'
LONG_DOUBLE = 'long double'


VALID_PRIMITIVE_TYPES = {'void': 0, 'char': 8, 'short': 16, 'short int': 16, 'int': 16, 'long': 16, 'long int': 32,
    'long long': 64, 'long long int': 64, 'float': 32, 'double': 64, 'long double': 80  # Depends on platform
    }


class TypeAttributes(object):
    def __init__(self, rank, bit_size, signed=True, integral=True, floating_point=False):
        self.rank = rank
        self.bit_size = bit_size
        self.signed = signed
        self.integral = integral
        self.floating_point = floating_point

        if floating_point:
            self.signed = False
            self.integral = False


# Note: if two items share the same rank, they are essentially the same type anyway.
# Note: there is a gap in the rankings in case int needs to move down
TYPE_ATTRIBUTES = {
    VOID:                    TypeAttributes(rank=0, bit_size=0, signed=False, integral=False, floating_point=False),
    CHAR:                    TypeAttributes(rank=1, bit_size=8),
    SIGNED_CHAR:             TypeAttributes(rank=1, bit_size=8),
    UNSIGNED_CHAR:           TypeAttributes(rank=2, bit_size=8, signed=False),
    SHORT:                   TypeAttributes(rank=3, bit_size=16),
    SHORT_INT:               TypeAttributes(rank=3, bit_size=16),
    SIGNED_SHORT:            TypeAttributes(rank=3, bit_size=16),
    SIGNED_SHORT_INT:        TypeAttributes(rank=3, bit_size=16),
    UNSIGNED_SHORT:          TypeAttributes(rank=4, bit_size=16, signed=False),
    UNSIGNED_SHORT_INT:      TypeAttributes(rank=4, bit_size=16, signed=False),
    INT:                     TypeAttributes(rank=7, bit_size=32),
    SIGNED:                  TypeAttributes(rank=7, bit_size=32),
    SIGNED_INT:              TypeAttributes(rank=7, bit_size=32),
    UNSIGNED:                TypeAttributes(rank=8, bit_size=32, signed=False),
    UNSIGNED_INT:            TypeAttributes(rank=8, bit_size=32, signed=False),
    LONG:                    TypeAttributes(rank=7, bit_size=32),
    LONG_INT:                TypeAttributes(rank=7, bit_size=32),
    SIGNED_LONG:             TypeAttributes(rank=7, bit_size=32),
    SIGNED_LONG_INT:         TypeAttributes(rank=7, bit_size=32),
    UNSIGNED_LONG:           TypeAttributes(rank=8, bit_size=32, signed=False),
    UNSIGNED_LONG_INT:       TypeAttributes(rank=8, bit_size=32, signed=False),
    LONG_LONG:               TypeAttributes(rank=9, bit_size=64),
    LONG_LONG_INT:           TypeAttributes(rank=9, bit_size=64),
    SIGNED_LONG_LONG:        TypeAttributes(rank=9, bit_size=64),
    SIGNED_LONG_LONG_INT:    TypeAttributes(rank=9, bit_size=64),
    UNSIGNED_LONG_LONG:      TypeAttributes(rank=10, bit_size=64, signed=False),
    UNSIGNED_LONG_LONG_INT:  TypeAttributes(rank=10, bit_size=64, signed=False),
    FLOAT:                   TypeAttributes(rank=11, bit_size=32, floating_point=True),
    DOUBLE:                  TypeAttributes(rank=12, bit_size=64, floating_point=True),
    LONG_DOUBLE:             TypeAttributes(rank=13, bit_size=80, floating_point=True)
}


INTEGRAL_TYPES = tuple(filter(
    lambda t: t is not None, [key if value.integral else None for key, value in TYPE_ATTRIBUTES.items()]))

FLOATING_POINT_TYPES = tuple(filter(
    lambda t: t is not None, [key if value.floating_point else None for key, value in TYPE_ATTRIBUTES.items()]))

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


def get_bit_size(type_specifier_str):

    type_attribute = TYPE_ATTRIBUTES.get(type_specifier_str, None)

    if type_attribute:
        return type_attribute.bit_size
    else:
        raise Exception('Invalid or unknown type ({}).'.format(type_specifier_str))


def is_integral_type(type_specifier_str:str):
    return type_specifier_str in INTEGRAL_TYPES


def is_floating_point_type(type_specifier_str):
    return type_specifier_str in FLOATING_POINT_TYPES


def get_promoted_type(one_type, other_type):
    if one_type == other_type:
        return one_type, CAST_UNAFFECTED
    elif is_integral_type(one_type) and is_integral_type(other_type) or \
         is_floating_point_type(one_type) and is_floating_point_type(other_type):

        return one_type if TYPE_ATTRIBUTES[one_type].rank > TYPE_ATTRIBUTES[other_type].rank else other_type, CAST_UP
    elif is_floating_point_type(one_type):
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


def is_pointer_type(item):
    """
    This method is a band-aid of sorts, since we didn't really design well for pointers. Anyone should feel free to
    put some work into this aspect project.
    """
    pass

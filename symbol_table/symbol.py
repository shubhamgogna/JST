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


class PointerDeclaration(object):
    def __init__(self):
        self.qualifiers = []

    def add_qualifiers(self):
        pass

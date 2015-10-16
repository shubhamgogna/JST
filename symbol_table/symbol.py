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
    def __init__(self, name, identifier='', type=None):
        self.name = name
        self.__type = ''  # int, float, etc.
        self.__identifier = identifier
        self.__pointer_count = 0
        self.__array_dim_count = 0
        self.__array_dims = []
        self.__storage_specifiers = []  # auto, static, extern, etc.
        self.__type_qualifier = None    # const, volatile

    def __repr__(self):
        return self.__type + (self.__pointer_count * '*') + self.__identifier
        # TODO: add arrays and args


class FunctionSymbol(Symbol):
    def __int__(self, identifier, type=None):
        super(FunctionSymbol, self).__init__(identifier, type)
        self.arguments = []


class ConstantSymbol(Symbol):
    def __int__(self, identifier, value, type=None):
        super(ConstantSymbol, self).__init__(identifier, type)
        self.value = value

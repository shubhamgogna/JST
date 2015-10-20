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


class DeclarationSpecifiers(object):
    def __init__(self):
        # List of AUTO, REGISTER, STATIC, EXTERN, TYPEDEF
        self.storage_classes = []
        # List for specifiers to allow for things like 'unsigned int' or 'long double'
        self.type_specifiers = []
        # In GCC, type qualifiers are idempotent
        self.type_qualifiers = set()

    def add_storage_class(self, storage_class_specifier):
        if storage_class_specifier in self.storage_classes:
            raise Exception('Duplication of storage class specifier %s' % storage_class_specifier)
        else:
            self.storage_classes.append(storage_class_specifier)

    def add_type_specifier(self, specifier):
        # TODO There are other cases. Also `long long` is not allowed by the first check.
        # TODO: check for unsigned along with float types and such
        if (specifier is 'long' and 2 <= self.type_specifiers.count('long')) or \
                specifier in self.type_specifiers:
            raise Exception('Too many instances of type specifier \'%s\' in type declaration' % specifier)
        else:
            self.type_specifiers.append(specifier)

    def add_type_qualifier(self, qualifier):
        self.type_qualifiers.add(qualifier)

    def __str__(self):
        storage_class_str = ' '.join(self.storage_classes) if self.storage_classes else ''
        type_qualifier_str = ' '.join(self.type_qualifiers) if self.type_qualifiers else ''
        type_specifier_str = ' '.join(self.type_specifiers) if self.type_specifiers else 'UNKNOWN'

        return '{}, {}, {}'.format(storage_class_str, type_qualifier_str, type_specifier_str)

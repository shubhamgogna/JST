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


class LabelCounter(object):
    next_value = 0
    str_format = '%05d'

    @staticmethod
    def get():
        result = LabelCounter.str_format % LabelCounter.next_value
        LabelCounter.next_value += 1
        return result

    @staticmethod
    def reset():
        LabelCounter.next_value = 0


class GenericTicketCounter(object):
    def __init__(self, prefix=''):
        if prefix == '':
            self.prefix = ''
        else:
            self.prefix = prefix + '_'
        self.next_value = 0

    def get(self):
        ticket = '{prefix}{value:>05}'.format(prefix=self.prefix, value=self.next_value)
        self.next_value += 1
        return ticket

UUID_TICKETS = GenericTicketCounter()
INT_REGISTER_TICKETS = GenericTicketCounter(prefix='ireg')
FLOAT_REGISTER_TICKETS = GenericTicketCounter(prefix='freg')

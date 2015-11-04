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

import unittest
from ticket_counting.ticket_counters import LabelCounter


class TestLabelCounter(unittest.TestCase):
    def setUp(self):
        LabelCounter.reset()

    def test_get_one(self):
        self.assertEqual("00000", LabelCounter.get())

    def test_get_five(self):
        self.assertEqual("00000", LabelCounter.get())
        self.assertEqual("00001", LabelCounter.get())
        self.assertEqual("00002", LabelCounter.get())
        self.assertEqual("00003", LabelCounter.get())
        self.assertEqual("00004", LabelCounter.get())

    def test_get_more_than_ten(self):
        self.assertEqual("00000", LabelCounter.get())
        LabelCounter.next_value = 10
        self.assertEqual("00010", LabelCounter.get())
        self.assertEqual("00011", LabelCounter.get())
        self.assertEqual("00012", LabelCounter.get())

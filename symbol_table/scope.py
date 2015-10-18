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

from bintrees import RBTree
from symbol_table.symbol import Symbol

class Scope(object):

   def __init__(self):
      self.map = RBTree()

   def insert(self, symbol):
      if type(symbol) is Symbol:
         self.map[symbol.identifier] = symbol
      else:
         raise TypeError("'symbol' is not an instance of Symbol.")

   def find(self, name):
      return self.map.get(name, None)

   def size(self):
      return len(self.map)

   def __repr__(self):
      symbols = []
      for key, value in self.map.items():
         symbols.append("  " + key + " : " + repr(value))
      return "\n".join(symbols)

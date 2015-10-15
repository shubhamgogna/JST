from bintrees import RBTree
from symbol_table.symbol import Symbol

class Scope(object):

   def __init__(self):
      self.map = RBTree()

   def insert(self, symbol):
      if type(symbol) is Symbol:
         self.map[symbol.name] = symbol
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

from symbol_table.scope import Scope
from symbol_table.symbol import Symbol


class SymbolTable(object):

   def __init__(self):
      self.table = [Scope()]

   def push(self, scope = None):
      if scope is None:
         scope = Scope()
      if type(scope) is Scope:
         self.table.append(scope)
      else:
         raise TypeError("'scope' is not an instance of Scope.")

   def pop(self):
      return self.table.pop()

   def insert(self, symbol):
      if type(symbol) is Symbol:
         shawdowed = False

         for scope in self.table:
            result = scope.find(symbol.name)
            if result is not None:
               if scope is self.table[-1]:
                  return "EXISTS"
               else:
                  shawdowed = True

         self.table[-1].insert(symbol)
         return "SUCCESS" if not shawdowed else "SHADOWED"
      else:
         raise TypeError("'symbol' is not an instance of Symbol.")

   def find(self, name):
      for scope in reversed(self.table):
         result = scope.find(name)
         if result is not None:
            return result
      return None

   def size(self):
      return len(self.table);

   def __repr__(self):
      scopes = []
      for index, scope in enumerate(self.table):
         scopes.append(repr(index) + '\n' + repr(scope))
      return "\n".join(scopes)

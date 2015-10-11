from symbol_table import SymbolTable
from symbol import Symbol

def assertTrue(name, cond):
   if cond:
      print("[SUCCESS] " + name)
   else:
      print("[FAILURE] " + name)

sym = SymbolTable()
sym.insert(Symbol("A"))
sym.insert(Symbol("B"))
sym.insert(Symbol("C"))

assertTrue("Contains A", sym.find("A") != None)
assertTrue("Does not contain D", sym.find("D") == None)

assertTrue("# Scopes == 1", sym.size() == 1)
sym.pop()
assertTrue("# Scopes == 0 (After pop)", sym.size() == 0)

sym.push()
sym.insert(Symbol("A"))
sym.insert(Symbol("B"))
sym.insert(Symbol("C"))
sym.push()
sym.insert(Symbol("D"))
assertTrue("Symbol EXISTS detected", sym.insert(Symbol("D")) == "EXISTS")
assertTrue("Symbol SHADOWED detected", sym.insert(Symbol("C")) == "SHADOWED")

print(sym)

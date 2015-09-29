/******************************************************************************
@file TesterSymbolTable.hpp
******************************************************************************/
#include <iostream>
#include "SymbolTable.cpp"

void assertTrue(const char* testName, bool result);

void assertFalse(const char* testName, bool result);

bool find(Scope& scope, const std::string& name);

int main()
{
   SymbolTable sym;

   sym.top().insert(Symbol("a"));
   sym.top().insert(Symbol("b"));

   assertTrue("Top contains 'a'",
      find(sym.top(), "a"));
   assertTrue("Top contains 'b'",
      find(sym.top(), "b"));
   assertFalse("Top does not contain 'c'",
      find(sym.top(), "c"));

   assertTrue("SymbolTable size is 1", sym.size() == 1);
   sym.pop();
   assertTrue("SymbolTable size is 0", sym.size() == 0);

   try
   {
      sym.top().insert(Symbol("a"));
   }
   catch(std::out_of_range ex)
   {
      assertTrue("Attempt to access top of empty table throws exception",
         std::string(ex.what()).compare(
         std::string("[ SymbolTable::top() ] Table is empty!")) == 0);
   }

   sym.push();
   sym.top().insert(Symbol("a"));
   sym.top().insert(Symbol("b"));
   sym.push();
   sym.top().insert(Symbol("c"));
   sym.top().insert(Symbol("d"));

   assertTrue("SymbolTable[0] contains 'a'",
      find(sym[0], "a"));
   assertFalse("SymbolTable[0] does not contain 'c'",
      find(sym[0], "c"));
   assertFalse("SymbolTable[1] does not contain 'b'",
      find(sym[1], "b"));
   assertTrue("SymbolTable[1] contains 'd'",
      find(sym[1], "d"));

   try
   {
      sym[1000].insert(Symbol("a"));
   }
   catch(std::out_of_range ex)
   {
      assertTrue("Attempt to access out of range Scope throws exception",
         std::string(ex.what()).compare(
         std::string("[ SymbolTable::operator[] ] Index out of range!")) == 0);
   }

   return 0;
}

void assertTrue(const char* testName, bool result)
{
   std::cout << ((result) ? "[Success] " : "[Failure] ") << testName << std::endl;
}

void assertFalse(const char* testName, bool result)
{
   assertTrue(testName, !result);
}

bool find(Scope& scope, const std::string& name)
{
   Symbol* symbolPtr = scope.find(name);

   if(symbolPtr == nullptr) { return false; }

   return (symbolPtr -> getName()).compare(name) == 0;
}

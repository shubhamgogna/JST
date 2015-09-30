/******************************************************************************
@file TesterSymbolTable.hpp
******************************************************************************/
#include <iostream>
#include "SymbolTable.cpp"

void assertTrue(const char* testName, bool result);

void assertFalse(const char* testName, bool result);

int main()
{
   SymbolTable sym;

   sym.top().insert(Symbol("a"));
   sym.top().insert(Symbol("b"));

   assertTrue("Top contains 'a'",
      sym.top().find("a", nullptr));
   assertTrue("Top contains 'b'",
      sym.top().find("b", nullptr));
   assertFalse("Top does not contain 'c'",
      sym.top().find("c", nullptr));

   assertTrue("SymbolTable size is 1", sym.size() == 1);
   sym.pop(nullptr);
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
      sym[0].find("a", nullptr));
   assertFalse("SymbolTable[0] does not contain 'c'",
      sym[0].find("c", nullptr));
   assertFalse("SymbolTable[1] does not contain 'b'",
      sym[1].find("b", nullptr));
   assertTrue("SymbolTable[1] contains 'd'",
      sym[1].find("d", nullptr));

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

   SymbolTable copy(sym);

   copy.pop(nullptr);
   copy.push();
   copy.push();
   copy.push();
   copy.top().insert(Symbol("Something"));
   copy.top().insert(Symbol("Different"));

   std::cout << sym << std::endl;
   std::cout << copy << std::endl;

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

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

   sym.insert(Symbol("a"));
   sym.insert(Symbol("b"));

   assertTrue("Top contains 'a'", sym.find("a"));
   assertTrue("Top contains 'b'", sym.find("b"));
   assertFalse("Top does not contain 'c'", sym.find("c"));

   assertTrue("SymbolTable size is 1", sym.size() == 1);
   sym.pop();
   assertTrue("SymbolTable size is 0", sym.size() == 0);

   try
   {
      sym.top().insert(Symbol("a"));
   }
   catch(const std::out_of_range& ex)
   {
      assertTrue("Attempt to access top of empty table throws exception",
         std::string(ex.what()).compare(
         std::string("[ SymbolTable::top() ] Table is empty!")) == 0);
   }

   sym.push();
   sym.insert(Symbol("a"));
   sym.insert(Symbol("b"));
   sym.push();
   sym.insert(Symbol("c"));
   sym.insert(Symbol("d"));

   assertTrue("SymbolTable[0] contains 'a'", sym[0].find("a"));
   assertFalse("SymbolTable[0] does not contain 'c'", sym[0].find("c"));
   assertFalse("SymbolTable[1] does not contain 'b'", sym[1].find("b"));
   assertTrue("SymbolTable[1] contains 'd'", sym[1].find("d"));

   assertTrue("Insert 'd' into SymbolTable again",
      sym.insert(Symbol("d")) == SymbolTable::InsertResult::EXISTS);
      assertTrue("Inserted shadowed 'b' into SymbolTable",
      sym.insert(Symbol("b")) == SymbolTable::InsertResult::SHADOWED);

   try
   {
      sym[1000].insert(Symbol("a"));
   }
   catch(const std::out_of_range& ex)
   {
      assertTrue("Attempt to access out of range Scope throws exception",
         std::string(ex.what()).compare(
         std::string("[ SymbolTable::operator[] ] Index out of range!")) == 0);
   }

   SymbolTable copy(sym);

   copy.pop();
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

/******************************************************************************
@file SymbolTable.cpp
******************************************************************************/
#ifndef SYMBOL_TABLE_IMPL
#define SYMBOL_TABLE_IMPL

#include "SymbolTable.hpp"

SymbolTable::SymbolTable()
{
   table.push_back(Scope());
}

SymbolTable::SymbolTable(const SymbolTable& src)
{
   std::vector<Scope>::const_iterator it;

   table.clear();

   for(it = src.table.begin(); it != src.table.end(); ++it)
   {
      table.push_back(*it);
   }
}


const SymbolTable& SymbolTable::operator=(const SymbolTable& src)
{
   if(&src == this) { return src; }

   std::vector<Scope>::const_iterator it;

   table.clear();

   for(it = src.table.begin(); it != src.table.end(); ++it)
   {
      table.push_back(*it);
   }
}

SymbolTable::~SymbolTable()
{
   table.clear();
}

bool SymbolTable::insert(const Symbol& symbol)
{
   std::pair<std::string, Symbol> elemToInsert(symbol.getName(), symbol);

   // TODO
   // Symbol can be shadowed. Check can be done here and an appropriate
   // status code can be returned.

   table.back().insert(elemToInsert);
}

bool SymbolTable::find(const std::string& name, Symbol& symbol)
{
   std::vector<Scope>::iterator it;

   for(it = table.begin(); it != table.end(); ++it)
   {
      Scope::iterator elemIter = it -> find(name);

      if(elemIter != it -> end())
      {
         symbol = elemIter -> second;
         return true;
      }
   }

   return false;
}

void SymbolTable::pushScope()
{
   table.push_back(Scope());
}

bool SymbolTable::popScope(Scope& scope)
{
   if(table.empty()) { return false; }

   scope = table.back();
   table.pop_back();

   return true;
}

bool SymbolTable::print(const size_t& level)
{
   if(table.empty() || level < 0 || level >= table.size())
   {
      return false;
   }

   Scope& scope = table[level];
   Scope::iterator it;

   std::cout << "Level " << level << std::endl;
   for(it = scope.begin(); it != scope.end(); ++it)
   {
      std::cout << "  " << (it -> first)
         << ": " << (it -> second)
         << std::endl;
   }

   return true;
}

size_t SymbolTable::size()
{
   return table.size();
}

#endif

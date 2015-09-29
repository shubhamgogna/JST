/******************************************************************************
@file SymbolTable.cpp
******************************************************************************/
#ifndef SYMBOL_TABLE_IMPL
#define SYMBOL_TABLE_IMPL

#include "SymbolTable.hpp"

SymbolTable::SymbolTable()
{
   table.push_back(Scope(0));
}

SymbolTable::SymbolTable(const SymbolTable& src)
{
   std::vector<Scope>::const_iterator it;

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

void SymbolTable::push()
{
   Scope newScope(table.size());

   table.push_back(newScope);
}

Scope* SymbolTable::pop()
{
   if(table.empty()) { return nullptr; }

   Scope* scopePtr = &(table.back());

   table.pop_back();

   return scopePtr;
}

Scope& SymbolTable::operator[](int index)
{
   if(table.empty() || index < 0 || index >= table.size())
   {
      throw std::out_of_range("[ SymbolTable::operator[] ] Index out of range!");
   }

   return table[index];
}

Scope& SymbolTable::top()
{
   if(table.empty())
   {
      throw std::out_of_range("[ SymbolTable::top() ] Table is empty!");
   }

   return table.back();
}

size_t SymbolTable::size()
{
   return table.size();
}

std::ostream& operator<<(std::ostream& stream, const SymbolTable& symbolTable)
{
   std::vector<Scope>::const_iterator it;

   for(it = symbolTable.table.begin(); it != symbolTable.table.end(); ++it)
   {
      stream << *it << std::endl;
   }

   return stream;
}

#endif

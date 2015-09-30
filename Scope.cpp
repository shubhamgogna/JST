/******************************************************************************
@file Scope.cpp
******************************************************************************/
#ifndef SCOPE_IMPL
#define SCOPE_IMPL

#include "Scope.hpp"

Scope::Scope(int level) : level(level) {}

Scope::Scope(const Scope& src) : level(src.level)
{
   std::map<std::string, Symbol>::const_iterator it;

   for(it = src.map.begin(); it != src.map.end(); ++it)
   {
      map.insert(*it);
   }
}

const Scope& Scope::operator=(const Scope& src)
{
   if(&src == this) { return src; }

   if(src.level != level)
   {
      throw "[ Scope::operator=() ] Levels do not match!";
   }

   std::map<std::string, Symbol>::const_iterator it;

   map.clear();

   for(it = src.map.begin(); it != src.map.end(); ++it)
   {
      map.insert(*it);
   }

   return *this;
}

Scope::~Scope()
{
   map.clear();
}

void Scope::insert(const Symbol& symbol)
{
   std::pair<std::string, Symbol> elemToInsert(symbol.getName(), symbol);

   map.insert(elemToInsert);
}

bool Scope::find(const std::string& name, Symbol* dest)
{
   std::map<std::string, Symbol>::iterator it = map.find(name);

   if(it != map.end())
   {
      if(dest != nullptr)
      {
         (*dest) = (it -> second);
      }

      return true;
   }

   return false;
}

int Scope::getLevel() const
{
   return level;
}

size_t Scope::size() const
{
   return map.size();
}

std::ostream& operator<<(std::ostream& stream, const Scope& scope)
{
   std::map<std::string, Symbol>::const_iterator it;

   stream << "Level " << scope.level << std::endl;

   for(it = scope.map.begin(); it != scope.map.end(); ++it)
   {
      stream << "  " << (it -> first) << " : " << (it -> second) << std::endl;
   }

   return stream;
}

#endif

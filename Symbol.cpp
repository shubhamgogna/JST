/******************************************************************************
@file Symbol.cpp
******************************************************************************/
#ifndef SYMBOL_IMPL
#define SYMBOL_IMPL

#include "Symbol.hpp"

Symbol::Symbol(const std::string& name) : name(name) {}

Symbol::Symbol(const Symbol& src) : name(src.name) {}

const Symbol& Symbol::operator=(const Symbol& src)
{
   if(&src == this) { return src; }

   // Reserved for future non-const member variables

   return *this;
}

Symbol::~Symbol()
{
   // Reserved for future non-const member variables
}

/**
@return Identifier
**/
const std::string& Symbol::getName()
{
   return name;
}

std::ostream& operator<<(std::ostream& stream, const Symbol& symbol)
{
   stream << symbol.name;
   return stream;
}

#endif

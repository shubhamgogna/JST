/******************************************************************************
@file Symbol.cpp
******************************************************************************/
#ifndef SYMBOL_IMPL
#define SYMBOL_IMPL

#include "Symbol.hpp"

Symbol::Symbol(const Symbol& src)
{
   identifier = src.identifier;
}

const Symbol& Symbol::operator=(const Symbol& src)
{
   if(&src == this) { return src; }

   identifier = src.identifier;
}

Symbol::~Symbol()
{
   identifier.clear();
}

/**
@param[in] name String itentifier for the symbol
@param[in] symbol Data for the symbol
@return If insert succeeded or not
**/
bool Symbol::setName(const std::string& name)
{
   identifier = name;
}

/**
@return Identifier
**/
const std::string& Symbol::getName()
{
   return identifier;
}

std::ostream& operator<<(std::ostream& stream, const Symbol& symbol)
{
   stream << symbol.identifier;
   return stream;
}

#endif

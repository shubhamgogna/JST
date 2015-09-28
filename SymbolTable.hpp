/******************************************************************************
@file SymbolTable.hpp
******************************************************************************/
#ifndef SYMBOL_TABLE_DEF
#define SYMBOL_TABLE_DEF

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <stddef.h>
#include "Symbol.cpp"
using namespace std;

class SymbolTable
{
   typedef map<string, Symbol> Scope;

   public:
      SymbolTable();
      SymbolTable(const SymbolTable&);
      const SymbolTable& operator=(const SymbolTable&);
      ~SymbolTable();

      /**
      @param[in] name String itentifier for the symbol
      @param[in] symbol Data for the symbol
      @return If insert succeeded or not
      **/
      bool insertSymbol(const string& name, const Symbol& symbol);

      /**
      @param[in] name String itentifier for the symbol
      @param[out] symbol Data for the symbol
      @return If lookup succeeded or not
      **/
      bool findSymbol(const string& name, Symbol& symbol);

      /**
      @return If a new empty scope was pushed
      **/
      bool pushScope();

      /**
      @param[out] scope Scope containing all identifiers and their Symbols
      @return If a scope was popped or not
      **/
      bool popScope(Scope& scope);

      /**
      @param[in] level Scope level to print
      @return If scope at level exists or not
      **/
      bool printScope(const size_t& level);

      /**
      @return Total number of levels (scopes) in the table
      **/
      size_t size();

   private:
      vector<Scope> table;
};

#endif

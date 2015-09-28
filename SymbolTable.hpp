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

class SymbolTable
{
   typedef std::map<std::string, Symbol> Scope;

   public:
      SymbolTable();
      SymbolTable(const SymbolTable&);
      const SymbolTable& operator=(const SymbolTable&);
      ~SymbolTable();

      /**
      Inserts a symbol in the most recent (last) scope.

      @param[in] symbol Symbol to add.
      @return True if the insert was successful. False if not.
      **/
      bool insert(const Symbol& symbol);

      /**
      Finds a symbol in the all scopes with the passed name. The search
      begins in the most recent (last) scope.

      @param[in] name Name of the symbol.
      @param[out] symbol Symbol that was found (unmodified if not found).
      @return True if symbol was found. False if not.
      **/
      bool find(const std::string& name, Symbol& symbol);

      /**
      Pushes an empty scope onto the table.
      **/
      void pushScope();

      /**
      Pops the most recent (last) scope off the table. Scopes are
      typedef-ed map<string, Symbol> and can be accessed as such.

      @param[out] scope Scope that was found (unmodified if not found).
      @return True if table was not empty. False if table was empty.
      **/
      bool popScope(Scope& scope);

      /**
      Prints the specified scope to STDOUT.

      @param[in] level Level of scope to print. (Last = size() - 1)
      @return True if printed. False if table is empty or level
      was out of bounds.
      **/
      bool print(const size_t& level);

      /**
      @return Total number of levels (scopes) in the table.
      **/
      size_t size();

   private:
      std::vector<Scope> table;
};

#endif

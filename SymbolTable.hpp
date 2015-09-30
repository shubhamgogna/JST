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
#include "Scope.cpp"

class SymbolTable
{
   public:
      SymbolTable();
      SymbolTable(const SymbolTable&);
      const SymbolTable& operator=(const SymbolTable&);
      ~SymbolTable();

      /**
      Pushes an empty scope onto the table.
      **/
      void push();

      /**
      Pops the most recent (last) scope off the table.

      @param[out] dest Pointer to the Scope to copy to. If
      this is 'nullptr', the copy will not be performed.
      @return True if popped and false if not.
      **/
      bool pop(Scope* dest);

      /**
      @param[in] index Level of Scope to access.
      @returns Reference to the index-th Scope.
      @throws std::out_of_range exceptions when index is out of range.
      **/
      Scope& operator[](size_t index);

      /**
      @return Reference to the last (top of the stack) Scope.
      @throws std::out_of_range exceptions when index is out of range.
      **/
      Scope& top();

      /**
      @return Total number of levels (scopes) in the table.
      **/
      size_t size();

      /**
      Output stream operator overload.

      @param[in] stream Stream to output to.
      @param[in] scope SymbolTable to print.
      @return The same 'stream' object that was passed into the function.
      **/
      friend std::ostream& operator<<(std::ostream& stream,
         const SymbolTable& symbolTable);

   private:
      std::vector<Scope> table;
};

#endif

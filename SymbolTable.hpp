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
      Pushes an empty scope onto the stack.
      **/
      void push();

      /**
      Pops the most recent (top) scope off the stack.

      @param[out] dest Pointer to the Scope to copy to. If
      this is 'nullptr', the copy will not be performed.
      @return True if popped and false if not.
      **/
      bool pop(Scope* dest);

      /**
      @param[int] dest Pointer to the Scope to copy to. If
      this is 'nullptr', the copy will not be performed.
      @return InsertResult enum.
      **/
      InsertResult insert(const Symbol& symbol);

      /**
      This method will search the top scope first before
      searching the rest of the stack.

      @param[in] name Name of the symbol.
      @param[out] dest Pointer to the Symbol to copy to. If
      this is 'nullptr', the copy will not be performed.
      @return True if found and false if not.
      **/
      bool find(const std::string& name, Symbol* dest);

      /**
      The top of the stack is at [size() - 1]. The bottom of the stack
      is at [0].

      @param[in] index Level of Scope to access.
      @returns Reference to the index-th Scope.
      @throws std::out_of_range exception when index is out of range.
      **/
      Scope& operator[](size_t index);

      /**
      @return Reference to the Scope at the top of the stack.
      @throws std::out_of_range exception when the stack is empty.
      **/
      Scope& top();

      /**
      @return Number of Scopes in the stack.
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

      /**
      Enums for the result of SymbolTable::insert().
      **/
      enum class InsertResult
      {
         /* Inserted with no errors. */
         SUCCESS,

         /* Not inserted because symbol already exists in the top scope. */
         EXISTS,

         /* Inserted into the top scope, but exists in previous scopes. */
         SHADOWED
      };

   private:
      std::vector<Scope> table;
};

#endif

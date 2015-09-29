/******************************************************************************
@file Scope.hpp
******************************************************************************/
#ifndef SCOPE_DEF
#define SCOPE_DEF

#include <iostream>
#include <string>

class Scope
{
   public:
      Scope(int level);
      Scope(const Scope& src);
      const Scope& operator=(const Scope&);
      ~Scope();

      /**
      @param symbol Symbol to add (or overwrite if one exists).
      **/
      void insert(const Symbol& symbol);

      /**
      @param name Name of the symbol.
      @return A pointer to the Symbol which will be 'nullptr' if not found.
      **/
      Symbol* find(const std::string& name);

      /**
      @return Level of the scope.
      **/
      int getLevel() const;

      /**
      @return Number of Symbols in the scope.
      **/
      size_t size() const;

      /**
      Output stream operator overload.

      @param[in] stream Stream to output to.
      @param[in] scope Scope to print.
      @return The same 'stream' object that was passed into the function.
      **/
      friend std::ostream& operator<<(std::ostream& stream, const Scope& scope);

   private:
      const int level;
      std::map<std::string, Symbol> map;
};

#endif

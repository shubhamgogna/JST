/******************************************************************************
@file Symbol.hpp
******************************************************************************/
#ifndef SYMBOL_DEF
#define SYMBOL_DEF

#include <iostream>
#include <string>

class Symbol
{
   public:
      Symbol(const std::string& name);
      Symbol(const Symbol& src);
      const Symbol& operator=(const Symbol&);
      ~Symbol();

      /**
      @return Name of the symbol.
      **/
      const std::string& getName();

      /**
      Output stream operator overload.

      @param[in] stream Stream to output to.
      @param[in] symbol Symbol to print.
      @return The same 'stream' object that was passed into the function.
      **/
      friend std::ostream& operator<<(std::ostream& stream, const Symbol& symbol);

   private:
      const std::string name;
};

#endif

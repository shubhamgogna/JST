/******************************************************************************
@file Symbol.hpp
******************************************************************************/
#ifndef SYMBOL_DEF
#define SYMBOL_DEF

#include <string>

class Symbol
{
	public:
		Symbol() {};
		Symbol(const Symbol&);
		const Symbol& operator=(const Symbol&);
		~Symbol();

		/**
		@param[in] name String itentifier for the symbol
		@param[in] symbol Data for the symbol
		@return If insert succeeded or not
		**/
		bool setName(const std::string&);

		/**
		@return Identifier
		**/
		const std::string& getName();

	private:
		std::string identifier;

		friend std::ostream& operator<<(std::ostream&, const Symbol&);
};

#endif

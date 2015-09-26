/******************************************************************************
@file Symbol.cpp
******************************************************************************/
#include <string>
using namespace std;

class Symbol
{
	public:
		Symbol();
		Symbol(const Symbol&);
		Symbol& operator=(const Symbol&);
		~Symbol();

		/**
		@param[in] name String itentifier for the symbol
		@param[in] symbol Data for the symbol
		@return If insert succeeded or not
		**/
		bool setName(const string&);

		/**
		@return Identifier
		**/
		const string& getName();

	private:
		string identifier;
};

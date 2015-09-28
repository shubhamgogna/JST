/******************************************************************************
@file SymbolTable.hpp
******************************************************************************/
#ifndef SYMBOL_TABLE_IMPL
#define SYMBOL_TABLE_IMPL

#include "SymbolTable.h"

// 'using' NEEDED?
using namespace std;

SymbolTable::SymbolTable()
{
	// Are there any symbols that should be inserted by default?
	// If so, they should be placed in a map here before
	// being pushed into the vector

	table.push_back(map<string, Symbol>());
}

SymbolTable::SymbolTable(const SymbolTable& src)
{
	table.clear();

	vector<map<string, Symbol>::iterator it;
	for(it = src.table.begin(); it != src.table.end(); ++it)
	{
		table.push_back(*it);
	}
}


SymbolTable::SymbolTable& operator=(const SymbolTable& src)
{
	if(src == NULL || &src == this) { return src; }

	table.clear();

	vector<map<string, Symbol>::iterator it;
	for(it = src.table.begin(); it != src.table.end(); ++it)
	{
		table.push_back(*it);
	}
}

SymbolTable::~SymbolTable()
{
	table.clear();
}

/**
@param[in] name String itentifier for the symbol
@param[in] symbol Data for the symbol
@return If insert succeeded or not
**/
bool SymbolTable::insertSymbol(const string& name, const Symbol& symbol)
{
	pair<string, Symbol> elemToInsert(name, symbol);

	table.back().insert(elemToInsert);
}

/**
@param[in] name String itentifier for the symbol
@param[out] symbol Data for the symbol
@return If lookup succeeded or not
**/
bool SymbolTable::findSymbol(const string& name, Symbol& symbol)
{
	vector<map<string, Symbol>::iterator it;

	for(it = src.table.begin(); it != src.table.end(); ++it)
	{
		map<string, Symbol>::iterator elemIter = it -> find(name);

		if(elemIter != it -> end())
		{
			symbol = *elemIter;
			return true;
		}

		// TODO It's possible a variable is being shadowed.
		// Maybe return an ENUM in that case?
	}

	return false;
}

/**
@return If a new empty scope was pushed
**/
bool SymbolTable::pushScope()
{
	table.push_back(map<string, Symbol>());
}

/**
@param[out] scope Scope containing all identifiers and their Symbols
@return If a scope was popped or not
**/
bool SymbolTable::popScope(map<string, Symbol>& scope)
{
	if(table.empty()) { return false; }

	scope = table.back();
	table.pop_back();

	return true;
}

/**
@param[in] level Scope level to print
@return If scope at level exists or not
**/
bool SymbolTable::printScope(const size_t& level)
{
	if(table.empty()) { return false; }

	map<string, Symbol>& closestScope = table.back();
	map<string, Symbol>::iterator it;

	for(it = closestScope.begin(); it != closestScope.end(); ++it)
	{
		cout << (it -> first) << ": " << (it -> second) << endl;
	}

	return true;
}

/**
@return Total number of levels (scopes) in the table
**/
size_t SymbolTable::size()
{
	return table.size();
}

#endif

/******************************************************************************
@file TesterSymbolTable.hpp
******************************************************************************/
#include <iostream>
#include "SymbolTable.cpp"

void testFind(SymbolTable& sym, const std::string& name);

int main()
{
	SymbolTable sym;
	std::map<std::string, Symbol> tempScope;

	std::cout << "[Testing] insert() and pushScope()" << std::endl;

	sym.insert(Symbol("a"));
	sym.insert(Symbol("b"));
	sym.pushScope();

	sym.insert(Symbol("c"));
	sym.insert(Symbol("d"));
	sym.pushScope();

	sym.insert(Symbol("e"));
	sym.insert(Symbol("f"));
	sym.pushScope();

	sym.insert(Symbol("c"));

	std::cout << "\n[Testing] print()" << std::endl;

	for(int i = sym.size() - 1; i >= 0; --i)
	{
		sym.print(i);
	}

	std::cout << "\n[Testing] find()" << std::endl;

	testFind(sym, std::string("a"));
	testFind(sym, std::string("b"));
	testFind(sym, std::string("c"));
	testFind(sym, std::string("d"));
	testFind(sym, std::string("e"));
	testFind(sym, std::string("f"));
	testFind(sym, std::string("g"));

	std::cout << "\n[Testing] popScope()" << std::endl;

	sym.popScope(tempScope);
	sym.popScope(tempScope);

	std::cout << "\n[Testing] print()" << std::endl;

	for(int i = sym.size() - 1; i >= 0; --i)
	{
		sym.print(i);
	}

	return 0;
}

void testFind(SymbolTable& sym, const std::string& name)
{
	Symbol temp("?");

	std::cout << "Does table contain '" << name << "'? "
		<< ((sym.find(name, temp)) ? "Yes" : "No") << std::endl;
}

# This file is part of JST.
#
# JST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# JST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with JST.  If not, see <http://www.gnu.org/licenses/>.

import math

from ast.base_ast_node import BaseAstNode
from utils import type_utils
from utils import operator_utils
from ticket_counting.ticket_counters import LABEL_TICKETS
from ticket_counting.ticket_counters import INT_REGISTER_TICKETS
from ticket_counting.ticket_counters import FLOAT_REGISTER_TICKETS
from tac.tac_generation import *

# Setup register allocation table and address table to keep track of where vars
# are declared so can be accessed throughout each node.
register_allocation_table = {}


##
# Node for the declaration of an array using the symbol, dimensions, and qualifiers.
##
class ArrayDeclaration(BaseAstNode):
    """
    Requires: Type and dimensional information from the symbol build in the symbol table.
    Output:   Probably no direct output in the form of temporary registers, but the memory assigned for the
              thing should be recorded somewhere.
    """

    def __init__(self, symbol, dimensions, dim_qualifiers, **kwargs):
        super(ArrayDeclaration, self).__init__(**kwargs)

        self.dimensions = dimensions
        self.dim_qualifiers = dim_qualifiers

        self.symbol = symbol

    def name(self, arg=None):
        # raise NotImplementedError('Add the array dimensions and the Symbol to the array declaration node.')
        array_dims = '[' + ']['.join([str(dimension) for dimension in self.dimensions]) + ']'
        arg = self.symbol.type_str() + array_dims + ' ' + self.symbol.identifier
        return super(ArrayDeclaration, self).name(arg)

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        # Single integer and char declaration should take up 1 word (4 bytes)
        # Arrays need padding at the end to finish the word
        byte_size = int(math.ceil(self.symbol.size_in_bytes() / 4) * 4)
        output = [SUBIU('StackPointer', 'StackPointer', byte_size)]
        return output


##
# Node for referencing an array through subscripts.
##
class ArrayReference(BaseAstNode):
    """
    Requires: Information about the array being dereferenced and the results of any expressions indicating the
              indices where dereferencing is occuring, stored in temporary registers. An indication of if an rvalue
              or lvalue should be produced should be given (since an lvalue likely means a pointer should be returned
              vs. a raw value).
    Output:   In the case of an lvalue, a temporary register with the address of the memory of the element of interest,
              in the case of an rvalue, a temporary register containing the actual value of the element.
    """

    def __init__(self, symbol, subscripts=None, **kwargs):
        super(ArrayReference, self).__init__(**kwargs)

        self.symbol = symbol
        self.subscripts = subscripts if subscripts else []

    def get_resulting_type(self):
        """
        For interface compliance with the other expression nodes.
        """
        type_str = self.symbol.get_type_str()
        first_open_bracket = type_str.index('[')
        return type_str[:first_open_bracket]

    @property
    def immutable(self):
        return self.symbol.immutable

    def check_subscripts(self):
        if len(self.symbol.array_dims) != len(self.subscripts):
            return False, 'Symbol has {} dimensions, but only {} were provided.'\
                .format(len(self.symbol.array_dims), len(self.subscripts))
        return True, None

    def name(self, arg=None):
        return super(ArrayReference, self).name(arg=self.symbol.identifier)

    @property
    def children(self):
        children = []
        children.extend(self.subscripts)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

        # get memory location of array

        # calculate memory offset based on subscripts

        # return memory location


class Assignment(BaseAstNode):
    """
    Requires: An lvalue register produced by the expression of the thing being assigned to and an rvalue register
              containing the value being assigned.
    Output:   A temporary rvalue register that contains the value that was assigned. Perhaps a slight optimization would
              be to just return that rvalue register that the RHS gave this node to start with?
    """
    def __init__(self, operator, lvalue, rvalue, **kwargs):
        super(Assignment, self).__init__(**kwargs)

        self.operator = operator
        self.lvalue = lvalue
        self.rvalue = rvalue

    def get_resulting_type(self):
        return self.lvalue.get_resulting_type()

    def name(self, arg=None):
        return super(Assignment, self).name(arg=operator_utils.operator_to_name(self.operator))

    @property
    def children(self):
        children = []
        children.append(self.lvalue)
        children.append(self.rvalue)
        return tuple(children)

    def to_3ac(self, include_source=False):
        output = []

        # get memory address of lvalue by calling to3ac on lvalue
        left = self.lvalue.to_3ac()
        lval = left['register']
        if '3ac' in left:
            output.extend(left['3ac'])

        # get memory address of rvalue by calling to3ac on rvalue
        right = self.rvalue.to_3ac()
        rval = right['register']
        if '3ac' in right:
            output.extend(right['3ac'])

        # TODO: Fix this??
        # # load rvalue into register - does this need to happen or not?
        # is there a 3ac command for this?
        # value = register_allocation_table[rval]

        # TODO: Fix this??
        # call 3ac instruction to load value of rval's reg to lval's memory location
        # Note: not sure how this assign thing is supposed to be used....
        #       right now both are registers, should the rvalue be the actual value? I don't think so but not sure
        output.append(ASSIGN(rval, lval, rval))

        return output


# TODO (Shubham) The return type needs to be explicitly stated here.
class BinaryOperator(BaseAstNode):
    """
    Requires: Two rvalue registers that contain the values to be operated on.
    Output:   An rvalue register containing the value of the result of the operation.
    """
    def __init__(self, operator, lvalue, rvalue, **kwargs):
        super(BinaryOperator, self).__init__(**kwargs)

        self.operator = operator
        self.lvalue = lvalue
        self.rvalue = rvalue

    def get_resulting_type(self):
        lvalue_type = self.lvalue.get_resulting_type()
        rvalue_type = self.rvalue.get_resulting_type()

        # TODO (Shubham) We may just need to make a table according to operations
        # For example:
        #   Comparison operators always result in an integral type even though operands can be non-integrals
        #   Shift operators require an int on the left (right can be downcast to an int), so they result in an 'int'
        #   +/-/*/div operations result in a highest precision type
        #   Mod operation always has to return an integral type
        #   Bitwise AND, OR, and XOR require integers and have to return an integral type
        resulting_type, cast_result = type_utils.get_promoted_type(lvalue_type, rvalue_type)

        return resulting_type

    def name(self, arg=None):
        return super(BinaryOperator, self).name(arg=operator_utils.operator_to_name(self.operator))

    @property
    def children(self):
        children = []
        children.append(self.lvalue)
        children.append(self.rvalue)
        return tuple(children)

    def to_3ac(self, include_source=False):
        # raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

        output = []

        # get memory address of lvalue by calling to3ac on lvalue
        left = self.lvalue.to_3ac()
        lval = left['register']
        if '3ac' in left:
            output.extend(left['3ac'])

        # load lvalue into register  - does this need to happen or not?

        # get memory address of rvalue by calling to3ac on rvalue
        right = self.rvalue.to_3ac()
        rval = right['register']
        if '3ac' in right:
            output.extend(right['3ac'])

        # load rvalue into register - does this need to happen or not?

        # get temporary register
        # TODO: Add in checking for int or float so can pull correct ticket
        reg = INT_REGISTER_TICKETS.get()

        #TODO: NEED TO ADD IN OPTIONS BASED ON TYPE OF TICKET PULLED HERE
        # determine operator type and call correct 3ac instruction with registers
        if self.operator == '+':
            output.append(ADD(reg, lval, rval))
        if self.operator == '-':
            output.append(SUB(reg, lval, rval))
        if self.operator == '*':
            output.append(MUL(reg, lval, rval))
        if self.operator == '/':
            output.append(DIV(reg, lval, rval))
        if self.operator == '%':
            output.append(MOD(reg, lval, rval))
        if self.operator == '>>':
            # output.append(   (reg, lval, rval))
            # TODO: what function is this?
             raise NotImplementedError('Please implement the {} binary operator to3ac method.'.format(self.operator))
        if self.operator == '<<':
            # output.append(   (reg, lval, rval))
            # TODO: what function is this?
             raise NotImplementedError('Please implement the {} binary operator to3ac method.'.format(self.operator))
        if self.operator == '<':
            output.append(LT(reg, lval, rval))
        if self.operator == '<=':
            output.append(LE(reg, lval, rval))
        if self.operator == '>':
            output.append(GT(reg, lval, rval))
        if self.operator == '>=':
            output.append(GE(reg, lval, rval))
        if self.operator == '==':
            output.append(EQ(reg, lval, rval))
        if self.operator == '!=':
            output.append(NE(reg, lval, rval))
        if self.operator == '&':
            # output.append(  (reg, lval, rval))
            # TODO: what function is this?
             raise NotImplementedError('Please implement the {} binary operator to3ac method.'.format(self.operator))
        if self.operator == '|':
            # output.append(   (reg, lval, rval))
            # TODO: what function is this?
             raise NotImplementedError('Please implement the {} binary operator to3ac method.'.format(self.operator))
        if self.operator == '^':
            # output.append(    (reg, lval, rval))
            # TODO: what function is this?
             raise NotImplementedError('Please implement the {} binary operator to3ac method.'.format(self.operator))
        if self.operator == '&&':
            # output.append(  (reg, lval, rval))
            # TODO: what function is this?
             raise NotImplementedError('Please implement the {} binary operator to3ac method.'.format(self.operator))
        if self.operator == '||':
            # output.append(   (reg, lval, rval))
            # TODO: what function is this?
             raise NotImplementedError('Please implement the {} binary operator to3ac method.'.format(self.operator))

        # TODO: since don't have the value since not calculating anything, can't store it to the table yet
        # register_allocation_table[reg] = value

        return {'3ac': output, 'register': reg}


class Cast(BaseAstNode):
    """
    Requires: An rvalue of the value to be casted.
    Output:   An rvalue register containing the casted value (which might have changed over the course of the casting
              process).
    """
    def __init__(self, to_type, expression, **kwargs):
        super(Cast, self).__init__(**kwargs)

        self.to_type = to_type
        self.expression = expression

    def get_resulting_type(self):
        return self.to_type

    def name(self, arg=None):
        return super(Cast, self).name(self.to_type)

    @property
    def children(self):
        children = []
        # since to_type is like 'int' its an attribute, not a child
        # children.append(self.to_type)
        children.append(self.expression)
        return tuple(children)

    def to_3ac(self, include_source=False):
        output = []

        # get correct casted value
        if self.to_type == 'int':
            value = int(self.expression.value)
        if self.to_type == 'float':
            value = float(self.expression.value)
        if self.to_type == 'char':
            # value = char(self.expression)
            raise(NotImplementedError('Please implement char casting in p_cast_expressoin_2'))

        # load casted value into register and return register
        if type(value) is int:
            reg = INT_REGISTER_TICKETS.get()
            output.append(ADDI(reg, value, 0))
        if type(value) is float:
            reg = FLOAT_REGISTER_TICKETS.get()
            output.append(ADD(reg, value, 0))

        register_allocation_table[reg] = value

        return {'3ac': output, 'register': reg}


class CompoundStatement(BaseAstNode):
    """
    Requires: None.
    Output:   None.

    It is unlikely that this node will produce any 3AC, but will simply amalgamate the code generated by its children.
    """
    def __init__(self, declaration_list=None, statement_list=None, **kwargs):
        super(CompoundStatement, self).__init__(**kwargs)

        self.declaration_list = declaration_list
        self.statement_list = statement_list

    @property
    def children(self):
        children = []
        if self.declaration_list is not None:
            children.extend(self.declaration_list)
        if self.statement_list is not None:
            children.extend(self.statement_list)
        return tuple(children)

    def to_3ac(self, include_source=False):
        output = []

        # gen 3ac for declaration_list
        if self.declaration_list is not None:
            for item in self.declaration_list:
                output.extend(item.to_3ac())

        # gen 3ac for statement_list
        for item in self.statement_list:
            output.extend(item.to_3ac())

        return output


class Declaration(BaseAstNode):
    """
    Requires: The symbol information of the declaration.
    Output:   Probably no direct output in the form of temporary registers, but the memory assigned for the
              thing should be recorded somewhere.
    """
    def __init__(self, symbol, initialization_value=None, **kwargs):
        super(Declaration, self).__init__(**kwargs)

        self.symbol = symbol
        self.initialization_value = initialization_value

    def sizeof(self):
        return type_utils.type_size_in_bytes(self.symbol.type_str())

    def name(self, arg=None):
        arg = self.symbol.type_str() + ' ' + self.symbol.identifier
        return super(Declaration, self).name(arg)

    @property
    def children(self):
        children = []
        if self.initialization_value is not None:
            children.append(self.initialization_value)
        return tuple(children)

    def to_3ac(self, include_source=False):
        # Single integer and char declaration should take up 1 word (4 bytes)
        byte_size = int(math.ceil(self.symbol.size_in_bytes() / 4) * 4)
        output = [SUBIU('StackPointer', 'StackPointer', byte_size)]
        return output


##
# Root node of the AST.
##
class FileAST(BaseAstNode):
    """
    Requires: None.
    Output:   None.

    Simply amalgamates 3AC. Might not produce any code other than standard boilerplate.
    """
    def __init__(self, external_declarations=None, **kwargs):
        super(FileAST, self).__init__(**kwargs)

        self.external_declarations = external_declarations if external_declarations else []

    @property
    def children(self):
        childrens = []
        childrens.extend(self.external_declarations)
        return tuple(childrens)

    def to_3ac(self, include_source=False):
        # raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

        # gen 3ac for external declarations
        output = []
        for item in self.external_declarations:
            output.extend(item.to_3ac())

        for item in output:
            print(item)

        return output

    def to_graph_viz_str(self):
        return 'digraph {\n' + super(FileAST, self).to_graph_viz_str() + '}'


class FunctionCall(BaseAstNode):
    """
    Requires: An rvalue for each parameter that this node will then take appropriate actions to cast and copy into the
              activation frame.
    Output:   An rvalue in a temporary register. Take care to copy the value from the value that is stored in the MIPS
              designated return value register.
    """
    def __init__(self, function_symbol, arguments=None, **kwargs):
        super(FunctionCall, self).__init__(**kwargs)

        self.function_symbol = function_symbol
        self.arguments = arguments if arguments else []

    def get_resulting_type(self):
        return self.function_symbol.get_resulting_type()

    def name(self, arg=None):
        return super(FunctionCall, self).name(arg=self.function_symbol.identifier)

    @property
    def children(self):
        children = []
        children.extend(self.arguments)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class FunctionDeclaration(BaseAstNode):
    """
    Requires: The symbol information of the declaration.
    Output:   Nothing direct
    """
    def __init__(self, function_symbol, arguments=None, **kwargs):
        super(FunctionDeclaration, self).__init__(**kwargs)

        self.function_symbol = function_symbol

        self.identifier = function_symbol.identifier
        self.arguments = arguments if arguments else []

    def name(self, arg=None):
        arg = self.function_symbol.get_resulting_type() + ' ' + self.identifier
        return super(FunctionDeclaration, self).name(arg)

    @property
    def children(self):
        children = []
        children.extend(self.arguments)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

        # TODO: does this need any space in memory? No right?


class FunctionDefinition(BaseAstNode):
    """
    Requires: Information about its params and declarations so that it can build its activation frame appropriately
    Output:   Nothing other than the 3AC
    """

    def __init__(self, function_symbol, identifier, arguments, body, **kwargs):
        super(FunctionDefinition, self).__init__(**kwargs)

        self.function_symbol = function_symbol
        self.identifier = identifier
        self.body = body
        self.arguments = arguments if arguments else []

    def name(self, arg=None):
        arg = self.function_symbol.get_resulting_type() + ' ' + self.identifier
        return super(FunctionDefinition, self).name(arg)

    @property
    def children(self):
        children = []
        children.extend(self.arguments)
        if self.body:
            children.append(self.body)
        return tuple(children)

    def to_3ac(self, include_source=False):
        # raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

        # get label for function i.e. function name
        label = LABEL_TICKETS.get()

        # dump label
        label = LABEL(label)
        output = [label]

        # get 3ac for arguments
        for item in self.arguments:
            output.extend(item.to_3ac())
            # print(output)

        # gen 3ac for body
        # body will always be a compound statement.
        output.extend(self.body.to_3ac())
        # for item in self.body:
        #     output.append(item.to_3ac())
        #     # print(output)

        return output


class If(BaseAstNode):
    """
    Requires: 3AC from child nodes.
    Output:   No direct output, just the 3AC associated with the conditional checking and branching.
    """
    def __init__(self, conditional, if_true, if_false, **kwargs):
        super(If, self).__init__(**kwargs)

        self.conditional = conditional
        self.if_true = if_true
        self.if_false = if_false

    @property
    def children(self):
        children = []
        children.append(self.conditional)
        if self.if_true:
            children.append(self.if_true)
        if self.if_false:
            children.append(self.if_false)
        return tuple(children)

    def to_3ac(self, include_source=False):
        output = []

        # get three labels
        lTrue = LABEL_TICKETS.get()
        lEnd = LABEL_TICKETS.get()

        # gen 3ac for conditional
        # print(self.conditional, '\n\n\n')
        # result = self.conditional.to_3ac()
        # output.append(result['3ac'])
        #
        # # check the register that results from the conditional to see if false
        # reg = result['register']
        # if register_allocation_table[reg] is False:
        #     output.append(BREQ(lFalse, False, register_allocation_table[reg]))

        # get values of conditional
        # get memory address of lvalue by calling to3ac on lvalue
        left = self.conditional.lvalue.to_3ac()
        lval = left['register']
        if '3ac' in left:
            output.extend(left['3ac'])

        # load lvalue into register  - does this need to happen or not?

        # get memory address of rvalue by calling to3ac on rvalue
        right = self.conditional.rvalue.to_3ac()
        rval = right['register']
        if '3ac' in right:
            output.extend(right['3ac'])

        # # check which operator in conditional, to know which branch to take
        # branching on true
        if self.conditional.operator == '<':
            output.append(BRLT(lTrue, lval, rval))
        if self.conditional.operator == '<=':
            output.append(BRLE(lTrue, lval, rval))
        if self.conditional.operator == '>':
            output.append(BRGT(lTrue, lval, rval))
        if self.conditional.operator == '>=':
            output.append(BRGE(lTrue, lval, rval))
        if self.conditional.operator == '==':
            output.append(BREQ(lTrue, lval, rval))
        if self.conditional.operator == '!=':
            output.append(BRNE(lTrue, lval, rval))

        # if conditional is false, gen 3ac
        output.extend(self.if_false.to_3ac())
        output.append(BR(lEnd))

        # if conditional is true, dump label and gen 3ac
        output.append(LABEL(lTrue))
        output.extend(self.if_true.to_3ac())

        # dump end label
        output.append(LABEL(lEnd))

        return output


class InitializerList(BaseAstNode):
    def __init__(self, initializers=None, **kwargs):
        super(InitializerList, self).__init__(**kwargs)

        self.initializers = initializers if initializers else []

    @property
    def children(self):
        children = []
        children.extend(self.initializers)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


##
# Node for all forms of structured iteration (for, while, and do...while).
##
class IterationNode(BaseAstNode):
    """
    Requires: 3AC from child nodes. In the parser, the members of this node should have been initialized in such a way
              as to be correct, i.e. an error was thrown if the continuation condition was not given, so we are OK to
              make assumptions now, i.e. a missing continuation condition indicates an infinite for loop.
    Output:   No direct output, just the 3AC associated with the conditional checking and branching.
    """

    def __init__(self, is_pre_test_loop, initialization_expression, stop_condition_expression, increment_expression,
                 body_statements=None, **kwargs):
        super(IterationNode, self).__init__(**kwargs)

        self.is_pre_test_loop = is_pre_test_loop

        self.initialization_expression = initialization_expression
        self.stop_condition_expression = stop_condition_expression
        self.increment_expression = increment_expression
        self.body_statements = body_statements

    @property
    def children(self):
        children = []
        if self.initialization_expression:
            children.append(self.initialization_expression)
        if self.stop_condition_expression:
            children.append(self.stop_condition_expression)
        if self.increment_expression:
            children.append(self.increment_expression)
        if self.body_statements:
            children.append(self.body_statements)
        return tuple(children)

    def to_3ac(self, include_source=False):
        output = []
        condition_check_label = LABEL_TICKETS.get()
        condition_ok_label = LABEL_TICKETS.get()
        loop_exit_label = LABEL_TICKETS.get()

        # Check for pre-test loop
        if not self.is_pre_test_loop:
            if self.body_statements:
                output.extend(self.body_statements.to_3ac())

        # Initialize
        if self.initialization_expression:
            # TODO (Shubham) What type of information do we get back from expression?
            output.extend(self.initialization_expression.to_3ac())

        # Add condition check label
        output.append(LABEL(condition_check_label))

        # Check condition
        if self.stop_condition_expression:
            condition_tac = self.stop_condition_expression.to_3ac()

            # If condition is false
            output.extend(condition_tac['3ac'])
            output.append(BRNE(condition_ok_label, 0, condition_tac['register']))
            output.append(BR(loop_exit_label))

        # Add condition okay label
        output.append(LABEL(condition_ok_label))

        # Add loop instructions
        if self.body_statements:
            output.extend(self.body_statements.to_3ac())

        # Add increment expressions
        if self.increment_expression:
            # TODO (Shubham) What type of information do we get back from expression?
            output.extend(self.increment_expression.to_3ac())

        # Add loop instruction
        output.append(BR(condition_check_label))

        # Add loop exit label
        output.append(LABEL(loop_exit_label))

        return output


class Label(BaseAstNode):
    """
    Requires: Only its own name.
    Output:   The 3AC for a label.
    """
    def __init__(self, label_name, body_statement, **kwargs):
        super(Label, self).__init__(**kwargs)

        self.label_name = label_name
        self.body_statement = body_statement

    def name(self, arg=None):
        return super(Label, self).name(arg=self.label_name)

    @property
    def children(self):
        children = []
        children.append(self.body_statement)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class PointerDeclaration(BaseAstNode):
    """
    Not sure if this should remain an AST node, but rather an info collection class that gets disassembled and
    absorbed by the Symbol this contributes to.
    """
    def __init__(self, qualifiers=None, type_=None, **kwargs):
        super(PointerDeclaration, self).__init__(**kwargs)

        self.qualifiers = qualifiers if qualifiers else []
        self.type = type_  # TODO: what does this do/hold?

    def add_qualifiers(self, qualifiers):
        pass

    @property
    def children(self):
        children = []
        children.append(self.type)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class Return(BaseAstNode):
    """
    Requires: An appropriately initialized register containing information on where to jump to at the return of the
              function; an rvalue register containing the result of the associated expression. If the expression is
              empty, then the register should contain the value 0 (zero).
    Output:   None, per se, but it needs to store that rvalue in the designated MIPS return register.
    """
    def __init__(self, expression, **kwargs):
        super(Return, self).__init__(**kwargs)

        self.expression = expression

    def get_resulting_type(self):
        """
        For interface compliance with the other expression nodes.
        """
        return self.expression.get_resulting_type()

    @property
    def children(self):
        children = []
        if self.expression:
            children.append(self.expression)
        return tuple(children)

    def to_3ac(self, include_source=False):
        # raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

        # return value
        output = []
        prev_result = self.expression.to_3ac()
        # Note: Does not currently pass back the register of the value being returned....
        output.extend(prev_result['3ac'])
        output.append(RETURN())
        return output


class SymbolNode(BaseAstNode):
    """
    ** I'm not sure about this design, feel free to disagree. **
    Requires: The info contained here, especially memory where this stuff is declared.
    Output:   No direct output, but should contain the runtime information of the symbol.
    """
    def __init__(self, symbol, **kwargs):
        super(SymbolNode, self).__init__(**kwargs)

        if symbol:
            self.symbol = symbol
        else:
            raise ValueError('SymbolNode cannot have a \'None\' symbol.')

    def get_resulting_type(self):
        """
        For interface compliance with the other expression nodes.
        """
        return self.symbol.get_type_str()

    def name(self, arg=None):
        arg = self.symbol.get_type_str() + '_' + self.symbol.identifier
        return super(SymbolNode, self).name(arg)

    @property
    def immutable(self):
        return self.symbol.immutable

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        if self.symbol.global_memory_location:
            return {'register': 'Global_{}'.format(self.symbol.global_memory_location)}
        else:
            return {'register': 'Frame_{}'.format(self.symbol.activation_frame_offset)}


class UnaryOperator(BaseAstNode):
    """
    Requires: An lvalue for the operation to operate on.
    Output:   An rvalue that is either the result of the operation or the value of the symbol before the operation,
              depending on if the operator is a pre- or post- one.
    """
    def __init__(self, operator, expression, **kwargs):
        super(UnaryOperator, self).__init__(**kwargs)

        self.operator = operator
        self.expression = expression

    def get_resulting_type(self):
        return self.expression.get_resulting_type()

    def name(self, arg=None):
        return super(UnaryOperator, self).name(arg=operator_utils.operator_to_name(self.operator))

    @property
    def children(self):
        children = []
        children.append(self.expression)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

        # get memory location of expression by calling to3ac function

        # copy expression value to register

        # determine correct operator and apply to register


class Constant(BaseAstNode):
    """
    Requires: The value of the constant/constant expression as received from the parser.
    Output:   An rvalue register containing the value of the constant.
    """
    CHAR = 'char'

    INTEGER = 'int'

    LONG = 'long'

    LONG_LONG = 'long long'

    FLOAT = 'float'

    DOUBLE = 'double'

    def __init__(self, type_, value, **kwargs):
        super(Constant, self).__init__(**kwargs)

        self.type_declaration = type_
        self.value = value

    def get_resulting_type(self):
        """
        For interface compliance with the other expression types.
        """
        return self.type_declaration

    def name(self, **kwargs):
        return super(Constant, self).name(arg=str(self.value))

    @staticmethod
    def is_integral_type(source):
        return source.type_declaration is Constant.CHAR or \
            source.type_declaration is Constant.INTEGER or \
            source.type_declaration is Constant.LONG or \
            source.type_declaration is Constant.LONG_LONG

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        # raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

        output = []

        # load constant into register and return register
        reg = INT_REGISTER_TICKETS.get()
        output.append(ADDIU(reg, self.value, 0))

        register_allocation_table[reg] = self.value

        return {'3ac': output, 'register': reg}

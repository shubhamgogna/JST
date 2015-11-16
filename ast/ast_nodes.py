##
# These classes are AUTO-GENERATED!
# Most of the boilerplate should be written for you, so you should carefully handwrite methods
# that are unique or need special logic for overloading.
##

from ast.base_ast_node import BaseAstNode
from utils import type_utils
from utils.type_utils import Type
from utils import operator_utils


##
# This is a nested declaration of an array with the given type
##
class ArrayDeclaration(BaseAstNode):
    """
    Requires: Type and dimensional information from the symbol build in the symbol table.
    Output:   Probably no direct output in the form of temporary registers, but the memory assigned for the
              thing should be recorded somewhere.
    """

    def __init__(self, identifier, dim, dim_qualifiers, type_, **kwargs):
        super(ArrayDeclaration, self).__init__(**kwargs)

        self.dim = dim
        self.dim_qualifiers = dim_qualifiers

        self.identifier = identifier
        self.type = type_

    def name(self, arg=None):
        raise NotImplementedError('Add the array dimensions and the Symbol to the array declaration node.')
        ']['.join(self)
        arg = self.type.name_arg() + '_' + self.identifier
        return super(ArrayDeclaration, self).name(arg)

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


##
# REVISIT ME - Might need to switch attrs to children depending on how we handle arrays
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
        return self.symbol.type_declaration.get_type_str()

    def name(self, arg=None):
        return super(ArrayReference, self).name(arg=self.symbol.identifier)

    @property
    def children(self):
        children = []
        children.extend(self.subscripts)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


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
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


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

        return type_utils.get_promoted_type(lvalue_type, rvalue_type)

    def name(self, arg=None):
        return super(BinaryOperator, self).name(arg=operator_utils.operator_to_name(self.operator))

    @property
    def children(self):
        children = []
        children.append(self.lvalue)
        children.append(self.rvalue)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


# TODO (Shubham) This looks like it's for explicit conversions.
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

    @property
    def children(self):
        children = []
        children.append(self.to_type)
        children.append(self.expression)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


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
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class Declaration(BaseAstNode):
    """
    Requires: The symbol information of the declaration.
    Output:   Probably no direct output in the form of temporary registers, but the memory assigned for the
              thing should be recorded somewhere.
    """
    def __init__(self, identifier, qualifiers, storage, funcspec, type_, initialization_value, **kwargs):
        super(Declaration, self).__init__(**kwargs)

        self.identifier = identifier
        self.qualifiers = qualifiers
        self.storage = storage
        self.funcspec = funcspec

        self.type = type_
        self.initialization_value = initialization_value

    def sizeof(self):
        return self.type.sizeof()

    def name(self, arg=None):
        arg = self.type.name_arg() + '_' + self.identifier
        return super(Declaration, self).name(arg)

    @property
    def children(self):
        children = []
        if self.initialization_value is not None:
            children.append(self.initialization_value)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


##
# This is the top of the AST
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
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

    def to_graph_viz_str(self):
        return 'digraph {\n' + super(FileAST, self).to_graph_viz_str() + '}'


class FunctionCall(BaseAstNode):
    """
    Requires: An rvalue for each parameter that this node will then take appropriate actions to cast and copy into the
              activation frame.
    Output:   No output per se, but take care to store return value in the MIPS designated return value register.
    """
    def __init__(self, function_symbol, arguments=None, **kwargs):
        super(FunctionCall, self).__init__(**kwargs)

        self.function_symbol = function_symbol
        self.arguments = arguments if arguments else []

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
    def __init__(self, type_, identifier, arguments=None, **kwargs):
        super(FunctionDeclaration, self).__init__(**kwargs)

        self.identifier = identifier
        self.arguments = arguments if arguments else []
        self.type = type_

    def name(self, arg=None):
        arg = self.type.name_arg() + '_' + self.identifier
        return super(FunctionDeclaration, self).name(arg)

    @property
    def children(self):
        children = []
        children.extend(self.arguments)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class FunctionDefinition(BaseAstNode):
    """
    Requires: Information about its params and declarations so that it can build its activation frame appropriately
    Output:   Nothing other than the 3AC
    """

    def __init__(self, type_, identifier, arguments, body, **kwargs):
        super(FunctionDefinition, self).__init__(**kwargs)

        self.type = type_
        self.identifier = identifier
        self.body = body
        self.arguments = arguments if arguments else []

    def name(self, arg=None):
        arg = self.type.name_arg() + '_' + self.identifier
        return super(FunctionDefinition, self).name(arg)

    @property
    def children(self):
        children = []
        children.extend(self.arguments)
        if self.body:
            children.append(self.body)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


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
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


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
# This type of node handles all loops: for, while, and do...while.
##
class IterationNode(BaseAstNode):
    """
    Requires: 3AC from child nodes. In the parser, the members of this node should have been initialized in such a way
              as to be correct, i.e. an error was thrown if the continuation condition was not given, so we are OK to
              make assumptions now, i.e. a missing continuation condition indicates an infinite for loop.
    Output:   No direct output, just the 3AC associated with the conditional checking and branching.
    """

    def __init__(self, is_pre_test_loop, initialization_expression, stop_condition_expression, increment_expression,
                 body_statments=None, **kwargs):
        super(IterationNode, self).__init__(**kwargs)

        self.is_pre_test_loop = is_pre_test_loop

        self.initialization_expression = initialization_expression
        self.stop_condition_expression = stop_condition_expression
        self.increment_expression = increment_expression
        self.body_statements = body_statments

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
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))



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
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


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
        return self.symbol.type_declaration.get_type_str()

    def name(self, arg=None):
        arg = self.symbol.type_declaration.name_arg() + '_' + self.symbol.identifier
        return super(SymbolNode, self).name(arg)

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class TypeDeclaration(BaseAstNode):
    """
    Not sure if this should remain an AST node, but rather an info collection class that gets disassembled and
    absorbed by the Symbol this contributes to.
    """

    FLOAT_TYPES = {type_utils.FLOAT, type_utils.DOUBLE}
    INT_TYPES = {type_utils.CHAR, type_utils.SHORT, type_utils.INT, type_utils.LONG, type_utils.SIGNED, type_utils.UNSIGNED}

    def __init__(self, **kwargs):
        # Call the parent constructor
        super(TypeDeclaration, self).__init__(**kwargs)
        # In GCC, storage classes are idempotent (but there can only be one of each)
        self.storage_classes = set()
        # In GCC, qualifiers are idempotent
        self.type_qualifiers = set()
        # List allows for things like 'long long' and 'long double'
        self.type_specifiers = []
        # Indicated if the type is signed/unsigned
        # None = sign not applicable
        self.type_sign = None

    def name(self, arg=None):
        return super(TypeDeclaration, self).name(arg=self.name_arg())

    def name_arg(self):
        joined = [self.type_sign if self.type_sign else '',
                  '_'.join(self.storage_classes),
                  '_'.join(self.type_qualifiers),
                  '_'.join(self.type_specifiers)]
        return '_'.join([i for i in joined if i is not ''])

    def add_storage_class(self, storage_class_specifier):
        if storage_class_specifier in self.storage_classes:
            raise Exception('Duplication of storage class specifier "{}".'.format(storage_class_specifier))
        self.storage_classes.add(storage_class_specifier)

    def add_type_qualifier(self, type_qualifier):
        self.type_qualifiers.add(type_qualifier)

    def add_type_specifier(self, specifier):
        if specifier == 'unsigned' or specifier == 'signed':
            if self.type_sign is not None:
                raise Exception('Multiple signed/unsigned specifiers not allowed.')
            else:
                self.type_sign = specifier
        else:
            self.type_specifiers.insert(0, specifier)

    def get_type_str(self):
        return (self.type_sign + ' ' if self.type_sign else '') + ' '.join(self.type_specifiers)

    def sizeof(self):
        return type_utils.get_bit_size(self) / 4  # divide by 4 for bytes

    @property
    def is_const(self):
        return 'const' in self.type_qualifiers

    def __str__(self):
        storage_class_str = ' '.join(self.storage_classes) + ' ' if self.storage_classes else ''
        qualifier_str = ' '.join(self.type_qualifiers) + ' ' if self.type_qualifiers else ''
        specifier_str = ' '.join(self.type_specifiers) if self.type_specifiers else 'UNKNOWN'
        return '{}{}{}'.format(storage_class_str, qualifier_str, specifier_str)

    def __repr__(self):
        return self.name() + ': ' + str(self)

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


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


class Constant(BaseAstNode):
    """
    Requires: The value of the constant/constant expression as received from the parser.
    Output:   An rvalue register containing the value of the constant.
    """
    CHAR = TypeDeclaration()
    CHAR.type_sign = 'signed'
    CHAR.add_type_specifier('char')

    INTEGER = TypeDeclaration()
    INTEGER.type_sign = 'signed'
    INTEGER.add_type_specifier('int')

    LONG = TypeDeclaration()
    LONG.type_sign = 'signed'
    LONG.add_type_specifier('long')

    LONG_LONG = TypeDeclaration()
    LONG_LONG.type_sign = 'signed'
    LONG_LONG.add_type_specifier('long')
    LONG_LONG.add_type_specifier('long')

    FLOAT = TypeDeclaration()
    FLOAT.add_type_specifier('float')

    DOUBLE = TypeDeclaration()
    DOUBLE.add_type_specifier('double')

    def __init__(self, type_, value, **kwargs):
        super(Constant, self).__init__(**kwargs)

        self.type_declaration = type_
        self.value = value

    def get_resulting_type(self):
        """
        For interface compliance with the other expression types.
        """
        return self.type_declaration.get_type_str()

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
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

##
# These classes are AUTO-GENERATED!
# Most of the boilerplate should be written for you, so you should carefully handwrite methods
# that are unique or need special logic for overloading.
##


# The class for the base AST node
#
# This class will be inherited from for other types of AST nodes. Should hold all common functionality.
#
from ticket_counting.ticket_counters import UUID_TICKETS
from utils.compile_time_utils import OperatorUtils
from utils.primitive_types import Type


class BaseAstNode:
    # Initialize node with desired info
    #
    # @param children A list of child nodes
    # @param line_range A tuple of start line and end line for where this node applies
    # @param uuid A unique identifier number from a TicketCounter
    #
    def __init__(self, uuid=None, **kwargs):
        # Initialize the uuid
        self.uuid = uuid if uuid else UUID_TICKETS.get()

    # Define str function to concisely summarize a node with its uuid, name/type, and relevant info
    def __str__(self):
        return '{}_{}'.format(self.uuid, type(self).__name__)

    def name(self, arg=None):
        extra = '_' + str(arg) if arg else ''
        name_str = '{}{}_{}'.format(type(self).__name__, extra, self.uuid)

        return name_str

    # Define function for converting to 3ac
    def to_3ac(self, include_source=False):
        # TODO: something like: self.3ac = '\n'.join([child.to_3ac() for child in self.children])
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

    # TODO: Probably we will be able to remove the visit functionality since it should be encapsulated by 3ac
    # Define visit function for the iteration protocol
    def visit(self, node):
        # TODO: Copied from pyCparser's visit node.... may need to fix
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    # Define generic visit function to call if no explicit visitor function exists for a node.
    def generic_visit(self, node):
        # TODO: Copied from pyCparser's visit node.... may need to fix
        for c_name, c in node.children():
            self.visit(c)

    # Define method for getting a graphViz ready string
    def to_graph_viz_str(self):
        # print(self.name())
        # for child in self.children:
        #     if not isinstance(child, BaseAstNode):
        #         print(self.name(), child)
        #
        # for child in self.children:
        #     print(self.name(), 'child', child)
        #
        # print('\n'.join([str(child) for child in self.children]))

        descendant_names = ', '.join([child.name() for child in self.children])

        print(self.name(), 'descendants', descendant_names)

        output = '\t{} -> {{{}}};\n'.format(self.name(), descendant_names)

        for child in self.children:
            output += child.to_graph_viz_str()
        return output

    @property
    def children(self):
        return tuple([])


##
# This type of node handles all loops: for, while, and do...while.
##
class IterationNode(BaseAstNode):
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


# TODO (Shubham) What does this do? Is it just for visualization? It can probably be removed if so.
class ArrayDimLister(BaseAstNode):
    def __init__(self, dimensions, **kwargs):
        super(ArrayDimLister, self).__init__(**kwargs)

        self.dimensions = dimensions

    def name(self, arg=None):
        return super(ArrayDimLister, self).name(arg='_'.join(str(dimension) for dimension in self.dimensions))

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


##
# This is a nested declaration of an array with the given type
##
# TODO (Shubham) Is this node here so we can handle array 3AC differently? We can remove it and merge with Declaration,
# but I'm not sure if that is or isn't a good idea.
class ArrayDeclaration(BaseAstNode):
    def __init__(self, identifier, dim, dim_qualifiers, type_declaration, **kwargs):
        super(ArrayDeclaration, self).__init__(**kwargs)

        self.dim = dim
        self.dim_qualifiers = dim_qualifiers

        self.identifier = identifier
        self.type_declaration = type_declaration

        self.array_dim_dummy = ArrayDimLister(self.dim)

    def name(self, arg=None):
        return super(ArrayDeclaration, self).name(arg=self.identifier)

    @property
    def children(self):
        children = []
        children.append(self.type_declaration)
        children.append(self.array_dim_dummy)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


##
# REVISIT ME - Might need to switch attrs to children depending on how we handle arrays
##
class ArrayReference(BaseAstNode):
    def __init__(self, array_symbol, subscript, **kwargs):
        super(ArrayReference, self).__init__(**kwargs)

        self.array_symbol = array_symbol
        self.subscript = subscript

    @property
    def children(self):
        children = []
        children.append(self.array_symbol)
        children.append(self.subscript)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


# TODO (Shubham) Note to self: The return type of the assignment is the type of the left hand side.
class Assignment(BaseAstNode):
    def __init__(self, operator, lvalue, rvalue, **kwargs):
        super(Assignment, self).__init__(**kwargs)

        self.operator = operator
        self.lvalue = lvalue
        self.rvalue = rvalue

    def name(self, arg=None):
        return super(Assignment, self).name(arg=OperatorUtils.operator_to_name(self.operator))

    @property
    def children(self):
        children = []
        children.append(self.lvalue)
        children.append(self.rvalue)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


# TODO (Shubham) The return type here might need to be explicitly stated unlike assignment
class BinaryOperator(BaseAstNode):
    def __init__(self, operator, lvalue, rvalue, **kwargs):
        super(BinaryOperator, self).__init__(**kwargs)

        self.operator = operator
        self.lvalue = lvalue
        self.rvalue = rvalue

    def name(self, arg=None):
        return super(BinaryOperator, self).name(arg=OperatorUtils.operator_to_name(self.operator))

    @property
    def children(self):
        children = []
        children.append(self.lvalue)
        children.append(self.rvalue)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


##
# REVISIT ME - May need to add in stuff for line numbers for jumps in 3ac
##
class Break(BaseAstNode):
    def __init__(self, **kwargs):
        super(Break, self).__init__(**kwargs)

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class Case(BaseAstNode):
    def __init__(self, expression, statement_list=None, **kwargs):
        super(Case, self).__init__(**kwargs)

        self.expression = expression
        self.statement_list = statement_list if statement_list else []

    @property
    def children(self):
        children = []
        children.append(self.expression)
        children.extend(self.statement_list)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


# TODO (Shubham) This might be an important node for implicit conversions. I'm not clear on how it fits in yet.
class Cast(BaseAstNode):
    def __init__(self, to_type, expression, **kwargs):
        super(Cast, self).__init__(**kwargs)

        self.to_type = to_type
        self.expression = expression

    @property
    def children(self):
        children = []
        children.append(self.to_type)
        children.append(self.expression)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class CompoundStatement(BaseAstNode):
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


class Constant(BaseAstNode):
    INTEGER = 'int'
    FLOAT = 'float'

    def __init__(self, type_, value, **kwargs):
        super(Constant, self).__init__(**kwargs)

        self.type = type_
        self.value = value

    def name(self, **kwargs):
        return super(Constant, self).name(arg=self.value)

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class Continue(BaseAstNode):
    def __init__(self, **kwargs):
        super(Continue, self).__init__(**kwargs)

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class Declaration(BaseAstNode):
    def __init__(self, identifier, qualifiers, storage, funcspec, type_, initialization_value, bitsize, **kwargs):
        super(Declaration, self).__init__(**kwargs)

        self.identifier = identifier
        self.qualifiers = qualifiers
        self.storage = storage
        self.funcspec = funcspec

        self.type_ = type_
        self.initialization_value = initialization_value
        self.bitsize = bitsize

    def name(self, arg=None):
        return super(Declaration, self).name(arg=self.identifier)

    @property
    def children(self):
        children = []
        children.append(self.type_)
        if self.initialization_value is not None:
            children.append(self.initialization_value)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class Default(BaseAstNode):
    def __init__(self, statement_list=None, **kwargs):
        super(Default, self).__init__(**kwargs)

        self.statement_list = statement_list if statement_list else []

    @property
    def children(self):
        children = []
        children.extend(self.statement_list)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


##
# This is the top of the AST
##
class FileAST(BaseAstNode):
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
    def __init__(self, identifier, arguments, **kwargs):
        super(FunctionCall, self).__init__(**kwargs)

        self.identifier = identifier
        self.arguments = arguments

    def name(self, arg=None):
        return super(FunctionCall, self).name(arg=self.identifier)

    @property
    def children(self):
        children = []
        if self.arguments:
            children.append(self.arguments)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class FunctionDeclaration(BaseAstNode):
    def __init__(self, arguments, type, identifier, **kwargs):
        super(FunctionDeclaration, self).__init__(**kwargs)

        self.identifier = identifier
        self.arguments = arguments
        self.type = type

    def name(self, arg=None):
        return super(FunctionDeclaration, self).name(arg=self.identifier)

    @property
    def children(self):
        children = []
        children.append(self.arguments)
        children.append(self.type)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class FunctionDefinition(BaseAstNode):
    def __init__(self, type_, identifier, param_declarations, body, **kwargs):
        super(FunctionDefinition, self).__init__(**kwargs)

        self.type = type_
        self.identifier = identifier
        self.body = body
        self.param_declarations = param_declarations if param_declarations else ParameterList([])

    def name(self, arg=None):
        return super(FunctionDefinition, self).name(arg=self.identifier)

    @property
    def children(self):
        children = []
        children.append(self.type)
        children.append(self.param_declarations)
        if self.body:
            children.append(self.body)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class Goto(BaseAstNode):
    def __init__(self, name, **kwargs):
        super(Goto, self).__init__(**kwargs)

        self.name = name

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


# TODO (Shubham) What would this be used for? Possibly removable
class IdentifierType(BaseAstNode):
    def __init__(self, names, **kwargs):
        super(IdentifierType, self).__init__(**kwargs)

        self.names = names

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class If(BaseAstNode):
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


class Label(BaseAstNode):
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


class ParameterList(BaseAstNode):
    def __init__(self, parameters=None, **kwargs):
        super(ParameterList, self).__init__(**kwargs)

        self.parameters = parameters if parameters else []

    @property
    def children(self):
        children = []
        children.extend(self.parameters)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class PointerDeclaration(BaseAstNode):
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
    def __init__(self, expression, **kwargs):
        super(Return, self).__init__(**kwargs)

        self.expression = expression

    @property
    def children(self):
        children = []
        if self.expression:
            children.append(self.expression)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class Switch(BaseAstNode):
    def __init__(self, conditional, body_statement, **kwargs):
        super(Switch, self).__init__(**kwargs)

        self.conditional = conditional
        self.body_statement = body_statement

    @property
    def children(self):
        children = []
        children.append(self.conditional)
        children.append(self.body_statement)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class SymbolNode(BaseAstNode):
    def __init__(self, symbol, **kwargs):
        super(SymbolNode, self).__init__(**kwargs)

        if symbol:
            self.symbol = symbol
            self.identifier = symbol.identifier
        else:
            raise ValueError('SymbolNode cannot have a \'None\' symbol.')

    def name(self, arg=None):
        return super(SymbolNode, self).name(arg=self.identifier)

    @property
    def children(self):
        children = []
        children.append(self.symbol.decl_type)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class TernaryOperator(BaseAstNode):
    def __init__(self, conditional, if_true_expression, if_false_expression, **kwargs):
        super(TernaryOperator, self).__init__(**kwargs)

        self.conditional = conditional
        self.if_true_expression = if_true_expression
        self.if_false_expression = if_false_expression

    @property
    def children(self):
        children = []
        children.append(self.conditional)
        children.append(self.if_true_expression)
        children.append(self.if_false_expression)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class TypeDeclaration(BaseAstNode):
    FLOAT_TYPES = {Type.FLOAT, Type.DOUBLE}
    INT_TYPES = {Type.CHAR, Type.SHORT, Type.INT, Type.LONG, Type.SIGNED, Type.UNSIGNED}

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

    def name(self, **kwargs):
        joined = [self.type_sign if self.type_sign else '',
                  '_'.join(self.storage_classes),
                  '_'.join(self.type_qualifiers),
                  '_'.join(self.type_specifiers)]
        joined = [i for i in joined if i is not '']
        return super(TypeDeclaration, self).name(arg='_'.join(joined))

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
        return ' '.join(self.type_specifiers)

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
    def __init__(self, operator, expression, **kwargs):
        super(UnaryOperator, self).__init__(**kwargs)

        self.operator = operator

        self.expression = expression

    def name(self, arg=None):
        return super(UnaryOperator, self).name(arg=OperatorUtils.operator_to_name(self.operator))

    @property
    def children(self):
        children = []
        children.append(self.expression)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

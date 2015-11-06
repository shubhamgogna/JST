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
    def __init__(self, line_range=None, uuid=None, **kwargs):
        # initialize the line_range
        self.line_range = line_range

        # initialize the uuid
        # Note: Since we have multiple ticket counters, we need to pass them in as a param.
        self.uuid = uuid if uuid else UUID_TICKETS.get()

    # Define str function to concisely summarize a node with its uuid, name/type, and relevant info
    def __str__(self):
        return '{}_{}'.format(self.uuid, type(self).__name__)


    def name(self, arg=None):
        extra = '_' + str(arg) if arg else ''
        name_str = '{}{}_{}'.format(type(self).__name__, extra, self.uuid)

        return name_str

    #Define function for converting to 3ac
    def to_3ac(self, include_source=False):
        #TODO: something like: self.3ac = '\n'.join([child.to_3ac() for child in self.children])
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

    # TODO: Probably we will be able to remove the visit functionality since it should be encapsulated by 3ac
    # Define visit function for the iteration protocol
    def visit(self, node):
        #TODO: Copied from pyCparser's visit node.... may need to fix
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    # Define generic visit function to call if no explicit visitor function exists for a node.
    def generic_visit(self, node):
        #TODO: Copied from pyCparser's visit node.... may need to fix
        for c_name, c in node.children():
            self.visit(c)


    # Define method for getting a graphViz ready string
    def to_graph_viz_str(self):
        print(self.name())
        for child in self.children:
            if not isinstance(child, BaseAstNode):
                print(self.name(), child)
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
    def __init__(self, is_pre_test_loop, initialization_expression, stop_condition_expression, increment_expression, body_statments=None, **kwargs):
        super(IterationNode, self).__init__(**kwargs)

        self.is_pre_test_loop = is_pre_test_loop

        self.initialization_expression = initialization_expression
        self.stop_condition_expression = stop_condition_expression
        self.increment_expression = increment_expression

        self.body_statments = body_statments if body_statments else []

    @property
    def children(self):
        children = []
        children.append(self.initialization_expression)
        children.append(self.stop_condition_expression)
        children.append(self.increment_expression)
        children.append(self.body_statments)
        return tuple(children)

    def to_3ac(self, a_dummy_parameter, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

class ArrayDimLister(BaseAstNode):
    def __init__(self, dimensions, **kwargs):
        super(ArrayDimLister, self).__init__(**kwargs)

        self.dimensions = dimensions

    def name(self):
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
class ArrayDeclaration(BaseAstNode):
    def __init__(self, identifier, dim, dim_qualifiers, type_declaration, **kwargs):
        super(ArrayDeclaration, self).__init__(**kwargs)

        self.dim = dim
        self.dim_qualifiers = dim_qualifiers

        self.identifier = identifier
        self.type_declaration = type_declaration

        self.array_dim_dummy = ArrayDimLister(self.dim)

    @property
    def children(self):
        children = []
        children.append(self.type_declaration)
        children.append(self.identifier)
        children.append(self.array_dim_dummy)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

##
# REVISIT ME - Might need to swtich attrs to children depending on how we handle arrays
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


class Assignment(BaseAstNode):
    def __init__(self, operator, lvalue, rvalue, **kwargs):
        super(Assignment, self).__init__(**kwargs)

        self.operator = operator

        self.lvalue = lvalue
        self.rvalue = rvalue

    def name(self):
        return super(Assignment, self).name(arg=OperatorUtils.operator_to_name(self.operator))

    @property
    def children(self):
        children = []
        children.append(self.lvalue)
        children.append(self.rvalue)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class BinaryOperator(BaseAstNode):
    def __init__(self, operator, lvalue, rvalue, **kwargs):
        super(BinaryOperator, self).__init__(**kwargs)

        self.operator = operator

        self.lvalue = lvalue
        self.rvalue = rvalue

    def name(self):
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

    def to_3ac(self, break_to_label, include_source=False):
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
        self.statement_list = statement_list if statement_list else []


    @property
    def children(self):
        children = []
        if self.declaration_list is not None:
            children.append(self.declaration_list)
        children.extend(self.statement_list)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

class Constant(BaseAstNode):
    INTEGER = 'int'
    FLOAT = 'float'

    def __init__(self, type, value, **kwargs):
        super(Constant, self).__init__(**kwargs)

        self.type = type
        self.value = value

    def name(self):
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

    def to_3ac(self, continue_to_label, include_source=False):
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


    @property
    def children(self):
        children = []
        children.append(self.type_)
        children.append(self.identifier)
        if self.initialization_value is not None:
            children.append(self.initialization_value)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class DeclarationList(BaseAstNode):
    def __init__(self, declaration_list=None, **kwargs):
        super(DeclarationList, self).__init__(**kwargs)

        self.declaration_list = declaration_list if declaration_list else []

    @property
    def children(self):
        children = []
        children.extend(self.declaration_list)
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


class EmptyStatement(BaseAstNode):
    def __init__(self, **kwargs):
        super(EmptyStatement, self).__init__(**kwargs)

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class ExpressionList(BaseAstNode):
    def __init__(self, expressions=None, **kwargs):
        super(ExpressionList, self).__init__(**kwargs)



        self.expressions = expressions if expressions else []

    @property
    def children(self):
        children = []
        children.extend(self.expressions)
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

    def name(self):
        super(FunctionCall, self).name(arg=self.identifier)

    @property
    def children(self):
        children = []
        children.append(self.identifier)
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

    def name(self):
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
    def __init__(self, declarations, param_declarations, body, **kwargs):
        super(FunctionDefinition, self).__init__(**kwargs)

        self.identifier = declarations.identifier

        self.declarations = declarations
        self.body = body

        self.param_declarations = param_declarations if param_declarations else []

    def name(self):
        print('FuncDef-declarations:', type(self.declarations))

        return super(FunctionDefinition, self).name(arg=self.identifier)

    @property
    def children(self):
        children = []
        children.append(self.declarations)
        children.append(self.body)
        children.append(self.param_declarations)
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


class ID(BaseAstNode):
    def __init__(self, identifier, **kwargs):
        super(ID, self).__init__(**kwargs)

        self.identifier = identifier

    def name(self):
        return super(ID, self).name(arg=self.identifier)

    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


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
        children.append(self.if_true)
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

    def name(self):
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
        super(TypeDeclaration, self).__init__(**kwargs)

        self.storage_class = []
        self.qualifiers = set()  # in gcc, type qualifiers are idempotent
        self.type_specifier = []  # being a list allows for things like 'unsigned int', 'long double'

        # From pycparser
        # def __init__(self, declaration_name, qualifiers, type, **kwargs):
        #     self.declaration_name = declaration_name
        #     self.qualifiers = qualifiers
        #
        #     self.type = type

    def name(self):

        if(len(self.qualifiers)):
            return super(TypeDeclaration, self).name(arg='_'.join(self.qualifiers) + '_' + '_'.join(self.type_specifier))
        else:
            return super(TypeDeclaration, self).name(arg='_'.join(self.qualifiers) + '_'.join(self.type_specifier))

    def add_storage_class(self, storage_class_specifier):
        if storage_class_specifier in self.storage_class:
            raise Exception('Duplication of storage class specifier "{}".'.format(storage_class_specifier))

        self.storage_class.append(storage_class_specifier)

    def add_qualifier(self, type_qualifier):
        self.qualifiers.add(type_qualifier)

    def add_type_specifier(self, specifier):

        if (specifier is 'long' and 2 <= self.type_specifier.count('long')) or specifier in self.type_specifier:
            raise Exception('Too many instances of type specifier "{}" in type declaration'.format(specifier))

        self.type_specifier.append(specifier)

        # TODO: check for unsigned along with float types and such

    def __str__(self):
        storage_class_str = ' '.join(self.storage_class) + ' ' if self.storage_class else ''
        qualifier_str = ' '.join(self.qualifiers) + ' ' if self.qualifiers else ''
        specifier_str = ' '.join(self.type_specifier) if self.type_specifier else 'UNKNOWN'

        return '{}{}{}'.format(storage_class_str, qualifier_str, specifier_str)

    def __repr__(self):
        return self.name() + ': ' + str(self)


    @property
    def children(self):
        children = []
        # children.append(self.type)  # TODO: keep this?
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class UnaryOperator(BaseAstNode):
    def __init__(self, operator, expression, **kwargs):
        super(UnaryOperator, self).__init__(**kwargs)

        self.operator = operator

        self.expression = expression

    def name(self):
        return super(UnaryOperator, self).name(arg=OperatorUtils.operator_to_name(self.operator))

    @property
    def children(self):
        children = []
        children.append(self.expression)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


class SymbolNode(BaseAstNode):
    def __init__(self, symbol, **kwargs):
        super(SymbolNode, self).__init__(**kwargs)

        if symbol:
            self.symbol = symbol
            self.id_node = ID(symbol.identifier)
        else:
            raise ValueError('SymbolNode cannot have a None symbol.')

    @property
    def children(self):
        children = []
        children.append(self.id_node)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))

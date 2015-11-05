##
# These classes are AUTO-GENERATED!
# Most of the boilerplate should be written for you, so you should carefully handwrite methods
# that are unique or need special logic for overloading.
##


class BaseAstNode(object):
    def __init__(self, **kwargs):
        pass

    def __str__(self):
        pass


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
        children.extend(self.body_statments)
        return tuple(children)

    def to_3ac(self, a_dummy_parameter, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output


##
# This is a nested declaration of an array with the given type
##
class ArrayDeclaration(BaseAstNode):
    def __init__(self, identifier, dim, dim_qualifiers, type, **kwargs):
        super(ArrayDeclaration, self).__init__(**kwargs)

        self.identifier = identifier
        self.dim = dim
        self.dim_qualifiers = dim_qualifiers

        self.type = type


    @property
    def children(self):
        children = []
        children.append(self.type)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output


##
# REVISIT ME - Might need to swtich attrs to children depending on how we handle arrays
##
class ArrayReference(BaseAstNode):
    def __init__(self, array_name, subscript, **kwargs):
        super(ArrayReference, self).__init__(**kwargs)

        self.array_name = array_name
        self.subscript = subscript



    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



class Assignment(BaseAstNode):
    def __init__(self, op, lvalue, rvalue, **kwargs):
        super(Assignment, self).__init__(**kwargs)

        self.op = op

        self.lvalue = lvalue
        self.rvalue = rvalue


    @property
    def children(self):
        children = []
        children.append(self.lvalue)
        children.append(self.rvalue)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



class BinaryOperator(BaseAstNode):
    def __init__(self, op, lvalue, rvalue, **kwargs):
        super(BinaryOperator, self).__init__(**kwargs)

        self.op = op

        self.lvalue = lvalue
        self.rvalue = rvalue


    @property
    def children(self):
        children = []
        children.append(self.lvalue)
        children.append(self.rvalue)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output


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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



class Constant(BaseAstNode):
    def __init__(self, type, value, **kwargs):
        super(Constant, self).__init__(**kwargs)

        self.type = type
        self.value = value



    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



class Continue(BaseAstNode):
    def __init__(self, **kwargs):
        super(Continue, self).__init__(**kwargs)




    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, continue_to_label, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



class Declaration(BaseAstNode):
    def __init__(self, name, qualifiers, storage, funcspec, type, initialization_value, bitsize, **kwargs):
        super(Declaration, self).__init__(**kwargs)

        self.name = name
        self.qualifiers = qualifiers
        self.storage = storage
        self.funcspec = funcspec

        self.type = type
        self.initialization_value = initialization_value
        self.bitsize = bitsize


    @property
    def children(self):
        children = []
        children.append(self.type)
        children.append(self.initialization_value)
        children.append(self.bitsize)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



class EmptyStatement(BaseAstNode):
    def __init__(self, **kwargs):
        super(EmptyStatement, self).__init__(**kwargs)




    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output


##
# This is the top of the AST
##
class FileAST(BaseAstNode):
    def __init__(self, external_declarations=None, **kwargs):
        super(FileAST, self).__init__(**kwargs)



        self.external_declarations = external_declarations if external_declarations else []

    @property
    def children(self):
        children = []
        children.extend(self.external_declarations)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



class FunctionCall(BaseAstNode):
    def __init__(self, name, arguments, **kwargs):
        super(FunctionCall, self).__init__(**kwargs)


        self.name = name
        self.arguments = arguments


    @property
    def children(self):
        children = []
        children.append(self.name)
        children.append(self.arguments)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



class FunctionDeclaration(BaseAstNode):
    def __init__(self, arguments, type, **kwargs):
        super(FunctionDeclaration, self).__init__(**kwargs)


        self.arguments = arguments
        self.type = type


    @property
    def children(self):
        children = []
        children.append(self.arguments)
        children.append(self.type)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output


class FunctionDefinition(BaseAstNode):
    def __init__(self, declarations, param_declarations, body, **kwargs):
        super(FunctionDefinition, self).__init__(**kwargs)

        self.declarations = declarations
        self.body = body

        self.param_declarations = param_declarations if param_declarations else []

    @property
    def children(self):
        children = []
        children.append(self.declarations)
        children.append(self.body)
        children.extend(self.param_declarations)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output


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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



class ID(BaseAstNode):
    def __init__(self, name, **kwargs):
        super(ID, self).__init__(**kwargs)

        self.name = name



    @property
    def children(self):
        children = []
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



class Label(BaseAstNode):
    def __init__(self, label_name, body_statement, **kwargs):
        super(Label, self).__init__(**kwargs)

        self.label_name = label_name

        self.body_statement = body_statement


    @property
    def children(self):
        children = []
        children.append(self.body_statement)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



class PointerDeclaration(BaseAstNode):
    def __init__(self, qualifiers, type, **kwargs):
        super(PointerDeclaration, self).__init__(**kwargs)

        self.qualifiers = qualifiers

        self.type = type


    @property
    def children(self):
        children = []
        children.append(self.type)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



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


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output


##
# WHAT ARE SOME OF THESE THINGS? I kinda think we can throw this one out since it prolly doesn't generate code.
##
class TypeDeclaration(BaseAstNode):
    def __init__(self, declaration_name, qualifiers, type, **kwargs):
        super(TypeDeclaration, self).__init__(**kwargs)

        self.declaration_name = declaration_name
        self.qualifiers = qualifiers

        self.type = type


    @property
    def children(self):
        children = []
        children.append(self.type)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output



class UnaryOperator(BaseAstNode):
    def __init__(self, operator, expression, **kwargs):
        super(UnaryOperator, self).__init__(**kwargs)

        self.operator = operator

        self.expression = expression


    @property
    def children(self):
        children = []
        children.append(self.expression)
        return tuple(children)

    def to_3ac(self, include_source=False):
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


    # This method will likely be implemented in the BaseAstNode
    # def to_graph_viz_str(self):
    #     descendant_names = ', '.join([child.name() for child in self.children])
    #     output = '{} -> {{}};\n'.format(self, descendant_names)
    #     for child in self.children:
    #         ouptut += child.to_graph_viz_str()
    #     return output


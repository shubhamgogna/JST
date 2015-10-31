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

import sys

# The class for the base AST node
#
# This class will be inherited from for other types of AST nodes. Should hold all common functionality.
#
class BaseAstNode:
    # Initialize node with desired info
    #
    # @param children A list of child nodes
    # @param line_range A tuple of start line and end line for where this node applies
    # @param uuid A unique identifier number from a TicketCounter
    #
    def __init__(self, children=[], line_range=None, uuid=None, **kwargs):

        # initialize children
        self.children = children

        # initialize the line_range
        self.line_range = line_range

        # initialize the uuid
        self.uuid = uuid
        # TODO: Since we have multiple ticket counters, we probably need to pass them in as a param.

    # Define str function to concisely summarize a node with its uuid, name/type, and relevant info
    def __str__(self):
        #TODO: Not sure what all info we want to print here.  Later on will probably need to print more info?
        return '{}_{}'.format(self.uuid, type(self).__name__)


    #Define stub function for converting to 3ac
    def to_3ac(self, include_source=False):
        #TODO
        raise NotImplementedError('Please implement the {}.to_3ac(self) method.'.format(type(self).__name__))


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
        #TODO: May need to fix this
        descendant_names = ', '.join([child.name() for child in self.children])
        output = '{} -> {{}};\\n'.format(self, descendant_names)
        for child in self.children:
            ouptut += child.to_graph_viz_str()
        return output


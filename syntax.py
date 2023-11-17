# Import necessary functions and classes from lexical.py
from lexical import token_patterns, regexAll, tokenize

# Define a Node class to represent nodes in the parse tree and AST
class Node:
    def __init__(self, label, value=None, children=None):
        self.label = label
        self.value = value
        self.children = children if children else []

    def __repr__(self, level=0):
        # Representation of the node, including label and optional value
        ret = "\t" * level + repr(self.label)
        if self.value:
            ret += f"({self.value})"
        ret += "\n"
        for child in self.children:
            # Recursively represent child nodes
            ret += child.__repr__(level + 1)
        return ret

# Define a Parser class for parsing tokens into a parse tree and AST
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = 0
        self.parse_tree = None
        self.ast = None

    def parse(self):
        # Initialize parsing by setting the current token and parsing the expression
        self.current_token = self.tokens[self.index]
        self.parse_tree = self.parse_Expression()
        self.ast = self.build_ast(self.parse_tree)
        return self.parse_tree, self.ast

    def match(self, token_type):
        # Check if the current token matches the expected token type
        if self.current_token[1] == token_type:
            self.index += 1
            if self.index < len(self.tokens):
                # Move to the next token if available
                self.current_token = self.tokens[self.index]
            return True
        return False

    def parse_Expression(self):
        # Parse an expression, which can consist of terms combined with addition or subtraction
        node = Node('Expression')
        node.children.append(self.parse_Term())
        while self.current_token[1] in ['token_plusOp', 'token_minusOp']:
            # Handle addition or subtraction operators
            operator = Node(self.current_token[0])
            self.match(self.current_token[1])
            right = self.parse_Term()
            node.children.extend([operator, right])
        return node

    def parse_Term(self):
        # Parse a term, which can consist of factors combined with multiplication or division
        node = Node('Term')
        node.children.append(self.parse_Factor())
        while self.current_token[1] in ['token_multyOp', 'token_divideOp']:
            # Handle multiplication or division operators
            operator = Node(self.current_token[0])
            self.match(self.current_token[1])
            right = self.parse_Factor()
            node.children.extend([operator, right])
        return node

    def parse_Factor(self):
        # Parse a factor, which can be an integer or an expression in parentheses
        node = Node('Factor')
        if self.current_token[1] == 'token_int':
            # Handle integer
            node.children.append(Node('Integer', self.current_token[0]))
            self.match('token_int')
        elif self.current_token[1] == 'token_LEFT_PAREN':
            # Handle expression in parentheses
            self.match('token_LEFT_PAREN')
            node.children.append(self.parse_Expression())
            self.match('token_RIGHT_PAREN')
        else:
            raise SyntaxError("Invalid factor")
        return node

    def build_ast(self, parse_tree_node):
        # Recursively build the abstract syntax tree (AST) from the parse tree
        if parse_tree_node.label == 'Expression':
            if len(parse_tree_node.children) == 1:
                return self.build_ast(parse_tree_node.children[0])
            else:
                # Handle binary expressions
                operator = parse_tree_node.children[1].label
                left = self.build_ast(parse_tree_node.children[0])
                right = self.build_ast(parse_tree_node.children[2])
                return (operator, left, right)
        elif parse_tree_node.label == 'Term':
            if len(parse_tree_node.children) == 1:
                return self.build_ast(parse_tree_node.children[0])
            else:
                # Handle binary expressions
                operator = parse_tree_node.children[1].label
                left = self.build_ast(parse_tree_node.children[0])
                right = self.build_ast(parse_tree_node.children[2])
                return (operator, left, right)
        elif parse_tree_node.label == 'Factor':
            if len(parse_tree_node.children) == 1:
                return self.build_ast(parse_tree_node.children[0])
            else:
                # Handle expressions in parentheses
                return self.build_ast(parse_tree_node.children[1])
        elif parse_tree_node.label == 'Integer':
            # Convert integer value to an integer
            return int(parse_tree_node.value)
        else:
            raise ValueError("Invalid parse tree node label")

# Function to print the tree representation of a tree or AST
def print_tree_representation(tree, indent=0):
    if isinstance(tree, Node):
        print("    " * indent + tree.label)
        for child in tree.children:
            # Recursively print child nodes
            print_tree_representation(child, indent + 1)
    else:
        print("    " * indent + str(tree))

# Main part of the script
if __name__ == "__main__":
    user_input = input("Enter an arithmetic expression: ")
    tokens = tokenize(user_input)

    parser = Parser(tokens)
    parse_tree, ast = parser.parse()

    print("\nParse Tree:")
    print_tree_representation(parse_tree)

    print("\nAbstract Syntax Tree:")
    print_tree_representation(ast)
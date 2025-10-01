from lexer import Lexer
from parser import Parser
from ast_printer import print_ast

code = """
let x = 10;
let y = 0;
while (x) {
    y = y + x;
    x = x - 1;
}
print(y);
"""

lexer = Lexer(code)
parser = Parser(lexer)
tree = parser.parse()

print("Raw AST:")
print(tree)

print("\nPretty AST:")
print_ast(tree)

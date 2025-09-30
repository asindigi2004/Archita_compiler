from lexer import Lexer
from parser import Parser

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

def print_ast(node, indent=0):
    pad = "  " * indent
    if node is None:
        print(pad + "None")
        return
    if hasattr(node, '__dict__'):
        print(f"{pad}{node.__class__.__name__}")
        for k,v in node.__dict__.items():
            print(f"{pad}  {k}:")
            if isinstance(v, list):
                for item in v:
                    print_ast(item, indent+2)
            else:
                print_ast(v, indent+2)
    else:
        print(pad + str(node))

print_ast(tree)

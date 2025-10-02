from lexer import Lexer
from parser import Parser
from codegen import CodeGen
from vm import VM
import ast_nodes

class ExprParser(Parser):
    """Parse a single expression instead of full program."""
    def parse(self):
        return self.expr()

def run_expr(expr_line: str):
    try:
        # Lex + parse as expression
        lexer = Lexer(expr_line)
        parser = ExprParser(lexer)
        tree = parser.parse()  # returns ast_nodes node

        # Wrap in Print node so VM prints it
        tree = ast_nodes.Print(tree)

        # Codegen
        codegen = CodeGen()
        codegen.generate(tree)

        # VM execution
        vm = VM(codegen.instructions)
        vm.run()
    except Exception as e:
        print(f"[Error] {e}")

def main():
    print("MiniLang Expression Compiler. Type 'exit' to quit.")

    while True:
        line = input(">>> ").strip()
        if line.lower() == "exit":
            break
        if line:
            run_expr(line)

if __name__ == "__main__":
    main()

# run_bytecode.py
from lexer import Lexer
from parser import Parser
from ast_printer import print_ast
from codegen import CodeGen
from vm import VM   # or "from vm import VM" if you're using the if/elif version

SAMPLE = r'''
let x = 10;
let y = 0;
while (x) {
  y = y + x;
  x = x - 1;
}
print(y);
'''

def run(source=SAMPLE, show_ast=True, show_bytecode=True):
    # 1. Lex + Parse
    lexer = Lexer(source)
    parser = Parser(lexer)
    tree = parser.parse()

    # 2. Pretty AST
    if show_ast:
        print("=== Pretty AST ===")
        print_ast(tree)
        print()

    # 3. Codegen
    gen = CodeGen()
    gen.generate(tree)

    if show_bytecode:
        print("=== Bytecode ===")
        for i, instr in enumerate(gen.instructions):
            print(f"{i:03d}: {instr}")
        print()

    # 4. VM Execution
    print("=== VM Output ===")
    vm = VM(gen.instructions)
    vm.run()
    print("=================")


if __name__ == "__main__":
    run()

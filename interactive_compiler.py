# interactive_compiler.py
from lexer import Lexer
from parser import Parser
from ast_printer import print_ast
from codegen import CodeGen
from vm import VM

def run_source(source):
    """Compile and execute a MiniLang program from source string."""
    try:
        # Lex + Parse
        lexer = Lexer(source)
        parser = Parser(lexer)
        tree = parser.parse()

        # Optional: pretty-print AST
        print("\n=== AST ===")
        print_ast(tree)
        print()

        # Generate bytecode
        codegen = CodeGen()
        codegen.generate(tree)

        # Optional: show bytecode
        print("=== Bytecode ===")
        for i, instr in enumerate(codegen.instructions):
            print(f"{i:03d}: {instr}")
        print()

        # Execute VM
        print("=== Output ===")
        vm = VM(codegen.instructions)
        vm.run()
        print("=================\n")

    except Exception as e:
        print(f"[Error] {e}")

def main():
    print("MiniLang Interactive Compiler")
    print("Type your program below. End with an empty line to run.")
    print("Example:")
    print("let x = 5;\nlet y = x + 3;\nprint(y);\n")

    lines = []
    while True:
        try:
            line = input(">>> ")
            if line.strip() == "":
                # compile and run accumulated lines
                if lines:
                    program = "\n".join(lines)
                    run_source(program)
                    lines = []  # clear for next program
                else:
                    print("Exiting compiler.")
                    break
            else:
                lines.append(line)
        except KeyboardInterrupt:
            print("\nExiting compiler.")
            break

if __name__ == "__main__":
    main()

from lexer import Lexer
from parser import Parser
from codegen import CodeGen
from vm import VM

def run_line(source_line: str):
    """Compile and execute a single MiniLang statement or expression."""
    try:
        # Lex + Parse
        lexer = Lexer(source_line)
        parser = Parser(lexer)
        tree = parser.parse()

        # Codegen
        codegen = CodeGen()
        codegen.generate(tree)

        # VM execution
        vm = VM(codegen.instructions)
        vm.run()

    except Exception as e:
        print(f"[Error] {e}")

def main():
    print("MiniLang One-Line Compiler. Type 'exit' to quit.")

    while True:
        try:
            line = input(">>> ").strip()
            if line.lower() == "exit":
                break
            if line:
                run_line(line)
        except KeyboardInterrupt:
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()

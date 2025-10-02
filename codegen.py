# codegen.py
import ast_nodes

class CodeGen:
    def __init__(self):
        self.instructions = []
        self.label_count = 0

    def new_label(self):
        lbl = f"L{self.label_count}"
        self.label_count += 1
        return lbl

    def emit(self, instr):
        self.instructions.append(instr)

    def generate(self, node):
        if isinstance(node, ast_nodes.Program):
            for stmt in node.statements:
                self.generate(stmt)

        elif isinstance(node, ast_nodes.Number):
            self.emit(("PUSH", node.value))

        elif isinstance(node, ast_nodes.Var):
            self.emit(("LOAD", node.name))

        elif isinstance(node, ast_nodes.BinOp):
            self.generate(node.left)
            self.generate(node.right)
            if node.op == "PLUS":
                self.emit(("ADD",))
            elif node.op == "MINUS":
                self.emit(("SUB",))
            elif node.op == "MUL":
                self.emit(("MUL",))
            elif node.op == "DIV":
                self.emit(("DIV",))
            elif node.op == "EQ":
                self.emit(("EQ",))
            elif node.op == "NEQ":
                self.emit(("NEQ",))
            elif node.op == "LT":
                self.emit(("LT",))
            elif node.op == "GT":
                self.emit(("GT",))
            elif node.op == "LE":
                self.emit(("LE",))
            elif node.op == "GE":
                self.emit(("GE",))
            else:
                raise Exception(f"Unknown operator {node.op}")

        elif isinstance(node, ast_nodes.Assign):
            self.generate(node.expr)
            self.emit(("STORE", node.name))

        elif isinstance(node, ast_nodes.Print):
            self.generate(node.expr)
            self.emit(("PRINT",))

        elif isinstance(node, ast_nodes.While):
            start_lbl = self.new_label()
            end_lbl = self.new_label()

            self.emit(("LABEL", start_lbl))
            self.generate(node.cond)
            self.emit(("JUMP_IF_FALSE", end_lbl))
            for stmt in node.body:
                self.generate(stmt)
            self.emit(("JUMP", start_lbl))
            self.emit(("LABEL", end_lbl))

        else:
            raise Exception(f"Unknown AST node: {node}")

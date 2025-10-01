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

            self.emit((f"LABEL", start_lbl))
            self.generate(node.cond)
            self.emit(("JUMP_IF_FALSE", end_lbl))
            for stmt in node.body:
                self.generate(stmt)
            self.emit(("JUMP", start_lbl))
            self.emit((f"LABEL", end_lbl))

        else:
            raise Exception(f"Unknown AST node: {node}")

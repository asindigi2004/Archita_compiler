# test_codegen.py
import unittest
import ast_nodes
from codegen import CodeGen


class TestCodeGen(unittest.TestCase):

    def setUp(self):
        self.cg = CodeGen()

    def gen(self, node):
        self.cg.instructions = []   # reset between tests
        self.cg.generate(node)
        return self.cg.instructions

    # --- Arithmetic ---
    def test_plus(self):
        node = ast_nodes.BinOp(ast_nodes.Number(2), "PLUS", ast_nodes.Number(3))
        instrs = self.gen(node)
        self.assertEqual(instrs, [("PUSH", 2), ("PUSH", 3), ("ADD",)])

    def test_minus(self):
        node = ast_nodes.BinOp(ast_nodes.Number(5), "MINUS", ast_nodes.Number(2))
        instrs = self.gen(node)
        self.assertEqual(instrs, [("PUSH", 5), ("PUSH", 2), ("SUB",)])

    def test_mul(self):
        node = ast_nodes.BinOp(ast_nodes.Number(4), "MUL", ast_nodes.Number(6))
        instrs = self.gen(node)
        self.assertEqual(instrs, [("PUSH", 4), ("PUSH", 6), ("MUL",)])

    def test_div(self):
        node = ast_nodes.BinOp(ast_nodes.Number(8), "DIV", ast_nodes.Number(2))
        instrs = self.gen(node)
        self.assertEqual(instrs, [("PUSH", 8), ("PUSH", 2), ("DIV",)])

    # --- Comparisons ---
    def test_eq(self):
        node = ast_nodes.BinOp(ast_nodes.Var("x"), "EQ", ast_nodes.Number(10))
        instrs = self.gen(node)
        self.assertEqual(instrs, [("LOAD", "x"), ("PUSH", 10), ("EQ",)])

    def test_neq(self):
        node = ast_nodes.BinOp(ast_nodes.Var("y"), "NEQ", ast_nodes.Number(0))
        instrs = self.gen(node)
        self.assertEqual(instrs, [("LOAD", "y"), ("PUSH", 0), ("NEQ",)])

    def test_lt(self):
        node = ast_nodes.BinOp(ast_nodes.Var("a"), "LT", ast_nodes.Var("b"))
        instrs = self.gen(node)
        self.assertEqual(instrs, [("LOAD", "a"), ("LOAD", "b"), ("LT",)])

    def test_gt(self):
        node = ast_nodes.BinOp(ast_nodes.Var("a"), "GT", ast_nodes.Var("b"))
        instrs = self.gen(node)
        self.assertEqual(instrs, [("LOAD", "a"), ("LOAD", "b"), ("GT",)])

    def test_le(self):
        node = ast_nodes.BinOp(ast_nodes.Var("a"), "LE", ast_nodes.Var("b"))
        instrs = self.gen(node)
        self.assertEqual(instrs, [("LOAD", "a"), ("LOAD", "b"), ("LE",)])

    def test_ge(self):
        node = ast_nodes.BinOp(ast_nodes.Var("a"), "GE", ast_nodes.Var("b"))
        instrs = self.gen(node)
        self.assertEqual(instrs, [("LOAD", "a"), ("LOAD", "b"), ("GE",)])

    # --- Assign ---
    def test_assign(self):
        node = ast_nodes.Assign("x", ast_nodes.Number(42))
        instrs = self.gen(node)
        self.assertEqual(instrs, [("PUSH", 42), ("STORE", "x")])

    # --- Print ---
    def test_print(self):
        node = ast_nodes.Print(ast_nodes.Var("x"))
        instrs = self.gen(node)
        self.assertEqual(instrs, [("LOAD", "x"), ("PRINT",)])

    # --- While ---
    def test_while(self):
        node = ast_nodes.While(
            cond=ast_nodes.Var("x"),
            body=[ast_nodes.Assign("x",
                    ast_nodes.BinOp(ast_nodes.Var("x"), "MINUS", ast_nodes.Number(1)))]
        )
        instrs = self.gen(node)

        # structure: LABEL L0, cond, JUMP_IF_FALSE L1, body..., JUMP L0, LABEL L1
        self.assertEqual(instrs[0][0], "LABEL")
        self.assertEqual(instrs[1:], [
            ("LOAD", "x"),
            ("JUMP_IF_FALSE", "L1"),   # label names depend on counter
            ("LOAD", "x"),
            ("PUSH", 1),
            ("SUB",),
            ("STORE", "x"),
            ("JUMP", "L0"),
            ("LABEL", "L1")
        ])


if __name__ == "__main__":
    unittest.main()

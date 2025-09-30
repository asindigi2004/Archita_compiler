# parser.py - recursive descent parser

from lexer import Lexer
import ast_nodes as ast

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current = self.lexer.get_next_token()

    def eat(self, ttype):
        if self.current[0] == ttype:
            self.current = self.lexer.get_next_token()
        else:
            raise Exception(f"Unexpected token {self.current}, expected {ttype}")

    def parse(self):
        stmts = []
        while self.current[0] != 'EOF':
            stmts.append(self.statement())
        return ast.Program(stmts)

    def statement(self):
        t, v = self.current
        if t == 'LET':
            self.eat('LET')
            name = self.current[1]; self.eat('ID')
            self.eat('ASSIGN')
            expr = self.expr()
            self.eat('SEMI')
            return ast.Assign(name, expr)

        if t == 'ID':  # assignment without 'let'
            name = v; self.eat('ID')
            self.eat('ASSIGN')
            expr = self.expr()
            self.eat('SEMI')
            return ast.Assign(name, expr)

        if t == 'PRINT':
            self.eat('PRINT'); self.eat('LPAREN')
            expr = self.expr()
            self.eat('RPAREN'); self.eat('SEMI')
            return ast.Print(expr)

        if t == 'WHILE':
            self.eat('WHILE'); self.eat('LPAREN')
            cond = self.expr(); self.eat('RPAREN')
            self.eat('LBRACE')
            body = []
            while self.current[0] != 'RBRACE':
                body.append(self.statement())
            self.eat('RBRACE')
            return ast.While(cond, body)

        raise Exception(f"Unexpected token {self.current}")

    # expr → term (("+"|"-") term)*
    def expr(self):
        node = self.term()
        while self.current[0] in ('PLUS','MINUS'):
            op = self.current[0]; self.eat(op)
            node = ast.BinOp(node, op, self.term())
        return node

    # term → factor (("*"|"/") factor)*
    def term(self):
        node = self.factor()
        while self.current[0] in ('MUL','DIV'):
            op = self.current[0]; self.eat(op)
            node = ast.BinOp(node, op, self.factor())
        return node

    # factor → INT | ID | "(" expr ")" | "-" factor
    def factor(self):
        t, v = self.current
        if t == 'INT':
            self.eat('INT'); return ast.Number(v)
        if t == 'ID':
            self.eat('ID'); return ast.Var(v)
        if t == 'LPAREN':
            self.eat('LPAREN'); node = self.expr(); self.eat('RPAREN'); return node
        if t == 'MINUS':
            self.eat('MINUS')
            return ast.BinOp(ast.Number(0), 'MINUS', self.factor())
        raise Exception(f"Unexpected factor: {self.current}")

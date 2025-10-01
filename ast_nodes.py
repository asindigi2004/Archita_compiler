class Node:
    pass


class Program(Node):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program(statements={self.statements})"


class Number(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class Var(Node):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Var({self.name})"


class BinOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinOp(left={self.left}, op={self.op}, right={self.right})"


class Assign(Node):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

    def __repr__(self):
        return f"Assign(name={self.name}, expr={self.expr})"


class While(Node):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

    def __repr__(self):
        return f"While(cond={self.cond}, body={self.body})"


class Print(Node):
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"Print(expr={self.expr})"

#ast_nodes.py

class Node:
    pass

class Program(Node):
    def __init__(self,statements):
        self.statements=statements

class Number(Node):
    def __init__(self,value):
        self.value=value

class Var(Node):
    def __init__(self,name):
        self.name=name

class BinOp(Node):
    def __init__(self,left,op,right):
        self.left=left
        self.op=op
        self.right=right

class Assign(Node):
    def __init__(self,name,expr):
        self.name=name
        self.expr=expr

class While(Node):
    def __init__(self,cond,body):
        self.cond=cond
        self.body=body

class Print(Node):
    def __init__(self, expr):
        self.expr = expr

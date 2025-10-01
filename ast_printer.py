from ast_nodes import *

def print_ast(node, indent=0):
    prefix = "  " * indent
    if isinstance(node, Program):
        print(f"{prefix}Program")
        for stmt in node.statements:
            print_ast(stmt, indent + 1)
    elif isinstance(node, Number):
        print(f"{prefix}Number: {node.value}")
    elif isinstance(node, Var):
        print(f"{prefix}Var: {node.name}")
    elif isinstance(node, BinOp):
        print(f"{prefix}BinOp: {node.op}")
        print_ast(node.left, indent + 1)
        print_ast(node.right, indent + 1)
    elif isinstance(node, Assign):
        print(f"{prefix}Assign: {node.name}")
        print_ast(node.expr, indent + 1)
    elif isinstance(node, While):
        print(f"{prefix}While")
        print(f"{prefix}  Condition:")
        print_ast(node.cond, indent + 2)
        print(f"{prefix}  Body:")
        for stmt in node.body:
            print_ast(stmt, indent + 2)
    elif isinstance(node, Print):
        print(f"{prefix}Print")
        print_ast(node.expr, indent + 1)
    else:
        print(f"{prefix}{node}")

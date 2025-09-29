from lexer import Lexer

code = """
let x = 5;
let y = x + 3;
print(y);
while (y) {
  y = y - 1;
}
"""

lexer = Lexer(code)
tokens = []
tok = lexer.get_next_token()
while tok[0] != 'EOF':
    tokens.append(tok)
    tok = lexer.get_next_token()

print(tokens)

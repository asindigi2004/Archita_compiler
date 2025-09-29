# lexer.py - MiniLang Lexer

RESERVED = {
    'let': 'LET',
    'print': 'PRINT',
    'while': 'WHILE',
}

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current = text[self.pos] if text else None

    def advance(self):
        """Move one character ahead."""
        self.pos += 1
        self.current = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current and self.current.isspace():
            self.advance()

    def number(self):
        start = self.pos
        while self.current and self.current.isdigit():
            self.advance()
        return ('INT', int(self.text[start:self.pos]))

    def identifier(self):
        start = self.pos
        while self.current and (self.current.isalnum() or self.current == '_'):
            self.advance()
        word = self.text[start:self.pos]
        return (RESERVED.get(word, 'ID'), word)

    def get_next_token(self):
        while self.current is not None:
            if self.current.isspace():
                self.skip_whitespace()
                continue
            if self.current.isdigit():
                return self.number()
            if self.current.isalpha() or self.current == '_':
                return self.identifier()

            ch = self.current
            self.advance()

            if ch == '+': return ('PLUS', '+')
            if ch == '-': return ('MINUS', '-')
            if ch == '*': return ('MUL', '*')
            if ch == '/': return ('DIV', '/')
            if ch == '=': return ('ASSIGN', '=')
            if ch == ';': return ('SEMI', ';')
            if ch == '(': return ('LPAREN', '(')
            if ch == ')': return ('RPAREN', ')')
            if ch == '{': return ('LBRACE', '{')
            if ch == '}': return ('RBRACE', '}')

            raise Exception(f"Unknown char: {ch}")

        return ('EOF', None)

import re

class Lexer:
    def __init__(self, program):
        self.program = program
        self.tokens = []
        self.lexemes = []
        self.token_patterns = [
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('OPERATOR', r'[+-]'),
            ('SEPARATOR', r';'),
            ('WHITESPACE', r'\s+'),
        ]
        self.current_position = 0

    def get_tokens(self):
        return self.tokens, self.lexemes

    def lexer(self):
        while self.current_position < len(self.program):
            match = None
            for token_type, pattern in self.token_patterns:
                regex = re.compile(pattern)
                match = regex.match(self.program, self.current_position)
                if match:
                    lexeme = match.group(0)
                    if token_type != 'WHITESPACE':  # Ignore whitespace
                        self.tokens.append(token_type)
                        self.lexemes.append(lexeme)
                    self.current_position += len(lexeme)
                    break
            if not match:
                raise ValueError(f"Unexpected character at position {self.current_position}")

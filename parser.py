class SyntaxAnalyzer:
    def __init__(self, tokens, lexemes, print_switch=False, output_file=None):
        self.tokens = tokens
        self.lexemes = lexemes
        self.print_switch = print_switch
        self.output_file = output_file
        self.current_token_index = 0
        self.line_number = 1

    def get_current_token(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index], self.lexemes[self.current_token_index]
        return None, None

    def consume(self):
        self.current_token_index += 1

    def print_production(self, production_rule):
        if self.print_switch and self.output_file:
            self.output_file.write(production_rule + '\n')

    def parse(self):
        # Start parsing with the expression (E)
        self.E()
        if self.current_token_index < len(self.tokens):
            self.error("Unexpected tokens at end of input")

    def E(self):
        self.print_production("E -> T E'")
        self.T()
        self.E_prime()

    def E_prime(self):
        token, lexeme = self.get_current_token()
        if token == 'OPERATOR' and lexeme in ['+', '-']:
            self.print_production("E' -> + T E' | - T E'")
            self.consume()
            self.T()
            self.E_prime()
        else:
            self.print_production("E' -> ε")

    def T(self):
        self.print_production("T -> F T'")
        self.F()
        self.T_prime()

    def T_prime(self):
        token, lexeme = self.get_current_token()
        if token == 'OPERATOR' and lexeme in ['*', '/']:
            self.print_production("T' -> * F T' | / F T'")
            self.consume()
            self.F()
            self.T_prime()
        else:
            self.print_production("T' -> ε")

    def F(self):
        token, lexeme = self.get_current_token()
        if token == 'SEPARATOR' and lexeme == '(':
            self.print_production("F -> ( E )")
            self.consume()  # consume '('
            self.E()
            token, lexeme = self.get_current_token()
            if token == 'SEPARATOR' and lexeme == ')':
                self.consume()  # consume ')'
            else:
                self.error("Expected ')'")
        elif token == 'IDENTIFIER':
            self.print_production("F -> id")
            self.consume()  # consume identifier
        else:
            self.error("Expected identifier or '('")

    def error(self, message):
        token, lexeme = self.get_current_token()
        error_msg = f"Syntax Error: {message} at token '{token}', lexeme '{lexeme}' on line {self.line_number}\n"
        if self.output_file:
            self.output_file.write(error_msg)
        else:
            print(error_msg)

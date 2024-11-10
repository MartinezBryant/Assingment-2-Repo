class SyntaxAnalyzer:
    def __init__(self, tokens, lexemes, print_switch=False, output_file=None):
        self.tokens = tokens
        self.lexemes = lexemes
        self.print_switch = print_switch
        self.output_file = output_file
        self.current_token_index = 0
    
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
    
    def E(self):
        token, lexeme = self.get_current_token()
        self.print_token_and_lexeme(token, lexeme)
        
        if token == 'IDENTIFIER':
            self.print_production("E -> T E’")
            self.T()
            self.E_prime()
        else:
            self.error("Expected identifier at the start of E.")
    
    def E_prime(self):
        token, lexeme = self.get_current_token()
        self.print_token_and_lexeme(token, lexeme)
        
        if token == 'OPERATOR' and lexeme in ['+', '-']:
            self.print_production(f"E’ -> {lexeme} T E’")
            self.consume()
            self.T()
            self.E_prime()
        else:
            self.print_production("E’ -> ε")
    
    def T(self):
        token, lexeme = self.get_current_token()
        self.print_token_and_lexeme(token, lexeme)
        
        if token == 'IDENTIFIER':
            self.print_production("T -> id")
            self.consume()
        else:
            self.error("Expected identifier in T.")
    
    def print_token_and_lexeme(self, token, lexeme):
        if self.output_file:
            self.output_file.write(f"Token: {token}, Lexeme: {lexeme}\n")
    
    def error(self, message):
        if self.output_file:
            self.output_file.write(f"Error: {message}\n")

import re

# Token definitions
KEYWORDS = {"function", "integer", "boolean", "real", "if", "else", "fi", "while", "return", "get", "put"}
OPERATORS = {"==", "!=", ">", "<", "<=", ">=", "+", "-", "*", "/", "="}
SEPARATORS = {"(", ")", "{", "}", ";", ","}

# Regular expressions for FSM
identifier_re = r'^[a-zA-Z][a-zA-Z0-9]*$'
integer_re = r'^[0-9]+$'
real_re = r'^[0-9]+\.[0-9]+$'

# Token types
TOKEN_IDENTIFIER = "identifier"
TOKEN_INTEGER = "integer"
TOKEN_REAL = "real"
TOKEN_KEYWORD = "keyword"
TOKEN_OPERATOR = "operator"
TOKEN_SEPARATOR = "separator"
TOKEN_UNKNOWN = "unknown"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []

    def is_keyword(self, word):
        return word in KEYWORDS

    def is_operator(self, char):
        return char in OPERATORS

    def is_separator(self, char):
        return char in SEPARATORS

    def tokenize(self):
        # Removing comments
        self.source_code = re.sub(r'\[\*.*?\*\]', '', self.source_code)
        
        # Split source code into tokens with regex for operators and separators
        pattern = re.compile(r'\s+|([(){};,])|([<>!=]=|[-+*/=<>])')
        tokens = pattern.split(self.source_code)
        tokens = [t for t in tokens if t and not t.isspace()]  # Remove empty tokens and whitespace

        i = 0
        while i < len(tokens):
            token = tokens[i]

            # Identifiers and Keywords
            if re.match(identifier_re, token):
                if self.is_keyword(token):
                    self.tokens.append((TOKEN_KEYWORD, token))
                else:
                    self.tokens.append((TOKEN_IDENTIFIER, token))

            # Integers
            elif re.match(integer_re, token):
                if i + 1 < len(tokens) and tokens[i + 1] == '.':
                    # Handle real numbers
                    real_number = token + '.' + tokens[i + 2]
                    if re.match(real_re, real_number):
                        self.tokens.append((TOKEN_REAL, real_number))
                        i += 2  # Skip the next two tokens ('.' and fractional part)
                    else:
                        self.tokens.append((TOKEN_UNKNOWN, real_number))
                else:
                    self.tokens.append((TOKEN_INTEGER, token))

            # Real numbers
            elif re.match(real_re, token):
                self.tokens.append((TOKEN_REAL, token))

            # Operators
            elif self.is_operator(token):
                self.tokens.append((TOKEN_OPERATOR, token))

            # Separators
            elif self.is_separator(token):
                self.tokens.append((TOKEN_SEPARATOR, token))

            # Unknown tokens
            else:
                self.tokens.append((TOKEN_UNKNOWN, token))

            i += 1

    def print_tokens(self):
        # Set the header with appropriate spacing
        print(f"{'Token':<15}{'Lexeme':<15}")
        print("-" * 30)
        
        # Print each token and lexeme
        for token, lexeme in self.tokens:
            print(f"{token:<15}{lexeme:<15}")

    def write_tokens_to_file(self, output_file):
        with open(output_file, 'w') as f:
            f.write("Token\tLexeme\n")
            for token, lexeme in self.tokens:
                f.write(f"{token}\t{lexeme}\n")

if __name__ == "__main__":
    # Example source code to be tokenized
    source_code = """ 
    function convert(fahr integer) { 
        return 5 * (fahr - 32) / 9; 
    }
    integer low, high, step; 
    get(low, high, step); 
    while (low <= high) { 
        put(low); 
        put(convert(low)); 
        low = low + step; 
    }
    """
    
    # Instantiate the lexer and tokenize the source code
    lexer = Lexer(source_code)
    lexer.tokenize()
    
    # Print tokens to the console
    lexer.print_tokens()
    
    # Write tokens to a file
    lexer.write_tokens_to_file("tokens_output.txt")

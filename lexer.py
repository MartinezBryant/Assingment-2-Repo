# lexer.py - Replace this with your actual lexer logic
def simple_lexer(input_string):
    # This is a very simple lexer just for demonstration purposes
    token_map = {
        'a': 'id',
        'b': 'id',
        'c': 'id',
        'x': 'id',
        'y': 'id',
        'z': 'id',
        '=': '=',
        '+': '+',
        '-': '-',
        ';': ';'
    }
    tokens = []
    for char in input_string:
        if char in token_map:
            tokens.append(token_map[char])
    return tokens

# Example usage in another file:
# input_tokens = simple_lexer("a = b + c;")

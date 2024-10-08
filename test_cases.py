# test_cases.py - Test cases for the parser

# Import the lexer and parser functions
from lexer import simple_lexer
from parser import parse

# Test Case 1: Simple Assignment
def test_case_1():
    print("Test Case 1: a = b + c;")
    source_code = "a = b + c;"
    input_tokens = simple_lexer(source_code)  # Generate tokens using lexer
    parse(input_tokens)  # Parse the token stream
    print("\n")

# Test Case 2: Expression with Subtraction
def test_case_2():
    print("Test Case 2: x - y;")
    source_code = "x - y;"
    input_tokens = simple_lexer(source_code)  # Generate tokens using lexer
    parse(input_tokens)  # Parse the token stream
    print("\n")

# Test Case 3: Standalone Identifier
def test_case_3():
    print("Test Case 3: z;")
    source_code = "z;"
    input_tokens = simple_lexer(source_code)  # Generate tokens using lexer
    parse(input_tokens)  # Parse the token stream
    print("\n")

# Run all test cases
if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()

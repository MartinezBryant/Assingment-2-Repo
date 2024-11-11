from lexer import Lexer
from parser import SyntaxAnalyzer

def run_test_case(program, test_case_number):
    # Define a single output file for each test case
    output_file_name = f"test_case_{test_case_number}_output.txt"

    # Open the output file for writing
    with open(output_file_name, 'w') as output_file:
        # Step 1: Tokenize the input program using the lexer
        lexer = Lexer(program)
        lexer.tokenize()  # Run the lexer on the program
        tokens, lexemes = zip(*lexer.tokens)  # Get the tokens and lexemes

        # Write Lexer Output
        output_file.write(f"Running test case {test_case_number}:\n\n")
        output_file.write("Lexer Output (Tokens and Lexemes):\n")
        for token, lexeme in zip(tokens, lexemes):
            output_file.write(f"Token: {token}, Lexeme: {lexeme}\n")
        
        # Step 2: Parse the tokens using the syntax analyzer
        parser = SyntaxAnalyzer(
            tokens, 
            lexemes, 
            print_switch=True, 
            output_file=output_file  # Use the same output file for production and errors
        )
        
        # Write Production Output
        output_file.write("\nParser Production Output:\n")
        parser.parse()

        # Errors will be handled within the parser class itself and written to the same file
        output_file.write("\nParser Error Output (if any):\n")
        # Error messages will be written to the same output file during the parse

# Test Case 1: Simple addition
test_case_1 = """
a + c * (d / 4 * e);
"""

# Test Case 2: Simple subtraction
test_case_2 = """
x + 245 / a;
"""

# Test Case 3: Multiple terms with addition and subtraction
test_case_3 = """
a + c/5 * 2;
"""

# Run the test cases with separate output files for each case
run_test_case(test_case_1, 1)
run_test_case(test_case_2, 2)
run_test_case(test_case_3, 3)
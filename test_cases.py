from lexer import Lexer
from parser import SyntaxAnalyzer

def run_test_case(program, output_file):
    # Step 1: Tokenize the input program
    lexer = Lexer(program)
    lexer.lexer()  # Run the lexer on the program
    tokens, lexemes = lexer.get_tokens()  # Get the tokens and lexemes

    # Write tokens and lexemes to the output file
    output_file.write(f"\nRunning test case:\n{program}\n")
    output_file.write("Tokens and Lexemes:\n")
    for token, lexeme in zip(tokens, lexemes):
        output_file.write(f"Token: {token}, Lexeme: {lexeme}\n")
    
    # Step 2: Parse the tokens using the syntax analyzer
    parser = SyntaxAnalyzer(tokens, lexemes, print_switch=True, output_file=output_file)
    parser.parse()

# Open the output file once, before running all test cases
with open('all_test_cases_output.txt', 'w') as output_file:
    # Test Case 1: Simple addition
    program1 = """
    a + b;
    """
    run_test_case(program1, output_file)

    # Test Case 2: Simple subtraction
    program2 = """
    x - y;
    """
    run_test_case(program2, output_file)

    # Test Case 3: Multiple terms with addition and subtraction
    program3 = """
    a + b - c;
    """
    run_test_case(program3, output_file)

    # Test Case 4: Multiple identifiers with no operator
    program4 = """
    a b c;
    """
    run_test_case(program4, output_file)

    # Test Case 5: Operator at the start
    program5 = """
    + a - b;
    """
    run_test_case(program5, output_file)

    # Test Case 6: Empty expression (epsilon case)
    program6 = """
    a;
    """
    run_test_case(program6, output_file)

    # Test Case 7: Expression with multiple terms and different operators
    program7 = """
    a + b - c + d;
    """
    run_test_case(program7, output_file)

    # Test Case 8: Expression with missing operand after operator
    program8 = """
    a + - b;
    """
    run_test_case(program8, output_file)

    # Test Case 9: Long expression
    program9 = """
    x + y - z + w - v + u;
    """
    run_test_case(program9, output_file)

    # Test Case 10: Invalid operator sequence
    program10 = """
    a + - b;
    """
    run_test_case(program10, output_file)

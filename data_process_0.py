import ast
import tokenize
import io

def get_code_tokens(line):
    code_tokens = []
    for token in tokenize.tokenize(io.BytesIO(line.encode('utf-8')).readline):
        code_tokens.append(token.string)
    return code_tokens

def extract_code_and_ast(source_code):
    code_token_sequences = []
    structural_ast_sequences = []

    for line in source_code.split('\n'):
        # Remove non-ASCII characters and comments
        line = ''.join([char for char in line if ord(char) < 128]).split('#')[0]
        line = line.strip()

        if line:
            code_tokens = get_code_tokens(line)

            for token in code_tokens:
                # Replace user-defined variables with symbolic tokens
                if token.isidentifier():
                    token = 'USER_VARIABLE'
                code_token_sequences.append(token)

    # Obtain structural AST sequences
    tree = ast.parse(source_code)
    stack = [tree]
    
    while stack:
        node = stack.pop()
        node_id = ast.dump(node)
        structural_ast_sequences.append(node_id)
        
        for child in ast.iter_child_nodes(node):
            stack.append(child)

    return code_token_sequences, structural_ast_sequences

# Example usage
source_code = """
contract SimpleStorage {
    uint storedData;
    
    function set(uint x) public {
        storedData = x;
    }
    
    function get() public view returns (uint) {
        return storedData;
    }
}
"""

code_tokens, ast_sequences = extract_code_and_ast(source_code)
print("Code Token Sequences:")
print(code_tokens)
print("Structural AST Sequences:")
print(ast_sequences)

import ast

class CustomASTNode:
    def __init__(self, node_type, value):
        self.type = node_type
        self.value = value

def extract_ast_sequences(source_code):
    ast_sequences = []

    tree = ast.parse(source_code)
    stack = [tree]

    while stack:
        node = stack.pop()
        node_type = type(node).__name
        node_value = None

        if isinstance(node, ast.Name):
            node_value = node.id
        elif isinstance(node, ast.Str):
            node_value = node.s
        elif isinstance(node, ast.Num):
            node_value = node.n

        ast_node = CustomASTNode(node_type, node_value)
        ast_sequences.append(ast_node)

        for child in ast.iter_child_nodes(node):
            stack.append(child)

    return ast_sequences

# Example usage
contract_code = """
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

ast_sequences = extract_ast_sequences(contract_code)
for node in ast_sequences:
    print(f"Type: {node.type}, Value: {node.value}")

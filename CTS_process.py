import re

# Function to remove non-ASCII characters and comments
def clean_contract(contract_text):
    # Remove non-ASCII characters
    contract_text = ''.join([char if ord(char) < 128 else ' ' for char in contract_text])

    # Remove single-line comments
    contract_text = re.sub(r'\/\/[^\n]*', '', contract_text)

    # Remove multi-line comments
    contract_text = re.sub(r'\/\*.*?\*\/', '', contract_text, flags=re.DOTALL)

    return contract_text

# Function to replace numerical variables with <NUM>
def replace_numerical_variables(contract_text):
    return re.sub(r'\b\d+\b', '<NUM>', contract_text)

# Function to replace string variables with <STR>
def replace_string_variables(contract_text):
    return re.sub(r'\"[^\"]*\"', '<STR>', contract_text)

# Function to replace address variables with <ADDR>
def replace_address_variables(contract_text):
    return re.sub(r'0x[0-9a-fA-F]+', '<ADDR>', contract_text)

# Read the content of the smart contract file
with open('sample_contract.sol', 'r', encoding='utf-8') as file:
    contract_text = file.read()

# Normalize the contract text
contract_text = clean_contract(contract_text)
contract_text = replace_numerical_variables(contract_text)
contract_text = replace_string_variables(contract_text)
contract_text = replace_address_variables(contract_text)

#print("contract text", contract_text)
# Split the contract text into tokens

tokens = contract_text.split()

# Assign a unique index for each token
token_index = {}
#unique_tokens = set(tokens)
tokens = re.findall(r'\S+|\w+', contract_text)
print("tokens", tokens)
unique_tokens = []
token_indices = {}
index = 0

for token in tokens:
    if token not in token_indices:
        token_indices[token] = index
        unique_tokens.append(token)
        index += 1

# Convert tokens to indices
token_sequences = [token_indices[token] for token in tokens]


# Print the Code Token Sequences
print("Code Token Sequences:")
print(token_sequences)

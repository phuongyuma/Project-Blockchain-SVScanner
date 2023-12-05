const parser = require('solidity-parser-antlr');
const fs = require('fs');

const contractFilePath = 'sample_contract.sol'; // Replace with the path to your Solidity contract file

const contractSource = fs.readFileSync(contractFilePath, 'utf8');
const ast = parser.parse(contractSource, { loc: true });

// Helper function to extract structural information from the AST
function extractStructuralInfo(node) {
    const info = { type: node.type };

    if (node.name) {
        info.name = node.name;
    }

    if (node.children) {
        info.children = node.children.map(extractStructuralInfo);
    }

    return info;
}

const structuralAST = extractStructuralInfo(ast);

console.log(JSON.stringify(structuralAST, null, 2));

// Simple Node.js example
function greet(name = 'World') {
    return `Hello, ${name}!`;
}

function add(a, b) {
    return a + b;
}

module.exports = { greet, add };

// Example usage
if (require.main === module) {
    console.log(greet());
    console.log(greet('GitHub Actions'));
    console.log('2 + 3 =', add(2, 3));
}
const { greet, add } = require('./index');

// Simple tests
console.log('Running tests...');

// Test greet function
const result1 = greet();
if (result1 === 'Hello, World!') {
    console.log('✓ greet() test passed');
} else {
    console.log('✗ greet() test failed');
    process.exit(1);
}

const result2 = greet('Test');
if (result2 === 'Hello, Test!') {
    console.log('✓ greet("Test") test passed');
} else {
    console.log('✗ greet("Test") test failed');
    process.exit(1);
}

// Test add function
const result3 = add(2, 3);
if (result3 === 5) {
    console.log('✓ add(2, 3) test passed');
} else {
    console.log('✗ add(2, 3) test failed');
    process.exit(1);
}

console.log('All tests passed! 🎉');
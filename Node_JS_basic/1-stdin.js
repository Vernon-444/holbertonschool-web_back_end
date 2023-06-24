// Print 'Welcome to Holberton School, what is your name?'
// get input, and display name provided
// when user ends program will display "This important software is now closing"
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});


readline.question("Welcome to Holberton School, what is your name?\n", function(name) {
  console.log(`Your name is: ${name}`);
});

if (!process.stdin.isTTY) {
  process.on('exit', function(code) {
    process.stdout.write("This important software is now closing\n");
    process.exit(0);
  });
}

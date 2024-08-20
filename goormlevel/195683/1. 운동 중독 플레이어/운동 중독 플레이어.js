const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input;
rl.on('line', (line) => {
	input = line;
	rl.close();
});

rl.on('close', () => {
	const[ w, r] = input.split(" ").map(Number);
	console.log(Math.floor((r / 30 + 1) * w))
})
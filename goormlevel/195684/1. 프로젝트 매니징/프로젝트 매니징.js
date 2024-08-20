const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input = [];
rl.on('line', (line) => {
	input.push(line)
});

rl.on('close', () => {
	const [count] = input
	let [h, m] = input[1].split(" ").map(Number);
	m += input.slice(2).map(Number).reduce((acc, next) => acc + next , 0);
	
	
	console.log(`${Math.floor((h + Math.floor(m / 60)) % 24)} ${m % 60}`)
})
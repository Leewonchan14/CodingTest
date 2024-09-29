const fs = require('fs')

const [n, ...inputs] = fs.readFileSync('/dev/stdin').toString().trim().split("\n").map(s => s.trim());


const stk = []

for (let s of inputs) {
  const [a, b] = s.trim().split(" ");

  if (a === "push") {
    stk.push(b);
  } else if (a === "top") {
    console.log(stk.length === 0 ? -1 : stk.at(-1))
  } else if (a === "size") {
    console.log(stk.length)
  } else if (a === "empty") {
    console.log(stk.length === 0 ? 1 : 0)
  } else if (a === "pop") {
    console.log(stk.length === 0 ? -1 : stk.pop())
  }
}

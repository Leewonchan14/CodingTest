const fs = require('fs')

const inputs = fs.readFileSync('/dev/stdin').toString().trim().split("\n").slice(1)

function isCorrect(arr) {
  const stk = []
  for(let s of arr){
    if(s === ")"){
      if(stk.at(-1) !== "(")return false
      stk.pop()
      continue
    }
    stk.push(s)
  }

  return stk.length === 0
}

for(let s of inputs){
  console.log(isCorrect(s.split("")) ? "YES" : "NO")
}
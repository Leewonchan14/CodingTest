const fs = require("fs");

// const [n, m] = [4,2]

const [n, m] = fs
.readFileSync("/dev/stdin")
.toString()
.trim()
.split(" ")
.map(Number);

const recursive = (li) => { 
  if(li.length === m){
    console.log(li.join(" "));
    return;
  }

  for(let i = 1; i<= n; i++){
    if(li.find((v) => v === i)) continue;
    li.push(i);
    recursive(li);
    li.pop();
  }
}

recursive([])

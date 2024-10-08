const fs = require("fs");

// const [n, m] = [4,2]

const [n, m] = fs
.readFileSync("/dev/stdin")
.toString()
.trim()
.split(" ")
.map(Number);

const visited = {}

const recursive = (li) => { 
  if(li.length === m){
    console.log(li.join(" "));
    return;
  }

  for(let i = 1; i<= n; i++){
    if(visited[i]) continue;
    visited[i] = true;
    li.push(i);
    recursive(li);
    li.pop();
    visited[i] = false;
  }
}

recursive([]);

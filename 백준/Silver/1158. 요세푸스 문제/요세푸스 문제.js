const fs = require('fs');

const [n, k] = fs.readFileSync('/dev/stdin').toString().trim().split(" ").map(Number);

let head
let tail

for(let i = 1; i <= n; i++){
    let newNode = {value: i}
    if (i === 1){
        newNode.left = newNode;
        newNode.right = newNode;
        head = newNode;
        tail = newNode;
        continue;
    }
    
    newNode.left = tail;
    newNode.right = head;
    tail.right = newNode;
    head.left = newNode;
    tail = newNode;
}

const result = []

let temp = head;
while(result.length !== n){
    for(let i = 0; i < k - 1; i++){
        temp = temp.right;
    }
    
    temp.left.right = temp.right;
    temp.right.left = temp.left;
    result.push(temp.value);
    temp = temp.right;
}

console.log("<" + result.map(String).join(", ") + ">")
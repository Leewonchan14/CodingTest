const fs = require('fs')

const n = Number(fs.readFileSync('/dev/stdin').toString().trim())

class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class Queue{
    constructor() {
        this.head = null;
        this.tail = null;        
    }

    shift() {
        const value = this.head.value;
        this.head = this.head.right;
        if(!this.head) {
            this.head = null;
            this.tail = null;
        }
        return value;
    }
    
    push(value) {
        const newNode = new Node(value);
        if(!this.tail) {
            this.tail = newNode;
            this.head = newNode;
            return
        }
        
        this.tail.right = newNode;
        newNode.left = this.tail;
        this.tail = newNode;
    }
}

const que = new Queue();

for(let i = 0; i < n; i++){
    que.push(i + 1);
}

while(que.head.right){
    que.shift();
    que.push(que.shift())
}

console.log(que.shift())
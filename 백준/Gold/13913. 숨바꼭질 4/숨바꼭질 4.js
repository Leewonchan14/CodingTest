const fs = require("fs");

const [n, k] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

class Deque {
  head = undefined;
  tail = undefined;
  constructor() {}

  unshift(v) {
    const newNode = { v };
    if (this.head === undefined) {
      head = newNode;
      tail = newNode;
      return;
    }

    this.head.pre = newNode;
    this.head = newNode;
  }
  push(v) {
    const newNode = { v };
    if (this.tail === undefined) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }

    this.tail.next = newNode;
    this.tail = newNode;
  }
  shift() {
    const ret = this.head.v;
    this.head = this.head.next;
    if (!this.head) {
      this.tail = this.head;
    }
    return ret;
  }
  pop() {
    const ret = this.tail.v;
    this.tail = this.tail.pre;
    if (!this.tail) {
      this.head = this.tail;
    }
    return ret;
  }

  isEmpty() {
    return this.head === undefined;
  }
}

const main = () => {
  const graph = {};
  const visited = Array(10 ** 5 + 1).fill(false);
  let total = 0;
  visited[n] = true;
  const que = new Deque();
  que.push([n, 0]);
  while (!que.isEmpty()) {
    let [start, cnt] = que.shift();

    if (start == k) {
      total = cnt;
      break;
    }

    for (let d of [-1, 1, start]) {
      let nn = start + d;

      if (0 <= nn && nn < visited.length && !visited[nn]) {
        graph[nn] = start;
        visited[nn] = true;
        que.push([nn, cnt + 1]);
      }
    }
  }

  const li = [k];
  while (li.at(-1) in graph) {
    li.push(graph[li.at(-1)]);
  }

  li.reverse();

  return [total, li];
};

const [cnt, li] = main();

console.log(cnt);
console.log(li.map(String).join(" "));

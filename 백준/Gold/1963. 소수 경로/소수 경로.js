const fs = require("fs");
const read = fs.readFileSync("dev/stdin").toString().trim();
// const read = `3
// 1033 8179
// 1373 8017
// 1033 1033`;

let [tc, ...arr] = read.split("\n");
tc = Number(tc);
arr = arr.map((ab) => ab.split(" ").map(Number));
const che = Array(10 ** 4).fill(true);

const isPrime = (a) => {
  if (che[4] == false) return che[a];

  for (let i = 2; i < che.length; i++) {
    if (che[i]) {
      for (let j = i * 2; j < che.length; j += i) {
        che[j] = false;
      }
    }
  }

  return che[a];
};

const all_num = (num) => {
  num = String(num);
  const result = [];
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 10; j++) {
      if (i == 0 && j == 0) continue;

      const new_num = Array.from(new String(num));
      new_num[i] = String(j);

      result.push(Number(new_num.join("")));
    }
  }

  return result;
};

const bfs = (a, b) => {
  que = [];
  visited = new Set();
  que.push([a, 0]);
  visited.add(a);

  while (que.length) {
    const [a, cnt] = que.shift();

    if (a == b) {
      return cnt;
    }

    for (let na of all_num(a)) {
      if (isPrime(na) && !visited.has(na)) {
        visited.add(na);
        que.push([na, cnt + 1]);
      }
    }
  }

  return "Impossible";
};

for (let [a, b] of arr) {
  console.log(bfs(a, b));
}

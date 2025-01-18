const fs = require("fs");
const read = fs.readFileSync("dev/stdin").toString().trim();

// const read = `6
// 5 1 0 5`;

var [n, arr] = read.split("\n");

n = Number(n);
let [r1, c1, r2, c2] = arr.split(" ").map(Number);
let d = [
  [-2, -1],
  [-2, 1],
  [0, -2],
  [0, 2],
  [2, -1],
  [2, 1],
];
visited = new Set();

const bfs = () => {
  que = [];
  que.push([r1, c1, 0]);

  visited.add(r1 * n + c1);

  while (que.length) {
    let [r, c, cnt] = que.shift();
    if (r == r2 && c == c2) return cnt;

    for (let dd of d) {
      let nr = r + dd[0];
      let nc = c + dd[1];

      if (nr < 0 || nr >= n || nc < 0 || nc >= n || visited.has(nr * n + nc))
        continue;

      visited.add(nr * n + nc);
      que.push([nr, nc, cnt + 1]);
    }
  }

  return -1;
};

const main = () => {
  return bfs();
};

console.log(main());

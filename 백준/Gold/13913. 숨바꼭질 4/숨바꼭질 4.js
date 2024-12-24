const fs = require("fs");
// const [n, k] = [5, 17];
const [n, k] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const main = () => {
  const graph = {};
  const visited = Array(10 ** 5 + 1).fill(false);
  let total = 0;
  visited[n] = true;
  const que = [[n, 0]];
  while (que.length > 0) {
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

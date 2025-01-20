const fs = require("fs");
const read = fs.readFileSync("dev/stdin").toString().trim();

// const read = `1 1 2`;
// const read = `10 15 35`;

const [a, b, c] = read.split(" ").map(Number);
visited = new Set();
visited.add([a, b, c].sort((a, b) => a - b).join(","));

const findGroup = (li) => {
  const result = [];
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (i === j) continue;

      if (li[i] < li[j]) {
        result.push([i, j]);
      }
    }
  }

  return result;
};

const main = () => {
  que = [[a, b, c]];
  while (que.length) {
    tu = que.shift();

    if (tu[0] == tu[1] && tu[1] == tu[2] && tu[0] == tu[2]) {
      return 1;
    }

    for (let [i, j] of findGroup(tu)) {
      const k = 3 - i - j;

      const li = [0, 0, 0];
      li[i] = tu[i] * 2;
      li[j] = tu[j] - tu[i];
      li[k] = tu[k];
      const key = li.sort((a, b) => a - b).join(",");

      if (!visited.has(key)) {
        visited.add(key);
        que.push(li);
      }
    }
  }

  return 0;
};

console.log(main());

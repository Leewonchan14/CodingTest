const fs = require("fs");

let read = fs.readFileSync("dev/stdin").toString().trim();

let [n, ...arr] = read.split("\n");
arr = arr.map((s) => [...s.trim()]);
const mapper = {};

const setMapper = () => {
  const counter = {};
  let maxv = Math.max(...arr.map((s) => s.length));
  for (let i = -1; i >= -maxv; i--) {
    for (let a of arr) {
      if (!a.at(i)) continue;
      counter[a.at(i)] = (counter[a.at(i)] ?? 0) + 10 ** (i * -1 - 1);
    }
  }

  const sorted = Object.keys(counter).sort((a, b) => counter[b] - counter[a]);

  for (let i = 9; i > 9 - sorted.length; i--) {
    mapper[sorted[9 - i]] = i;
  }
};

const main = () => {
  setMapper();
  return arr.reduce(
    (acc, a) => acc + parseInt(a.map((s) => mapper[s]).join("")),
    0
  );
};

console.log(main());

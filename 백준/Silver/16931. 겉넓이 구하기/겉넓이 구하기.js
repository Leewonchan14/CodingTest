const fs = require("fs");

const [nm, ...arr] = fs.readFileSync("dev/stdin").toString().trim().split("\n");

const [n, m] = nm.split(" ").map(Number);
const maps = arr.map((s) => s.split(" ").map(Number));

const count_line = (li) => {
  let total = li[0];
  for (let i = 1; i < li.length; i++) {
    if (li[i] > li[i - 1]) {
      total += li[i] - li[i - 1];
    }

    if (li[i] < li[i - 1]) {
      total += li[i - 1] - li[i];
    }
  }

  total += li.at(-1);
  return total;
};

const main = () => {
  let total = n * m * 2;
  for (let cols of maps) {
    total += count_line(cols);
  }

  let rows = [];
  for (let c = 0; c < maps[0].length; c++) {
    rows.push([]);
    for (let r = 0; r < maps.length; r++) {
      rows[c].push(maps[r][c]);
    }
  }

  for (let rr of rows) {
    total += count_line(rr);
  }

  return total;
};

console.log(main());

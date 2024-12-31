const fs = require("fs");
let read = fs.readFileSync("dev/stdin").toString().trim();

let [n, ...maps] = read.split("\n");
n = Number(n);

maps = maps.map((s) => s.split(" ").map(Number));

const compact = (li) => {
  let comp = li.filter((s) => s != 0);
  for (let i = 0; i < comp.length - 1; i++) {
    if (comp[i] == comp[i + 1]) {
      comp[i] *= 2;
      comp[i + 1] = 0;
    }
  }
  comp = comp.filter((s) => s != 0);
  const rest = new Array(li.length - comp.length).fill(0);
  return [...comp, ...rest];
};

const left = (maps) => {
  return maps.map((r) => compact(r));
};

const right = (maps) => {
  return maps.map((r) => compact(r.reverse()).reverse());
};

const flip = (maps) => {
  new_maps = [];
  for (let c = 0; c < maps[0].length; c++) {
    new_maps.push([]);
    for (let r = 0; r < maps.length; r++) {
      new_maps[c].push(maps[r][c]);
    }
  }
  return new_maps;
};

const up = (maps) => {
  return flip(left(flip(maps)));
};

const down = (maps) => {
  return flip(right(flip(maps)));
};

const funcs = [up, right, down, left];

const combiH = (n, k) => {
  const li = [];
  const result = [];
  const recur = () => {
    if (li.length == k) {
      result.push([...li]);
      return;
    }

    for (let i = 0; i < n; i++) {
      li.push(i);
      recur();
      li.pop();
    }
  };

  recur();

  return result;
};

const main = () => {
  let maxv = 0;
  for (let li of combiH(4, 5)) {
    let n_maps = maps.map((s) => Array.from(s));
    for (let i of li) {
      n_maps = funcs[i](n_maps);
    }

    maxv = Math.max(maxv, Math.max(...n_maps.map((s) => Math.max(...s))));
  }

  return maxv;
};

console.log(main());

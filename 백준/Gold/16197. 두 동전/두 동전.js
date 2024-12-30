const fs = require('fs')
const read = fs.readFileSync('dev/stdin').toString().trim()


let [nm, ...arr] = read.split("\n");
const [n, m] = nm.split(" ").map(Number);
arr = arr.map((s) => s.split(""));
const visited = {
  visit: [],
  isIn(y1, x1, y2, x2) {
    const key = y2 * n + x2;
    return key in this.visit[y1][x1];
  },
  add(y1, x1, y2, x2) {
    this.visit[y1][x1][y2 * n + x2] = true;
  },
  init() {
    const coin = [];
    for (let r = 0; r < n; r++) {
      visited.visit.push([]);
      for (let c = 0; c < m; c++) {
        visited.visit.at(-1).push({});
        if (arr[r][c] == "o") {
          coin.push([r, c]);
        }
      }
    }

    return coin;
  },
};

const dy = [0, -1, 0, 1];
const dx = [-1, 0, 1, 0];

const isOut = (y, x) => {
  return !(0 <= y && y < n && 0 <= x && x < m);
};

const isOutOnlyOne = (y1, x1, y2, x2) => {
  const a = isOut(y1, x1);
  const b = isOut(y2, x2);
  return (a || b) && !(a && b);
};

const isLoad = (y, x) => {
  return !isOut(y, x) && arr[y][x] != "#";
};

const bfs = (y1, x1, y2, x2) => {
  const que = [[y1, x1, y2, x2, 0]];
  visited.add(y1, x1, y2, x2);

  while (que.length > 0) {
    const item = que.shift();
    y1 = item[0];
    x1 = item[1];
    y2 = item[2];
    x2 = item[3];
    const cnt = item[4];

    if (cnt >= 10) return -1;

    for (let i = 0; i < 4; i++) {
      const ny1 = y1 + dy[i];
      const nx1 = x1 + dx[i];
      const ny2 = y2 + dy[i];
      const nx2 = x2 + dx[i];

      if (isOutOnlyOne(ny1, nx1, ny2, nx2)) {
        return cnt + 1;
      }

      if (
        isLoad(ny1, nx1) &&
        !isLoad(ny2, nx2) &&
        !visited.isIn(ny1, nx1, y2, x2)
      ) {
        visited.add(ny1, nx1, y2, x2);
        que.push([ny1, nx1, y2, x2, cnt + 1]);
      }
      if (
        isLoad(ny2, nx2) &&
        !isLoad(ny1, nx1) &&
        !visited.isIn(y1, x1, ny2, nx2)
      ) {
        visited.add(y1, x1, ny2, nx2);
        que.push([y1, x1, ny2, nx2, cnt + 1]);
      }

      if (
        isLoad(ny2, nx2) &&
        isLoad(ny1, nx1) &&
        !visited.isIn(ny1, nx1, ny2, nx2)
      ) {
        visited.add(ny1, nx1, ny2, nx2);
        que.push([ny1, nx1, ny2, nx2, cnt + 1]);
      }
    }
  }

  return -1;
};

const main = () => {
  const coin = visited.init();
  console.log(bfs(...coin[0], ...coin[1]));
};

main();

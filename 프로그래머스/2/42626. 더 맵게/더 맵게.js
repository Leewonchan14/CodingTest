let heap = [];

function swap(a,b){
  let temp = heap[a];
  heap[a] = heap[b];
  heap[b] = temp;
}

function heapify_down() {
  let temp = 0;

  while (true) {
    let left = temp * 2 + 1;
    let right = temp * 2 + 2;
    let smallest = temp;

    if (left < heap.length && heap[left] < heap[smallest]) {
      smallest = left;
    }
    if (right < heap.length && heap[right] < heap[smallest]) {
      smallest = right;
    }
    if (smallest === temp) {
      break;
    }
    swap(temp, smallest);
    temp = smallest;
  }
}

function heapify_up() {
  let temp = heap.length - 1;
  let par = Math.floor((temp - 1) / 2);
  while (temp !== 0 && heap[temp] < heap[par]) {
    swap(par, temp);
    temp = par;
    par = Math.floor((temp - 1) / 2);
  }
}


function push(v) {
  heap.push(v)
  heapify_up();
}

function popleft() {
  const rt = heap[0];
  swap(0, heap.length - 1)
  heap.pop()
  heapify_down();
  return rt;
}

function solution(scoville, K) {
  for (let i of scoville) {
    push(i);
  }

  let cnt = 0;

  while (heap.length >= 2 && heap[0] < K) {
    let a = popleft();
    let b = popleft() * 2
    push(a + b);
    cnt += 1;
  }

  return heap[0] >= K ? cnt : -1;
}

// console.log(solution([1, 2, 3, 9, 10, 12], 7));
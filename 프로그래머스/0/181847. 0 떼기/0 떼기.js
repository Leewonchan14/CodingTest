function solution(n_str) {
    return [...n_str].reduce((acc, v, i) => acc === "" && v === "0" ? "" : acc + v, "")
}
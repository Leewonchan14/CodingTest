tops = [["N" if i == "0" else "S" for i in input().strip()] for _ in range(4)]
n = int(input())

options = [list(map(int, input().split())) for _ in range(n)]
options = [[i[0] - 1, ("LEFT" if i[1] == -1 else "RIGHT")] for i in options]
# [[k1, "LEFT"], [k2, "RIGHT"], ...]

RIGHT_IDX = 2
LEFT_IDX = 6

def spin(k, direct, source):
    if k < 0 or k >= 4:
        return
    
    top_right = tops[k][RIGHT_IDX]
    top_left = tops[k][LEFT_IDX]
    
    other_direct = "RIGHT" if direct == "LEFT" else "LEFT"
    if direct == "LEFT":
        tops[k] = tops[k][1:] + [tops[k][0]]
    else:
        tops[k] = [tops[k][-1]] + tops[k][:-1]
        
    
    if k - 1 >= 0 and k - 1 != source and top_left != tops[k - 1][RIGHT_IDX]:
        spin(k - 1, other_direct, k)
        
    if k + 1 < 4 and k + 1 != source and top_right != tops[k + 1][LEFT_IDX]:
        spin(k + 1, other_direct, k)

for kk, dd in options:
    spin(kk, dd, -1)
    
print(int("".join(["1" if t[0] == "S" else "0" for t in tops[::-1]]), 2))


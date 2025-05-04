tops = [["N" if i == "0" else "S" for i in input().strip()] for _ in range(4)]
n = int(input())

options = [[int(i) for i in input().split()] for _ in range(n)]
options = [[i[0] - 1, "LEFT" if i[1] == -1 else "RIGHT"] for i in options]

LEFT_IDX = 6
RIGHT_IDX = 2

def spin(k, direct, source):
    top_left = tops[k][LEFT_IDX]
    top_right = tops[k][RIGHT_IDX]
    
    other_direct = "LEFT" if direct == "RIGHT" else "RIGHT"
    
    if direct == "LEFT":
        tops[k] = tops[k][1:] + [tops[k][0]]
    else:
        tops[k] = [tops[k][-1]] + tops[k][:-1]
        
    if k - 1 != source and k - 1 >= 0 and top_left != tops[k - 1][RIGHT_IDX]:
        spin(k - 1, other_direct, k)
        
    if k + 1 != source and k + 1 <= 3 and top_right != tops[k + 1][LEFT_IDX]:
        spin(k + 1, other_direct, k)
        
        
for k, direct in options:
    spin(k, direct, -1)

t12 = [t[0] for t in tops]

bit_t12 = ["1" if t == "S" else "0" for t in t12]

print(int("".join(bit_t12[::-1]), 2))
    

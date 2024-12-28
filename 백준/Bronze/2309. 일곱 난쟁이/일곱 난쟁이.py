keys = [int(input()) for i in range(9)]

sums = sum(keys)

def main():
    for i in range(8):
        for j in range(i + 1, 9):
            if sums - keys[i] - keys[j] == 100:
                li = [keys[k] for k in range(9) if k != i and k != j]
                li.sort()
                print(*li)
                return
            
            
main()
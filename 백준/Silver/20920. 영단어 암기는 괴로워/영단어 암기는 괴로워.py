# 자주 나오는 단어일수록 앞에 배치한다.
# 해당 단어의 길이가 길수록 앞에 배치한다.
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
# $M$이상인 단어들만 외운다고 한다.
# 7 4
# apple
# ant
# sand
# apple
# append
# sand
# sand
import sys

n, m, = map(int, input().split())
dic = {}
for i in range(n):
    s = sys.stdin.readline().rstrip()
    if len(s) >= m:
        dic[s] = dic.get(s, 0) + 1

li = list(dic.items())
li.sort(key=lambda i: (1 / i[1], 1/len(i[0]), i[0]))
for item in li:
    print(item[0])
    

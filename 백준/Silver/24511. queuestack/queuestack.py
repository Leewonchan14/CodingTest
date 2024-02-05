import sys
from collections import deque

n = int(input())
isStack = sys.stdin.readline().rstrip().split()

in_ = sys.stdin.readline().rstrip().split()

in_ = [in_[i] for i in range(len(in_)) if isStack[i] == "0"]

sys.stdin.readline().rstrip()

s = sys.stdin.readline().rstrip().split()

s_ = s[:len(s) - len(in_)]

in__ = in_[::-1]
if len(s) < len(in_):
    in__ = in__[:len(s)]
    s_ = []

print(" ".join(sum((in__, s_), [])))

n, k = map(int, input().split())

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

head = None
tail = None
for i in range(1, n + 1):
    new_node = Node(i)
    if not tail:
        new_node.left = new_node
        new_node.right = new_node
        head = new_node
        tail = new_node
        continue

    new_node.right = head
    new_node.left = tail
    tail.right = new_node
    head.left = new_node
    tail = new_node

temp = head

result = []

while len(result) != n:
    for i in range(k - 1):
        temp = temp.right

    temp.left.right = temp.right
    temp.right.left = temp.left
    result.append(temp.value)
    temp = temp.right

print("<" + ", ".join(map(str, result)) + ">")




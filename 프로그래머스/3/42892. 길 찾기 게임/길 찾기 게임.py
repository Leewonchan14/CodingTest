import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, value, num):
        self.left = None
        self.right = None
        self.value = value
        self.num = num


def insert(parent_node, new_node):
    if not parent_node:
        return new_node

    if new_node.value < parent_node.value:
        parent_node.left = insert(parent_node.left, new_node)
    else:
        parent_node.right = insert(parent_node.right, new_node)

    return parent_node


def preorder(root, ls):
    if not root:
        return
    ls.append(root.num)
    preorder(root.left, ls)
    preorder(root.right, ls)


def postorder(root, ls):
    if not root:
        return
    postorder(root.left, ls)
    postorder(root.right, ls)
    ls.append(root.num)


def solution(nodeinfo):
    nodeinfo = [(a, *b) for a, b in enumerate(nodeinfo)]

    nodeinfo.sort(key=lambda x: (-x[2], x[1]), reverse=True)

    root = None
    while nodeinfo:
        num, value, *_ = nodeinfo.pop()
        new_node = Node(value, num + 1)
        root = insert(root, new_node)

    result = [[], []]
    preorder(root, result[0])
    postorder(root, result[1])
    return result


# print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))

from typing import *
from collections import deque


class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode'=None, right: 'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right


"""
1. 如果给定的数组是符合完全二叉树，即长度 = 2 * n - 1，n为层数
"""
# 递归
def build_tree1(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = build_tree1(arr, 2 * i + 1)
    root.right = build_tree1(arr, 2 * i + 2)
    return root

# 迭代
def build_tree2(arr):
    n = len(arr)
    nodes = []
    for i in range(n):
        nodes.append(TreeNode(arr[i]) if arr[i] else None)
    for i in range(n):
        if nodes[i] is not None:
            if 2 * i + 1 < n:
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < n:
                nodes[i].right = nodes[2 *  i + 2]
    return nodes[0]



"""
2. 力扣中的形式：如果给定的数组不一定符合完全二叉树，而是层序遍历，且最后一层到最后一个节点就停止
例：中序遍历第一个样例 [1, null, 2, 3]
    1
     \
      2
     /
    3
"""
def build_tree3(arr):
    if not arr:
        return None
    n = len(arr)
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q:
        node = q.popleft()
        if i < n and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < n and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root



def tree_to_list(root):
    ans = []
    if root is None:
        return ans
    q = deque([root])
    while q:
        lvl = []
        for _ in range(len(q)):
            curr = q.popleft()
            if curr:
                lvl.append(curr.val)
                q.append(curr.left)
                q.append(curr.right)
            else:
                lvl.append(None)
        ans.append(lvl)
    ans = [i for x in ans for i in x]
    # 去掉结尾的None，保证到最后一层最后一个有值的node为止
    while ans[-1] is None:
        ans.pop()
    return ans


arr1 = [1,2,3,4,5,None,8,None,None,6,7,None,None,9,None]  # 完全二叉树
# arr1 = [1, None, 2, None, None, 3, None]
root1 = build_tree1(arr1)
root2 = build_tree2(arr1)

print(tree_to_list(root1))
print(tree_to_list(root2))

arr2 = [1,2,3,4,5,None,8,None,None,6,7,9]  # 力扣样例格式
# arr2 = [1, None, 2, 3]
root3 = build_tree3(arr2)
print(tree_to_list(root3))






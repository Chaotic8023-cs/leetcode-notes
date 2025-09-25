from collections import deque
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    层序遍历：树左下角的值其实就是最后一层最左边的值，所以用层序遍历即可。每次记录每层的第一个节点，当层序遍历完后，则为最后一层的第一个节点。
    """
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        prev = None  # 用来记录每层的第一个节点
        q = deque([root])
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if i == 0:  # 记录每层的第一个节点，当循环完后就是最后一层的第一个节点
                    prev = curr
        return prev.val

    """
    递归写法（可以不用记）：找最下层最左边的叶子节点其实就是找深度最大的第一个叶子节点！所以一个先序遍历就行，每次遇到深度更大的叶子节点就
    更新一次ans即可。
    """
    def findBottomLeftValue1(self, root: Optional[TreeNode]) -> int:
        def traverse(root, depth):
            nonlocal max_depth, ans
            if not root:
                return
            if not root.left and not root.right and depth > max_depth:  # 只记录拥有更大深度的叶子节点
                max_depth = depth
                ans = root.val
            traverse(root.left, depth + 1)
            traverse(root.right, depth + 1)

        max_depth = 0
        ans = 0
        traverse(root, 1)
        return ans
    

# 巧妙解法：从右到左层序遍历，最后一个节点一定是左下角！
class Solution1:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            node = q.popleft()
            # 从右到左，所以先加right
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val





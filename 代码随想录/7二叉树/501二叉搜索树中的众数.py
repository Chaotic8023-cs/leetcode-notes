from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    遍历的同时更新ans：中序遍历BST，并记录当前元素的count，同时每次更新ans，根据当前遍历元素目前的count和已经记录的max_count。
    """
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if not root:
                return
            # 左
            traverse(root.left)
            # 中
            nonlocal prev, count, max_count, ans
            # 先根据prev和curr（root.val）来更新count。更新后count和curr统一了，即curr当前一共出现count次
            if prev is None:  # 注意这里prev是数值，不能用if not prev来检查prev是否为None，因为如果prev是0也会是True！
                count = 1
            elif root.val == prev:
                count += 1
            else:  # root.val != prev
                count = 1
            # 更新prev指针
            prev = root.val
            # 然后在每一步，都进行结果的更新，这样遍历完了也就更新完了。可以避免如果只在元素交换时更新，遍历完如果元素没变，还得多更新一次
            if count == max_count:  # 等于max_count了就记录当前的元素
                ans.append(root.val)
            if count > max_count:  # 大于max_count了就清空ans（即删除之前出现次数更小的那些元素），然后加入现在这个目前freq最高的元素
                max_count = count
                ans = [root.val]  # 清空ans并更新为curr，因为curr出现次数最大了
            # 右
            traverse(root.right)

        prev = None
        count = 0
        max_count = 0
        ans = []
        traverse(root)
        return ans


    """
    按普通二叉树对待：直接遍历二叉搜索树然后记录所有元素的count，最后选出众数即可
    """
    def findMode1(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root, freq):
            if not root:
                return
            traverse(root.left, freq)
            freq[root.val] = freq.get(root.val, 0) + 1
            traverse(root.right, freq)

        freq = {}
        traverse(root, freq)  # 遍历BST并记录元素的frequency
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        mode = freq[0][1]
        ans = []
        # 选出出现频率最高的一个或多个数
        for i in range(len(freq)):
            if freq[i][1] == mode:
                ans.append(freq[i][0])
            else:
                break
        return ans


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(0, None, TreeNode(0))
    print(sol.findMode(root))





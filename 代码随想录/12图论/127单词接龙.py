from collections import deque
from typing import *
# https://kamacoder.com/problempage.php?pid=1183


class Solution:
    """
    BFS：既然要找最短路径，则用BFS，BFS找到的答案一定是最短路径！
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)  # 转成set大幅提高效率，O(n)查询变O(1)
        if endWord not in wordList:
            return 0
        chars = "abcdefghijklmnopqrstuvwxyz"
        visited = set()
        q = deque([(beginWord, 1)])  # 用一个count来记录路径长度（注意，这次和岛屿面积不一样，岛屿面积是算q一共pop掉了几个元素，而算path长度则是看搜索树有几层）
        while q:
            word, count = q.popleft()
            if word == endWord:
                return count
            for i in range(len(word)):
                for c in chars:
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordList and next_word not in visited:
                        visited.add(next_word)
                        q.append((next_word, count + 1))
        return 0


"""
相似题目：卡码110
https://kamacoder.com/problempage.php?pid=1183
此题beginStr和endStr都不在wordList中
"""


def main():
    def diff(c1, c2):
        cnt = 0
        for i in range(len(c1)):
            if c1[i] != c2[i]:
                cnt += 1
        return cnt

    # 读取数据
    n = int(input())
    beginStr, endStr = input().split()
    strList = []
    for _ in range(n):
        strList.append(input())
    strList = set(strList)
    # 解题
    chars = "abcdefghijklmnopqrstuvwxyz"
    q = deque([(beginStr, 1)])
    visited = set()
    ans = 0
    while q:
        curr_word, path_len = q.popleft()
        if diff(curr_word, endStr) == 1:  # 因为endStr不在wordList中，所以需要手动检查!
            ans = path_len + 1
            break
        for i in range(len(curr_word)):
            for c in chars:
                w = curr_word[:i] + c + curr_word[i + 1:]
                if w in strList and w not in visited:
                    visited.add(w)
                    q.append((w, path_len + 1))
    # 打印答案
    print(ans)


if __name__ == '__main__':
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.ladderLength(beginWord, endWord, wordList))
















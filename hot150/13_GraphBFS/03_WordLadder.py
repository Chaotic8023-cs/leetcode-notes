# 127
from typing import *
from utils.pprintdp import pprintdp
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        此题其实和#433一样，只是时间限制更严
        如果用visited就会超时，所以我们直接从wordList remove掉见过的word来防止每次都得遍历一次整个wordList
        需要注意的是，不能变loop一个list边remove它的element，这会使得iterator跳过过下一个element，因为remove掉一个element
        后面的index都变了，所以要注意！
        我们使用set，因为wordList很大，所以我们直接对current word进行改变，把所有能变一个字母的可能都试一下，这样可以找出这个word变化后
        在wordList中所有的情况，大大减少了search space，所以是efficient的
        """
        q = deque([beginWord])
        dic = set(wordList)
        count = 1  # ladder的长度包含beginWord
        if beginWord in dic:
            dic.remove(beginWord)
        while q:
            for _ in range(len(q)):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return count
                # 直接变curr_word，找出在wordList中所有可能的变化
                for i in range(len(curr_word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = curr_word[:i] + c + curr_word[i+1:]
                        if next_word in dic:
                            dic.remove(next_word)
                            q.append(next_word)
            count += 1
        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    sol = Solution()
    print(sol.ladderLength(beginWord, endWord, wordList))


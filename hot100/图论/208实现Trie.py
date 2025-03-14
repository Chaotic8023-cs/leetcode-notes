from typing import *


class Node:
    def __init__(self):
        # 每层存26个字母的指针
        self.children = [None] * 26
        self.end = False  # end标记：当前字母为某个单词的结尾（标准Trie无重复，所以一个boolean即可）

"""
用一个树实现即可，每层存26个字母的指针，这样访问某个字母就是O(1)
"""
class Trie:
    def __init__(self):
        self.root = Node()  # root为根节点，第一个字母在从第二层开始，即从root的children中开始

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if curr.children[ord(c) - ord('a')] is None:
                curr.children[ord(c) - ord('a')] = Node()
            curr = curr.children[ord(c) - ord('a')]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if curr.children[ord(c) - ord('a')] is None:
                return False
            curr = curr.children[ord(c) - ord('a')]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if curr.children[ord(c) - ord('a')] is None:
                return False
            curr = curr.children[ord(c) - ord('a')]
        return True





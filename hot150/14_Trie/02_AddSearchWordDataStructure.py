# 211
from typing import *


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if cur.children[ord(c) - ord('a')] is None:
                cur.children[ord(c) - ord('a')] = TrieNode()
            cur = cur.children[ord(c) - ord('a')]
        cur.is_end = True

    # self try
    def dot_search(self, node: TrieNode, word: str):
        if not word:  # len(word) == 0
            return node.is_end  # found
        if word[0] != '.':
            """
            比如search ab，首先是在root找ab，看有没有a的node，如果有，则继续在node a找b
            即等word为空时，我们是在node b找空，则直接返回当前的node(b)是否是word end即可
            """
            if node.children[ord(word[0]) - ord('a')] is None:
                return False
            return self.dot_search(node.children[ord(word[0]) - ord('a')], word[1:])
        else:
            for i in range(26):  # dot 可以匹配任意一个字母，所以进行遍历
                if node.children[i] is not None:
                    if self.dot_search(node.children[i], word[1:]):
                        return True
            return False


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.dot_search(self.trie.root, word)


if __name__ == '__main__':
    dic = WordDictionary()
    dic.addWord("bad")
    dic.addWord("dad")
    dic.addWord("mad")
    print(dic.search(".a."))




# 208
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

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if cur.children[ord(c) - ord('a')] is None:
                return False
            cur = cur.children[ord(c) - ord('a')]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        # 和search一抹一样只是最后一个node不需要是end
        cur = self.root
        for c in prefix:
            if cur.children[ord(c) - ord('a')] is None:
                return False
            cur = cur.children[ord(c) - ord('a')]
        return True

    def delete(self, word: str):
        if self.search(word):
            self._delete_word(self.root, word)  # in-place, the trie is modified during the recursive delete
            return True
        return False

    def _count(self, node):
        return sum([1 for i in range(len(node.children)) if node.children[i] is not None])

    def _delete_word(self, node: TrieNode, word: str):
        if not word:
            if self._count(node) > 0:  # last node has children -> word to be deleted is a prefix of other words
                node.is_end = False  # mark this last node in the prefix not an ending word node
                return node
            return None
        if node.children[ord(word[0]) - ord('a')] is None:  # word not present in Trie -> no change
            return node  # return same copy, so no change to the trie
        # replace with new nodes after recursive deletion (the nodes below can be unchanged/tail deleted/all deleted)
        node.children[ord(word[0]) - ord('a')] = self._delete_word(node.children[ord(word[0]) - ord('a')], word[1:])
        # if after recursive deletion of the children the current node has no children left, then current node
        # can be safely deleted by returning None to the upper level recursion
        if self._count(node) > 0:
            return node
        return None


class TrieNode1:
    def __init__(self):
        self.children = {x: None for x in 'abcdefghijklmnopqrstuvwxyz'}
        # 注意，这个count可能在中间node，比如插入了app和apple，那么中间的p的count就是1！
        self.count = 0  # indicate the number of word ending at this node，用来记录单词结尾


# self try：应该改进，用array更快!
class Trie1:
    """
    前缀树实现方式如下：
    每个node存一个children，包含对应所有alphabet里的字母的pointer
    如果a的pointer不是None，即说明root下有个node a
    每个node都有一个字母表大小的pointer list，来记录它下面的nodes
    """

    def __init__(self):
        self.root = TrieNode1()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if cur.children[c] is None:
                cur.children[c] = TrieNode1()
            cur = cur.children[c]
        cur.count += 1

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if cur.children[c] is None:
                return False
            cur = cur.children[c]
        return cur.count > 0  # if count > 0 means this is the end of the word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if cur.children[c] is None:
                return False
            cur = cur.children[c]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("and")
    trie.insert("an")
    trie.insert("ant")
    trie.insert("dad")
    trie.insert("do")
    trie.delete("and")

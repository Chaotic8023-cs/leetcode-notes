# 146
from typing import *


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        """
        用双向链表(head和tail)来按照访问顺序存储nodes，最近使用的在head
        用哈希表cache来记录每个node在双向链表中的位置，即直接存储node本身(也就是指针)
        """
        self.size = 0
        self.cache = {}
        # head和tail作为双向链表的两个头，里面的才是真正的elements
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        每次get即一次访问，将这个node移动到head
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        如果key已经有了，则通过哈希表cache找到node，更新value，并移动到head
        如果没有，则插入到head，并检查cache是否已满
        满了的话把LRU node移除掉，即链表末尾的那个node
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                node = self.remove_tail()
                self.size -= 1
                self.cache.pop(node.key)

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_node(self, node):
        # 不用管这个node的next和prev指针，因为如果之后要移动到head，add_to_head里会更新这两个指针
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node






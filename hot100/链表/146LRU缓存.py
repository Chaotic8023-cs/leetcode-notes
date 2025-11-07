from typing import *


class Node:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next

"""
双向链表+哈希表
1. 双向链表：
    用head和tail表示头和尾巴，这两个只是头部和尾部的端点节点，为了方便操作而创造的，真正的节点是要加入到他们两个的中间的。
    从头到尾的节点顺序是按使用顺序排列的，最新被使用的在头，最久没被使用的在尾
2. 哈希表：
    用一个mapping来记录key到节点的映射，用来快速找到双向链表中的节点
    
get：
    get一次即用过一次，也就是我们要使这个node变为最新被使用过的，所以我们先用mapping得到节点，然后移动到头部
    
put；
    如果key已经存在，则更新value，并且移动到头部（也记作使用一次）；如果key不存在，则直接创建一个Node加入到头部。
    如果超容了，则删除最久未使用的节点，即从尾部删除一个节点。
"""
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.mapping = {}  # 哈希表：key -> 节点
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        # 如果key存在，则移动到head，表示这个node最新被用过
        node = self.mapping[key]
        self.remove_node(node)
        self.add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            node = self.mapping[key]
            node.val = value  # 如果存在则要更新value
            self.remove_node(node)
            self.add_to_head(node)
        else:
            node = Node(key, value)
            self.add_to_head(node)
            self.mapping[key] = node
            self.size += 1
            if self.size > self.capacity:  # 如果超容，则删除最旧的node，即最后一个node
                node = self.tail.prev
                self.remove_node(node)
                self.mapping.pop(node.key)  # 映射也得删除这个尾部的节点！
                self.size -= 1

    # 删除一个节点：直接删除（不用管它的两个指针，因为不会被用到，且如果要更新的话也会在add_to_head中更新）
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 在头部插入一个节点，即放到head后，第一个节点前
    def add_to_head(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head

"""
add_to_head也可以这么写，但是不如上面的写法好记：

def add_to_head(self, node):
    node.next = self.head.next
    node.prev = self.head
    self.head.next = node
    node.next.prev = node
"""








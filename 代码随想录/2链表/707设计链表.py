from typing import *


# 这个可以自己写出来，不难
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.dummy
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        prev_head = self.dummy.next
        self.dummy.next = new_head
        new_head.next = prev_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        # 找到末尾
        curr = self.dummy
        while curr.next:
            curr = curr.next
        # 这时候curr就是末尾的节点
        new_node = ListNode(val)
        curr.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:  # 如果index大于size，则不加入（等于size则加入到末尾，下面的代码可以统一实现）
            return None
        # 先找到index前面的那个node
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        # 在curr的后面插入新节点
        prev_next = curr.next
        new_node = ListNode(val)
        curr.next = new_node
        new_node.next = prev_next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return None
        # 找到index前面的那个node
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        # 删除curr后的一个节点
        nn = curr.next.next
        curr.next = nn
        self.size -= 1


from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    把反转函数单独提出来，使代码更模块化。每次提前记录反转前k组的前一个节点，结尾节点，和下一个k组的初始节点，
    然后单独对这个隔离出来的k组进行反转，最后连接对应的节点。

    loop循环的条件是只要当前k组的第一个节点存在，那我们就进循环。
    start：当前k组的前一个节点
    end：当前k组的最后一个node
    我们先找从start找end，如果在没找到之前链表就没了，说明当前k组的节点数不足，可以直接return
    找到end之后，在反转前我们需要记录
        1. 下一个k组的第一个节点，这个节点在反转后需要和当前k组反转后的尾巴连接（next_group_first_node）
        2. 当前k组的最后一个节点，即当前k组反转后的头部（prev_first_nod）
    隔离当前k组，并进行反转，反转函数返回的是反转前的最后一个节点，即反转后的头部
    最后进行连接：
        1. start和反转后的头部连接：start.next = reverse(prev_first_node)
        2. 反转后的k组尾巴和下一个k组的开头连接：prev_first_node.next = next_group_first_node
    最终更新start和end到下一个k组开头的前一个节点使得while循环继续：
        start = end = prev_first_node （下一个k组开头的前一个节点就是当前k组反转后的尾巴，即反转前的第一个节点prev_first_node）
    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
            return prev  # 返回当前k组的结尾，即反转后应作为当前k组的第一个节点

        dummy = ListNode(next=head)
        start = end = dummy
        # 只要当前k组有第一个node就进行循环
        while end.next:
            # 先获取当前k组的末尾，如果节点数不够则直接返回
            for _ in range(k):
                end = end.next
                if end is None:  # 当前k组里的节点数少于k，则停止反转直接返回head
                    return dummy.next
            # 如果当前k组的node都存在，则先隔离当前k组的链表，再将其反转，最后将反转后的链表两头进行连接
            # 首先预存指针供反转后连接使用
            next_group_first_node = end.next  # 存储下一个k组的第一个节点，和反转后的尾巴相接
            prev_first_node = start.next  # 存储反转前k组的第一个node，也就是反转后的尾巴
            # 隔离当前k组，然后反转当前的k组，并把反转后的头（reverse函数返回的节点）和尾（反转前的头，即prev_first_node）进行连接
            end.next = None
            start.next = reverse(prev_first_node)  # start接反转后的头
            prev_first_node.next = next_group_first_node  # 反转后的尾巴（即原来k组的头）
            # 更新start和end使循环继续
            start = end = prev_first_node
        return dummy.next

    """
    优化变量名命名：
    start：当前要反转的k组的前一个节点
    curr：遍历完指向k组中的最后一个节点
    next_head：下一个要反转的k组的第一个节点
    curr_end：指向k组翻转后的尾巴，即翻转前的头
    curr_head：指向k组翻转后的头，即翻转前的尾巴
    """
    def reverseKGroup1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
            return prev

        dummy = ListNode(next=head)
        start = dummy
        while start:
            # start为当前要翻转的k组的前一个节点，每次从start开始curr右移k次，最后curr就会指向当前k组的最后一个节点
            curr = start
            for _ in range(k):
                curr = curr.next
                if curr is None:
                    return dummy.next
            # 翻转当前k组
            next_head = curr.next
            curr.next = None
            curr_end = start.next
            curr_head = reverse(start.next)
            # 拼接
            start.next = curr_head
            curr_end.next = next_head
            # 更新start为下一个要翻转的k组的前一个节点，即当前k组翻转后的尾巴curr_end
            start = curr_end






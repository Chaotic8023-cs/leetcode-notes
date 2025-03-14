# 380
from random import choice
from typing import *
from utils.pprintdp import pprintdp

"""
如果只是insert和delete O(1)的话一个hashtable就够，但是
要getRandom的话hashtable没index，所以还需要一个array来
存vals
"""


class RandomizedSet:

    def __init__(self):
        self.dic = {}  # key：val，value：在arr中的index
        self.arr = []  # 存val

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        # 把val插入到arr末尾
        self.dic[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        i = self.dic[val]
        # 将val与arr的末尾元素互换（这里直接用末尾覆盖掉就行，因为接下来直接删掉这个末尾就可以了　）
        self.arr[i] = self.arr[-1]
        # 在哈希表里更新这个末尾元素的index
        self.dic[self.arr[i]] = i
        # 在arr里删除最后一个元素（已经移到原来val的地方覆盖掉val了）
        self.arr.pop()
        # 在dic里直接删除掉key=val的
        self.dic.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.arr)



if __name__ == '__main__':
    sol = RandomizedSet()


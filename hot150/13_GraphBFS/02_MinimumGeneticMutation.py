# 433
from typing import *
from utils.pprintdp import pprintdp
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        注意，此题意思是一个valid的mutation是一次只能变一个字母，bank的意思是所有valid的mutation的结果，即每次变完一个字母结果
        必须在bank里，也就是说从start变到end，中间的也必须在bank中
        其实就是一般BFS，bank中与当前gene差一个字母的相当于就是next state
        """
        q = deque([startGene])
        visited = {startGene}
        count = 0
        while q:
            for _ in range(len(q)):  # 运用层序遍历，就不用记录depth了，count就是depth，即最短路径
                gene = q.popleft()
                if gene == endGene:  # goal check
                    return count
                for b in bank:
                    diff = sum(x != y for x, y in zip(gene, b))
                    if b not in visited and diff == 1:
                        visited.add(b)
                        q.append(b)
            count += 1
        return -1







if __name__ == '__main__':
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    sol = Solution()
    print(sol.minMutation(startGene, endGene, bank))


# 399
from typing import *
from collections import defaultdict


class Solution:
    # self try
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        对于每个分式a/b，我们可以记作a=n1*b，那么第二个分式b/c我们可以记作b=n2*c，
        于是如果我们要求a/c，则可通过连续替换得到a = n1*b = n1*(n2*c) = n1n2 * c
        所以我们可以将此题转换成graph，a/b=2即两个节点a和b，a到b的edge为2，b到a的edge为1/2，
        分别代表a=2b和b=2a，那么如果求query x/y，则问题转化为在graph中找到path x->y，结果就是edge的值连乘

        graph表示为nested dictionary，g[x][y]=n表示x=n*y
        """
        # 根据equations构建graph
        g = defaultdict(lambda: defaultdict(lambda: -1.0))
        for i, (x, y) in enumerate(equations):
            g[x][y] = values[i]
            g[y][x] = 1 / values[i]

        # 在graph中找x->y的一条路径
        def find_edge(x, y):
            if x not in g.keys() or y not in g.keys():  # 起始节点和目标节点只要一个不存在，则无法找到path
                return None
            if x == y:  # 如果起始=目标，即求x/x = 1
                return 1
            visited = set()

            def find(x, y):
                if x not in visited:
                    visited.add(x)
                    for k in g[x].keys():
                        if k not in visited:
                            if k == y:  # found y
                                return g[x][y]
                            ans = find(k, y)  # 如在a->b->c->d中找a/d，则calls: find(a, d) -> find(b, d) -> find(c, d)
                            if ans:
                                return g[x][k] * ans
            return find(x, y)

        ans = []
        for x, y in queries:
            ans.append(find_edge(x, y) or -1)
        return ans

    # Union Find (逻辑比较复杂，不建议记)
    def calcEquation1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        w：记录每个node对于root的比例，即w[x] = x / root(x) = v，也就是x是root(x)的v倍
        p：parent array
        """
        # weight初始化，因为一开始parent是它自己，所以weight是1，即x/p(x) = x/x = 1
        w = defaultdict(lambda: 1.0)
        p = defaultdict()
        # parent array初始化，每个node的parent一开始是它自己
        for x, y in equations:
            p[x], p[y] = x, y

        """
        find使用路径压缩，不但压缩了路径，还顺便更新weights
        使得每次union完x这条path上的weights变正确
        """
        def find(x):
            if p[x] != x:
                original_parent = p[x]
                p[x] = find(p[x])
                w[x] *= w[original_parent]
            return p[x]

        """
        建立union find，对于个equation x/y = v
        我们先find(x)和find(y)找到px和py
        如果px就是py，说明它们已经在一个set里，即之前已经建立过比例关系了，直接跳过（理论上equation不会出现两个相同的x/y)
        如果处于两个不同的set，那我们就把px接到py下面，py是新root：
        merge后，因为原来的py子树里的weights还是对于py的，所以py子树里的weights不用变；
        但是这时px子树里的nodes的weight还是对于px的（未更新前px和py都是1），所以px子树的weights需要更新。
        因为我们在find里进行了path compression，所以此处仅需更新px的weight（即x所在原子树的root px的weight w[px]）
        我们这样想：因为x/y=v，即x是y的v倍，merge后的新root是py，所以w[x]应该更新为v*w[y]，
        即对于y来说，merge后的root还是py，那么x既然是y的v倍，那么对于同样的root py来说，w[x]应该是v倍的w[y]，即v*w[y]
        但是此时px的这个子树的weights还是相对于原来的root px的，即此时w[x]表示x是原px的w[x]倍，
        更新后的w[x]应该变成v*w[y]，x又是原px的w[x]倍，所以w[px]就更新为 (v*w[y]) / w[x]
        
        为什么只更新w[px]就可以？
        更新完px的weight后，理论上应该更新它所有children的weight：我们更新px的weight是根据原始x的weight的，
        即建立在原来x是px的w[x]倍的基础上，根据新的比例x/y=v，我们算出新w[x]应该是多少（但不直接更新），再通过原来的比例w[x]算出更新后
        的px的weight。
        这样更新px的某个child的weight时，只需乘上这个child自己的weight，即按原来的比例这个child是px的多少倍，乘上更新后的px的weight即可
        注意：w[px]是根据比例x/y更新的，但因为px的所有children的weight w[c]都是相对于原来px的比例，所以w[px]更新后，所有children的正确weight
        只需乘上它们对于px的倍数（即w[c]）即可更新完成。

        在解决每个query时，我们在下面if里有检查它们的parent是否相同，即在一个set里 -> 有比例关系。
        同时，调用find也使得对应的query的两个variable的weight更新正确（在之前的union中只更新了px，x的weight会在下次find时更新）
        所以最终只需返回 w[x] / w[y]即可
        
        因为w[x]是对于root的倍数，w[y]是对于同一个root的倍数
        所以w[x]/w[y] = (w[x]/w[root]) / (w[y]/w[root]) = w[x] / w[y]即我们要的比例x/y
        """

        """
        在算如何更新w[px]时，有个误区：
        union前，wpa和wpb都是1，即(wa / wpa) / (wb / wpb) = wa / wb = v
        那么我们带入wpb=1，可以解出wpa = wa / (v * wb)
        这个看似正确，但是更新后wa和wpa都应该更新了，一开始的等式成立仅建立在要么wa和wpa都没更新，要么就是wa和wpa都更新了，
        所以解出的wpa = wa / (v * wb)，我们不能带入原来wa来算！
        所以不能这么算，而是用上面讲的通过a/b的值v来算：pb树在union后weight不需要更新因为root还是pb，又因为a/b=v，所以union后
        wa应该更新为v倍的wb，即v * wb，又根据原来pa树的比例，a是pa的wa倍，即能得到新wpa= (v*wb)/wa
        """
        for i, v in enumerate(values):
            x, y = equations[i]
            px, py = find(x), find(y)
            if px == py:
                continue
            p[px] = py
            w[px] = v * w[y] / w[x]

        ans = []
        for x, y in queries:
            if x not in p or y not in p or find(x) != find(y):  # 这里call了find，使得对应weights正确更新
                ans.append(-1)
            else:
                ans.append(w[x] / w[y])

        return ans


if __name__ == '__main__':
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    sol = Solution()
    print(sol.calcEquation(equations, values, queries))



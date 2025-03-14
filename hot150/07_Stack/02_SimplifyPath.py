# 71
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        """
        我们用一个stack来记录当前的path，底部是root，头部是当前subdirectory
        eg："/a/b/c" -> ['a', 'b', 'c']
        先把input path根据'/' split一下，然后看每个directory：
            1. '.' or ''
            '.'表示当前directory，
            ''的话说明在path中间遇到了多个'/'，也可能是到path结尾了，
            所以不需要做任何操作（就跳过了'.'或多个'/'）
            2. '..':
            表上跳回上一个directory，则stack.pop()把当前stack中的path去掉一个，
            即返回了上一层
            3. 正常名字:
            直接加入stack，加入到当前的path中
        最后给开头和中间加上'/'即可
        """
        for d in path:
            if d == '' or d == '.':
                continue
            elif d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    path = "/.../a/../b/c/../d/./"
    sol = Solution()
    print(sol.simplifyPath(path))

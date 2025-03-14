import sys


"""
58. 区间和（第九期模拟笔试）
https://kamacoder.com/problempage.php?pid=1070

重点：对于不知道还剩多少行的读取用sys.stdin!
"""
def main():
    #读取数组
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    # 使用前缀和来减少暴力解法中的重复计算
    ps = [0]  # 提前预留一个0方便前缀和计算
    s = 0
    for n in arr:
        s += n
        ps.append(s)
    # 对于不知道还剩多少行的读取用sys.stdin!
    for line in sys.stdin:
        a, b = map(int, line.split())
        print(ps[b + 1] - ps[a])  # 用前缀和数组计算区间和


if __name__ == '__main__':
    main()




import sys
input = sys.stdin.read


"""
44. 开发商购买土地（第五期模拟笔试）
https://kamacoder.com/problempage.php?pid=1044
一个2D版本的区间和：维护行和列的区间和
"""
def main():
    # 读数据
    data = input().split()
    n, m = int(data[0]), int(data[1])
    arr = []
    for i in range(n):
        t = []
        for j in range(m):
            t.append(int(data[2 + i * m + j]))
        arr.append(t)

    # 解题：提前记录行和列的前缀和
    p_row = []
    curr_sum = 0
    for i in range(n):
        curr_sum += sum(arr[i])
        p_row.append(curr_sum)

    p_col = []
    curr_sum = 0
    for j in range(m):
        for i in range(n):
            curr_sum += arr[i][j]
        p_col.append(curr_sum)

    # 遍历计算最小差
    ans = float('inf')
    # 按row划分：A: [0:i), B: [i:n)
    for i in range(1, n):
        sum_A = p_row[i - 1]
        sum_B = p_row[n - 1] - p_row[i - 1]
        ans = min(ans, abs(sum_A - sum_B))

    # 按col划分：A: [0:j), B: [j:m)
    for j in range(1, m):
        sum_A = p_col[j - 1]
        sum_B = p_col[m - 1] - p_col[j - 1]
        ans = min(ans, abs(sum_A - sum_B))

    # 打印答案
    print(ans)


if __name__ == '__main__':
    main()


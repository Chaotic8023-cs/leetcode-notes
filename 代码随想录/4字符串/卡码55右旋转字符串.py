# https://kamacoder.com/problempage.php?pid=1065


"""
向右旋转k个即直接把末尾的k个提取出来再拼上前面的。
"""
def main():
    # 读取数据
    k = int(input().strip())
    s = input().strip()
    # 解题
    n = len(s)
    k %= n  # 对长度求余以获得最小等效k
    print(s[n - k:] + s[:n - k])  # 取最后的k个字母拼到前面即可


# 反转
def main1():
    def reverse(i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1

    k = int(input())
    s = list(input())
    n = len(s)
    k %= n
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    print(''.join(s))


if __name__ == '__main__':
    main()

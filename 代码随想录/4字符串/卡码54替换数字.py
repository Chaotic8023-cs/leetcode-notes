# https://kamacoder.com/problempage.php?pid=1064


"""
转成list做，如过遇到数字就直接给arr[i]改成"number"，因为python的list支持多个data type！
如果是别的语言，统计数字，再把arr扩充到目标长度，然后用双指针，一个指针指向原数组末尾用来遍历原数组的元素，
一个指针指向扩容后的末尾，用来赋值。第一个指针遍历的时候第二个指针同时赋值，遇到数字就填一个number。注意这两个
指针都是从后向前，所以要反着来。
"""
def main():
    s = input()
    arr = list(s)
    for i in range(len(arr)):
        if arr[i].isdigit():
            arr[i] = "number"
    print(''.join(arr))


if __name__ == '__main__':
    main()


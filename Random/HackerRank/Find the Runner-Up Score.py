if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = []
    for ele in arr:
        l.append(ele)
    l.sort()
    l2 = []
    for ele in l:
        if ele not in l2:
            l2.append(ele)
    print(l2[-2])

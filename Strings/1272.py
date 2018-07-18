for k in range(int(input())):
    S = input().split()
    if S == []: print('')
    else:
        res = ''
        for k in S:
            res += k[0]
        print(res)

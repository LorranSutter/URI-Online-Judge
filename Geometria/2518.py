from math import sqrt

while True:
    try:
        N = int(input())
        H, C, L = map(int, input().split())

        res = str(float(round(sqrt(H*H + C*C) * N * L / 10000,4)))

        len_res = len(res[res.index('.')+1:])
        if len_res < 4:
            print(res + '0' * (4-len_res))
        else:
            print(res)
    except:
        break

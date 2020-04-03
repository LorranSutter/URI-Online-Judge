X, Y = tuple(map(int,input().split()))

res = ""
for k in range(1,Y+1):
    res = res + str(k) + " "
    if k%X == 0:
        print(res[:-1])
        res = ""

if len(res) != 0:
    print(res[:-1])

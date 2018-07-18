C = int(input())
for k in range(C):
    B, E = map(int, input().split())
    res = ''
    for w in range(min(B,E),max(B,E)+1):
        res += str(w)
    print(res+res[::-1])

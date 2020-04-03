res = 0
for _ in range(int(input())):
    T, V = map(int,input().split())
    res += T*V

print(res)
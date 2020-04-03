res = 0
A = int(input())

for _ in range(int(input())):
    if int(input())*A >= 40000000:
        res += 1

print(res)
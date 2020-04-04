tot = 0

for _ in range(int(input())):
    L, C = map(int, input().split())

    tot += C if L > C else 0

print(tot)
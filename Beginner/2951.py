runes = dict()

N, G = map(int,input().split())

for _ in range(N):
    R, Y = input().split()
    runes[R] = int(Y)

input()

X = input().split()

res = sum([runes[r] for r in X])

print(res)
print('My precioooous' if res < G else 'You shall pass!')
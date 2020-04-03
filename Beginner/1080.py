maior = int(input())
pos = 1

for k in range(99):
    n = int(input())
    if n > maior:
        maior = n
        pos = k+2

print(maior)
print(pos)

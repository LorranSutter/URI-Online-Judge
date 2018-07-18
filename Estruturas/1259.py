N = int(input())
par = []
impar = []
for k in range(N):
    num = int(input())
    if num % 2 == 0: par.append(num)
    else: impar.append(num)

par.sort()
impar.sort(reverse=True)

for k in par: print(k)
for k in impar: print(k)

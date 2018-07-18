O = input()
num = 0
soma = 0
for k in range(12):
    for w in range(12):
        num = float(input())
        if w>k: soma += num
if   O == 'S': print("{0:.1f}".format(soma))
elif O == 'M': print("{0:.1f}".format(soma/66))

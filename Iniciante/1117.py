val = 0
soma = 0
while True:
    N = float(input())
    if N < 0 or N > 10: print("nota invalida")
    else:
        soma+=N
        val+=1
    if val == 2: break
print("media = %.2f" % (soma/2))

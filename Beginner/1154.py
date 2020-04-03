soma = 0
k = 0
while True:
    I = int(input())
    if I < 0: break
    soma+=I
    k+=1

print("%.2f" % (soma/k))

par = 0
impar = 0
pos = 0
neg = 0
for k in range(5):
    num = int(input())
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1

print("%d valor(es) par(es)" % (par))
print("%d valor(es) impar(es)" % (impar))
print("%d valor(es) positivo(s)" % (pos))
print("%d valor(es) negativo(s)" % (neg))

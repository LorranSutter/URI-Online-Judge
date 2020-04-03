N = int(input())
cont = 0
d = 0
for k in range(N):
    C = input()
    for w in C:
        if w == '<': cont+=1
        elif w == '>' and cont != 0:
            d += 1
            cont-=1
    print(d)
    d = 0
    cont = 0

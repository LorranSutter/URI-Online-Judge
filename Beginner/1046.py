h1, h2 = map(int, input().split())

if h1 == h2:
    res = 24
elif h2 < h1:
    res = 24-h1+h2
else:
    res = h2-h1
print("O JOGO DUROU %d HORA(S)" % (res))

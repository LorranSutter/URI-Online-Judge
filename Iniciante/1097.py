I = 1
J = 7
fim = 5
while True:
    print("I=%d J=%d" % (I,J))
    if I == 9 and J == 13: break
    if J == fim:
        I += 2
        fim += 2
        J = fim+2
    else: J -= 1

I = 1
J = 7
while True:
    print("I=%d J=%d" % (I,J))
    if I == 9 and J == 5: break
    if J == 5:
        I += 2
        J = 7
    else: J -= 1

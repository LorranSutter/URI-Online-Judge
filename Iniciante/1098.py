i = 0
while i <= 2:
    if i == 1.0:
        i = 1
    elif i == 2.0:
        i = 2
    for j in range(1,4):
        print("I={0} J={1}".format(i, j + i))
    i += 0.2
    i = round(i,1)

H = int(input())

while H != 0:

    h = H
    biggest = h
    while h != 1:
        if h % 2 == 0:
            h //= 2
        else:
            h = 3 * h + 1
            if h > biggest:
                biggest = h

    print(biggest)
    H = int(input())

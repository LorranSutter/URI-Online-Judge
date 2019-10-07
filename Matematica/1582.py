def mdc(a,b):
    while b != 0:
        r = a % b
        a,b = b,r
    return a

while True:
    try:
        x, y, z = sorted(map(int, input().split()))

        if x*x + y*y == z*z:
            if mdc(x,mdc(y,z)) == 1:
                print("tripla pitagorica primitiva")
            else:
                print("tripla pitagorica")
        else:
            print("tripla")
    except:
        break

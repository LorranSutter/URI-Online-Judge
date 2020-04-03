for k in range(int(input())):
    X = int(input())
    if X == 0:
        print("NULL")
        continue
    res  = "EVEN " if X%2 == 0 else "ODD "
    res += "POSITIVE" if X > 0 else "NEGATIVE"
    print(res)

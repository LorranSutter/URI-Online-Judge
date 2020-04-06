while True:
    try:
        S = input()
        res = ''
        up = True
        for k in S:
            if k.isalpha():
                if up:
                    res += k.upper()
                else:
                    res += k.lower()
                up = not up
            else:
                res += k
        print(res)

    except:
        break

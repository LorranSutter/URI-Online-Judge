for _ in range(int(input())):
    S = input()

    if len(S) != 20:
        print('INVALID DATA')
    elif S[:2] != 'RA':
        print('INVALID DATA')
    else:
        S = S[2:]
        num = None
        for k in range(18):
            if S[k] != '0':
                num = S[k:]
                break
        
        if num == None:
            print('INVALID DATA')
        else:
            print(num)

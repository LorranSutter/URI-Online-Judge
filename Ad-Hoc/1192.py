for k in range(int(input())):
    S = input()
    if   S[0] == S[2]  : print("%d" % (int(S[0])*int(S[2])))
    elif S[1].isupper(): print("%d" % (int(S[2])-int(S[0])))
    else               : print("%d" % (int(S[0])+int(S[2])))

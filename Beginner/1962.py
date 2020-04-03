for k in range(int(input())):
    T = int(input())
    if T < 2015: print("%d D.C." % (2015-T))
    else: print("%d A.C." % (T-2015+1))

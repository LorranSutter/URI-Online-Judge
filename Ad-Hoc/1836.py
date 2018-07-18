from math import sqrt

f_HP = lambda B,IV,EV,L: (IV+B+sqrt(EV)/8+50)*L/50+10
f_S = lambda B,IV,EV,L: (IV+B+sqrt(EV)/8)*L/50+5

for k in range(int(input())):
    C = input().split()
    HP = list(map(int,input().split()))
    AT = list(map(int,input().split()))
    DF = list(map(int,input().split()))
    SP = list(map(int,input().split()))

    print("Caso #" + str(k+1) + ": " + C[0] + " nivel " + C[1])
    print("HP: %d" % (f_HP(HP[0],HP[1],HP[2],int(C[1]))))
    print("AT: %d" % (f_S(AT[0],AT[1],AT[2],int(C[1]))))
    print("DF: %d" % (f_S(DF[0],DF[1],DF[2],int(C[1]))))
    print("SP: %d" % (f_S(SP[0],SP[1],SP[2],int(C[1]))))

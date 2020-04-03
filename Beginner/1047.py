h1, m1, h2, m2 = map(int, input().split())

time1 = h1*60 + m1
time2 = h2*60 + m2
timeDiff = time2 - time1

hDiff = timeDiff//60
mDiff = timeDiff%60

if hDiff == mDiff == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if hDiff < 0:
        hDiff = 24 + hDiff
    print("O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)".format(hDiff, mDiff))

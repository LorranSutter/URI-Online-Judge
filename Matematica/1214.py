for k in range(int(input())):
    C = list(map(int,input().split()))
    media = sum(C[1:])/C[0]
    acima = sum([1 for k in C[1:] if k > media])
    print("%.3f%%" % (acima/C[0]*100))

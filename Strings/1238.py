for k in range(int(input())):
    a,b = input().split()
    if len(a) < len(b):
        menor = a
        maior = b
    else:
        menor = b
        maior = a
    res = ''
    for k in range(len(menor)):
        res += a[k]
        res += b[k]
    print(res+maior[k+1:])

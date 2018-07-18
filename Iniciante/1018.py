N = int(input())
notas = [100,50,20,10,5,2,1]
print(N)
for k in notas:
    n = divmod(N,k)
    N = n[1]
    print('{} nota(s) de R$ {},00'.format(n[0],k))

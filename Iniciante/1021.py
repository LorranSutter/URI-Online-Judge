N = float(input())
notas = [100,50,20,10,5,2]
moedas = [100,50,25,10,5]
print("NOTAS:")
for k in notas:
    n = divmod(N,k)
    N = n[1]
    print("{0:d} nota(s) de R$ {1:.2f}".format(int(n[0]),k))
N *= 100
print("MOEDAS:")
for k in moedas:
    n = divmod(N,k)
    N = n[1]
    print('{0:d} moeda(s) de R$ {1:.2f}'.format(int(n[0]),k/100))
print('{0:d} moeda(s) de R$ {1:.2f}'.format(int(N),0.01))

n = str(int(input()))
st = str(n)
aux = ""

for i in range(len(st)):
    aux+= str(int(n)%10)
    n = n[:-1]

print(aux)

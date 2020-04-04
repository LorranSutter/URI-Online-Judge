# Sinceramente nao sei o que ha de errado... 20% de erro

soma = 0
num_notas = 0
new_calc = 0

while new_calc != 2:
    while num_notas != 2:
        n = float(input())
        if n >= 0 and n <= 10:
            num_notas += 1
            soma += n
        else: print("nota invalida")
    print("media = %.2f" % (soma/2))
    num_notas = 0
    soma = 0
    new_calc = 0
    while new_calc != 1 and new_calc != 2:
        new_calc = input("novo calculo (1-sim 2-nao)")
        try:
            new_calc = int(new_calc)
        except:
            new_calc = int(float(new_calc))
            continue

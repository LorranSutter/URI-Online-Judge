# Runtime error

S1 = input() # some encoding problem
S2 = input()

cpf = ''
cpf_len = 0

soma1 = ''
ponto = False
nums_ponto = -1

for k in S1:
    if k.isnumeric():
        if cpf_len < 11:
            cpf += k
            cpf_len += 1
        elif nums_ponto < 2:
            if ponto:
                nums_ponto += 1
            soma1 += k
        else:
            break
    elif k == '.':
        ponto = True
        nums_ponto += 1
        soma1 += k

soma2 = ''
ponto = False
nums_ponto = -1

for k in S2:
    if k.isnumeric():
        if nums_ponto < 2:
            if ponto:
                nums_ponto += 1
            soma2 += k
        else:
            break
    elif k == '.':
        ponto = True
        nums_ponto += 1
        soma2 += k

print("cpf " + cpf)
print("%.2f" % (float(soma1)+float(soma2)))

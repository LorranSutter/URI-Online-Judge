#Sinceramente nao sei o que esta errado...

S = input()
res = ''
up = True
for k in S:
    if k != ' ':
        if up: res += k.upper()
        else:  res += k.lower()
        up = not up
    else: res += ' '
print(res)

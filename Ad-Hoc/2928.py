impossible = False
jumps = 0
ice = 0

for _ in range(int(input())):
    row = input()[0]

    if impossible:
        continue
    elif row == '.':
        ice += 1
        if ice >= 3:
            impossible = True
    elif ice > 0:
        jumps += 1
        ice = 0

if impossible:
    print('N')
elif ice > 0:
    print(jumps + 1)
else:
    print(jumps)

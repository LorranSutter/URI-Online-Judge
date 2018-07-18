numCaw = 0
res = [0,0,0]

while numCaw < 3:
    line = input()
    if line == 'caw caw':
        numCaw += 1
    else:
        line = line.replace('*','1').replace('-','0')
        res[numCaw] += int(line,2)

for k in res: print(k)

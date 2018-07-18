#Sinceramente nao sei o que esta errado...

for k in range(int(input())):
    p = 0
    n = int(input())
    inst = [0 for k in range(n)]
    for w in range(n):
        I = input()
        if I == "LEFT":
            p-=1
            inst[w] = -1
        elif I == "RIGHT":
            p+=1
            inst[w] = 1
        else:
            p += inst[int(I[-1])-1]
            inst[w] = inst[int(I[-1])-1]
    print(p)

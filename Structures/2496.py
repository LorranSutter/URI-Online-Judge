ordered = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for _ in range(int(input())):
    N = int(input())
    M = input()

    areNot = False
    unordered = []
    for k in range(N):
        if M[k] != ordered[k]:
            unordered.append(k)
            if len(unordered) > 2:
                areNot = True
                break

    if areNot:
        print("There aren't the chance.")
        continue
    if len(unordered) == 0:
        print("There are the chance.")
        continue

    M = list(M)
    M[unordered[0]], M[unordered[1]] = M[unordered[1]], M[unordered[0]]

    for k in range(N):
        if M[k] != ordered[k]:
            print("There aren't the chance.")
            continue

    print("There are the chance.")

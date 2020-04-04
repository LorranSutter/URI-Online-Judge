# Time limit exeeded

while True:
    try:
        X, Y, M = map(int, input().split())

        for k in range(M):
            x, y = map(int, input().split())
            if x <= X and y <= Y:
                print("Sim")
                continue
            if y <= X and y <= Y:
                print("Sim")
                continue
            print("Nao")
    except:
        break

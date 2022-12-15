for k in range(int(input())):
    h, d, g = map(int, input().split())
    if h < 200 or h > 300:
        print("Nao")
        continue
    if d < 50:
        print("Nao")
        continue
    if g < 150:
        print("Nao")
        continue
    print("Sim")

h = 1
while True:
    a = input()
    if a == '0': break
    if a in input():
        print("Instancia %d" % (h))        
        print("verdadeira")
        print("")
    else:
        print("Instancia %d" % (h))
        print("falsa")
        print("")
    h+=1

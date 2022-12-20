input()
failled = False
previous = 0
index = 1
for r in input().split():
    if int(r) < previous:
        failled = True
        break
    previous = int(r)
    index += 1

if failled: print(index)
else: print(0)

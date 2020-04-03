even = [None, None, None, None, None]
odd = [None, None, None, None, None]

countEven = 0
countOdd = 0

for k in range(15):
    num = int(input())

    if num%2 == 0:
        even[countEven] = num
        countEven += 1

        if countEven == 5:
            for k in range(countEven):
                print("par[{0}] = {1}".format(k,even[k]))
            countEven = 0
            even = [None, None, None, None, None]
    else:
        odd[countOdd] = num
        countOdd += 1

        if countOdd == 5:
            for k in range(countOdd):
                print("impar[{0}] = {1}".format(k,odd[k]))
            countOdd = 0
            odd = [None, None, None, None, None]

if countOdd > 0:
    for k in range(countOdd):
        print("impar[{0}] = {1}".format(k,odd[k]))
if countEven > 0:
    for k in range(countEven):
        print("par[{0}] = {1}".format(k,even[k]))

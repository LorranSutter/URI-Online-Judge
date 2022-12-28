# Runtime error

digits = '123456789'
for _ in range(int(input())):

    numbers = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    luckyNumber = ''
    firstFound = False

    for number in input():
        numbers[number] += 1
    
    for digit in digits:
        if numbers[digit] != 0:
            if not firstFound:
                luckyNumber += digit
                luckyNumber += '0' * numbers['0']
                numbers[digit] -= 1
                firstFound = True
            luckyNumber += digit * numbers[digit]
    
    print(luckyNumber)

equals = True
line = input()

while line != '*':
    words = line.split()
    letter = words[0][0].lower()

    for l in words:
        if l[0].lower() != letter:
            equals = False
            break
    
    print('Y' if equals else 'N')

    equals = True
    line = input()

while True:
    try:
        numWords = 0
        totalLength = 0
        for word in input().split():
            if len(word) == 1:
                if word.isalpha():
                    totalLength += 1
                    numWords += 1
            else:
                if word[:-1].isalpha():
                    if word[-1].isalpha():
                        totalLength += len(word)
                        numWords += 1
                    elif word[-1] == '.':
                        totalLength += len(word)-1
                        numWords += 1

        m = 0
        if numWords != 0:
            m = totalLength // numWords
        if m <= 3:
            print(250)
        elif m > 3 and m < 6:
            print(500)
        else:
            print(1000)
    except:
        break

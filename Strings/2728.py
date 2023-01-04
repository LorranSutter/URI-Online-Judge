cobol = ['c','o','b','o','l']
while True:
    try:
        words = input().split('-')
        bug = False
        for i in [0,1,2,3,4]:
            word = words[i].lower()
            if word[0] != cobol[i] and word[-1] != cobol[i]:
                bug = True
                break
        if bug:
            print('BUG')
        else:
            print('GRACE HOPPER')
    except:
        break

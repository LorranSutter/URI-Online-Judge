for n in range(int(input())):
    solution = True
    matrix =[[],[],[]]
    lineArray = [False for _ in range(9)]
    columnArrays = [[False for _ in range(9)] for _ in range(9)]
    semiSquares = [[False for _ in range(9)] for _ in range(9)]
    shiftLine = 0

    for lineShift in range(9):
        if not solution:
            input()
        else:
            lineArrayLocal = lineArray.copy()
            line = input().split()
            shiftColumn = 0
            for i,num in enumerate(line):
                ID = int(num)-1
                if lineArrayLocal[ID]:
                    solution = False
                    break
                lineArrayLocal[ID] = True

                if columnArrays[i][ID]:
                    solution = False
                    break
                columnArrays[i][ID] = True

                if semiSquares[shiftColumn + shiftLine][ID]:
                    solution = False
                    break
                semiSquares[shiftColumn + shiftLine][ID] = True
                if i%3 == 2:
                    shiftColumn += 1

            if lineShift%3 == 2:
                shiftLine += 3
    
    print('Instancia {}'.format(n+1))
    if solution:
        print('SIM')
    else:
        print('NAO')
    print()

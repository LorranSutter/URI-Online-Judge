for k in range(int(input())):
    D1 = input()
    D2, D3, D4, D5 = tuple(input().split())
    D6 = input()

    probs = 0

    if D1 == '*' and D6 == '*': probs += 1
    if D2 == '*' and D4 == '*': probs += 1
    if D3 == '*' and D5 == '*': probs += 1

    print(48 if probs == 3 else 8 if probs == 2 else 2 if probs == 1 else 1)

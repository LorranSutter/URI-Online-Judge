for k in range(int(input())):
    S = input()
    print(S[:len(S)//2][::-1]+S[len(S)//2:][::-1])

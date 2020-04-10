for _ in range(int(input())):
    C = input().split('k')

    S1 = C[0].count('a')
    S2 = C[1].count('a')

    print('k' + S1*S2*'a')
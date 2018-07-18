alpha = dict()
for k in range(26):
    alpha[97+k] = 0

for k in range(int(input())):
    mais = 0
    S = input()
    for w in S:
        a = ord(w.lower())
        if a >= 97 and a <= 122:
            alpha[a] += 1
            if alpha[a] > mais: mais = alpha[a]
    res = ''
    for k in range(26):
        if alpha[97+k] == mais: res+=chr(97+k)
    print(res)
    for k in range(26):
        alpha[97+k] = 0

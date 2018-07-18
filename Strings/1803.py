F = ''
L = ''
S = input()
N = len(S)
M = [S[k+1] for k in range(N-2)]
F = S[0]
L = S[-1]
for k in range(3):
    S = input()
    for w in range(N-2):
        M[w] += S[w+1]
    F += S[0]
    L += S[-1]

res = ''
for w in range(N-2):
    res += chr((int(F)*int(M[w])+int(L))%257)
print(res)

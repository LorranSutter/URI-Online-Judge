N = list(map(int, input().split()))

n1 = N[0]
n2 = N[1]
n3 = N[2]

print(min(N))
N.remove(min(N))
print(min(N))
print(max(N))
print("")
print(n1)
print(n2)
print(n3)

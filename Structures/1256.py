N = int(input())

for k in range(N):
    M, C = map(int, input().split())
    nums = map(int, input().split())

    hash = [[] for _ in range(M)]

    for num in nums:
        key = num%M
        hash[key].append(str(num))

    for n, value in enumerate(hash):
        if value != []:
            print(str(n) + " -> " + " -> ".join(value) + " -> \\")
        else:
            print(str(n) + " -> \\")

    if k+1 < N:
        print()
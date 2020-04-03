A, N = map(int,input().split())

while N <= 0:
    N = int(input())

print(int((A+A+N-1)*N/2))

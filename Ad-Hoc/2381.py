N, K = map(int, input().split())

students = [input() for _ in range(N)]

print(sorted(students)[K-1])
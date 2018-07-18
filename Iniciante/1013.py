A, B, C = tuple(map(int,input().split()))
maiorAB = (A+B+abs(A-B))//2
print(((maiorAB+C+abs(maiorAB-C))//2), "eh o maior")

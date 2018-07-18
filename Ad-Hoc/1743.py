X = input().split()
Y = input().split()

compativel = "Y"

for k in range(len(X)):
	if X[k] == Y[k]:
		compativel = "N"
		break

print(compativel)

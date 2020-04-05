res = []
for word in input().split():
    if word[:2] == word[2:4]:
        res.append(word[2:])
    else:
        res.append(word)

print(' '.join(res))
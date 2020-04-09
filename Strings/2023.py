names = []

while True:
    try:
        names.append(input())
    except:
        break

names = sorted(names, key = lambda x: x.lower())
print(names[-1])
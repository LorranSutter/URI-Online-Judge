letters = ['B','C','D','E']
i = 1

print(" " * 7 + "A")
for k,letter in enumerate(letters):
    print(" " * (6-k) + letter + " " * i + letter)
    i += 2
i -= 2
for k,letter in enumerate(reversed(letters[:-1]),4):
    i -= 2
    print(" " * k + letter + " " * i + letter)
print(" " * 7 + "A")

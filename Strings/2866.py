for _ in range(int(input())):
    msg = [letter for letter in input() if letter.islower()]
    print(''.join(msg[::-1]))
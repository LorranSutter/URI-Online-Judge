for _ in range(int(input())):

    output = ''
    sentence = input()
    for letter in sentence:
        output += chr(ord(letter) + 3) if letter.isalpha() else letter

    if len(output) == 1:
        print(chr(ord(output) - 1))
    else:
        output = output[::-1]
        
        half = len(output) // 2

        halfOutput = ''
        for letter in output[half:]:
            halfOutput += chr(ord(letter) - 1)

        print(output[:half] + halfOutput)

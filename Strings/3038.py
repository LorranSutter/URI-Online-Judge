decrypt = {
    '@':'a',
    '&':'e',
    '!':'i',
    '*':'o',
    '#':'u'
    }
keys = decrypt.keys()

while True:
    try:
        decrypted = ''

        for letter in input():
            if letter in keys:
                decrypted += decrypt[letter]
            else:
                decrypted += letter
        print(decrypted)
    except:
        break

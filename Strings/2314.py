# Runtime error

# Traceback (most recent call last):
#   File "Main.py", line 9, in 
#     s = input()
#   File "/usr/lib/python3.4/encodings/ascii.py", line 26, in decode
#     return codecs.ascii_decode(input, self.errors)[0]
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 959: ordinal not in range(128)
# Command exited with non-zero status (1)

s = input() # Some encoding problem
s2 = ""
cont = ""
for k in s:
    if k == '{':
        if s2 != "":
            print(cont+s2)
        print(cont+"{")
        cont += "...."
        s2 = ""
    elif k == '}':
        if s2 != "":
            print(cont+s2)
        cont = cont[:-4]
        print(cont+"}")
    elif k == ';':
        if "for" not in s2:
            print(cont+s2+";")
            s2 = ""
        else:
            s2 += k
    else:
        s2 += k

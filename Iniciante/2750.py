line = '-'*39
bases = '|' + '  ' + 'decimal' + '  ' + '|' + '  ' + 'octal' + '  ' + '|' + '  ' + 'Hexadecimal' + '  ' + '|'
blankNum1 = '|' + ' '*6 + '{0}' + ' '*4 + '|' + ' '*4 + '{1}' + ' '*4 + '|' + ' '*7 + '{2}' + ' '*7 + '|'
blankNum2 = '|' + ' '*6 + '{0}' + ' '*4 + '|' + ' '*3 + '{1}' + ' '*4 + '|' + ' '*7 + '{2}' + ' '*7 + '|'
blankNum3 = '|' + ' '*5 + '{0}' + ' '*4 + '|' + ' '*3 + '{1}' + ' '*4 + '|' + ' '*7 + '{2}' + ' '*7 + '|'

print(line)
print(bases)
print(line)

for k in range(8):
    print(blankNum1.format(k, oct(k)[2:], hex(k)[2:]))
for k in range(8,10):
    print(blankNum2.format(k, oct(k)[2:], hex(k)[2:].upper()))
for k in range(10,16):
    print(blankNum3.format(k, oct(k)[2:], hex(k)[2:].upper()))

print(line)

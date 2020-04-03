N = float(input())

if N > 4500:
    print("R$ %.2f" % ((N-4500)*0.28 + 350))
elif N > 3000 and N <= 4500:
    print("R$ %.2f" % ((N-3000)*0.18 + 80))
elif N > 2000 and N <= 3000:
    print("R$ %.2f" % ((N-2000)*0.08))
else:
    print("Isento")

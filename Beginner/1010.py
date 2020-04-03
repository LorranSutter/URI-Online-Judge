cod1, num1, val1 = input().split()
cod2, num2, val2 = input().split()
print("VALOR A PAGAR: R$ %.2f" % (int(num1)*float(val1) + int(num2)*float(val2)))

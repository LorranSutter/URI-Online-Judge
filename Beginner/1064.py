count = 0
soma = 0
for k in range(6):
    num = float(input())
    if num > 0:
        count += 1
        soma += num

print("%d valores positivos" % (count))
print("%.1f" % (soma/count))

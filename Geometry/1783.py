def lineSlope(x0, y0, x1, y1):
    return (y1-y0)/(x1-x0)


def lineConstant(slope, x, y):
    return -slope*x+y


def midPoint(x0, y0, x1, y1):
    return (x1+x0)/2, (y1+y0)/2


def lineIntesection(m1, m2, b1, b2):
    x = (b2-b1)/(m1-m2)
    y = m1*x+b1
    return x, y

# In this case we have infinity slope, which yields a zero division error
# Must figure out other way to calculate that
# x0_old, y0_old = 0.50, -0.50
# x1_old, y1_old = -1.00, 0.00
# x0_new, y0_new = -0.50, -0.50
# x1_new, y1_new = 0.00, 1.00
for k in range(int(input())):
    x0_old, y0_old = map(float, input().split())
    x1_old, y1_old = map(float, input().split())
    x0_new, y0_new = map(float, input().split())
    x1_new, y1_new = map(float, input().split())

    midPoint0 = midPoint(x0_old, y0_old, x0_new, y0_new)
    lineSlope0 = lineSlope(x0_old, y0_old, x0_new, y0_new)
    lineSlopeMidPoint0 = -1/lineSlope0
    lineConstantMidPoint0 = lineConstant(
        lineSlopeMidPoint0, midPoint0[0], midPoint0[1])

    midPoint1 = midPoint(x1_old, y1_old, x1_new, y1_new)
    lineSlope1 = lineSlope(x1_old, y1_old, x1_new, y1_new)
    lineSlopeMidPoint1 = -1/lineSlope1
    lineConstantMidPoint1 = lineConstant(
        lineSlopeMidPoint1, midPoint1[0], midPoint1[1])

    inter = lineIntesection(lineSlopeMidPoint0, lineSlopeMidPoint1,
                            lineConstantMidPoint0, lineConstantMidPoint1)

    print(inter[0], inter[1])
    print('Caso #{}: {:.2f} {:.2f}'.format(k+1, inter[0], inter[1]))

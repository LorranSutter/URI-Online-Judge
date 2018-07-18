d = {'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6,'0':6}

for k in range(int(input())):
    print("%d leds" % (sum([d[k] for k in input()])))

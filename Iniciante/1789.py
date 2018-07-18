while True:
    try:
    	N = input()
    	bigger = max(tuple(map(int,input().split())))

    	if bigger < 10:
    		print(1)
    	elif bigger < 20:
    		print(2)
    	else:
    		print(3)
    except:
        break

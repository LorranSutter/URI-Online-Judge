# Wrong answer 30%

while True:
    try:
        n, m = input().split()
        nums = dict()
        i = 0
        for k in input():
            if k != ' ':
                i += 1
                if k in nums.keys():
                    nums[k].append(i)
                else:
                    nums[k] = [i]

        for w in range(int(m)):
            k, v = input().split()

            if v in nums.keys():
                try:
                    print(nums[v][int(k)-1])
                except:
                    print(0)
            else:
                print(0)
    except:
        break

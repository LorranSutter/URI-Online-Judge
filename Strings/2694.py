for k in range(int(input())):

    nums = ""
    res = 0

    for n in input():
        if n.isnumeric():
            nums += n
        elif nums != "":
            res += int(nums)
            nums = ""

    if nums != "":
        res += int(nums)

    print(res)

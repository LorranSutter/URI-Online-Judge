# Wrong answer 10%

name = input()

YESnames = []
NOnames = []
first = ""
biggestName = 0
habay = ""

while name != "FIM":
    name, choice = name.split()

    if choice == "YES":
        if first == "":
            first = name

        l = len(name)
        if biggestName < l:
            biggestName = l

        if name not in YESnames:
            YESnames.append(name)

    else:
        NOnames.append(name)

N = int(input())
S = input().split()

res = ''
for k in S:
    if len(k) > 3: res+=k+' '
    elif k[:2] == "OB": res+="OBI "
    elif k[:2] == "UR": res+="URI "
    else: res+=k+' '

print(res[:-1])

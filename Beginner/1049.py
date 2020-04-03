S1 = input()
S2 = input()
S3 = input()

if S1 == "vertebrado":
    if S2 == "ave":
        if S3 == "carnivoro": print("aguia")
        else: print("pomba")
    elif S3 == "onivoro": print("homem")
    else: print("vaca")
else:
    if S2 == "inseto":
        if S3 == "hematofago": print("pulga")
        else: print("lagarta")
    elif S3 == "hematofago": print("sanguessuga")
    else: print("minhoca")

# Wrong answer 5%

N1, N2, S1, S2 = input().split(maxsplit=3)

N1 = int(N1)
N2 = float(N2)

print('{}{}{}{}'.format(N1,N2,S1,S2))
print('{}\t{:.6f}\t{}\t{}'.format(N1,N2,S1,S2))
print('{:>10}{:>10.6f}{:>10}{:>10}'.format(N1,N2,S1,S2))

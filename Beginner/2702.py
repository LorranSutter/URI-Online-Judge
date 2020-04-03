Ca, Ba, Pa = map(int,input().split())
Cr, Br, Pr = map(int,input().split())

tot = 0

if Ca < Cr: tot += Cr-Ca
if Ba < Br: tot += Br-Ba
if Pa < Pr: tot += Pr-Pa

print(tot)
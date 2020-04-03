N1, N2, N3, N4 = map(float,input().split())
media = (2*N1 + 3*N2 + 4*N3 + N4)/10

print("Media: %.1f" % (media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %.1f" % (exame))
    media = (media+exame)/2
    if media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % (media))

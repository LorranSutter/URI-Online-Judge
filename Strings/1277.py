for k in range(int(input())):
	num_alunos = int(input())
	alunos = input().split()
	faltas = input().split()
	res = ''
	for w in range(num_alunos):
		if faltas[w].count('P')/(len(faltas[w])-faltas[w].count('M')) < 0.75: res += alunos[w] + ' '
	print(res[:-1])

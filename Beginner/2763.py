import re

cpf = re.search("^(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$", input())

for num in cpf.groups():
    print(num)

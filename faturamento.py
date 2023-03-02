import json

with open("dados.json") as file:
	data = json.load(file)

dados = []
acima = []

for i in data["dias"]:
	if i.get("valor") > 0:
		dados.append(i.get("valor"))

x = min(dados)
# print(round(x, 2))

y = max(dados)
# print(round(y, 2))

for i in data["dias"]:
	if i.get("valor") == x:
		print(f'O menor valor de faturamento encontrado: {i.items()}')

for i in data["dias"]:
	if i.get("valor") == y:
		print(f'O maior valor de faturamento encontrado: {i.items()}')

media = sum(dados)/len(dados)
# print(round(media,2))

for i in data["dias"]:
	if i.get("valor") > media:
		acima.append(i.get("dia"))

print(f'Número de dias em que o valor foi superior a média mensal: {len(acima)} dias.')
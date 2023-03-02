pen = 0
ultimo = 1
n = int(input("Qual número deseja encontrar? "))
count = 0
fiboray = [pen, ultimo]

while count <= n:
	fibo = ultimo + pen
	pen = ultimo
	ultimo = fibo
	count += 1
	fiboray.append(fibo)

print(fiboray)

if n in fiboray:
	print("O número informado pertence a sequência.")
else:
	print("O número informado não pertence a sequência.")
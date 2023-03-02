sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros


psp = round((sp/total)*100)
prj = round((rj/total)*100)
pmg = round((mg/total)*100)
pes = round((es/total)*100)
pout = round((outros/total)*100)



print(f"Porcentagem de SP {psp}%")
print(f"Porcentagem de RJ {prj}%")
print(f"Porcentagem de MG {pmg}%")
print(f"Porcentagem de ES {pes}%")
print(f"Porcentagem de Outros {pout}%")
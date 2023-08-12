n=0
fecha=''
tb=5
costtal=0
fecha=input("la boleta es para finde semana?(si o no)")
n=int(input('ingresa la cantidad de boletas a comprar: '))
if fecha=='si':
  costtal=tb*1.20
else:
  costtal=tb

print("el costo total a pagar:", costtal*n)

palco=''
palco=input("Seleccione el palco(a,b o c)")
if palco=='a':
  costtal= costtal + tb*.1
elif palco=='b':
  costtal= costtal + tb*.05
else:
  palco=='c'

print("el costo total segun palco a pagar es: ", costtal*n)

if n>=5 and n<=10:
  costtal=costtal*.9
if n>=15 and n<=20:
    costtal=costtal*.85
if n>=25:
    costtal=costtal*.8
print("el costo total a pagar:", round(costtal*n,2))
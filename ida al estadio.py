n=0
sector=''
tbg=50000
tbv=120000
tbp=150000
costtal=0
sector=input("ingrese sector boleta: ")
n=int(input('ingrese cantidad de boletas: '))
if sector=='general':
    costtal=tbg
elif sector=='vip':
    costtal=tbv
else:
   costtal=tbp
print("el costo total a pagar:", costtal*n)

licor=''
s=0
g=250000
byw=390000
master=500000
licor=input("ingrese botella de licor: ")
s=int(input("ingrese cantidad de botellas: "))
if licor=='guaro':
  costtal= costtal + g*1.15
elif licor=='black':
  costtal= costtal + byw*1.15
else:
    costtal= costtal+master*1.15
print("el costo total segun botella y sector a pagar es: ", costtal*s)

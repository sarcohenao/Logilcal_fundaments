n=0
sala=50
cine=''
costtal=0
estreno1=12.00
normal2=7.50
matine3=5.00
cine=input("ingrese tipo proyeccion: ")
n=int(input("ingrese cantidad de boletas: "))
if cine=='estreno':
    costtal = estreno1
elif cine=='normal':
    costtal = normal2
else:
    costtal = matine3
print("el costo total a pagar por la funcion es: ", round(costtal*sala*n))
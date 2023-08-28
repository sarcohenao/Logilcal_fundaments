for i in range(2,9):
    print(i,i ** 3, "iteracion: ", i-1)
print('fin del ciclo')

#iteracion inversa
for i in range(100,0,-5):
    print(i)
print('fin del ciclo')

tab2=[2,4,6,8,10,12,14,16,18,20]
n=0
for i in tab2:
    n=n+1
    print("2 x",n,i**1)
print("fin del ciclo")

for i in range(5):
    print(i)
print("fin del ciclo")

for i in range(2,4):
    print(i)
print("fin del ciclo")

for i in range(-4,0,2):
    print(i)
print("fin del ciclo")

letras=[]
for i in range(5):
    letra=input("ingrese por favor 5 letras:")
    letras.append(letra)
#la impresion como tal:
for letra in letras:
    print(letra)
 
letras=[]
for i in range(5):
    letra=input("ingrese por favor 5 letras:")
    letras.append(letra)
#la impresion como tal:
for letra in letras:
    print(letra,end=',')
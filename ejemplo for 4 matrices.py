letras=[]
for i in range(5):
    letra=input("ingrese por favor 5 letras:")
    letras.append(letra)
#la impresion como tal:
for letra in letras:
    print(letra,end=',')
#fin de este ejemplo

letras = []
for i in range(5):
    letra=input("ingrese una letra {} de 5: ".format(i+1))
    letras.append(letra)
for i in range(5):
    print("  "* i + letras[i])
print("fin del ciclo")
#fin de este ejemplo

letras = []
for i in range(5):
    letra=input("ingrese una letra {} de 5: ".format(i+1))
    letras.append(letra)
for i in range(5):
    print("  "* i + letras[4-i])
print("fin del ciclo")
#fin de este ejemplo


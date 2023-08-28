filas=3
colum=3
m=[]
for i in range(filas):
    filas=[]
    for j in range(colum):
        val=int(input(f"ingrese varios datos {i},{j}: "))
        filas.append(val)
    m.append(filas)
for filas in m:
    for val in filas:
        print(val, end='  ')
    print()
print("diagonal: ")
for i in range(min(filas,colum)):
    print(m[i][j])

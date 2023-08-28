#L=[2,8,10]
#for i in range(3):
#    print(L[2-i])
    

#horizontal
#L=[2,8,10]
#for i in range(3):
#    print(L[i],end=' ')

    
#diagonal derecha
#L=[2,8,10]
#for i in range(3):
#    print(" "*i,L[i])

#diagonal derecha inversa
#L=[2,8,10]
#for i in range(3):
#    print(" "*i,L[2-i])

#diagonal izquierda
#L=[2,8,10]
#for i in range(3):
#    print(" "*(2-i),L[i])

#diagonal izquierda inversa
#L=[2,8,10]
#for i in range(3):
#    print(" "*(2-i),L[2-i])

#m=[ ]
#for fila in range(4):
#    for column in range(4):
        #m=int(input("ingrese el valor: ")):
#        m.append(0)
#print(type(m))
#print(m)
#for fila in range(4):
#    for column in range(4):
#        print(m[column],end=" ")
#    print()

#m=[ ]
#for fila in range(4):
#    for column in range(4):
#        #m=int(input("ingrese el valor: ")):
#        m.append(0)
#print(type(m))
#print(m)
#for fila in range(4):
#    for column in range(4):
#        if fila==column:
#            print(1,end=" ")
#        else:
#            print(m[column],end=" ")
#    print()
    
#m=[ ]
#for fila in range(4):
#    for column in range(4):
#        m.append(0)
#print(type(m))
#print(m)
#for fila in range(4):
#    for column in range(4):
#        if fila+column==3:
#            print(1,end=" ")
#        else:
#            print(m[column],end=" ")
#    print()

#f=int(input("ingrese cantidad de filas: "))
#c=int(input("ingrese cantidad de columnas: "))
#m=[]
#for fila in range(f):
#    for column in range(c):
#        m.append(0)
#for fila in range(f):
#    for column in range(c):
#        if fila==0 or column==0 or fila==f-1 or column==c-1:
#            print(1,end=" ")
#        else:
#            print(m[column],end=" ")
#    print()


f=int(input("ingrese cantidad de filas: "))
c=int(input("ingrese cantidad de columnas: "))
m=[]
for fila in range(f):
    for column in range(c):
        m.append(0)
for fila in range(f):
    for column in range(c):
        if fila==f//2 or column==c//2:
            print(1,end=" ")
        else:
            print(m[column],end=" ")
    print()
    
#f=int(input("ingrese cantidad de filas: "))
#c=int(input("ingrese cantidad de columnas: "))
#m=[]
#for fila in range(f):
#    for column in range(c):
#        m.append(0)
#for fila in range(f):
#    for column in range(c):
#        if fila>=column:
#            print(1,end=" ")
#        else:
#            print(m[column],end=" ")
#    print()
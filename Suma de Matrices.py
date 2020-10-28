a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[9,8,7],[6,5,4],[3,2,1]]
#print(a)
#def DimensionMatriz():
#Primero debemos considerar que las dimensiones sean iguales
def SumaMatrices(x,y):
    if len(x)==len(y) and len(x[0])==len(y[0]):
        c=[]
        for i in range(len(x)):
            c.append([])
            for j in range(len(x[0])):
                #Sumamos las matrices en cada uno de sus ubicaciones
                c[i].append(x[i][j]+y[i][j])
        return c
    else:
        return None

#Generamos una funcion para graficar las 3 funciones
#def GraficarMatriz(e):
 #   for i in range(len(a)):
  #      print(e[i], end="  ")
   #     print()
d=print(SumaMatrices(a,b))









"""
c=[]
d=True
for i in range(0,int(len(x))):
    if int(len(x[i]))==int(len(y[i])):
        d
    else:
        d=not d
        print("Tienen diferentes dimensiones")

def SumaMatrices():
    if len(x)==len(y):
        for i in range(len(x)):
            for j in range(len(x)):
                c.append(print(x[i][j]+y[i][j])
                print(c)
    else:
    return
"""





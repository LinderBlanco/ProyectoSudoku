print("--------TABLA DE MULTIPLICAR--------")
x=int(input("Digite x>0: "))
while x<=1:
    x = int(input("Digite x>0: "))
for i in range(1,x+1):
    for j in range(1,x+1):
        print("{:<6}".format(i*j),  end="")
    print()

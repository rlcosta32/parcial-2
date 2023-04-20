print("======================")
print("BIENVENIDO AL PROGRAMA")
print("======================")

list = []

while True:
    try:
        numUsuario = int(input("Ingresa un número positivo-> "))
        if numUsuario > 0:
            break
        else:
            print("El número que ingresastes no es positivo!. Inténtalo de nuevo.")
    except ValueError:
        print("El dato que ingresastes no es un número entero!. Inténtalo de nuevo.")

sum = 0
for i in range(1, numUsuario+1):
    sum += 1/i
    list.append(f"1/{i}")

print("El resultado de la serie es:", sum)

for j in list:
    print(j," + ",end= "")


print("\n")
print("===================================================")
print("EL PROGRAMA A FINALIZADO, GRACIAS POR UTILIZARLO :)")
print("===================================================")
numeros=[]
for i in range(10):
    numero =int(input(f"ingrese un numero{i+1}: "))
    numeros.append(numero)
numerosPares=[num for num in numeros if num % 2==0]
print("numeros pares", numerosPares)
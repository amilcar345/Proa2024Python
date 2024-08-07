frase=input("ingrese una frase: ")
contadorDeVocales=0
vocales="aeiouAEIOU"
for letra in frase:
    if letra in vocales:
     contadorDeVocales +=1 
print("la cantidad de voclaes son ",contadorDeVocales)
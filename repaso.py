contraseña =input("escriba una contraseña")
listacontraseña =[]
for i in contraseña:
    print("*", end="")
    listacontraseña.append(i)
print ()
print (listacontraseña)
listacontraseña.pop(4)
print(listacontraseña)
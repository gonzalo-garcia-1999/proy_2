contraseña_nueva=input("Ingrese su nueva contraseña: ")
b=0
c=0
d=0
e=0
Contraseñas_anteriores=["Hola1", "Hola2", "HOla3", "hoLa4"]
if contraseña_nueva in Contraseñas_anteriores:
    print("Contraseña Invalida")
else:
    if contraseña_nueva.isalpha()==False and contraseña_nueva.isdigit() == False and contraseña_nueva.isalnum()== True:
        for i in contraseña_nueva:
            if contraseña_nueva[c].isupper()==True:
                d+=1
            e+=1
        if d>=1:
            print("contraseña valida")
        else:
            print("contraseña invalida")
    else:
        print("Contraseña Invalida")

def lectura_if_boolean():
    print("Hola!")
    print("En esta parte se te va a enseñar sobre las estructuras selectivas. Sin embargo, para entender que son las estructuras selectivas, se necesita entender que es un boolean. \n Una expresión booleana compara a dos factores y da una respuesta entre verdadero y falso dependiendo del resultado de la comparación.")
    print(" Algunos ejemplos de expresiones booleanas: \n mayor: a>b \n mayor o igual: a>=b \n menor: a<b \n menor o igual: a<=b \n igual: a==b \n no igual: a!=b")
    print("También, pueden haber expresiones booleanas que comparen mas de dos propiedades de distintos elementos. Por ejemplo:\n a<b and a<c \n a==b or a==c \n ")
    print("Además, se pueden utilizar expresiones aritmeticas con los booleanss, tal y como:\n a+b>c+d \n a*b==b*c \n a%c!=a%b")
    return
def ejercicio_boolean1():
    print("Ahora, intetalo tu!")
    print("Abajo, puedes encontrar diversos problemas con booleans, analiza los dos numeros que aparecen y escribe el boolean correcto para relacionarlos")
    print("4    5")
    prueba1boolean= input("Escribe el boolean de comparación (<,>,<=,>=,) que relaciona los dos numeros de arriba aca: ")
    print("1    -1")
    prueba2boolean = input("Escribe el boolean de comparación (<,>,<=,>=) que relaciona los dos numeros de arriba aca: ")
    print("10   10")
    prueba3boolean= input("Escribe el boolean de igualdad (==, !=) que relaciona los dos numeros de arriba aca: ")
    print("2    5")
    prueba4boolean=input("Escribe el boolean de igualdad (==, !=) que relaciona los dos numeros de arriba aca: ")
    contador_boolean=0
    if prueba1boolean == "<":
        contador_boolean += 1
    if prueba2boolean == ">":
        contador_boolean += 1
    if prueba3boolean == "==":
        contador_boolean += 1
    if prueba4boolean =="!=":
        contador_boolean += 1
    print("Obtuviste", contador_boolean, "preguntas bien")
    if contador_boolean== 4:
        print("¡Muy bien tuviste todo bien!")
    if contador_boolean < 4:
        print("¿Quieres seguir practicando?")
        seguir_practicando = input("Si quieres escribe la palabra si acá: ")
        while seguir_practicando =="si":
            print("Ahora, intetalo tu!")
            print(
                "Abajo, puedes encontrar diversos problemas con booleans, analiza los dos numeros que aparecen y escribe el boolean correcto para relacionarlos")
            print("4    5")
            prueba1boolean = input(
                "Escribe el boolean de comparación (<,>,<=,>=,) que relaciona los dos numeros de arriba aca: ")
            print("1    -1")
            prueba2boolean = input(
                "Escribe el boolean de comparación (<,>,<=,>=) que relaciona los dos numeros de arriba aca: ")
            print("10   10")
            prueba3boolean = input(
                "Escribe el boolean de igualdad (==, !=) que relaciona los dos numeros de arriba aca: ")
            print("2    5")
            prueba4boolean = input(
                "Escribe el boolean de igualdad (==, !=) que relaciona los dos numeros de arriba aca: ")
            contador_boolean = 0
            if prueba1boolean == "<":
                contador_boolean += 1
            elif prueba2boolean == ">":
                contador_boolean += 1
            elif prueba3boolean == "==":
                contador_boolean += 1
            elif prueba4boolean == "!=":
                contador_boolean += 1
            print("Obtuviste", contador_boolean, "preguntas bien")
            if contador_boolean < 4:
                print("¿Quieres seguir practicando?")
                seguir_practicando = input("Si quieres escribe la palabra si acá: ")


    return
ejercicio_boolean1()

def ejercicio_boolean2():
    print("¡Creiste que te librabas de los booleans pero no! Aquí hay otro ejercicio más que debes de resolver. Estas son expresiones boolean. Responde si cada expresión es True or false \n Escribe T si es True y F si es False")
    print("1 < 3")
    prueba1boolean2 = input("Escribe tu respuesta acá: ")
    print("5.0 > 4.999")
    prueba2boolean2 = input("Escribe tu respuesta acá: ")
    print("7 >= 7")
    prueba3boolean2 = input("Escribe tu respuesta acá: ")
    print("2+2 >= 5")
    prueba4boolean2 = input("Escribe tu respuesta aca: ")
    print("True or False")
    prueba5boolean2 = input("Escribe tu respuesta aca: ")
    print("False and True")
    prueba6boolean2 = input("Escribe tu respuesta aca: ")
    print("not True")
    prueba7boolean2 = input("Escribe tu respuesta aca: ")
    print("2.0-1.5 != 4.0-3.5")
    prueba8boolean2 = input("Escribe tu respuesta aca: ")
    print("3>4 or (2<=3 and 9<10)")
    prueba9boolean2 = input("Escribe tu respuesta aca: ")
    print("not(4>5 and 3.00<=3.01)")
    prueba10boolean2 = input("Escribe tu respuesta aca: ")
    print("5%5 != 3%4")
    prueba11boolean2= input("Escribe tu respuesta aca: ")
    contador_boolean2 = 0
    if prueba1boolean2 == "True" or prueba1boolean2 == "true" or prueba1boolean2 == "T" or prueba1boolean2 == "t":
        contador_boolean2 += 1
    if prueba2boolean2 == "True" or prueba2boolean2 == "true" or prueba2boolean2 == "T" or prueba2boolean2 == "t":
        contador_boolean2 += 1
    if prueba3boolean2 == "True" or prueba3boolean2 == "true" or prueba3boolean2 == "T" or prueba3boolean2 == "t":
        contador_boolean2 += 1
    if prueba4boolean2 == "False" or prueba4boolean2 == "false" or prueba4boolean2 == "F" or prueba4boolean2 == "f":
        contador_boolean2 += 1
    if prueba5boolean2 == "True" or prueba5boolean2 == "true" or prueba5boolean2 == "T" or prueba5boolean2 == "t":
        contador_boolean2 += 1
    if prueba6boolean2 == "False" or prueba6boolean2 == "false" or prueba6boolean2 == "F" or prueba6boolean2 == "f":
        contador_boolean2 += 1
    if prueba7boolean2 == "False" or prueba7boolean2 == "false" or prueba7boolean2 == "F" or prueba7boolean2 == "f":
        contador_boolean2 += 1
    if prueba8boolean2 == "False" or prueba8boolean2 == "false" or prueba8boolean2 == "F" or prueba8boolean2 == "f":
        contador_boolean2 += 1
    if prueba9boolean2 == "True" or prueba9boolean2 == "true" or prueba9boolean2 == "T" or prueba9boolean2 == "t":
        contador_boolean2 += 1
    if prueba10boolean2 == "True" or prueba9boolean2 == "true" or prueba10boolean2 == "T" or prueba10boolean2 == "t":
        contador_boolean2 += 1
    if prueba11boolean2 == "True" or prueba9boolean2 == "true" or prueba11boolean2 == "T" or prueba11boolean2 == "t":
        contador_boolean2 += 1
    print("Obtuviste", contador_boolean2, " sobre 11 preguntas bien")
    if contador_boolean2 == 11:
        print("¡Muy bien tuviste todo bien!")
    if contador_boolean2 < 11:
        print("¿Quieres seguir practicando?")
        seguir_practicando = input("Si quieres escribe la palabra si acá: ")
        while seguir_practicando == "si":
            print("¡Creiste que te librabas de los booleans pero no! Aquí hay otro ejercicio más que debes de resolver. Responde si cada expresión es True or false")
            print("1 < 3")
            prueba1boolean2 = input("Escribe tu respuesta acá: ")
            print("5.0 > 4.999")
            prueba2boolean2 = input("Escribe tu respuesta acá: ")
            print("7 >= 7")
            prueba3boolean2 = input("Escribe tu respuesta acá: ")
            print("2+2 >= 5")
            prueba4boolean2 = input("Escribe tu respuesta aca: ")
            print("True or False")
            prueba5boolean2 = input("Escribe tu respuesta aca: ")
            print("False and True")
            prueba6boolean2 = input("Escribe tu respuesta aca: ")
            print("not True")
            prueba7boolean2 = input("Escribe tu respuesta aca: ")
            print("2.0-1.5 != 4.0-3.5")
            prueba8boolean2 = input("Escribe tu respuesta aca: ")
            print("3>4 or (2<=3 and 9<10)")
            prueba9boolean2 = input("Escribe tu respuesta aca: ")
            print("not(4>5 and 3.00<=3.01)")
            prueba10boolean2 = input("Escribe tu respuesta aca: ")
            print("5%5 != 3%4")
            prueba11boolean2 = input("Escribe tu respuesta aca: ")
            contador_boolean2 = 0
            if prueba1boolean2 == "True" or prueba1boolean2 == "true" or prueba1boolean2 == "T" or prueba1boolean2 == "t":
                contador_boolean2 += 1
            if prueba2boolean2 == "True" or prueba2boolean2 == "true" or prueba2boolean2 == "T" or prueba2boolean2 == "t":
                contador_boolean2 += 1
            if prueba3boolean2 == "True" or prueba3boolean2 == "true" or prueba3boolean2 == "T" or prueba3boolean2 == "t":
                contador_boolean2 += 1
            if prueba4boolean2 == "False" or prueba4boolean2 == "false" or prueba4boolean2 == "T" or prueba4boolean2 == "t":
                contador_boolean2 += 1
            if prueba5boolean2 == "True" or prueba5boolean2 == "true" or prueba5boolean2 == "T" or prueba5boolean2 == "t":
                contador_boolean2 += 1
            if prueba6boolean2 == "False" or prueba6boolean2 == "false" or prueba6boolean2 == "F" or prueba6boolean2 == "f":
                contador_boolean2 += 1
            if prueba7boolean2 == "False" or prueba7boolean2 == "false" or prueba7boolean2 == "F" or prueba7boolean2 == "f":
                contador_boolean2 += 1
            if prueba8boolean2 == "False" or prueba8boolean2 == "false" or prueba8boolean2 == "F" or prueba8boolean2 == "f":
                contador_boolean2 += 1
            if prueba9boolean2 == "True" or prueba9boolean2 == "true" or prueba9boolean2 == "T" or prueba9boolean2 == "t":
                contador_boolean2 += 1
            if prueba10boolean2 == "True" or prueba9boolean2 == "true" or prueba10boolean2 == "T" or prueba10boolean2 == "t":
                contador_boolean2 += 1
            if prueba11boolean2 == "True" or prueba9boolean2 == "true" or prueba11boolean2 == "T" or prueba11boolean2 == "t":
                contador_boolean2 += 1
            print("Obtuviste", contador_boolean2, "preguntas bien")
            if contador_boolean2 == 11:
                print("¡Muy bien tuviste todo bien!")
            if contador_boolean2 < 11:
                print("¿Quieres seguir practicando?")
                seguir_practicando = input("Si quieres escribe la palabra si acá: ")
ejercicio_boolean2()

def lectura_estructura_selectiva():
    print("")
    print("Ahora que ya dominaste las expresiones booleanas es momento de aprender que es una estructura selectiva. Estas son aquellas que evalúan una expresión,\n generalmente booleana, y a partir del resultado propuesto, se toma una o más decisiones. Esisten trs tipos las de slección simple, selección doble y selección múltiple ")
    print("Una estructura selectiva simple es aquella que después de evaluar una conidición determina su valor (verdadero/falso) y, si el valor da verdadero entonces la condición se llevará a cabo")
    print("Por ejemplo:")
    print("")
    print("if a > 5:")
    print("""   print("este numero es mayor a 5")""")
    print("")
    print("Entonces, si a==6 se imprimiría la frase: este numero es mayor a 5, pero si a==4, no se imprimiría nada y la frase no se imprimiría")
    print("Nótese dos cosas:")
    print("1: se utiliza la expresión if para plantear una expresión selectiva")
    print("2: los puntos después del 5 al concretar el if los cuales sn necesarios para el sintaxis")
    print("")
    print("")
    print("Ahora, se va a imprimir un ejemplo de una estructura selectiva doble. Esta tiene dos caracteristicas, la palabra if y la palabra else")
    print("La palabra if denota e seguimiento de esa parte de la función si la condición es verdad. La palabra else denota el seguimiento de la función si la condición planteada \n en el if no es verdad ")
    print("Por ejemplo:")
    print("if a > 5:")
    print("""   print("este numero es mayor a 5")""")
    print("else:")
    print("""   print("este numero no es mayor a 5")""")
    print("")
    print("Entonces, acá, si el numero es mayor a 5 pasaría por la condición if e imprimiría el texto (este numero es mayor a 5). \n Sin embargo, si el numero no es mayor a 5 se imprimiría la segunda frase (este numero no es mayor a 5")
    print("Por ejemplo, si a = 4, entonces se imprimiría: este numero no es mayor a 5 pero, si a = 6, se imprimiría: este numero es mayor a 5. OJO: el bloque de else es siempre opcional")
    print("")
    print("")
    print("Finalmente, existen las estructuras selectivas multiples.\n Estas existen cuando hay multiples caminos que un if puede recorer y hay varias opciones que se quieren que probar. Para esto se utiliza la palabra elif después de el primer if\n Por ejemplo: ")
    print("if a>5:")
    print("""   print("este numero es mayor a 5")""")
    print("elif 4<=a<=5:")
    print("""   print("este numero esta entre 4 y 5")""")
    print("elif a<4:")
    print("""   print("este numero es menor a 4")""")
    print("")
    print("Entonces, acá hay varias opciones por donde el programa puede pasar. \nSi es que a fuera mayor a 5 se ejecutaría la primera idea, si a estuviera entre 4 y 5 se ejecutaría lo segundo y si a fuera menor que 4 se ejecutaría la indicación que está debajo del 3 elif. ")
    print("Por ejemplo: \n si a = 6, se imprime: este numero es mayor a 5 \n si a = 4.5, se imprime: este numero esta entre 4 y 5 \n si a = 2, se imprime: este numero es menor a 4 ")
    print("")
    print("")
    print("Ahora, un ejemplo:")
    print("Escribe un programa que permita a una persona escribir su edad y determine si es mayor de edad o no" )
    print("El programa sería así:")
    print("")
    print("""edad = int(input("Ingrese su edad: "))""")
    print("if edad >= 18:")
    print("""   print("Eres mayor de edad")""")
    print("else:")
    print("""   print("no puedes entrar")""")
    print("")
    print("Finalmente, también existen los if anidados. Estos se verían así:")
    print("")
    print("if B1:")
    print("   if B2:")
    print("       S1")
    print("   else:")
    print("       S2")
    print("")
    return
lectura_estructura_selectiva()

def ejercicio_estructura_selectiva():
    print("Acá hay dos ejercicio y dos programas incompletos. Escribe la linea que falta en ambos para que el programa funcione")
    print("Nota: sea exacto")
    print("")
    print("Ejercicio 1:")
    print("Los Martes Cineplanet ofrce precios especiales a sus clientes.\n Escriba un Programa que permita leer como dato la edad de una persona y, segun las instrucciones abajo, determine el precio a pagar")
    print("")
    print("Edad                | Precio")
    print("____________________|________")
    print("hasta 15 años       | 7 soles ")
    print("de 16 hasta 59 años | 12 soles")
    print("de 60 a más         | 5 soles")
    print("")
    print("Condición: Se escribe exactamente lo que sale en la tabla")
    print("Ejemplo:")
    print("Input 1: 18")
    print("Output 1: 12 soles")
    print("")
    print("Codigo incompleto:")
    print("")
    print("""edad = int(input(""))""")
    print("if edad <= 15:")
    print("""   print("7 soles")""")
    print("elif edad <= 59")
    print("""   print("12 soles")""")
    lineafaltante1=input("")
    print("""    print("5 soles")""")
    print("")
    print("Ejercicio 2:")
    print("Escribir un programa que permita leer el pH y el programa indique el tipo de solución. El tipo de solución se encuentra en la siguiente tabla:")
    print("")
    print(" pH level    | Solution Category")
    print("__________________________________")
    print("   0-4       |    Strong Acid")
    print("   5-6       |     Weak Acid")
    print("    7        |       Neutral")
    print("   8-9       |     Weak Base")
    print("   10-14     |    Strong Base")
    print("Condición: se imprime exactamente el valor que sale en la tabla")
    print("Ejemplo:")
    print("input 1: 3")
    print("Strong Acid")
    print("")
    print("Nota: Usar If Anidado")
    print("")
    print("Ejercicio Incompleto:")
    print("if 0<=pH<=4:")
    print("""   print("Strong Acid")""")
    print("else:")
    print("   if 5<=pH<=6:")
    print("""      print("Weak acid")""")
    print("   else:")
    print("      if 7==pH:")
    print("""         print("Neutral")""")
    print("      else:")
    print("         if 8<=pH<=9:")
    print("""            print("Weak base")""")
    print("         else:")
    lineafaltante2=input("              ")
    print("""                print("Strong base")""")
    print("            else:")
    print("""               print("valor de pH no válido""")
    contadorestructuraselectiva1 = 0
    if lineafaltante1 == "else:":
        contadorestructuraselectiva1 += 1
    if lineafaltante2 == "if 10<=pH<=14:":
        contadorestructuraselectiva1 += 1
    if contadorestructuraselectiva1 == 2:
        print("Muy bien, tuviste todo bien")
    if contadorestructuraselectiva1 < 2:
        print("Tuviste", contadorestructuraselectiva1,"/2 preguntas bien")
        seguirpracticando = input("Si quieres seguir practicando escribe la palabra si acá:")
        while seguirpracticando == "si":
            print(
                "Acá hay dos ejercicio y dos programas incompletos. Escribe la linea que falta en ambos para que el programa funcione")
            print("Nota: sea exacto")
            print("")
            print("Ejercicio 1:")
            print(
                "Los Martes Cineplanet ofrce precios especiales a sus clientes.\n Escriba un Programa que permita leer como dato la edad de una persona y, segun las instrucciones abajo, determine el precio a pagar")
            print("")
            print("Edad                | Precio")
            print("____________________|________")
            print("hasta 15 años       | 7 soles ")
            print("de 16 hasta 59 años | 12 soles")
            print("de 60 a más         | 5 soles")
            print("")
            print("Condición: Se escribe exactamente lo que sale en la tabla")
            print("Ejemplo:")
            print("Input 1: 18")
            print("Output 1: 12 soles")
            print("")
            print("Codigo incompleto:")
            print("")
            print("""edad = int(input(""))""")
            print("if edad <= 15:")
            print("""   print("7 soles")""")
            print("elif edad <= 59")
            print("""   print("12 soles")""")
            lineafaltante1 = input("")
            print("""    print("5 soles")""")
            print("")
            print("Ejercicio 2:")
            print(
                "Escribir un programa que permita leer el pH y el programa indique el tipo de solución. El tipo de solución se encuentra en la siguiente tabla:")
            print("")
            print(" pH level    | Solution Category")
            print("__________________________________")
            print("   0-4       |    Strong Acid")
            print("   5-6       |     Weak Acid")
            print("    7        |       Neutral")
            print("   8-9       |     Weak Base")
            print("   10-14     |    Strong Base")
            print("Condición: se imprime exactamente el valor que sale en la tabla")
            print("Ejemplo:")
            print("input 1: 3")
            print("Strong Acid")
            print("")
            print("Nota: Usar If Anidado")
            print("")
            print("Ejercicio Incompleto:")
            print("if 0<=pH<=4:")
            print("""   print("Strong Acid")""")
            print("else:")
            print("   if 5<=pH<=6:")
            print("""      print("Weak acid")""")
            print("   else:")
            print("      if 7==pH:")
            print("""         print("Neutral")""")
            print("      else:")
            print("         if 8<=pH<=9:")
            print("""                      print("Weak base")""")
            print("         else:")
            lineafaltante2 = input(" ")
            print("""                      print("Strong base")""")
            print("             else:")
            print("""                print("valor de pH no válido)""")
            contadorestructuraselectiva1 = 0
            if lineafaltante1 == "else:":
                contadorestructuraselectiva1 += 1
            if lineafaltante2 == "if 10<=pH<=14:":
                contadorestructuraselectiva1 += 1
            if contadorestructuraselectiva1 == 2:
                print("Muy bien, tuviste todo bien")
            if contadorestructuraselectiva1 < 2:
                print("Tuviste", contadorestructuraselectiva1, "/2 preguntas bien")
                seguirpracticando = input("Si quieres seguir practicando escribe la palabra si acá:")

    return
ejercicio_estructura_selectiva()


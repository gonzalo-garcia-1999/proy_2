comenzar_lista=["comenzar","start"]
True_V=["True","T","t","true"]
False_F=["False","false","F","f"]
si_exp=["si","Si","yes"]
no_exp=["no","No"]
C_usuarios=["usuario1","usuario2","usuario3","usuario4","usuario5","usuario6","usuario7","usuario8","usuario9","usuario10"]
Usuario="usuario"
#instrucciones
def instrucciones():
  print("\nInstrucciones:")
  
  lista_instrucciones=[
  "Al finalizar una lectura o ejercicio insertar 'continuar' o 'salir'",
  "Si esta regresando al programa inserte el numero que esta al lado del tema en el que se quedo",
  "Insertar todo en minusculas", 
  "Al final de un ejercicio insertar 'regresar' si desea retornar a la lectura",
  "Para comenzar inserte 'comenzar'"
  ]

  for numero_de_instruccion in range(len(lista_instrucciones)):
    instruccion_general=str(numero_de_instruccion+1)+"."+lista_instrucciones[numero_de_instruccion]
    print(instruccion_general)
  correr_instrucciones=input("\nInserte aquí: ")
  while correr_instrucciones !="comenzar":
      print("\nDisculpa, no entendí. Ingrese comenzar, por favor")
      correr_instrucciones=input("\nInserte aquí: ")
  if correr_instrucciones in comenzar_lista:
      contenido()
#Menu
def main_menu():
  print("\nBienvenido")
  print("\nEste programa le enseñara a usar python.")
  contador1=0
  C_usuarios=["usuario1","usuario2","usuario3","usuario4","usuario5","usuario6","usuario7","usuario8","usuario9","usuario10"]
  usuario="usuario0"
  lista_menu=[
  "Comenzar",
  "Seleccionar usuario",
  "Usuario seleccionado",
  "Eliminar datos de un usuario",
  "Instrucciónes",
  "Creditos'"
  ]
  for numero_de_menu in range(len(lista_menu)):
    instruccion_g=str(numero_de_menu+1)+"."+lista_menu[numero_de_menu]
    print(instruccion_g)
  while contador1 ==0:
    correr_menu=input("\nInserte aquí: ")
    if correr_menu =="1":
      contador1=1
      if usuario != "usuario" :
        contenido()
      else:
        print("\n-------------------------------------"
              "\nPrimero debes seleccionar un usuario"
              "\n------------------------------------")
        main_menu()
    elif correr_menu== "2":
      contador1=1
      print("\n----------------------"
              "\nSelección de Usuario"
              "\n--------------------")
      x=input("Ingrese su N° de usuario: ")
      usuario=seleccionar_usuario(x)
      main_menu()
    elif correr_menu=="3":
      print("El %s esta en juego"%(usuario))

    elif correr_menu=="4":
      contador1=1
      eliminar_datos_()
    elif correr_menu=="5":
      contador1=1
      instrucciones()
    elif correr_menu=="6":
      contador1=1
      creditos()
    else:
      print("Error, por favor inserte el número de la opción")
      correr_menu=input("Inserte aquí:")
def seleccionar_usuario(a):
  C_usuarios=["usuario1","usuario2","usuario3","usuario4","usuario5","usuario6","usuario7","usuario8","usuario9","usuario10"]
  usuario="usuario"
  if a=="1":
    usuario=C_usuarios[0]
  elif a=="2":
    usuario=C_usuarios[1]
  elif a=="3":
    usuario=C_usuarios[2]
  elif a=="4":
    usuario=C_usuarios[3]
  elif a=="5":
    usuario=C_usuarios[4]
  elif a=="6":
    usuario=C_usuarios[5]
  elif a=="7":
    usuario=C_usuarios[6]
  elif a=="8":
    usuario=C_usuarios[7]
  elif a=="9":
    usuario=C_usuarios[8]
  elif a=="10":
    usuario=C_usuarios[9]
  else:
    print("Error")
  return usuario
  
#Variables
def lectura_varibales_int():
    print("\n LOS ENTEROS (int):"
          "\nLos números enteros son aquellos que no tienen decimales, tanto positivos como negativos."
          "\nEn Python se pueden representar mediante el tipo int (de integer, entero) o el tipo long (largo)."
          "\nLa única diferencia es que el tipo long permite almacenar números más grandes.Es aconsejable no utilizar el tipo long a menos que sea necesario, para no malgastar memoria."
          "\n"
          "\nEjemplo 1:"
          "\n entero= 2"
          "\n "
          "\nEjemplo 2:"
          "\n entero2= 412")
    a=input()
    if a=="":
        lectura_variables_float()
def lectura_variables_float():
    print("\nLOS REALES"
          "\nLos números reales son los que tienen decimales. En Python se expresan mediante el tipo float."
          "\nPara representar un número real en Python se escribe primero la parte entera, seguido de un punto y por último la parte decimal. "
          "\n"
          "\n Ejemplo:"
          "\n real: 1.234"
          "\n"
          "\n También se puede utilizar notación científica, y añadir una e (de exponente) para indicar un exponente en base 10. "
          "\n "
          "\nEjemplo:"
          "\n real: 0.34e-2 ; sería equivalente a 0.34 x 10 a la -2 = 0.34 0.01 = 0.0034")
    a = input()
    if a == "":
        lectura_variables_str()
    elif a=="salir":
      contenido()
def lectura_variables_bool():
    print("LOS"
          "\nComo decíamos el tipo booleano sólo puede tener dos valores: True (cierto) y False (falso). "
          "\nEstos valores son especialmente importantes para las expresiones condicionales y los bucles.")
def lectura_variables_str():
    print("\nLAS CADENAS"
          "\nLas cadenas no son más que texto encerrado entre comillas simples (‘cadena’) o dobles (“cadena”). "
          "\nDentro de las comillas se pueden añadir caracteres especiales escapándolos con ‘\’ como ‘\ n’,para una nueva línea, o ‘\ t’, para la tabulación."
          "\nUna cadena puede estar precedida por el carácter ‘u’ (Unicode) o 'r' (Raw) "
          "\nLas cadenas raw se distinguen de las normales en que los caracteres escapados mediante la barra invertida (\) "
          "\nno se sustituyen por sus contrapartidas. Esto es especialmente útil, por ejemplo, para las expresiones regulares."
          "\n También es posible encerrar una cadena entre triples comillas (simples o dobles). "
          "\nDe esta forma podremos escribir el texto en varias líneas, y al imprimir la cadena, se respetarán los saltos de línea"
          "\nque introdujimos sin tener que recurrir al carácter '\ n', así como las comillas sin tener que escaparlas."
          "\n"
          "\nLas cadenas también admiten operadores como la suma (concatenación de cadenas) y la multiplicación.")
    a=input()
    if a=="":
      lectura_if_boolean()
def lectura_variables():
    print("-------------------------------------------------------------------------------------"
          "\n(Durante la lectura usted tendrá la opción de presionar Enter para continuar)"
          "\n-------------------------------------------------------------------------------------"
          "\n SECCIÓN 1: VARIABLES")
    print(
        "\nEn esta sección del programa se te va a enseñar sobre las variables."
        "\nUna variable es una magnitud que puede tener un valor cualquiera de los comprendidos en un conjunto."
        "\nLas variables pueden tener cualquier nombre y cuando se quiere asociar un valor o relacionar el valor a una variable se usa el signo igual'='"
        "\n"
        "\nEjemplo:"
        "\nArea = 1"
        "\n"
        "\nEn Python los datos simples se categorizan según su tipo, los cuales son:"
        "\n int: Representa enteros "
        "\n float: representa números reales"
        "\n str: representa las cadenas de texto"
        "\n bool: representa datos boolean"
        "\n"
        "\n Para saber cual es el tipo de una variable se utiliza -type(x) ; donde x es la variable")
    a=input()
    if a =="":
        print("Ahora vamos a profundizar las definiciones de cada tipo")
        lectura_varibales_int()
#Ejercicos Variables
def ejercicios_variables():
  print("Habiendo visto toda la teoria, debo asegurarme que hayas comprendido"
  "\nPor eso, ahora veremos algunos ejercicios")
#Estructuras selectivas
def lectura_if_boolean():
    print("Hola!")
    print("En esta parte se te va a enseñar sobre las estructuras selectivas. Sin embargo, para entender que son las estructuras selectivas, se necesita entender que es un boolean. \n Una expresión booleana compara a dos factores y da una respuesta entre verdadero y falso dependiendo del resultado de la comparación.")
    print(" Algunos ejemplos de expresiones booleanas: \n mayor: a>b \n mayor o igual: a>=b \n menor: a<b \n menor o igual: a<=b \n igual: a==b \n no igual: a!=b")
    print("También, pueden haber expresiones booleanas que comparen mas de dos propiedades de distintos elementos. Por ejemplo:\n a<b and a<c \n a==b or a==c \n ")
    print("Además, se pueden utilizar expresiones aritmeticas con los booleanss, tal y como:\n a+b>c+d \n a*b==b*c \n a%c!=a%b")
    a=input()
    while a!="":
      print("\nPor favor, no escribas palabras sin sentido.(Presiona Enter para continuar)")
      a=input()
    if a=="":
      print("Ahora, intetalo tu!")
      ejercicio_boolean1()
def ejercicio_boolean1():
    print("\nAbajo, puedes encontrar diversos problemas con booleans, analiza los dos numeros que aparecen y escribe el boolean correcto para relacionarlos")
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
    if contador_boolean < 5:
        print("¿Quieres seguir practicando?")
        seguir_practicando = input("si/no: ")
        if seguir_practicando in si_exp:
          seguir_practicando="s"
          ejercicio_boolean1()
        elif seguir_practicando in no_exp:
          ejercicio_boolean2()
        else:
          print("Error.Responde si o no")
          seguir_practicando=input("(si/no):")
def ejercicio_boolean2():
    print("-----------------------------------------------")
    print("\n¡Creiste que te librabas de los booleans pero no! Aquí hay otro ejercicio más que debes de resolver. Estas son expresiones boolean. Responde si cada expresión es True or false \n Escribe T si es True y F si es False")
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
    if prueba1boolean2 in True_V:
        contador_boolean2 += 1
    if prueba2boolean2 in True_V:
        contador_boolean2 += 1
    if prueba3boolean2 in True_V:
        contador_boolean2 += 1
    if prueba4boolean2 in False_F:
        contador_boolean2 == contador_boolean2
    if prueba5boolean2 in True_V:
        contador_boolean2 += 1
    if prueba6boolean2 in False_F:
        contador_boolean2 += 1
    if prueba7boolean2 in False_F:
        contador_boolean2 += 1
    if prueba8boolean2 in False_F:
        contador_boolean2 += 1
    if prueba9boolean2 in True_V:
        contador_boolean2 += 1
    if prueba10boolean2 in True_V:
        contador_boolean2 += 1
    if prueba11boolean2 in True_V:
        contador_boolean2 += 1
    print("Obtuviste", contador_boolean2, " sobre 11 preguntas bien")
    if contador_boolean2 == 11:
        print("¡Muy bien tuviste todo bien!")
        siguiente=input("\n Ahora presiona Enter si quieres continuar a la siguiente sección:")
        if siguiente=="":
          lectura_estructura_selectiva()
    if contador_boolean2 < 11:
        print("¿Quieres seguir practicando?")
        seguir_practicando2 = input("Si quieres escribe la palabra si acá: ")
    if seguir_practicando2 in si_exp:
        ejercicio_boolean2()
    elif seguir_practicando2 in no_exp:
      print("\nEntonces seguiremos con la educación")
      lectura_estructura_selectiva()
    else:
      seguir_practicando2=="nada"
      print("Error")
      print("¿Quieres seguir practicando?")
      seguir_practicando2 = input("(si/no):")   
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
#Listas
def lecturna_conjuntos():
    print("\n---------------------"
          "\nSECCIÓN 4: LISTAS"
          "\n---------------------"
          "\nAntes de conocer las listas  debemos saber que son los conjuntos."
          "\nUn conjunto, es una colección no ordenada y sin elementos repetidos. "
          "\nLos usos básicos de éstos incluyen verificación de pertenencia y eliminación de entradas duplicadas."
          "\n"
          "\nEjemplo1:"
          "\nanimales = ['perro','gato','conejo','tortuga']; en este conjunto se puede"
          "\n"
          "\nAsí mismo se puede establecer un conjunto dentro de una variable"
          "\nEjemplo2:"
          "\nanimales_domesticos=set(animales); de este modo la variable animales_domesticos esta conformada por el conjunto animales"
          "\n")
def lectura_listas():
    print("\nLa lista en Python son variables que almacenan arrays, internamente cada posición puede ser un tipo de datos distinto."
          "\nEn Python tiene varios tipos de datos compuestos, usados para agrupar otros valores. "
          "\nEl más versátil es la lista, la cual puede ser escrita como una lista de valores separados por coma (ítems) entre corchetes."
          "\nNo es necesario que los ítems de una lista tengan todos el mismo tipo.")
#Funciones
def lectura_función():
    print("Una función es un conjunto de instrucciones que realizan alguna tarea y esta tarea va a invocar más de una vez un mismo programa.")
    print("a) Pueden recibir o no parámetros")
    print("b) Pueden retornar un valor o pueden no retornar ningun valor")
    print("""Para escribir una función se tiene que comenzar la función con la palabra "def" """)
    print("")
    print("Ejemplo:")
    print("def DoSomething():")
    print("    value = 1")
    print("    return value")
    print("")
    print("""En este caso se crea la función utilizando la palabra "def". \n Luego, se nombra la función.\n Se le manda una labor que hacer a la función, la cual recibe un valor de uno y, \n finalmente, se retorna el valor asignado. """)
    print("")
    print("Hay que principalmente tener cuidado con algunas cosas")
    print("")
    print("1) siempre define tu función")
    print("""2) Acuerdate que el nombre de tu función tiene que ser una sola palabra. Puede tener "_", "-", "/" o cualquier otro caracter para unir palabras pero no pueden haber espacios entre palabras """)
    print("3) siempre tienen que haber brackets al terminar de escribir la función")
    print("""4) La función siempre tiene que terminar con la palabra "return" """)
    print("5) Si se quiere llamar a la función, se tiene que escribir su nombre afuera")
    print("")
    print("Otro ejemplo:")
    print("")
    print("Cree una función la cual cambie grados centigrados a Kelvin")
    print("")
    print("def fahr_to_Kelvin(temp):")
    print("   return((temp-32)*(5/9))")
    print("""temperatura=int(input("Ingresa tu temperatura en farenheit":))""")
    print("""print("fahr_to_kelvin(temperatura)""")
    print("")
    print("")
    print("También se pueden utilizar funciones dentro de funciones")
    print("Un ejemplo es la función print")
    print("Si se escribe la función print dentro de una función se estaría imprimiendo el valor indicado")
    print("")
    print("Por ejemplo:")
    print("")
    print("")
    print("def licencia():")
    print("""    print("Copyright 2017")""")
    print("""    print("AUS204")""")
    print("      return")
    print("licencia()")
    print("")
    print("")
    print("Otro probelam que se puede encontrar con las funciones es la definición de las variables. Acá hay una función ara ilustrarlo:")
    print("")
    print("def escribe_suma():")
    print("    suma=a+b")
    print("""    print("La suma de {a} y {b} es: {suma}")""")
    print("    return")
    print("a=4")
    print("b=5")
    print("escribe_suma()")
    print("")
    print("")
    print("El problema de esta función es que los valores son muy específicos ya que la función solo funcionaría con los valores a y b. Además siempre va a imprimir el resultado, lo cual no siempre es útil")
    print("Esto puede solucionarse")
    print("")
    print("Aca está la función mejorada:")
    print("")
    print("")
    print("def escribe_suma(x,y):")
    print("    suma=x+y")
    print("    return suma")
    print("a=4")
    print("b=5")
    print("escribe_suma(a,b)")
    print("""print(f"La suma de {a} y {b} es: {suma}") """)
    print("")
    print("¿Vez la diferencia?")
    print("El último programa es más general y por lo tanto más reutilizable ya que generaliza algunos términos")
    print("")
    print("Un último ejemplo")
    print("")
    print("")
    print("lado = 0")
    print("def main():")
    print("    lado = int(input())")
    print("    print(cuadrado_área())")
    print("    return")
    print("")
    print("def cuadrado_área():")
    print("    return lado**2")
    print("")
    print("")
    print("Ya que la variable lado esta afuera de los scopes de las otras funciones, se puede utilizar en ambas funciones y puede ser accedida por cualquier parte")
    print("Sino, se tendría que variar la variable lado a otra variable para la función cuadrado_area")
    return
def ejercicio_funciones():
    print("Ahora, harás un pequeño quiz para ver si has comprendido el tema de funciones. Tienes que escribir el output de los siguientes códigos:")
    print("")
    print("Constrains: Ingresa solo el número")
    print("")
    print("Numero 1 ,Función 1:")
    print("")
    print("")
    print("def f(x):")
    print("    return g(x)+h(x)")
    print("")
    print("def g(x):")
    print("    return 4*h(x)")
    print("")
    print("def h(x):")
    print("    return x**2")
    print("")
    print("print(f(2))")
    print("")
    output1funciones = int(input("Ingresa el output de la función: "))
    print("")
    print("")
    print("Numero 2 ,Función 1:")
    print("")
    print("")
    print("def f(x):")
    print("    return g(x)+h(x)")
    print("")
    print("def g(x):")
    print("    return 4*h(x)")
    print("")
    print("def h(x):")
    print("    return x**2")
    print("")
    print("print(f(3))")
    print("")
    output2funciones = int(input("Ingresa el output de la función: "))
    print("")
    print("")
    print("Numero 3 ,Función 1:")
    print("")
    print("")
    print("def f(x):")
    print("    return g(x)+h(x)")
    print("")
    print("def g(x):")
    print("    return 4*h(x)")
    print("")
    print("def h(x):")
    print("    return x**2")
    print("")
    print("print(f(1))")
    print("")
    output3funciones = int(input("Ingresa el output de la función: "))
    print("")
    print("")
    print("")
    print("Numero 1 , Función 2")
    print("")
    print("")
    print("def funcion_misteriosa(n):")
    print("    suma = 0")
    print("    for i in range(n):")
    print("        suma=suma+i")
    print("    return(suma)")
    print("")
    print("print(funcion_misteriosa(4))")
    print("")
    output4funciones = int(input("Ingresa el output de la función: "))
    print("")
    print("")
    print("Numero 2 , Función 2")
    print("")
    print("")
    print("def funcion_misteriosa(n):")
    print("    suma = 0")
    print("    for i in range(n):")
    print("        suma=suma+i")
    print("    return(suma)")
    print("")
    print("print(funcion_misteriosa(8))")
    print("")
    output5funciones = int(input("Ingresa el output de la función: "))
    print("")
    print("")
    print("Numero 3 , Función 2")
    print("")
    print("")
    print("def funcion_misteriosa(n):")
    print("    suma = 0")
    print("    for i in range(n):")
    print("        suma=suma+i")
    print("    return(sum)a")
    print("")
    print("print(funcion_misteriosa(6))")
    print("")
    output6funciones = int(input("Ingresa el output de la función: "))
    print("")
    print("")
    print("")
    print("Numero 1, Función 3")
    print("")
    print("")
    print("")
    print("def funcion_x(variable):")
    print("    contador = 0")
    print("    for i in variable:")
    print("        if i in ['a', 'e','i','o','u']:")
    print("            contador=contador + 1")
    print("    return contador")
    print("")
    print("print(funcion_x(['amigo'])")
    print("")
    output7funciones = int(input("Ingresa el output de la función: "))
    print("")
    print("")
    print("")
    print("Numero 2, Función 3")
    print("")
    print("")
    print("")
    print("def funcion_x(variable):")
    print("    contador = 0")
    print("    for i in variable:")
    print("        if i in ['a', 'e','i','o','u']:")
    print("            contador=contador + 1")
    print("    return contador")
    print("")
    print("print(funcion_x(['hasta'])")
    print("")
    output8funciones = int(input("Ingresa el output de la función: "))
    print("")
    print("")
    print("")
    print("Numero 3, Función 3")
    print("")
    print("")
    print("")
    print("def funcion_x(variable):")
    print("    contador = 0")
    print("    for i in variable:")
    print("        if i in ['a', 'e','i','o','u']:")
    print("            contador=contador + 1")
    print("    return contador")
    print("")
    print("print(funcion_x(['Soy un hacker'])")
    print("")
    output9funciones = int(input("Ingresa el output de la función: "))
    contador_funciones = 0
    if output1funciones == 20:
        contador_funciones += 1
    if output2funciones == 45:
        contador_funciones += 1
    if output3funciones == 5:
        contador_funciones += 1
    if output4funciones == 6:
        contador_funciones += 1
    if output5funciones == 28:
        contador_funciones += 1
    if output6funciones == 15:
        contador_funciones += 1
    if output7funciones == 3:
        contador_funciones += 1
    if output8funciones == 2:
        contador_funciones += 1
    if output9funciones == 4:
        contador_funciones += 1
    if contador_funciones == 9:
        print("Muy bien, sacaste todo bien")
        volver_a_intentar = input("Si quieres volver a intentar los ejercicios escribe la palabra si acá: ")
    else:
        print("sacaste ",contador_funciones,"/sobre 9 preguntas bien")
        print("¿Quieres volver a intentar los ejercicios?")
        volver_a_intentar = input("Si quieres volver a intentar los ejercicios escribe la palabra si acá: ")
    while volver_a_intentar == "si":
            print(
                "Ahora, haras un pequeño quiz para ver si has comprendido el tema de funciones. Tienes que escribir el output de los siguientes códigos")
            print("Constrains: Ingresa solo el número")
            print("")
            print("Numero 1 ,Función 1:")
            print("")
            print("")
            print("def f(x):")
            print("    return g(x)+h(x)")
            print("")
            print("def g(x):")
            print("    return 4*h(x)")
            print("")
            print("def h(x):")
            print("    return x**2")
            print("")
            print("print(f(2))")
            print("")
            output1funciones = int(input("Ingresa el output de la función: "))
            print("")
            print("")
            print("Numero 2 ,Función 1:")
            print("")
            print("")
            print("def f(x):")
            print("    return g(x)+h(x)")
            print("")
            print("def g(x):")
            print("    return 4*h(x)")
            print("")
            print("def h(x):")
            print("    return x**2")
            print("")
            print("print(f(3))")
            print("")
            output2funciones = int(input("Ingresa el output de la función: "))
            print("")
            print("")
            print("Numero 3 ,Función 1:")
            print("")
            print("")
            print("def f(x):")
            print("    return g(x)+h(x)")
            print("")
            print("def g(x):")
            print("    return 4*h(x)")
            print("")
            print("def h(x):")
            print("    return x**2")
            print("")
            print("print(f(1))")
            print("")
            output3funciones = int(input("Ingresa el output de la función: "))
            print("")
            print("")
            print("")
            print("Numero 1 , Función 2")
            print("")
            print("")
            print("def funcion_misteriosa(n):")
            print("    suma = 0")
            print("    for i in range(n):")
            print("        suma=suma+i")
            print("    return(suma")
            print("")
            print("print(funcion_misteriosa(4)")
            print("")
            output4funciones = int(input("Ingresa el output de la función: "))
            print("")
            print("")
            print("Numero 2 , Función 2")
            print("")
            print("")
            print("def funcion_misteriosa(n):")
            print("    suma = 0")
            print("    for i in range(n):")
            print("        suma=suma+i")
            print("    return(suma")
            print("")
            print("print(funcion_misteriosa(8)")
            print("")
            output5funciones = int(input("Ingresa el output de la función: "))
            print("")
            print("")
            print("Numero 3 , Función 2")
            print("")
            print("")
            print("def funcion_misteriosa(n):")
            print("    suma = 0")
            print("    for i in range(n):")
            print("        suma=suma+i")
            print("    return(suma")
            print("")
            print("print(funcion_misteriosa(6)")
            print("")
            output6funciones = int(input("Ingresa el output de la función: "))
            print("")
            print("")
            print("")
            print("Numero 1, Función 3")
            print("")
            print("")
            print("")
            print("def funcion_x(variable):")
            print("    contador = 0")
            print("    for i in variable:")
            print("        if i in ['a', 'e','i','o','u']:")
            print("            contador=contador + 1")
            print("    return contador")
            print("")
            print("print(funcion_x(['amigo']")
            print("")
            output7funciones = int(input("Ingresa el output de la función: "))
            print("")
            print("")
            print("")
            print("Numero 2, Función 3")
            print("")
            print("")
            print("")
            print("def funcion_x(variable):")
            print("    contador = 0")
            print("    for i in variable:")
            print("        if i in ['a', 'e','i','o','u']:")
            print("            contador=contador + 1")
            print("    return contador")
            print("")
            print("print(funcion_x(['hasta']")
            print("")
            output8funciones = int(input("Ingresa el output de la función: "))
            print("")
            print("")
            print("")
            print("Numero 3, Función 3")
            print("")
            print("")
            print("")
            print("def funcion_x(variable):")
            print("    contador = 0")
            print("    for i in variable:")
            print("        if i in ['a', 'e','i','o','u']:")
            print("            contador=contador + 1")
            print("    return contador")
            print("")
            print("print(funcion_x(['Soy un hacker']")
            print("")
            output9funciones = int(input("Ingresa el output de la función: "))
            contador_funciones = 0
            if output1funciones == 20:
                contador_funciones += 1
            if output2funciones == 45:
                contador_funciones += 1
            if output3funciones == 5:
                contador_funciones += 1
            if output4funciones == 6:
                contador_funciones += 1
            if output5funciones == 28:
                contador_funciones += 1
            if output6funciones == 15:
                contador_funciones += 1
            if output7funciones == 3:
                contador_funciones += 1
            if output8funciones == 2:
                contador_funciones += 1
            if output9funciones == 4:
                contador_funciones += 1
            if contador_funciones == 9:
                print("Muy bien, sacaste todo bien")
                volver_a_intentar = input("Si quieres volver a intentar los ejercicios escribe la palabra si acá: ")
            else:
                print("sacaste ", contador_funciones, "/sobre 9 preguntas bien")
                print("¿Quieres volver a intentar los ejercicios?")
                volver_a_intentar = input("Si quieres volver a intentar los ejercicios escribe la palabra si acá: ")
    return()
#Creditos
def creditos():
  print("-----------------------------------------"
        "\nProgramasción:"
        "\nHumberto Bernal"
        "\nGonzalo Garcia"
        "\nAlexandra Meerovici"
        "\n"
        "\nPrograma finalizado")
#Contenido
def contenido():
  print("\nTemas")

  lista_contenido=[
  "Variables",
  "Estructuras de Control Selectivas",
  "Estructuras de Control Repetitivas",
  "Listas",
  "Funciones",
  "Strings",
  "Menu",
  "Salir"
  ]

  for numero_de_contenido in range(len(lista_contenido)):
    contenido_general=str(numero_de_contenido+1)+"."+lista_contenido[numero_de_contenido]
    print(contenido_general)
    
  for error_contenido in range(3):
    correr_contenido=input("\nIngrese Tema: ")
    if correr_contenido=="1" or correr_contenido=="variables":
      lectura_variables()
      break
    elif correr_contenido=="2" or correr_contenido=="estructuras de control selectivas":
      lectura_if_boolean()
      break
    elif correr_contenido=="3" or correr_contenido=="estructuras de control repetitivas":
      loops()
      break
    elif correr_contenido=="4" or correr_contenido=="listas":
      lecturna_conjuntos()
      break
    elif correr_contenido=="5" or correr_contenido=="funciones":
      lectura_función()
      break
    elif correr_contenido=="6" or correr_contenido=="strings":
      strings()
      break
    elif correr_contenido=="7" or correr_contenido=="menu":
      instrucciones()
      break
    elif correr_contenido=="8" or correr_contenido=="salir":
      print("El programa ha finalizado.")
      break
    else:
      print("\nPor favor ingrese el numero que marca el tema")
#START
main_menu()
#final

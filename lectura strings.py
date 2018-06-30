def lectura_strings():
    print("Un string es una cadena de caracteres. Esta generalmente está ordenada.\n Estas cadenas también,como las listas, tienen ciertos valores asignados. Por ejemplo, en la cadena: Monty Python, la M tendría el valor 0 y la P el valor 6, \n ")
    print("Entonces, si pusiera el texto:\n s = Monty Python \n print(s[2]) \n el output sería la letra n \n")
    print("Para delimitar tu cadena, necesitas poner el texto entre comillas simples, comillas dobles o comillas triples. Esto identificaría a un string. \n  ")
    print("""Tambén, existen muchos operadores con los strings. \nla expresión %d puede determinar un entero, %s un string y %f un float \n\nPor ejemplo:\n text = "%d tigres comen % 1f porción de %s en un %s (3, 0.5, 'trigo') \n print(text) \n \n   """)
    print("""Además, si se quiere utilizar un número en una cadena se debe concatenar la expresión utilizando la variable: str() 
    \nPor ejemplo: \n pi = 3.14 \n text = 'El valor de pi es: ' + str(pi)""")
    print("""Otras funciones que se pueden utilizar son: \n \nlen(): para hallar el largo de un string o cantidad de caracteres \n len('Esta es una frase') daría de output 17 \n\nfind: para determinar si un string está dentro de otro string. Devuelve el indice donde este string es hallado \n 'Esta es una frase'.find("frase") da de output 12 \n Si es que no se logra encontrar el string buscado,el programa devolverá -1 \n \nreplace: reemplaza el string a buscar por el indicado dentro del string grande \n 'Este es un string'.replace(string,String) da de output: Este es un String \n\njoin(): devuelve una cadena de texto donde los valores de la cadena original que llama el join aparecen separados por un caracter que fue pasado al join() como argumento\n s= "Escribe una frase" \n print(",".join(s)) \n da como output: E,s,c,r,i,b,e, ,u,n,a, ,f,r,a,s,e \n \nsplit(): aplicado a un string, crea una lista en la que cada elemento es una palabra del string\n S="Hola esta es una frase" \n s1, s2, s3, s4, s5 = s.split(' ') \n print(s1, s2) \n da de output: Hola esta\n \n \n""")
    print("""Otras funciones: \n \n capitalize(): Capitaliza el primer caracter de la cadena \n lower(): Convierte la cadena en minúscula \n upper(): convierte la cadena en mayúscula \n strip(): elimina los espacios en blanco a los costaods \n backslash t: inserta un tabulado'""")
    return()
lectura_strings()

def ejercicio_strings():
    true_tupla = ("T","t","true","True")
    false_tupla = ("F", "f", "false", "False")
    print("")
    print("Ahora es tu turno de practicar lo que son strings")
    print("")
    print("Pregunta 1")
    print("")
    print("¿Se puede separar un string en partes?")
    respuesta_1_strings = input("Responde True o False: ")
    print("")
    print("Pregunta 2")
    print("")
    print("""¿ Si tengo el  código:
    s = 'El numero pi es: ' + pi 
    ¿Obtendría un output?""")
    respuesta_2_strings = input("Responde True o False: ")
    print("")
    print("Pregunta 3")
    print("")
    print("""Teniendo el codigo:
    "La vida es mucho mejor con Python".find("Python")
    ¿El output sería 26?""")
    respuesta_3_strings = input("Responde True o False: ")
    print("")
    print("Pregunta 4")
    print("")
    print("¿Se pueden unir dos strings?")
    respuesta_4_strings = input("Responde True o False: ")
    print("")
    print("""Teniendo el codigo:
          s= "soy un hacker"
          print(",".join(s))
          ¿Mi output sería: soy, un, hacker?""")
    respuesta_5_strings = input("Responde True o False: ")
    print("")
    print("Pregunta 6")
    print("")
    print("¿Si utilizo la función find() y no encuentro la cadena buscada igual recibo un output?")
    respuesta_6_strings = input("Responde True o False: ")
    print("")
    contador_strings = 0
    if respuesta_1_strings in true_tupla:
        contador_strings += 1
    if respuesta_2_strings in false_tupla:
        contador_strings += 1
    if respuesta_3_strings in false_tupla:
        contador_strings += 1
    if respuesta_4_strings in true_tupla:
        contador_strings += 1
    if respuesta_5_strings in false_tupla:
        contador_strings += 1
    if respuesta_6_strings in true_tupla:
        contador_strings += 1
    print("tuviste ", contador_strings,"/6 bien")
    print("¿Quieres volver a intentarlo?")
    volver_a_intentar = input("Si quieres volver a intentarlo escribe la palabra si aca: ")
    if volver_a_intentar == "si" or volver_a_intentar == "sí":
        ejercicio_strings()
ejercicio_strings()



def algoritmos_busquedas_lectura():
    print("Así como existen algoritmos de ordenamiento también existen algoritmos de búsqueda.\nDe estos, se van a observar 2")
    print("")
    print("---------------")
    print("Busqueda lineal")
    print("---------------")
    print("")
    print("Ejemplo del algoritmo:")
    print("")
    print("""list = [10,14,19,26,27,31,33,35,42,43]
search = int(input("Ingrese el número a buscar"))
for i in range(0,len(list)):
  if search==list[i]:
    print(str(search) + " encontrado en la posición " + str(i))""")
    print("")
    print("- Es un algoritmo bastante sensillo.es que se puede usar en lineas desordenadas\n- la lista puede estar desordenada. \n- la velocidad de ejecución depende linearmente del tamaño del arreglo")
    print("")
    print("-----------------")
    print("Busqueda binaria")
    print("-----------------")
    print("")
    print("Ejemplo del algoritmo:")
    print("")
    print("""def binary_search(list, buscado):
    min = 0  
    max = len(list) - 1  
    while True:
        if max < min:
            return -1
        m = (min + max) // 2  
        if list[m] < buscado:
            min = m + 1  
        elif list[m] > buscado:
            max = m - 1
        else:
            return m

list = [10,14,19,26,27,31,33,35,42,43]
search = int(input("Ingrese el número a buscar"))
print (binary_search(list,search))""")
    print("")
    print("- Este utiliza el enfoque divide y venceras tal y como el algoritmo de ordenamiento MergeSort().\n- Se utiliza en listas ordenadas\n - Copara todos los valores con el elemento del medio de la lista y si no son iguales se elimina la mitad en la cual el valor no puede estar")
    print("")
    print("")
    return()
algoritmos_busquedas_lectura()

def ejercicios_ordenamiento():
    true_tupla = ("T", "t", "true", "True")
    false_tupla = ("F", "f", "false", "False")
    contador_sorting = 0
    print("")
    print("Ahora, vas a completar un pequeño quiz para ver si has entendido todo")
    print("")
    print("Pregunta 1")
    print("")
    print("¿Linear search se utiliza para algoritmos desordenados?")
    respuesta1 = input("Escribe si la respuesta es true o false: ")
    print("")
    print("Pregunta 2")
    print("")
    print("¿En la busqueda binaria se usa el enfoque divide y venceras?")
    respuesta2 = input("Escribe si la respuesta es true o false: ")
    print("")
    print("Pregunta 3")
    print("")
    print("¿Busueda lineal es más eficiente que busqueda binaria?")
    respuesta3 = input("Escribe si la respuesta es true o false: ")
    if respuesta1 in true_tupla:
        contador_sorting += 1
    if respuesta2 in true_tupla:
        contador_sorting += 1
    if respuesta3 in false_tupla:
        contador_sorting += 1
    print("tuviste ", contador_sorting, "/3 bien")
    print("¿Quieres volver a intentarlo?")
    volver_a_intentar_sorting = input("Si quieres volver a intentarlo escribe la palabra si aca: ")
    if volver_a_intentar_sorting == "si" or volver_a_intentar_sorting == "sí":
        ejercicios_ordenamiento()
    return()

ejercicios_ordenamiento()



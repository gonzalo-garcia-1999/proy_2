def bubbleSort(lista):
    for num in range(len(lista) - 1, 0, -1):
        for j in range(num):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista

def selectionSort(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i, len(lista)):
            if (lista[j]) < lista[min]:
                min = j
        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux
    return lista

def insertionSort(lista):
    for i in range(1, len(lista)):
        aux = lista[i]
        pos = i
        while pos > 0 and lista[pos - 1] > aux:
            lista[pos] = lista[pos - 1]
            pos = pos - 1
        lista[pos] = aux
    return lista


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist

def ordenar_listas():
    lista_corta=[1,22,44,31,9,103,4,1093,444,19]
    lista_larga = [53,64,17,8,15,47,81,5,31,72,93,32,25,37,26,27,58,23,89,26,76,78,28,51,56,53,49,81,4,94,55,2,51,5,53,5,93,37,39,90,56,80,25,7,10,52,3,36,49,40,64,18,66,45,70,44,14,54,70,28,44,24,45,36,14,98,88,94,55,57,3,90,66,90,95,5,7,3,11,83,99,98,17,90,30,44,29,53,18,44,32,60,86,17,74,15,56,24,92,96]
    print("Aca hay 2 listas una corta (10 numeros) y una larga (100 numeros). Prueba los algoritmos de ordenamiento por ti solo y ordena estas listas. \n \n Utiliza un cronómetro para verificar cual es más eficiente")
    print("")
    print("1) Lista Corta")
    print("2) Lista Larga")
    print("")
    print("a) Bubble Sort\nb)Selection Sort\nc) Insertion Sort\nd) Merge Sort")
    print("")
    lista_escogida = input("Escribe el numero 1 si quieres la lista corta o el numero 2 si quieres la lista larga aca: ")
    algoritmo_escogido = input("Ingresa la letra que corresponde al algoritmo que quieres probar ( a para BubbleSort, b para Selection Sort, c para Insertion Sort y d para Merge Sort): ")
    if lista_escogida == "1":
        if algoritmo_escogido == "a":
            print(bubbleSort(lista_corta))
        elif algoritmo_escogido == "b":
            print(selectionSort(lista_corta))
        elif algoritmo_escogido == "c":
            print(insertionSort(lista_corta))
        elif algoritmo_escogido == "d":
            print(mergeSort(lista_corta))
    elif lista_escogida == "2":
        if algoritmo_escogido == "a":
            print(bubbleSort(lista_larga))
        elif algoritmo_escogido == "b":
            print(selectionSort(lista_larga))
        elif algoritmo_escogido == "c":
            print(insertionSort(lista_larga))
        elif algoritmo_escogido == "d":
            print(mergeSort(lista_larga))
ordenar_listas()


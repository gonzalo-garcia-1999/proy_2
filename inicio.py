#instrucciones
def instrucciones():
  print("\nBienvenido")
  print("\nEste programa le enseñara a usar python.")
  print("\nInstrucciones:")
  
  lista_instrucciones=[
  "Al finalizar una lectura o ejercicio insertar 'continuar' o 'salir'",
  "Si esta regresando al programa inserte el numero que esta al lado del tema en el que se quedo",
  "Insertar todo en minusculas", 
  "Al final de un ejercicio insertar 'regresar' si desea retornar a la lectura",
   "Si esta regregrsando ingrese su usuario",
  "Para comenzar desde el comienzo inserte 'comenzar'"
  ]

  for numero_de_instruccion in range(len(lista_instrucciones)):
    instruccion_general=str(numero_de_instruccion+1)+"."+lista_instrucciones[numero_de_instruccion]
    print(instruccion_general)
  correr_instrucciones=input("\nInserte aquí: ")
  if correr_instrucciones=="comenzar":
    contenido()

#contenido
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
      variables()
    elif correr_contenido=="2" or correr_contenido=="estructuras de control selectivas":
      estructuras_de_control_selectivas()
    elif correr_contenido=="3" or correr_contenido=="estructuras de control repetitivas":
      loops()
    elif correr_contenido=="4" or correr_contenido=="listas":
      listas()
    elif correr_contenido=="5" or correr_contenido=="funciones":
      funciones()
    elif correr_contenido=="6" or correr_contenido=="strings":
      strings()
    elif correr_contenido=="7" or correr_contenido=="menu":
      instrucciones()
    elif correr_contenido=="8" or correr_contenido=="salir":
      break
    else:
      print("\nPor favor ingrese el numero que marca el tema")


#main
instrucciones()

#instrucciones
def instrucciones():
  print("Bienvenido")
  print("\nEste programa le enseñara a usar python.")
  print("\nInstrucciones:")
  
  lista_instrucciones=[
  "Para comenzar inserte el numero '1'", 
  "Al finalizar una lectura o ejercicio insertar 'continuar' o 'salir'",
  "Si esta regresando al programa inserte el numero que esta al lado del tema en el que se quedo",
  "Insertar todo en minusculas", 
  "En un ejercicio insertar 'regresar' si desea retornar a la lectura"
  ]
  
  for numero_de_instruccion in range(len(lista_instrucciones)):
    instruccion_general=str(numero_de_instruccion+1)+"."+lista_instrucciones[numero_de_instruccion]
    print(instruccion_general)

instrucciones()
#hola

import random
import string
import time
#Imports necesarios para que el programa funcione, el random permite conseguir un valor aleatorio el cual es utilizado para la ubicación aleatoria de las palabras en la cuadricula.
#El import string permite el uso de caracteres, simbolos y demás que normalmente la computadora no puede utilizar, teniendo acceso a la tabla ascii.
#Y por ultimo el import time permite el funcionamiento del temporizador utilizado para la sopa de letras.

def crear_cuadrícula(tamaño):  # Crea una cuadrícula vacía representada como una lista de strings.
  matriz = [["." for x in range(tamaño)] for y in range(tamaño)] # Toma los espacios vacios y los multplica por el número que define el usuario del tamaño de la cuadricula.
  return matriz
  
# Función para insertar palabras horizontalmente, verticalmente u horizontalmente
def insertar_palabra_simple(matriz, tamaño, palabra, dificultad):
  palabra_len = len(palabra)
  intentos = 100
  while intentos>0:
    fila_inicial = random.randint(0, tamaño - 1)
    col_inicial = random.randint(0, tamaño - 1)     #matriz[filas][columnas] 


    if dificultad == 1: 
      dirp = 'H'

      if dirp == 'H':
        if col_inicial + palabra_len <= tamaño:
          # Insertar palabra horizontalmente
          if all(matriz[fila_inicial][col_inicial + i] in ('.', palabra[i]) for i in range(palabra_len)):
            for i in range(palabra_len):
              matriz[fila_inicial][col_inicial + i] = palabra[i]
            return
      print(f"La palabra '{palabra}' no ha podido ser colocada conforme a la dirección {dirp} ")
      #Este código intenta colocar una palabra en una matriz, verificando si las casillas están vacías o coinciden con las letras de la palabra. 
      # Si todas las casillas son válidas, la palabra se coloca en la matriz y la función termina. Si no, se imprime un mensaje de error.


    elif dificultad == 2: 
      dirs = input("Decida la dirección para agregar la palabra: \n - 'H': Para horizontales \n - 'V': Para verticales \n  Aquí su decisión:  ").upper()      

      if dirs == 'H':
        if col_inicial + palabra_len <= tamaño:
          # Insertar palabra horizontalmente
          if all(matriz[fila_inicial][col_inicial + i] in ('.', palabra[i]) for i in range(palabra_len)):
            for i in range(palabra_len):
              matriz[fila_inicial][col_inicial + i] = palabra[i]
            return
        
      elif dirs == 'V':
        if fila_inicial + palabra_len <= tamaño:
          # Insertar palabra verticalemente
          if all(matriz[fila_inicial+i][col_inicial] in ('.', palabra[i]) for i in range(palabra_len)):
            for i in range(palabra_len):
              matriz[fila_inicial+i][col_inicial] = palabra[i]
            return
      print(f"La palabra '{palabra}' no ha podido ser colocada conforme a la dirección {dirs} ")
      #Este funciona de la misma manera al anterior, exceptuando que en vez de tener un direccionamiento horizontal, es un direccionamiento vertical
      #Claro esta, para esto el codigo cambia al efectuar la sumatoria del indice (i) en fila_inicial en vez de col_inicial.


    elif dificultad == 3: 
      dirt = input("Decida la dirección para agregar la palabra: \n - 'H': Para horizontales \n - 'V': Para verticales \n - 'D': Para diagonales \n Aquí su decisión:  ").upper()      

      if dirt == 'H':
        if col_inicial + palabra_len <= tamaño:
          # Insertar palabra horizontalmente
          if all(matriz[fila_inicial][col_inicial + i] in ('.', palabra[i]) for i in range(palabra_len)):
            for i in range(palabra_len):
              matriz[fila_inicial][col_inicial + i] = palabra[i]
            return
        
      elif dirt == 'V':
        if fila_inicial + palabra_len <= tamaño:
          # Insertar palabra verticalemente
          if all(matriz[fila_inicial+i][col_inicial] in ('.', palabra[i]) for i in range(palabra_len)):
            for i in range(palabra_len):
              matriz[fila_inicial+i][col_inicial] = palabra[i]
            return
        
      elif dirt == 'D':
        if fila_inicial + palabra_len <= tamaño and col_inicial + palabra_len <= tamaño:
          # Insertar palabra diagonalmente
          if all(matriz[fila_inicial+i][col_inicial + i] in ('.', palabra[i]) for i in range(palabra_len)):
            for i in range(palabra_len):
              matriz[fila_inicial+i][col_inicial+i] = palabra[i]
            return
      print(f"La palabra '{palabra}' no ha podido ser colocada conforme a la dirección {dirt} ")
      #Y este ultimo se ejecuta de la misma manera, exceptuando que tambien existe la opción de la diagonal, la cual para ser ejecutada la sumatoria del indice iria a ambos
      #Tanto para fila_inicial como para col_inicial permitiendo asi ese movimiento en diagonal.

    intentos -= 1 


def temporizador(segundos:int):
  while segundos > 0:
    minutes, seconds = segundos//60, segundos%60
    print (f"{minutes:02d}:{seconds:02d}") 
    time.sleep(1)
    segundos -= 1   
  print ("¡El tiempo ha finalizado!")
#Aqui se crea la función del temporizador, tomando los segundos dados por el usuario y convirtiendolos en minutos, y utilizando el time.sleep(1) para detener la ejecución del restado durante 1 segundo
#Obteniendo un temporizador


def encontrar_palabras(matriz, palabra):
  tamañoM = len(matriz)
  palabra_len = len(palabra)
  for x in range (tamañoM):
    for y in range (tamañoM - palabra_len):
      if "".join(matriz[x][y:y + palabra_len]) == palabra:
        for i in range(palabra_len):
          matriz[x][y + i] = f"({matriz[x][y + i]})"
  for y in range(tamañoM):
    for x in range(tamañoM - palabra_len + 1):
      if "".join(matriz[x + i][y] for i in range(palabra_len)) == palabra:
        for i in range(palabra_len):
          matriz[x + i][y] = f"({matriz[x + i][y]})"
  for x in range(tamañoM - palabra_len + 1):
    for y in range(tamañoM - palabra_len + 1):
      if "".join(matriz[x + i][y + i] for i in range(palabra_len)) == palabra:
        for i in range(palabra_len):
          matriz[x + i][y + i] = f"({matriz[x + i][y + i]})"
#Esta función se encarga de buscar la palabra iterando continuamente por las filas y columnas de la cuadricula.


def rellenar_matriz(matriz):
  for x in range (len(matriz)):
    for y in range (len(matriz[x])):
      if matriz[x][y] == '.':
        matriz[x][y] = random.choice(string.ascii_uppercase)
#Y esta es la función encargada del rellenado de los espaciós vacios de forma aleatoria utilizando los caracteres mayusculas de la tabla ASCII.
               
   

if __name__ == "__main__":
  print("¡Bienvenido a esta sopa de letras! \nA continuación, vamos a determinar sus condiciones.")
  tamaño = int(input("\n- Ingrese el tamaño de la sopa de letras (10-30): "))
  while tamaño < 10 or tamaño > 30:
    tamaño = int(input("- Por favor, ingrese un tamaño válido (10-30): ")) 
  #Primera interacción del Usuario con el programa, en este el programa solicita al usuario las condiciones 
  #siendo la primera de estas el tamaño de la cuadricula, en caso de que este dato no sea valido, entra en un bucle hasta que sea ejecutable.


  palabras = input("- Ingrese las palabras a encontrar (separadas por espacios): ").strip().upper().split()
  #Por este lado tenemos el ingreso de las palabras deseadas por el usuario para la sopa de letras, pasando por los metodos de strip, upper y split.
  #strip retorna las palabras sin espacios, upper las retorna en mayusculas sostenidas y split separa los caracteres de una palabra en una lista.

  dificultad = int(input("- Ingrese la dificultad deseada: \n 1. Fácil. \n 2. Intermedia \n 3. Difícil \n --> "))
  while dificultad not in [1, 2, 3]:
    dificultad = int(input("Por favor, ingrese una dificultad válida (1, 2 o 3): "))
  #En esta siguiente interacción con el programa, este solicita la dificultad deseada, la cual consta de 3 niveles y funciona con el mismo sistema del tamaño.
  #Esto es para que si se ingresa un valor no deseado el programa no se rompa al entrar en un ciclo.

  matriz = crear_cuadrícula(tamaño)
 
  for i in palabras:
    insertar_palabra_simple(matriz, tamaño, i, dificultad)
  
  rellenar_matriz(matriz)
  #Este es el llamado de las funciones con los datos ingresados por el usuario.
  
  tiempo_total = int(input("\n- Ingrese el tiempo total (en segundos) deseado para resolver la sopa de letras: "))
  #Ingreso de los segundos deseados por el usuario, y asi darle valor a la variable.

  print("\nSopa de letras generada:")

  for i in matriz:
    print(" ".join(i))
  #Impresión de la sopa de letras.
 

  print("\nEl tiempo ha comenzado! Mucha suerte.")
  temporizador(tiempo_total)
  #Impresión de el temporizador con el tiempo seleccionado por el usuario.


  puntaje = 0
  while len(palabras)>0:
    palabra_encontrada = input("\nIngrese una palabra encontrada: ").strip().upper()
    if palabra_encontrada in palabras:
      encontrar_palabras(matriz, palabra_encontrada)
      palabras.remove(palabra_encontrada)
      puntaje += 10
      print(f"¡Bien hecho! Puntaje total: {puntaje}")
      for i in matriz:
       print(" ".join(i))
  print(f"El juego ha terminado. \n Su puntaje final es: {puntaje}")
  #Sistema de puntaje en el cual al recibir la palabra encontrada este agregue 10 puntos, utilizando el remove para evitar que se ingrese la misma palabra 2 o mas veces y trucar los puntos.
# ProyectoProgramacion-Sopa-de-Letras
En el presente repositorio se desarrollará una aplicación que emule una sopa de letras utilizando Python para la materia de **Programación**

Somos grupo **The Porycodens** integrado por:
- Santiago Montoya.
- Robert Andres Calderon.
- Eduard Enrique Avellaneda.

# **Condiciones**

Para la elaboración del proyecto, se nos plantearon ciertas condiciones que dejaremos claras y son las siguientes:

1. Código original.
   
2. Uso de herramientas vistas en el curso.
   
3. Interacción y manejo a través de la consola.
   
4. Definidido por el usuario:
     - Matriz del tamaño de la sopa de letras (Min: 10x10, Max: 30x30)
     - Ingreso de las palabras: Lista de coordenadas, Strings.
     - Nivel de dificultad: Asociado a cantidad de palabras, verticales, horizontales, diagonal.

# **Aclaraciones Pertinentes**

A la fecha planeteada del proyecto, el tema "matrices" no se ha visto en el curso, por ende la resolución planteada (hasta haber abordado el tema) no incluira "matrices" respetando así la debida cronología del curso.
Para la entrega final se acatara la orden y se emplearan "matrices". Por el momento, se hara uso de lo previamente visto en el curso, como "funciones", "bucles", "strings", "import" y un gran etc que se vera en el desarrollo del codgio acontinuación.

# **Desarrollo Inicial**

Para empezar con este proyecto, teníamos que primero plantearnos cómo lo llevaríamos a cabo con el conocimiento que teníamos. A continuación, presentamos el enfoque inicial:

**1. Estructura del Programa**

El programa estará dividido en varias funciones para hacerlo modular y volverlo comprensible:

- Inicio del programa:

  - Mostrar el menú principal.

  - Solicitar al usuario el tamaño de la sopa de letras (validando que esté entre 10x10 y 30x30).
    
  - Solicitar la lista de palabras y sus coordenadas

    (si bien mencionamos anteriormente que no hariamos uso de las "matrices" por no haberlas visto aun en el curso, nos tomamos la liberta de emplear "listas", algo que al igual que con las "matrices" no habiamos visto, sin el uso de estas (las   
     "listas") seria mucho más complejo el poder llevarlo a cabo).

**2. Generación de la sopa de letras:**

  - Crear la cuadrícula como una cadena de texto con puntos (.) para representar espacios vacíos.

  - Colocar las palabras ingresadas por el usuario en las posiciones especificadas.

  - Rellenar los espacios vacíos con letras aleatorias (aqui hariamos uso del import random).

**3. Mostrar la sopa de letras:**

- Imprimir la cuadrícula en la consola de forma legible.

# **Desarrollo del Codigo**

Para empezar, primero teniamos que importar los modulos "string" y "random".

**- String:** Nos permite importar todas las letras del alfabeto en ingles, estas mismas se utilizaran para rellenar la sopa de letras.

**- Random:** Hace que las letras importadas gracias a "string" se puedan ubicar aleatoriamente en la cuadricula de la sopa de letras, así como exoger aleatorimante la dirección en que se dispondran las palabras.


```python
import random
import string

def crear_cuadricula(tamaño):  # Crea una cuadrícula vacía representada como una lista de strings.
    return ["." * tamaño for _ in range(tamaño)]   # Toma los espacios vacios y los multplica por el número que define el usuario del tamaño de la cuadricula.
```

**Una vez definida esa función y habiendo importado los modulos, viene la parte más larga del codigo, la de colocar las palabras aleatoriamente:**

```python
def colocar_palabras(cuadricula, palabras):
    # Coloca palabras horizontalmente o verticalmente en la cuadrícula.
    
    # Definimos el tamaño de la cuadrícula según la longitud de la lista de palabras.
    tamaño = len(cuadricula)  # Esto asume que la cuadrícula es una lista de listas (2D), y su tamaño es cuadrado.
    
    for palabra in palabras:  # Iteramos sobre cada palabra que queremos colocar en la cuadrícula.
        colocada = False  # Inicializamos la variable, y desde un inicio la caracterizamos como falsa, mientras se cumplan ciertas condiciones al final cambiara a "True", para saber si la palabra ya se ha colocado correctamente.
        
        while not colocada:  # Mientras la palabra no se haya colocado, seguimos intentando (hacemos uso de bucles)
            
            # Elegimos una dirección aleatoria: "H" para horizontal, "V" para vertical. Aquí es donde se hace uso del import random
            direccion = random.choice(["H", "V"])  
            
            if direccion == "H":  # Si la dirección elegida es horizontal:
                # Seleccionamos una fila aleatoria dentro de la cuadrícula.
                fila = random.randint(0, tamaño - 1)
                # Seleccionamos una columna aleatoria en la fila, asegurándonos de que haya espacio suficiente para la palabra.
                columna = random.randint(0, tamaño - len(palabra))
                
                # Comprobamos si todos los lugares donde queremos colocar la palabra están vacíos (representados por ".").
                if all(cuadricula[fila][columna + i] == "." for i in range(len(palabra))):         # Si están vacíos, colocamos la palabra en la fila y columna seleccionadas.
                    for i, letra in enumerate(palabra):                                               # Actualizamos la cuadrícula reemplazando los puntos con las letras de la palabra.
                        cuadricula[fila] = cuadricula[fila][:columna + i] + letra + cuadricula[fila][columna + i + 1:]
                    colocada = True                                                                    # Marcamos la palabra como colocada.

            elif direccion == "V":  # Si la dirección elegida es vertical:
                # Seleccionamos una fila aleatoria donde cabe la palabra verticalmente.
                fila = random.randint(0, tamaño - len(palabra))
                # Seleccionamos una columna aleatoria en la cuadrícula.
                columna = random.randint(0, tamaño - 1)
                
                # Comprobamos si todos los lugares donde queremos colocar la palabra están vacíos.
                if all(cuadricula[fila + i][columna] == "." for i in range(len(palabra))):
                    # Si están vacíos, colocamos la palabra en la columna seleccionada.
                    for i, letra in enumerate(palabra):
                        # Actualizamos cada fila de la columna correspondiente.
                        cuadricula[fila + i] = cuadricula[fila + i][:columna] + letra + cuadricula[fila + i][columna + 1:]
                    colocada = True  # Marcamos la palabra como colocada.

```
**Luego creamos una función la cual rellena aleatoriamente los espacios vacios con letras, luego de poner las palabras a encontrar:**

```python
def rellenar_espacios(cuadricula):
    # Rellena los espacios vacíos con letras aleatorias.
    
    # Recorre cada fila de la cuadrícula (lista de listas).
    for fila in range(len(cuadricula)):  # Iteramos a través de cada fila en la cuadrícula.
        
        # Reemplaza cada punto (.) con una letra aleatoria de A-Z (mayúsculas).
        cuadricula[fila] = "".join(
            random.choice(string.ascii_uppercase) if char == "." else char
            for char in cuadricula[fila]
        )
```
**Una vez hecho todo el proceso detras del funcionamiento de la sopa de letras, queda mostrale al usuario el resultado final:**

```python
def imprimir_cuadricula(cuadricula):
    # Imprime la cuadrícula de forma legible.
    for fila in cuadricula:
        print(" ".join(fila))

```

**Ahora para definir cual va a ser el tamaño de la cuadricula se le pregunta al usuario:**

```python
def sopa_de_letras():
    print("¡Bienvenido a la Sopa de Letras!")  # Se imprime este mensaje que saluda al usuario.
    tamaño = int(input("Ingrese el tamaño de la sopa (entre 10 y 30): "))
    while tamaño < 10 or tamaño > 30:  # Se limita el tamaño de cuadricula entre 10 y 30.
        tamaño = int(input("Por favor, ingrese un tamaño válido (entre 10 y 30): "))  # De ser ingresado un número mayor a 30 o menor a 10, salta el siguiente mensaje.

    palabras = ["PYTHON", "CODIGO", "GRUPO", "SOPA", "LETRAS", "STRING", "MATRIZ"]       # Se crea una lista con las palbras que el usuario tendra que encontrar. Se pone en mayusculas ya que "string" importa las letras en mayusculas.
    print("Palabras en la sopa:", ", ".join(palabras))        # Imprime la sopa de letras con las palabras y llenado aleatoriamente.                    

    cuadricula = crear_cuadricula(tamaño)
    colocar_palabras(cuadricula, palabras)
    rellenar_espacios(cuadricula)                            # Se llaman a las funciones y sus argumentos para que el programa funcione correctamente.
    imprimir_cuadricula(cuadricula)

sopa_de_letras()
```
**Por ultimo el codgio completo y con ejecucuón de ejemplo:**
```python
import random
import string

def crear_cuadricula(tamaño):  # Crea una cuadrícula vacía representada como una lista de strings.
    return ["." * tamaño for _ in range(tamaño)]   # Toma los espacios vacios y los multplica por el número que define el usuario del tamaño de la cuadricula.

def colocar_palabras(cuadricula, palabras):
    # Coloca palabras horizontalmente o verticalmente en la cuadrícula.
    
    # Definimos el tamaño de la cuadrícula según la longitud de la lista de palabras.
    tamaño = len(cuadricula)  # Esto asume que la cuadrícula es una lista de listas (2D), y su tamaño es cuadrado.
    
    for palabra in palabras:  # Iteramos sobre cada palabra que queremos colocar en la cuadrícula.
        colocada = False  # Inicializamos la variable, y desde un inicio la caracterizamos como falsa, mientras se cumplan ciertas condiciones al final cambiara a "True", para saber si la palabra ya se ha colocado correctamente.
        
        while not colocada:  # Mientras la palabra no se haya colocado, seguimos intentando (hacemos uso de bucles)
            
            # Elegimos una dirección aleatoria: "H" para horizontal, "V" para vertical. Aquí es donde se hace uso del import random
            direccion = random.choice(["H", "V"])  
            
            if direccion == "H":  # Si la dirección elegida es horizontal:
                # Seleccionamos una fila aleatoria dentro de la cuadrícula.
                fila = random.randint(0, tamaño - 1)
                # Seleccionamos una columna aleatoria en la fila, asegurándonos de que haya espacio suficiente para la palabra.
                columna = random.randint(0, tamaño - len(palabra))
                
                # Comprobamos si todos los lugares donde queremos colocar la palabra están vacíos (representados por ".").
                if all(cuadricula[fila][columna + i] == "." for i in range(len(palabra))):         # Si están vacíos, colocamos la palabra en la fila y columna seleccionadas.
                    for i, letra in enumerate(palabra):                                               # Actualizamos la cuadrícula reemplazando los puntos con las letras de la palabra.
                        cuadricula[fila] = cuadricula[fila][:columna + i] + letra + cuadricula[fila][columna + i + 1:]
                    colocada = True                                                                    # Marcamos la palabra como colocada.

            elif direccion == "V":  # Si la dirección elegida es vertical:
                # Seleccionamos una fila aleatoria donde cabe la palabra verticalmente.
                fila = random.randint(0, tamaño - len(palabra))
                # Seleccionamos una columna aleatoria en la cuadrícula.
                columna = random.randint(0, tamaño - 1)
                
                # Comprobamos si todos los lugares donde queremos colocar la palabra están vacíos.
                if all(cuadricula[fila + i][columna] == "." for i in range(len(palabra))):
                    # Si están vacíos, colocamos la palabra en la columna seleccionada.
                    for i, letra in enumerate(palabra):
                        # Actualizamos cada fila de la columna correspondiente.
                        cuadricula[fila + i] = cuadricula[fila + i][:columna] + letra + cuadricula[fila + i][columna + 1:]
                    colocada = True  # Marcamos la palabra como colocada.

def rellenar_espacios(cuadricula):
    # Rellena los espacios vacíos con letras aleatorias.
    
    # Recorre cada fila de la cuadrícula (lista de listas).
    for fila in range(len(cuadricula)):  # Iteramos a través de cada fila en la cuadrícula.
        
        # Reemplaza cada punto (.) con una letra aleatoria de A-Z (mayúsculas).
        cuadricula[fila] = "".join(
            random.choice(string.ascii_uppercase) if char == "." else char
            for char in cuadricula[fila]

def sopa_de_letras():
    print("¡Bienvenido a la Sopa de Letras!")  # Se imprime este mensaje que saluda al usuario.
    tamaño = int(input("Ingrese el tamaño de la sopa (entre 10 y 30): "))
    while tamaño < 10 or tamaño > 30:  # Se limita el tamaño de cuadricula entre 10 y 30.
        tamaño = int(input("Por favor, ingrese un tamaño válido (entre 10 y 30): "))  # De ser ingresado un número mayor a 30 o menor a 10, salta el siguiente mensaje.

    palabras = ["PYTHON", "CODIGO", "GRUPO", "SOPA", "LETRAS", "STRING", "MATRIZ"]       # Se crea una lista con las palbras que el usuario tendra que encontrar. Se pone en mayusculas ya que "string" importa las letras en mayusculas.
    print("Palabras en la sopa:", ", ".join(palabras))        # Imprime la sopa de letras con las palabras y llenado aleatoriamente.                    

    cuadricula = crear_cuadricula(tamaño)
    colocar_palabras(cuadricula, palabras)
    rellenar_espacios(cuadricula)                            # Se llaman a las funciones y sus argumentos para que el programa funcione correctamente.
    imprimir_cuadricula(cuadricula)

sopa_de_letras()


¡Bienvenido a la Sopa de Letras!
Ingrese el tamaño de la sopa (entre 10 y 30): 20
Palabras en la sopa: PYTHON, CODIGO, GRUPO, SOPA, LETRAS, STRING, MATRIZ

Y K E Y R C X M F H R J A D Q M Q M V S
M N A S O P A H M W K X X A A Z J L W S
K E C H I X J K R P P E T G R U P O D V
G Y N J F O O E W Q V U T C P D L G D S
W A L U R S T G M L N P F R M K Y Q D S
C E V E V C V P J E R K T L Y A F A I M
G Y O T N W P Q P T L A C J V H D Q U D
J V J K L X J X A R H C Z N J K W J Z D
S Y J K H P W T R A U Z Y N C A I N X D
T P I D E D K T M S D R X N I E B C J U
C Y R J M T Q S A H X H Y C R X I Q W A
O T P C C Z X Q T W I F L Z G G R S Y V
D H N G D P M O R S T R I N G U P U F J
I O Z N O L E A I B P B A Y N V U Y F R
G N B J V F S H Z E D V H I N Z N A E W
O J N A T I N H L A P W A L E H B G Z W
S E C Q I V A A Y S B I Y P L H G T C U
Q W C Y O Q U Q K H G D X V B L P V E K
F U T K P M O F H Y W K J B V E C R E A
T W A K J K P D R H O D Q M Y P S F N M
```
# **Proximos Pasos**

Como proximos pasos para mejorar el aplicativo, se encuentran:

1. Mejorar el codigo:
   
   **- Incluir matrices**

3. Agregar niveles de dificultad:

   **- Facil: Solo palabas horizontales o verticales.**
   
   **- Medio: Horizontales y verticales.**
   
   **- Dificil: Horizontales, verticales y digaonales.**
    
4. Tratar de incluir cuenta regresiva:

   **- Esto tambien afectaria la dificultad.**

5. Interfaz grafica:

   **- Para visualizar la estructura de mejor manera.**

   **- Poder marcar como sombreadas o coloreadas las palabras encontradas**


# **CONTINUARA**

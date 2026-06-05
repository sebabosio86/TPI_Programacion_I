'''
UNIVERSIDAD: UTN Facultad San Nicolás
CARRERA: Tecnicatura Universitaria en Programación a Distancia
CÁTEDRA: Programación I
AÑO: 2026

Trabajo Práctico Integrador 

ALUMNOS:

xxxxxxxx  xxxxx - Comisión xx
Sebastián Ezequiel Bosio - Comisión 17

DESCRIPCIÓN:
    x

'''

#####################################################################################################################
# Declaración de FUNCIONES PRINCIPALES
#####################################################################################################################

def programa_principal():

    while True:

        print("\n--- MENÚ PRINCIPAL ---\n")
        print("1. Agregar nuevo país")
        print("2. Actualizar datos de un país")
        print("3. Buscar país por nombre")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir del sistema")

        # Ingresar opcion y validar
        opcion_menu = ingresar_entero("\nOpción: ", 1, 7)
        
        # Invoca a la función correspondiente de acuerdo a la opción seleccionada por el usuario.
        if opcion_menu == 1:
            agregar_pais()

        elif opcion_menu == 2:
            actualizar_datos()

        elif opcion_menu == 3:
            buscar_pais()

        elif opcion_menu == 4:

            filtrar_paises()

        elif opcion_menu == 5:
            ordenar_paises()
            
        elif opcion_menu == 6:

            pass

        else:

            ## OPCIÓN TEMPORAL PARA MOSTRAR LOS VALORES DEL DATASET
            with open("dataset_paises.csv", "r", encoding="utf-8") as archivo:

                lector = csv.DictReader(archivo)

                # Recorre el csv fila por fila
                for fila in lector:

                    print(f"{fila['nombre']}, {fila['poblacion']}, {fila['superficie']}, {fila['continente']}")

            return
            # # Opción 7 - Salir del programa
            # print("\nSaliendo del sistema")
            # print("Hasta la próxima")
            # return


#####################################################
#####################################################

# Agregar nuevo país 
def agregar_pais():

    print("\n" + "="*50)
    print(" "*11 + "--- AGREGAR NUEVO PAÍS ---")
    print("="*50 + "\n")

    while True:

        # Se ingresa el nombre del país que se desea incorporar al dataset
        nombre = validar_nombre("Nombre del país: ").strip().capitalize()

        # Invoca a la función para verificar si el país pertenece al dataset
        if verificar_existencia(nombre):
            print(f"ERROR: {nombre} ya pertenece a la base de datos.")

            # Si el país ya existe se pregunta si quiere reintentar e ingresar uno nuevo
            if reintentar():
                continue  # Reinicia el bloque
            else:
                return  # Vuelve al menú principal

        # Si el país no existe en el dataset se pide el resto de los datos.
        else:
            poblacion = ingresar_entero("Población: ", 1)
            superficie = ingresar_entero("Superficie en km²: ", 1)
            continente = validar_nombre("Continente: ").strip().capitalize()

            # Abre el csv en modo "a" para agregar los valores ingresados
            with open("dataset_paises.csv", "a", encoding="utf-8") as archivo:

                escritor = csv.writer(archivo)

                # Agrega una nueva línea en el dataset con los nuevos valores
                escritor.writerow([nombre, poblacion, superficie, continente])

            print("\n¡Datos guardados exitosamente!")
            input("\nPresione ENTER para volver al menú principal")

        return


#####################################################
#####################################################

# Actualizar datos de un país (población o superficie)
def actualizar_datos():

    # Comprueba si hay países cargados en el csv. Si la lista está vacía se vuelve al menú principal
    if lista_vacia():
        print("\nAún no hay datos cargados.")
        input("\nPresione ENTER para continuar")
        return

    print("\n" + "="*50)
    print(" "*7 + "--- ACTUALIZAR DATOS DE UN PAIS ---")
    print("="*50 + "\n")

    # Lista vacía que almacenará cada fila del archivo csv a medida que vaya leyendo
    dataset_temporal = []

    # Cabeceras de las columnas
    cabecera = ['nombre','poblacion','superficie','continente']

    while True:

        # Se ingresa el nombre del país que se desea incorporar al dataset
        nombre = validar_nombre("Nombre del país: ").strip().capitalize()

        # Invoca a la función para verificar si el país pertenece al dataset
        if not verificar_existencia(nombre):
            print(f"No se encontró {nombre} en la base de datos.")
        
            # Si el país no existe se pregunta si quiere reintentar e ingresar uno nuevo
            if reintentar():
                continue  # Reinicia el bloque
            else:
                return  # Vuelve al menú principal
            
        # Si el país ingresado existe, se muestra un sub menú
        else:
            
            print("\nSeleccione el dato que desea modificar:")
            print("\n1. Población")
            print("2. Superficie")
            print("3. Volver al menú principal")

            opcion_sub_menu = ingresar_entero("\nOpción: ", 1, 3)

            # Vuelve al menú principal
            if opcion_sub_menu == 3:
                return
            
            # Para la selección de la opción 1 o 2 se ingresa el valor que se quiere modificar
            else:
                
                if opcion_sub_menu == 1:
                    poblacion = ingresar_entero("\nNuevo valor para la población: ", 1)

                else:
                    superficie = ingresar_entero("\nNuevo valor para la superficie: ", 1)

                # Abre el csv en modo "r" para leerlo
                with open("dataset_paises.csv", "r", encoding="utf-8") as archivo:

                    # Convierte cada fila del csv en un diccionario
                    lector = csv.DictReader(archivo)

                    # Se recorre el csv fila por fila
                    for fila in lector:

                        # Encuentra el país buscado
                        if fila['nombre'] == nombre:

                            # Si se había seleccionado la opción 1, cambia el valor de población
                            if opcion_sub_menu == 1:
                                fila['poblacion'] = poblacion

                            # Si se había seleccionado la opción 2, cambia el valor de supericie
                            else:
                                fila['superficie'] = superficie
                                
                        # Cada fila recorrida (se haya modificado o no) se va guardando en esta lista temporal
                        dataset_temporal = dataset_temporal + [fila]

                # Reescribimos todo el archivo csv
                with open("dataset_paises.csv", "w", encoding="utf-8") as archivo:

                    escritor = csv.DictWriter(archivo, fieldnames= cabecera)

                    # Se agrega la cabecera del csv con los nombres definidos en fieldnames
                    escritor.writeheader()

                    # Escribe los datos del dataset temporal en el nuevo csv
                    escritor.writerows(dataset_temporal)
                
                # Muestra un mensaje de acuerdo al campo que se modificó
                if opcion_sub_menu == 1:
                    print("\nOperación exitosa. El valor de población se actualizó correctamente.")

                else:
                    print("\nOperación exitosa. El valor de superficie se actualizó correctamente.")
                
                input("\nPresione ENTER para volver al menú principal")

                return


#####################################################
#####################################################

# Buscar país por nombre (o parte del nombre) y mostrar sus datos (opción 3 del menú principal)
def buscar_pais():
    #Verificamos si hay paises cargados en el csv
    if lista_vacia():
        print("\nTodavia no hay datos cargados en el sistema. ")
        input("\nPresione ENTER para continuar")
        return
    
    print("\n" + "="*50)
    print(" "*10 + "--- BUSCAR PAÍS POR NOMBRE ---")
    print("="*50 + "\n")

    termino_buscado = validar_nombre("Ingrese el nombre (o parte del nombre) que desee buscar: ").lower()

    #Utilizamos un contador para saber si encontramos alguna coincidencia
    coincidencias_encontradas = 0

    print("\n" + "-"*70)
    print(f"{'Nombre':<20} | {'Población':<12} | {'Superficie (km²)':<16} | {'Continente'}")
    print("-"*70)

    #Abrimos el archivo para hacer la busqueda
    with open("dataset_paises.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            #Pasamos el nombre del pais del dataset a minuscualas para comparar de forma justa 
            nombre_pais_en_tabla = fila["nombre"].lower()

            if termino_buscado in nombre_pais_en_tabla:
                # Mostramos los datos en la consola
                print(f"{fila['nombre']:<20} | {fila['poblacion']:<12} | {fila['superficie']:<16} | {fila['continente']}")
                coincidencias_encontradas += 1


    print("-"*70)

    # Si el contador quedó en 0, significa que no hubo resultados (Exigencia de la consigna)
    if coincidencias_encontradas == 0:
        print(f"No se encontraron países que coincidan con '{termino_buscado.capitalize()}'.")
    else:
        print(f"Se encontraron {coincidencias_encontradas} coincidencia(s).")

    input("\nPresione ENTER para volver al menú principal")     

    return 


#####################################################
#####################################################

# Filtrar paises por continente, rango de población o rango de superficie (opción 4 del menú principal)

def filtrar_paises():
    #Comprobamos si hay datos usando la funcion lista_vacia()
    if lista_vacia():
        print("\nAun no hay datos cargados en el sistema.")
        input("\nPresione ENTER para continuar")
        return
    print("\n" + "="*50)
    print(" "*14 + "--- FILTRAR PAISES---")
    print("="*50 + "\n")

    print("Criterios para filtrar: ")
    print("1. Por Coninente ")
    print("2. Por Rango de poblacion ")
    print("3. Por rango de superficie ")
    print("4. Volver al menu principal")

    #Utilizamos la funcion ingresar_entero()
    opcion_filtro = ingresar_entero("\nSeleccione una opcion: ", 1, 4)

    if opcion_filtro == 4:
        #Volvemos al menu principal
        return
    
    #Inicializamos las variables que vamos a usar
    valor_texto = ""
    rango_min = 0
    rango_max = 0

    #Dependiendo la opcion que elija el usuario solicitaremos los datos que correspondan
    if opcion_filtro == 1:
        valor_texto = validar_nombre("Ingrese el nombre del continente: ")
    elif opcion_filtro == 2:
        rango_min = ingresar_entero("Ingrese el limite inferior de poblacion: ", 0)
        rango_max = ingresar_entero("Ingrese el limite superior de poblaicon: ", rango_min)
    elif opcion_filtro == 3:
        rango_min = ingresar_entero("Ingrese el limite inferior de superficie: ", 0)
        rango_max = ingresar_entero ("Ingrese el limite superior de superficie: ", rango_min)

    #Utilizamos un contador para verificar si hubo resultados y evitar fallos
    cantidad_resultados = 0

    print("\n" + "-"*60)
    print(f"{'Nombre':<20} | {'Población':<12} | {'Superficie (km²)':<16} | {'Continente'}")
    print("-"*60)

    with open("dataset_paises.csv","r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
    
        for fila in lector:
            #Utilizamos la funcion cumple_filtros()
            if cumple_filtros(fila, opcion_filtro, valor_texto, rango_min, rango_max):
                print(f"{fila['nombre']:<20} | {fila['poblacion']:<12} | {fila['superficie']:<16} | {fila['continente']}")
                cantidad_resultados += 1
    
    print("-"*60)

    #Si no encuenta nada
    if cantidad_resultados == 0:
        print("No se encontraron paises que cumplan con el criterio especificado. ")
    else:
        print(f"Se encontraron {cantidad_resultados} pais(es) que coinciden con el filtro. ")

    input("\nPresione ENTER para volver al menú principal")


#####################################################
#####################################################

# Ordenar países por nombre, población o superficie en orden ascendente o descendente (opción 5 del menú principal)
def ordenar_paises():
    
    # Comprueba si hay países cargados en el csv. Si la lista está vacía se vuelve al menú principal
    if lista_vacia():
        print("\nAún no hay datos cargados.")
        input("\nPresione ENTER para continuar")
        return
    
    print("\n" + "="*50)
    print(" "*13 + "--- ORDENAR PAÍSES ---")
    print("="*50 + "\n")

    print("\nSeleccione el criterio de ordenamiento:")
    print("\n1. Nombre")
    print("2. Población")
    print("3. Superficie")

    criterio = ingresar_entero("\nOpción: ", 1, 3)

    print("\nSeleccione el orden:")
    print("\n1. Ascendente")
    print("2. Descendente")

    orden = ingresar_entero("\nOpción: ", 1, 2)

    # Determina si es ascendente o descendente
    if orden == 1:
        ascendente = True
        texto_orden = "ASCENDENTE"

    else:
        ascendente = False
        texto_orden = "DESCENDENTE"
    
    # Se asigna nombre del criterio para mostrar en pantalla
    if criterio == 1:
        nombre_criterio = "NOMBRE"
        clave_orden = 'nombre'

    elif criterio == 2:
        nombre_criterio = "POBLACIÓN"
        clave_orden = 'poblacion'

    else:
        nombre_criterio = "SUPERFICIE"
        clave_orden = 'superficie'


    # Lista vacía que almacenará cada fila del archivo csv a medida que vaya leyendo
    lista_paises = []
    
    with open("dataset_paises.csv", "r", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            # Convierte población y superficie a números enteros (para poder compararlos correctamente)
            fila['poblacion'] = int(fila['poblacion'])
            fila['superficie'] = int(fila['superficie'])
            # Agrega cada fila con los datos convertidos a la lista de países
            lista_paises.append(fila)
    
    # Ordenamiento con método burbuja
    n = len(lista_paises)

    # Recorre la lista tantas veces como elementos tiene, menos 1
    for i in range(n - 1):
        
        # En cada recorrido, compara el elemento actual con el siguiente y los intercambia si están en el orden incorrecto
        for j in range(n - 1 - i):
            
            # Compara los valores correspondientes de cada país y los ordena de forma ascendente o descendente según corresponda
            if ascendente:
                if lista_paises[j][clave_orden] > lista_paises[j + 1][clave_orden]:
                    # Guarda el país actual en una variable auxiliar
                    aux = lista_paises[j]
                    # Reemplaza el país actual por el siguiente
                    lista_paises[j] = lista_paises[j + 1]
                    # Reemplaza el siguiente por el país guardado en la variable auxiliar
                    lista_paises[j + 1] = aux

            else:
                if lista_paises[j][clave_orden] < lista_paises[j + 1][clave_orden]:            
                    aux = lista_paises[j]
                    lista_paises[j] = lista_paises[j + 1]
                    lista_paises[j + 1] = aux

    print(f"\nPaíses ordenados por {nombre_criterio} en orden {texto_orden}.")

    print("\n" + "-"*70)
    print(f"{'Nombre':<20} | {'Población':<12} | {'Superficie (km²)':<16} | {'Continente'}")
    print("-"*70)

    for pais in lista_paises:
        print(f"{pais['nombre']:<20} | {pais['poblacion']:<12} | {pais['superficie']:<16} | {pais['continente']}")
    print("-"*70)

    input("\nPresione ENTER para volver al menú principal")

    return


#####################################################################################################################
# Declaración de FUNCIONES SECUNDARIAS
#####################################################################################################################

# Comprueba que el nombre de país ingresado no sea un string vacío
def validar_nombre(mensaje):

    while True:

        # Se pide ingresar el nombre del país
        nombre_pais = input(mensaje).strip().capitalize()
        
        # En caso de ingresar str vacío se muestra mensaje de error.
        if nombre_pais == "":
            print("\nERROR: No se ingresó ningún nombre.")
        else:
            return nombre_pais


#####################################################
#####################################################

# Valida que el valor ingresado sea un número entero. Se permiten argumentos de valor mínimo y máximo
def ingresar_entero(mensaje, min=None, max=None):

    while True:

        try:

            # Si pide ingresar el número
            numero = int(input(mensaje))

            if min is not None and numero < min:
                print(f"ERROR: El número debe ser mayor o igual a {min}.")
                continue

            if max is not None and numero > max:
                print(f"ERROR: El número debe ser menor o igual a {max}.")
                continue
            
            return numero
        
        # Si se ingresa otro dato que no sea entero se muestra un error.
        except ValueError:
            print("\nERROR: Debe ingresar un número válido.")


#####################################################
#####################################################

# Verifica si el país existe en el csv
def verificar_existencia(nombre_pais):

    with open("dataset_paises.csv", "r", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo)

        # Recorre el csv fila por fila
        for fila in lector:

            # fila[0] corresponde a los nombres de países. Si coincide devuelve True
            if fila['nombre'] == nombre_pais:
                return True

    return False


#####################################################
#####################################################

# Función para reinicar un bloque o volver al menú
def reintentar():

    while True:
        reintento = input("\n¿Reintentar? (S/N)").strip().lower()

        if reintento == "s":
            return True  # Vuelve a reiniciar el bloque
        if reintento == "n":
            return False # Sale de la función y vuelve al menú principal 
        else:
            print("\nERROR: Debe seleccionar una opción válida.")


#####################################################
#####################################################

# Revisa si el dataset está vacío. Si no hay filas devuelve True, de lo contrario devuelve False
def lista_vacia():

    with open("dataset_paises.csv", "r", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo)
        
        for fila in lector:
            return False

    return True
#####################################################
#####################################################

def cumple_filtros(pais, tipo_filtro, valor_filtro, min_filtro=None, max_filtro=None):
    #Con esta funcion verificamos si un diccionario de pais cumple con el criterio de filtrado seleccionado
    if tipo_filtro == 1:
        return pais["continente"].lower() == valor_filtro.lower()
    
    elif tipo_filtro == 2:
        poblacion = int(pais["poblacion"])
        return min_filtro <= poblacion <= max_filtro
    elif tipo_filtro == 3:
        superficie = int(pais["superficie"])
        return min_filtro <= superficie <= max_filtro
    
    return False



#####################################################################################################################
# Ejecución del programa principal
#####################################################################################################################

# Se importa la biblioteca csv
import csv

programa_principal()

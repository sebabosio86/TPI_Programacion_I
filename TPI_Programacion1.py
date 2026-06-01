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
        print("7. Salir del sistema\n")

        # Ingresar opcion y validar
        opcion_menu = ingresar_entero("\nOpción: ", 1, 7)
        
        # Invoca a la función correspondiente de acuerdo a la opción seleccionada por el usuario.
        if opcion_menu == 1:
            agregar_pais()

        elif opcion_menu == 2:

            pass

        elif opcion_menu == 3:
            
            pass

        elif opcion_menu == 4:

            pass

        elif opcion_menu == 5:

            pass
            
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
    print("="*50)

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

            print("\nDatos guardados exitosamente")
            input("\nPresione ENTER para continuar")

        return



#####################################################
#####################################################

# Actualizar datos de un país
def actualizar_datos():

    return



#####################################################################################################################

# Declaración de FUNCIONES SECUNDARIAS

#####################################################################################################################

# Comprueba que el nombre de país ingresado no sea un string vacío
def validar_nombre(mensaje):

    while True:

        # Se pide ingresar el nombre del país
        nombre_pais = input(mensaje).strip().lower()
        
        # En caso de ingresar str vacío se muestra mensaje de error.
        if nombre_pais == "":
            print("\nERROR: No se ingresó ningún nombre.")
        else:
            return nombre_pais


#####################################################
#####################################################

# Valida que el valor ingresado sea un número entero
def ingresar_entero(mensaje, min=None, max=None):

    while True:

        try:

            # Si pide ingresar el número
            numero = int(input(mensaje))

            if numero is not None and numero < min:
                print(f"ERROR: El número debe ser mayor o igual a {min}.")
                continue

            if numero is not None and numero > max:
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

        lector = csv.reader(archivo)

        # Saltar la cabecera
        next(lector)

        # Recorre el csv fila por fila
        for fila in lector:

            # fila[0] corresponde a los nombres de países. Si coincide devuelve True
            if fila[0] == nombre_pais:
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














#####################################################################################################################

# Ejecución del programa principal

#####################################################################################################################

# Se importa la biblioteca csv
import csv

programa_principal()

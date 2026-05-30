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
        while True:

            try:
                opcion =int(input("Opción: "))  # Usuario ingresa la ocpión del menú

                # Si está dentro del rango válido pasa al siguiente bloque
                if 1 <= opcion <= 7:  
                    break
                
                # Si está fuera de rango se repite el bucle
                else:  
                    print(f"\nERROR. Ingrese una opción válida (1-7).")
            
            # Si el valor ingresado no es un número válido muetra un error.
            except ValueError:  
                print(f"\nERROR: Debe ingresar un numero entre 1 y 7.")
        
        # Invoca a la función correspondiente de acuerdo a la opción seleccionada por el usuario.
        if opcion == 1:

            agregar_pais()
            pass

        elif opcion == 2:

            pass

        elif opcion == 3:
            
            pass

        elif opcion == 4:

            pass

        elif opcion == 5:

            pass
            
        elif opcion == 6:

            pass

        else:

            # Opción 7 - Salir del programa
            print("\nSaliendo del sistema")
            print("Hasta la próxima")
            return


#####################################################
#####################################################

# Agregar nuevo país
def agregar_pais():

    print("\n" + "="*50)
    print(" "*11 + "--- AGREGAR NUEVO PAÍS ---")
    print("="*50)

    #nombre_pais = validar_nombre("Nombre: ").strip().lower()


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
def ingresar_entero(mensaje):

    while True:

        try:

            # Si pide ingresar el número
            numero = int(input(mensaje))

            # Valida que el número ingresado sea mayor a 0
            if numero <= 0:
                print("\nERROR: Debe ingresar un número entero mayor que cero.")
                continue
            
            return numero
        
        # Si se ingresa otro dato que no sea entero se muestra un error.
        except ValueError:
            print("\nERROR: Debe ingresar un número entero mayor que cero.")


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


#####################################################################################################################

# Ejecución del programa principal

#####################################################################################################################

# Se importa la biblioteca csv
import csv

programa_principal()

import csv


#####################################################################################################################
# Declaración de FUNCIONES AUXILIARES
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

            # Veerifica que el número ingresado esté entre los rangos establecidos por los argumentos min y max
            if min is not None and max is not None:
                if numero < min or numero > max:
                    print(f"ERROR: El número debe estar entre {min} y {max}.")
                    continue

            # Verifica que el número ingresado sea mayor o igual al valor mínimo establecido
            if min is not None and numero < min:
                print(f"ERROR: El número debe ser mayor o igual a {min}.")
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


from funciones_auxiliares import validar_nombre, ingresar_entero, lista_vacia, cumple_filtros
import csv

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


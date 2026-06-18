from funciones_auxiliares import ingresar_entero, lista_vacia
import csv

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

    # Recorre la lista y muestra los datos
    for pais in lista_paises:
        print(f"{pais['nombre']:<20} | {pais['poblacion']:<12} | {pais['superficie']:<16} | {pais['continente']}")
    print("-"*70)

    input("\nPresione ENTER para volver al menú principal")

    return

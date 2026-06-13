from funciones_auxiliares import validar_nombre, lista_vacia
import csv


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

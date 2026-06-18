from funciones_auxiliares import lista_vacia
import csv

# Mostrar estadísticas (opción 6 del menú principal)
def mostrar_estadisticas():

    # Comprueba si hay países cargados en el csv. Si la lista está vacía se vuelve al menú principal
    if lista_vacia():
        print("\nAún no hay datos cargados.")
        input("\nPresione ENTER para continuar")
        return
    
    print("\n" + "="*50)
    print(" "*10 + "--- MOSTRAR ESTADÍSTICAS ---")
    print("="*50 + "\n")

    # Se definen variables para las estadísticas

    pais_mas_poblado = None  # Se asigna el valor None para poder comparar con el primer país del dataset y asignar el valor correspondiente
    pais_menos_poblado = None
    promedio_poblacion = 0
    promedio_superficie = 0
    paises_por_continente = {}  # Diccionario para contar la cantidad de países por continente
    cantidad_paises = 0  # Contador para la cantidad total de países para calcular promedios

    with open("dataset_paises.csv", "r", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo)

        # Recorre el csv fila por fila para calcular las estadísticas.
        for fila in lector:

            # Convierte población y superficie a números enteros para poder compararlos correctamente
            fila['poblacion'] = int(fila['poblacion'])
            fila['superficie'] = int(fila['superficie'])

            # Verifica si el país actual es el más poblado o el menos poblado y actualiza las variables correspondientes
            if pais_mas_poblado is None or fila['poblacion'] > pais_mas_poblado['poblacion']:
                pais_mas_poblado = fila

            if pais_menos_poblado is None or fila['poblacion'] < pais_menos_poblado['poblacion']:
                pais_menos_poblado = fila

            # Suma la población y superficie para calcular los promedios
            promedio_poblacion += fila['poblacion']
            promedio_superficie += fila['superficie']

            # Cuenta la cantidad de países por continente
            continente = fila['continente']

            # Si el continente ya está en el diccionario, incrementa su contador. 
            if continente in paises_por_continente:
                paises_por_continente[continente] += 1

            # Si el continente no está en el diccionario, lo agrega con un contador inicial de 1.
            else:
                paises_por_continente[continente] = 1

            cantidad_paises += 1  # Incrementa el contador de países.

    # Calcula los promedios dividiendo la suma total por la cantidad de países
    promedio_poblacion = int(promedio_poblacion / cantidad_paises)
    promedio_superficie = int(promedio_superficie / cantidad_paises)

    # Muestra las estadísticas
    print(f"País más poblado: {pais_mas_poblado['nombre']}")
    print(f"País menos poblado: {pais_menos_poblado['nombre']}")
    print(f"Promedio de población: {promedio_poblacion} habitantes")
    print(f"Promedio de superficie: {promedio_superficie} km²")

    # Muestra la cantidad de países por continente recorriendo el diccionario
    for continente, cantidad in paises_por_continente.items():
        print(f"{continente}: {cantidad} países")

    input("\nPresione ENTER para volver al menú principal")

from funciones_auxiliares import validar_nombre, ingresar_entero, verificar_existencia, reintentar, lista_vacia
import csv

# Actualizar datos de un país (opción 2 del menú principal)
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

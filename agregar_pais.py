from funciones_auxiliares import validar_nombre, ingresar_entero, verificar_existencia, reintentar
import csv
# Agregar nuevo país al dataset (opción 1 del menú principal)
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


'''
UNIVERSIDAD: UTN Facultad San Nicolás
CARRERA: Tecnicatura Universitaria en Programación a Distancia
CÁTEDRA: Programación I
AÑO: 2026

Trabajo Práctico Integrador 

ALUMNOS:

Bruno Nicolas Matcovich - Comisión 3
Sebastián Ezequiel Bosio - Comisión 17

DESCRIPCIÓN:
El programa es un sistema de gestión de datos de países que permite al usuario agregar nuevos países con su población, superficie y 
continente en un archivo CSV, así como también actualizar datos existentes, buscar países por nombre, filtrar países según ciertos criterios,
ordenar países por diferentes atributos y mostrar estadísticas de los países almacenados en el archivo CSV.
El programa utiliza funciones para organizar el código y facilitar la interacción con el usuario a través de un menú principal.
Además, se implementan validaciones para asegurar que los datos ingresados sean correctos. 

'''

#####################################################################################################################
#####################################################################################################################
#Se importan los diferentes modulos con las funciones correspondientes

from agregar_pais import agregar_pais

from funciones_auxiliares import ingresar_entero

from actualizar_datos import actualizar_datos

from buscar_pais import buscar_pais

from filtrar_paises import filtrar_paises

from ordenar_paises import ordenar_paises

from mostrar_estadisticas import mostrar_estadisticas
#####################################################################################################################
#####################################################################################################################


# Función principal que muestra el menú y permite al usuario seleccionar las diferentes opciones.
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
            mostrar_estadisticas()

        else:

            # Opción 7 - Salir del programa
            print("\nSaliendo del sistema")
            print("Hasta la próxima")
            return


#####################################################################################################################
# Ejecución del programa principal
#####################################################################################################################

# Llamado a la función principal para iniciar el programa
programa_principal()

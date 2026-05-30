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
        
        # Accede a la función correspondiente de acuerdo a la opción seleccionada por el usuario.
        if opcion == 1:

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

            # Opción salir del programa
            print("\nSaliendo del sistema")
            print("Hasta la próxima")
            return
        
#####################################################

# Agregar nuevo país

def agregar_pais():
    print("\n" + "="*50)
    print(" "*11 + "--- AGREGAR NUEVO PAÍS ---")
    print("="*50)


    return





#####################################################################################################################

# Ejecución del programa principal

#####################################################################################################################

# Se importa la biblioteca csv
import csv


# Trabajo Práctico Integrador

### Universidad Tecnológica Nacional 

### Facultad Regional San Nicolás

### Tecnicatura Universitaria en Programación a Distancia

### Programación I 

### Autores

* Bruno Nicolás Matcovich
* Sebastián Ezequiel Bosio

# Sistema de Gestión de Países

### Descripción

El programa es un sistema de gestión de datos de países que permite al usuario agregar nuevos países con su población, superficie y continente en un archivo CSV, así como también actualizar datos existentes, buscar países por nombre, filtrar países según ciertos criterios, ordenar países por diferentes atributos y mostrar estadísticas de los países almacenados en el archivo CSV.
El programa utiliza funciones para organizar el código y facilitar la interacción con el usuario a través de un menú principal. Además, se implementan validaciones para asegurar que los datos ingresados sean correctos.

## Archivos del proyecto

```text
├── Diagrama_de_flujo_TPI1.pdf
├── TPI_Programacion1.py
├── dataset_paises.csv
└── README.md
```

---

## Instrucciones de uso

- Ejecutar el programa

- Aparecerá el menú principal:

```text
--- MENÚ PRINCIPAL ---

1. Agregar nuevo país
2. Actualizar datos de un país
3. Buscar país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Salir del sistema
```

- Seleccionar la opción deseada ingresando el número correspondiente.

---

## Funcionalidades

### 1. Agregar nuevo país

Permite incorporar un nuevo país al archivo CSV.

**Datos solicitados:**

* Nombre del país
* Población
* Superficie
* Continente

**Ejemplo**

**Entrada**

```text
Nombre del país: Argentina
Población: 47000000
Superficie en km²: 2780400
Continente: América
```

**Salida**

```text
¡Datos guardados exitosamente!
```

---

### 2. Actualizar datos de un país

Permite modificar la población o la superficie de un país ya existente.

**Ejemplo**

**Entrada**

```text
Nombre del país: Argentina

1. Población
2. Superficie
3. Volver al menú principal

Opción: 1

Nuevo valor para la población: 48000000
```

**Salida**

```text
Operación exitosa. El valor de población se actualizó correctamente.
```

---

### 3. Buscar país por nombre

Permite buscar un país utilizando el nombre completo o una parte del mismo.

**Ejemplo**

**Entrada**

```text
Ingrese el nombre (o parte del nombre) que desee buscar: arg
```

**Salida**

```text
Nombre               | Población    | Superficie (km²) | Continente
--------------------------------------------------------------------
Argentina            | 48000000     | 2780400          | América

Se encontraron 1 coincidencia(s).
```

---

### 4. Filtrar países

Permite mostrar países según determinados criterios:

* Continente
* Rango de población
* Rango de superficie

**Ejemplo**

**Entrada**

```text
Seleccione una opción: 1
Ingrese el nombre del continente: América
```

**Salida**

```text
Nombre               | Población    | Superficie (km²) | Continente
--------------------------------------------------------------------
Argentina            | 48000000     | 2780400          | América
Brasil               | 211000000    | 8515767          | América
```

---

### 5. Ordenar países

Permite ordenar los registros por:

* Nombre
* Población
* Superficie

Además, se puede elegir:

* Orden ascendente
* Orden descendente

**Ejemplo**

**Entrada**

```text
Criterio: Población
Orden: Descendente
```

**Salida**

```text
Países ordenados por POBLACIÓN en orden DESCENDENTE.
```

Mostrando posteriormente la tabla ordenada.

---

### 6. Mostrar estadísticas

Calcula y muestra:

* País más poblado
* País menos poblado
* Promedio de población
* Promedio de superficie
* Cantidad de países por continente

**Ejemplo**

**Salida**

```text
País más poblado: China
País menos poblado: Uruguay
Promedio de población: 152000000 habitantes
Promedio de superficie: 3645000 km²

América: 5 países
Europa: 4 países
Asia: 3 países
```

---

## Validaciones implementadas

El programa incorpora controles para evitar errores durante la carga de información:

* No permite nombres vacíos.
* Verifica que los países no se encuentren duplicados.
* Comprueba que los valores numéricos sean enteros válidos.
* Controla rangos mínimos y máximos cuando corresponde.
* Detecta cuando el archivo de datos no contiene registros.

## Participación de los integrantes

Bruno Matkovich: 

* Escritura de las funciones buscar_pais, filtrar_paises y mostrar_estadisticas, correspondientes a las opciones 3, 4 y 6 del menú principal. 
* Desarrollo de funciones auxiliares:cumple_filtros, lista_vacía y reintentar.
* Desarrollo del informe final: introducción, marco teórico, pruebas del programa y capturas de pantalla.
  
Sebastián Bosio: 

* Desarrollo del menú principal del programa y las funciones agregar_pais, actualizar_datos y ordenar_paises (opciones 1, 2 y 5 del menú principal. 
* Diseño del diagrama de flujo.
* Desarrollo de funciones auxiliares: ingresar_entero, validar_existencia y validar_nombre.
* Desarrollo del informe final: dificultades y conclusiones.
* Redacción del archivo README.md

## Enlace al video demostrativo en Youtube

  https://www.youtube.com/watch?v=L2IoBFFEtIU&t=11s

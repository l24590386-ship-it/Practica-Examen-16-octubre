#INSTITUTO TECNOLOGICO DE SAN JUAN DEL RIO 
#ESTRUCTURA DE DATOS 
#UNIDAD 2
#NOMBRE : ROCIO MOLINA MONROY 
#Practica Examen 16 octubre
#--------------------------------------------

# DIFERENCIAS Y MODIFICACIONES RESPECTO AL CÓDIGO ORIGINAL
# - En lugar de trabajar con "Mascota", ahora usamos "Alumno" con nombre y calificación.
# - Se cargan automáticamente 10 alumnos desde un arreglo al iniciar la lista.
# - Se mantiene el menú interactivo para agregar, buscar, eliminar y mostrar alumnos.
# - Se agregaron funciones para buscar y eliminar por nombre y por calificación.
# - Se mejoró imprimir_lista() para validar lista vacía.
# ----------------------------------------------------------------------

# Clase Nodo
# ------------------------------------------------------------
class Nodo():
    dato = None
    siguiente = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Clase Alumno
# ------------------------------------------------------------
class Alumno():
    def __init__(self, nombre, calificacion) -> None:
        self.nombre = nombre
        self.calificacion = calificacion
    
    def __str__(self):
        return f"Alumno: {self.nombre}, Calificación: {self.calificacion}"
    
    def __eq__(self, __o: object) -> bool:
        return self.nombre.strip().lower() == __o.nombre.strip().lower() and self.calificacion == __o.calificacion

# Funciones para la lista ligada
# ------------------------------------------------------------
def agregar_al_final(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    if nodo_inicial == None:
        return nuevo_nodo
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    temporal.siguiente = nuevo_nodo
    return nodo_inicial

def agregar_al_inicio(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = nodo_inicial
    return nuevo_nodo

def imprimir_lista(nodo):
    if nodo == None:
        print("La lista está vacía.")
        return
    while nodo != None:
        print(f"Tenemos {nodo.dato}")
        nodo = nodo.siguiente

def obtener_cabeza(nodo_inicial):
    return nodo_inicial

def obtener_cola(nodo_inicial):
    if nodo_inicial == None:
        return None
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    return temporal

# Funciones de búsqueda y eliminación mejoradas
# ------------------------------------------------------------
def buscar_por_nombre(nodo, nombre):
    nombre = nombre.strip().lower()
    while nodo:
        if nodo.dato.nombre.strip().lower() == nombre:
            return nodo.dato
        nodo = nodo.siguiente
    return None

def buscar_por_calificacion(nodo, calificacion):
    while nodo:
        if nodo.dato.calificacion == calificacion:
            return nodo.dato
        nodo = nodo.siguiente
    return None

def eliminar_por_nombre(nodo, nombre):
    nombre = nombre.strip().lower()
    if nodo is None:
        return None
    # Eliminar de la cabeza si coincide
    while nodo and nodo.dato.nombre.strip().lower() == nombre:
        nodo = nodo.siguiente
    actual = nodo
    anterior = None
    while actual:
        if actual.dato.nombre.strip().lower() == nombre:
            if anterior:
                anterior.siguiente = actual.siguiente
            actual = actual.siguiente
        else:
            anterior = actual
            actual = actual.siguiente
    return nodo

def eliminar_por_calificacion(nodo, calificacion):
    if nodo is None:
        return None
    # Eliminar de la cabeza si coincide
    while nodo and nodo.dato.calificacion == calificacion:
        nodo = nodo.siguiente
    actual = nodo
    anterior = None
    while actual:
        if actual.dato.calificacion == calificacion:
            if anterior:
                anterior.siguiente = actual.siguiente
            actual = actual.siguiente
        else:
            anterior = actual
            actual = actual.siguiente
    return nodo

# Menú principal con 10 alumnos precargados
# ------------------------------------------------------------
def main():
    lista = None

    # 10 alumnos precargados individualmente
    lista = agregar_al_final(lista, Alumno("Rocío", 9.5))
    lista = agregar_al_final(lista, Alumno("Carlos", 8.7))
    lista = agregar_al_final(lista, Alumno("María", 10.0))
    lista = agregar_al_final(lista, Alumno("Luis", 7.8))
    lista = agregar_al_final(lista, Alumno("Fernanda", 9.0))
    lista = agregar_al_final(lista, Alumno("Jorge", 6.5))
    lista = agregar_al_final(lista, Alumno("Sofía", 8.2))
    lista = agregar_al_final(lista, Alumno("Andrés", 7.0))
    lista = agregar_al_final(lista, Alumno("Valeria", 9.3))
    lista = agregar_al_final(lista, Alumno("Miguel", 8.9))

    while True:
        print("\n===== MENÚ DE LISTA LIGADA DE ALUMNOS =====")
        print("1. Agregar alumno al inicio")
        print("2. Agregar alumno al final")
        print("3. Buscar alumno por nombre")
        print("4. Buscar alumno por calificación")
        print("5. Eliminar alumno por nombre")
        print("6. Eliminar alumno por calificación")
        print("7. Mostrar lista completa")
        print("8. Mostrar primer y último alumno")
        print("9. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del alumno: ")
            calificacion = float(input("Calificación: "))
            lista = agregar_al_inicio(lista, Alumno(nombre, calificacion))
            print(f"Alumno {nombre} agregado al inicio.")

        elif opcion == "2":
            nombre = input("Nombre del alumno: ")
            calificacion = float(input("Calificación: "))
            lista = agregar_al_final(lista, Alumno(nombre, calificacion))
            print(f"Alumno {nombre} agregado al final.")

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            resultado = buscar_por_nombre(lista, nombre)
            if resultado:
                print(f"Alumno encontrado: {resultado}")
            else:
                print("No se encontró el alumno.")

        elif opcion == "4":
            calificacion = float(input("Calificación a buscar: "))
            resultado = buscar_por_calificacion(lista, calificacion)
            if resultado:
                print(f"Alumno encontrado: {resultado}")
            else:
                print("No se encontró ningún alumno con esa calificación.")

        elif opcion == "5":
            nombre = input("Nombre del alumno a eliminar: ")
            lista = eliminar_por_nombre(lista, nombre)
            print(f"Alumno {nombre} eliminado si existía.")

        elif opcion == "6":
            calificacion = float(input("Calificación del alumno a eliminar: "))
            lista = eliminar_por_calificacion(lista, calificacion)
            print(f"Alumno con calificación {calificacion} eliminado si existía.")

        elif opcion == "7":
            imprimir_lista(lista)

        elif opcion == "8":
            cabeza = obtener_cabeza(lista)
            cola = obtener_cola(lista)
            print("Primer alumno:", cabeza.dato if cabeza else "No hay alumnos.")
            print("Último alumno:", cola.dato if cola else "No hay alumnos.")

        elif opcion == "9":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")
main()
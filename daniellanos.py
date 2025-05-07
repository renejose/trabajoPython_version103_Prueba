# -*- coding: utf-8 -*-
"""
Script de gestión de tareas con funciones y estructuras de datos.
"""

# Estructura de datos para almacenar las tareas (lista de diccionarios)
tareas = []

# Función para agregar una tarea
def agregar_tarea(nombre, prioridad="media"):
    """
    Agrega una nueva tarea a la lista.
    
    Args:
        nombre (str): Nombre de la tarea.
        prioridad (str): Prioridad de la tarea (alta, media, baja). Por defecto es "media".
    """
    tarea = {
        "nombre": nombre,
        "prioridad": prioridad,
        "completada": False
    }
    tareas.append(tarea)
    print(f"Tarea '{nombre}' agregada con prioridad {prioridad}.")

# Función para eliminar una tarea
def eliminar_tarea(nombre):
    """
    Elimina una tarea de la lista por su nombre.
    
    Args:
        nombre (str): Nombre de la tarea a eliminar.
    """
    global tareas
    tareas = [tarea for tarea in tareas if tarea["nombre"] != nombre]
    print(f"Tarea '{nombre}' eliminada.")

# Función para marcar una tarea como completada
def completar_tarea(nombre):
    """
    Marca una tarea como completada.
    
    Args:
        nombre (str): Nombre de la tarea a marcar.
    """
    for tarea in tareas:
        if tarea["nombre"] == nombre:
            tarea["completada"] = True
            print(f"Tarea '{nombre}' marcada como completada.")
            return
    print(f"No se encontró la tarea '{nombre}'.")

# Función para mostrar todas las tareas
def mostrar_tareas():
    """Muestra todas las tareas en la lista."""
    if not tareas:
        print("No hay tareas registradas.")
        return
    
    print("\n--- Lista de Tareas ---")
    for i, tarea in enumerate(tareas, 1):
        estado = "✓" if tarea["completada"] else "✗"
        print(f"{i}. [{estado}] {tarea['nombre']} (Prioridad: {tarea['prioridad']})")
    print("-----------------------\n")

# Función principal
def main():
    """Función principal que maneja el menú interactivo."""
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Marcar tarea como completada")
        print("4. Mostrar tareas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            prioridad = input("Prioridad (alta/media/baja): ").lower()
            if prioridad not in ["alta", "media", "baja"]:
                prioridad = "media"
            agregar_tarea(nombre, prioridad)
        
        elif opcion == "2":
            nombre = input("Nombre de la tarea a eliminar: ")
            eliminar_tarea(nombre)
        
        elif opcion == "3":
            nombre = input("Nombre de la tarea completada: ")
            completar_tarea(nombre)
        
        elif opcion == "4":
            mostrar_tareas()
        
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
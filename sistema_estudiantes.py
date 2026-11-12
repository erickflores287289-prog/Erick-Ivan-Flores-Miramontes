estudiantes = []


def mostrar_menu():
    print("\n=== Sistema de registro y análisis de estudiantes ===")
    print("1. Registrar un estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Consultar el promedio de un estudiante")
    print("4. Mostrar estadísticas generales del grupo")
    print("5. Salir del programa")
    print("6. Eliminar un estudiante")


def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)


def registrar_estudiante():
    identificacion = input("Número de identificación: ").strip()
    while not identificacion:
        print("La identificación no puede quedar vacía.")
        identificacion = input("Número de identificación: ").strip()

    while any(estudiante["identificacion"] == identificacion for estudiante in estudiantes):
        print("Ya existe un estudiante con esa identificación.")
        identificacion = input("Ingresa una identificación diferente: ").strip()
        while not identificacion:
            print("La identificación no puede quedar vacía.")
            identificacion = input("Número de identificación: ").strip()

    nombre = input("Nombre: ").strip()
    while not nombre:
        print("El nombre no puede quedar vacío.")
        nombre = input("Nombre: ").strip()

    calificaciones = []
    for numero in range(1, 4):
        while True:
            try:
                calificacion = float(input(f"Calificación {numero} (0-100): "))
                if 0 <= calificacion <= 100:
                    calificaciones.append(calificacion)
                    break
                print("La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Ingresa un número válido.")

    calificaciones = tuple(calificaciones)
    promedio = calcular_promedio(calificaciones)
    aprobado = promedio >= 70
    estudiante = {
        "identificacion": identificacion,
        "nombre": nombre,
        "calificaciones": calificaciones,
        "promedio": promedio,
        "aprobado": aprobado,
        "situacion": "Aprobado" if aprobado else "Reprobado",
    }
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} registrado correctamente.")


def mostrar_estudiantes():
    if not estudiantes:
        print("Todavía no hay estudiantes registrados.")
        return

    print("\n=== Estudiantes registrados ===")
    for estudiante in estudiantes:
        calificaciones = ", ".join(f"{nota:g}" for nota in estudiante["calificaciones"])
        print(f"Identificación: {estudiante['identificacion']}")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Calificaciones: {calificaciones}")
        print(f"Promedio: {estudiante['promedio']:.2f}")
        print(f"Situación: {estudiante['situacion']}")
        print("-" * 40)


def consultar_estudiante():
    identificacion = input("Identificación del estudiante: ").strip()
    for estudiante in estudiantes:
        if estudiante["identificacion"] == identificacion:
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Promedio: {estudiante['promedio']:.2f}")
            print(f"Situación: {estudiante['situacion']}")
            return
    print("No se encontró un estudiante con esa identificación.")


def mostrar_estadisticas():
    if not estudiantes:
        print("Todavía no hay estudiantes registrados.")
        return

    suma_promedios = 0
    aprobados = 0
    reprobados = 0
    promedio_mas_alto = estudiantes[0]["promedio"]

    for estudiante in estudiantes:
        suma_promedios += estudiante["promedio"]
        if estudiante["aprobado"]:
            aprobados += 1
        else:
            reprobados += 1
        if estudiante["promedio"] > promedio_mas_alto:
            promedio_mas_alto = estudiante["promedio"]

    promedio_general = suma_promedios / len(estudiantes)
    print("\n=== Estadísticas generales ===")
    print(f"Estudiantes registrados: {len(estudiantes)}")
    print(f"Promedio general: {promedio_general:.2f}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")
    print(f"Promedio más alto: {promedio_mas_alto:.2f}")


def eliminar_estudiante():
    identificacion = input("Identificación del estudiante que deseas eliminar: ").strip()
    for indice, estudiante in enumerate(estudiantes):
        if estudiante["identificacion"] == identificacion:
            estudiantes.pop(indice)
            print(f"Se eliminó el registro de {estudiante['nombre']}.")
            return
    print("No se encontró un estudiante con esa identificación.")


def main():
    opcion = 0
    while opcion != 5:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción: ").strip())
        except ValueError:
            print("Opción no válida. Ingresa un número del 1 al 6.")
            continue

        if opcion == 1:
            registrar_estudiante()
        elif opcion == 2:
            mostrar_estudiantes()
        elif opcion == 3:
            consultar_estudiante()
        elif opcion == 4:
            mostrar_estadisticas()
        elif opcion == 5:
            print("Programa finalizado.")
        elif opcion == 6:
            eliminar_estudiante()
        else:
            print("Opción no válida. Selecciona una opción del 1 al 6.")


if __name__ == "__main__":
    main()

notas = []
for i in range(3):
    fila = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota del estudiante {i+1} en la asignatura {j+1}: "))
        fila.append(nota)
    notas.append(fila)

print("\nPromedio por estudiannte:")
for i, fila in enumerate(notas):
    promedio = sum(fila) / len(fila)
    print(f"Estudiante {i+1}: {promedio:.2f}")
    if promedio < 3.5:
        print(f" El promedio del estudiante {i+1} es menor a 3.5.")

print("\nPromedio por asignatura:")
for j in range(3):
    suma_col = sum(notas[i][j] for i in range(3))
    promedio_col = suma_col / 3
    print(f"Asignatura {j+1}: {promedio_col:.2f}")

todos_aprobaron = all(all(nota >= 4.0 for nota in fila) for fila in notas)
if todos_aprobaron:
    print("\nTodos los estudinates aprobaron.")
else:
    print("\nNo todos los estudiantes aprobaron.")

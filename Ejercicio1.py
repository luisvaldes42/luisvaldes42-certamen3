temperaturas = input("Ingresa aquí 5 grados de temperatura distintos, separados por comas: ")
numeros = [float(n.strip()) for n in temperaturas.split(",")]

if all(15 <= n <= 30 for n in numeros):
    print("Todas las temperaturas estan dentro del rango de 15 a 30 grados.")
else:
    print("No todas las temperaturas estan dentro del rango de 15 a 30 grados.")

for n in numeros:
    if n < 15 or n > 30:
        print(f"La temperatura {n} esta fuera del rango de 15 a 30 grados.")

promedio = sum(numeros) / len(numeros)
print("Su promedio es: ", promedio)

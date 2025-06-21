edad = int(input("Ingrese su edad: "))
supervisor = input("¿Es supervisor? (si/no): ").strip().lower()
permiso = input("¿Tienes permiso? (si/no): ").strip().lower()

if edad >=18 and (supervisor == "si" or permiso == "si"):
    print("Puedes ingresar wiii :D")
else:
    print("No puedes ingresar amigo :(")
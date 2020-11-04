amigos={"Juan":18, "Pepe":19, "Maria":30}
nombre=str(input("Introduce el nombre de un amigo: "))
if nombre in amigos:
    print("La edad de {} es {}".format(nombre, amigos[nombre]))
else:
    print("No sé su edad")
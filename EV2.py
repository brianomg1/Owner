print("planificación para viajeros Falabella")
print("*"*20)
responde=[]
def calcular_total_viaje():
    # Solicitar información al usuario
    cantidad_destinos = int(input("Ingrese la cantidad de destinos: "))
    cantidad_viajeros = int(input("Ingrese la cantidad de viajeros: "))

    # Variables para almacenar el total a pagar
    total_pasajes = 0
    total_tours = 0
    # Calcular el total a pagar por pasajes y tours para cada destino
    for i in range(cantidad_destinos):
        responde.append(input(f"que quiere lugar es pais  {i+1}: "))
        valor_pasajes = float(input("Ingrese el valor de los pasajes entre destinos: "))
        cantidad_noches = int(input("Ingrese la cantidad de noches por destino: "))
        cantidad_tours = int(input("Ingrese la cantidad de tours por destino: "))
        valor_tours = float(input("Ingrese el valor de los tours por destino: "))

        total_pasajes += valor_pasajes * cantidad_viajeros
        total_tours += valor_tours * cantidad_tours * cantidad_viajeros * cantidad_noches

    # Calcular el total general del viaje sumando los pasajes y tours
    total_general = total_pasajes + total_tours

    # Imprimir el resultado
    print("\nResumen del viaje:")
    print(f"lugar pais:{responde}")
    print(f"Cantidad de destinos: {cantidad_destinos}")
    print(f"Cantidad de viajeros: {cantidad_viajeros}")
    print(f"Total a pagar por pasajes: ${total_pasajes}")
    print(f"Total a pagar por tours: ${total_tours}")
    print(f"Total general a pagar: ${total_general}")

# Ejecutar la función principal
calcular_total_viaje()

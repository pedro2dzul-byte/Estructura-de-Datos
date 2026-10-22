class Cola:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def __str__(self):
        return str(self.elementos)


class SistemaSeguros:
    def __init__(self):
        # Diccionario para almacenar una cola por cada número de servicio
        self.colas_servicios = {}
        # Diccionario para llevar el control del turno actual entregado por servicio
        self.contador_turnos = {}

    def registrar_cliente(self, num_servicio):
        if num_servicio not in self.colas_servicios:
            self.colas_servicios[num_servicio] = Cola()
            self.contador_turnos[num_servicio] = 0

        # Incrementar el número de atención correspondiente a la cola actual del servicio
        self.contador_turnos[num_servicio] += 1
        turno_asignado = self.contador_turnos[num_servicio]
        
        self.colas_servicios[num_servicio].encolar(turno_asignado)
        print(f"-> Cliente asignado al servicio {num_servicio}. Su número de atención es: {turno_asignado}")

    def atender_cliente(self, num_servicio):
        if num_servicio in self.colas_servicios and not self.colas_servicios[num_servicio].esta_vacia():
            cliente_atendido = self.colas_servicios[num_servicio].desencolar()
            print(f"<- Llamando a cliente del servicio {num_servicio}, con número de atención: {cliente_atendido}")
        else:
            print(f"¡No hay clientes en espera para el servicio {num_servicio}!")

def ejecutar_simulacion():
    sistema = SistemaSeguros()
    print("--- Sistema de Seguros Iniciado ---")
    print("Comandos: C<num> (Llegada de cliente, ej: C1), A<num> (Atender cliente, ej: A1), Salir (terminar)")

    while True:
        entrada = input("\nIngrese comando: ").strip()
        if entrada.lower() == 'salir':
            break
        
        if len(entrada) > 1:
            accion = entrada[0].upper()
            try:
                num_servicio = int(entrada[1:])
                if accion == 'C':
                    sistema.registrar_cliente(num_servicio)
                elif accion == 'A':
                    sistema.atender_cliente(num_servicio)
                else:
                    print("Comando no reconocido. Use 'C' para llegada o 'A' para atención.")
            except ValueError:
                print("Formato inválido. La letra debe ir seguida de un número entero (ej. C1, A2).")
        else:
            print("Entrada demasiado corta.")

# Descomenta la siguiente línea para ejecutar la simulación interactiva por consola:
# ejecutar_simulacion()
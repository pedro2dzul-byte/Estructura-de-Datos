
import tkinter as tk
from tkinter import messagebox


# Clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


# Clase Arbol
class Arbol:
    def __init__(self):
        self.raiz = None

    # Insertar un nodo
    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(self.raiz, dato)

    def _insertar(self, actual, dato):
        if dato < actual.dato:
            if actual.izquierdo is None:
                actual.izquierdo = Nodo(dato)
            else:
                self._insertar(actual.izquierdo, dato)

        elif dato > actual.dato:
            if actual.derecho is None:
                actual.derecho = Nodo(dato)
            else:
                self._insertar(actual.derecho, dato)

    # Buscar un nodo
    def buscar(self, dato):
        actual = self.raiz

        while actual is not None:
            if dato == actual.dato:
                return True
            elif dato < actual.dato:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return False

    # Encontrar el menor nodo
    def menor(self, nodo):
        actual = nodo

        while actual.izquierdo is not None:
            actual = actual.izquierdo

        return actual

    # Eliminar un nodo
    def eliminar(self, dato):
        self.raiz = self._eliminar(self.raiz, dato)

    def _eliminar(self, actual, dato):
        if actual is None:
            return None

        if dato < actual.dato:
            actual.izquierdo = self._eliminar(
                actual.izquierdo, dato
            )

        elif dato > actual.dato:
            actual.derecho = self._eliminar(
                actual.derecho, dato
            )

        else:
            # Caso 1: no tiene hijos
            if actual.izquierdo is None and actual.derecho is None:
                return None

            # Caso 2: tiene un solo hijo
            elif actual.izquierdo is None:
                return actual.derecho

            elif actual.derecho is None:
                return actual.izquierdo

            # Caso 3: tiene dos hijos
            sucesor = self.menor(actual.derecho)
            actual.dato = sucesor.dato
            actual.derecho = self._eliminar(
                actual.derecho, sucesor.dato
            )

        return actual

    # Recorrido Inorden
    def inorden(self, nodo, resultado):
        if nodo is not None:
            self.inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.dato)
            self.inorden(nodo.derecho, resultado)

    # Recorrido Preorden
    def preorden(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self.preorden(nodo.izquierdo, resultado)
            self.preorden(nodo.derecho, resultado)

    # Recorrido Postorden
    def postorden(self, nodo, resultado):
        if nodo is not None:
            self.postorden(nodo.izquierdo, resultado)
            self.postorden(nodo.derecho, resultado)
            resultado.append(nodo.dato)

    # Contar los nodos
    def contar(self, nodo):
        if nodo is None:
            return 0

        return (
            1
            + self.contar(nodo.izquierdo)
            + self.contar(nodo.derecho)
        )

    # Calcular la altura
    def altura(self, nodo):
        if nodo is None:
            return 0

        izquierda = self.altura(nodo.izquierdo)
        derecha = self.altura(nodo.derecho)

        return 1 + max(izquierda, derecha)


# Clase para la interfaz gráfica
class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Árbol Binario de Búsqueda")
        self.ventana.geometry("1000x700")
        self.ventana.configure(bg="#f0f0f0")

        self.arbol = Arbol()

        # Título
        titulo = tk.Label(
            ventana,
            text="ÁRBOL BINARIO DE BÚSQUEDA",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0"
        )
        titulo.pack(pady=15)

        # Entrada de datos
        panel = tk.Frame(ventana, bg="#f0f0f0")
        panel.pack(pady=10)

        tk.Label(
            panel,
            text="Valor:",
            font=("Arial", 12),
            bg="#f0f0f0"
        ).pack(side=tk.LEFT, padx=5)

        self.entrada = tk.Entry(
            panel,
            font=("Arial", 12),
            width=12
        )
        self.entrada.pack(side=tk.LEFT, padx=5)

        # Botones
        botones = tk.Frame(ventana, bg="#f0f0f0")
        botones.pack(pady=10)

        tk.Button(
            botones, text="Insertar",
            command=self.insertar,
            width=12
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            botones, text="Buscar",
            command=self.buscar,
            width=12
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            botones, text="Eliminar",
            command=self.eliminar,
            width=12
        ).grid(row=0, column=2, padx=5, pady=5)

        tk.Button(
            botones, text="Limpiar árbol",
            command=self.limpiar,
            width=12
        ).grid(row=0, column=3, padx=5, pady=5)

        # Área de dibujo con barras de desplazamiento
        marco = tk.Frame(ventana)
        marco.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        self.lienzo = tk.Canvas(
            marco,
            bg="white",
            height=350
        )

        barra_x = tk.Scrollbar(
            marco, orient=tk.HORIZONTAL,
            command=self.lienzo.xview
        )

        barra_y = tk.Scrollbar(
            marco, orient=tk.VERTICAL,
            command=self.lienzo.yview
        )

        self.lienzo.configure(
            xscrollcommand=barra_x.set,
            yscrollcommand=barra_y.set
        )

        barra_x.pack(side=tk.BOTTOM, fill=tk.X)
        barra_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.lienzo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Información de recorridos
        self.informacion = tk.Label(
            ventana,
            text="Recorridos: ",
            font=("Arial", 10),
            bg="#f0f0f0",
            justify=tk.LEFT,
            wraplength=950
        )
        self.informacion.pack(pady=8)

        self.estadisticas = tk.Label(
            ventana,
            text="Nodos: 0 | Altura: 0",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0"
        )
        self.estadisticas.pack(pady=8)

        self.actualizar()

    # Obtener el valor de la entrada
    def obtener_valor(self):
        try:
            return int(self.entrada.get())
        except ValueError:
            messagebox.showwarning(
                "Aviso",
                "Ingresa un número entero válido."
            )
            return None

    # Insertar
    def insertar(self):
        dato = self.obtener_valor()

        if dato is not None:
            if self.arbol.buscar(dato):
                messagebox.showinfo(
                    "Aviso",
                    "Ese valor ya existe en el árbol."
                )
            else:
                self.arbol.insertar(dato)
                self.entrada.delete(0, tk.END)
                self.actualizar()

    # Buscar
    def buscar(self):
        dato = self.obtener_valor()

        if dato is not None:
            if self.arbol.buscar(dato):
                messagebox.showinfo(
                    "Resultado",
                    f"El valor {dato} se encuentra en el árbol."
                )
            else:
                messagebox.showinfo(
                    "Resultado",
                    f"El valor {dato} no se encuentra."
                )

    # Eliminar
    def eliminar(self):
        dato = self.obtener_valor()

        if dato is not None:
            if self.arbol.buscar(dato):
                self.arbol.eliminar(dato)
                self.entrada.delete(0, tk.END)
                self.actualizar()
                messagebox.showinfo(
                    "Resultado",
                    f"Se eliminó el valor {dato}."
                )
            else:
                messagebox.showinfo(
                    "Resultado",
                    "El valor no existe en el árbol."
                )

    # Limpiar el árbol
    def limpiar(self):
        self.arbol.raiz = None
        self.actualizar()

    # Actualizar información y dibujo
    def actualizar(self):
        self.lienzo.delete("all")

        resultado_inorden = []
        resultado_preorden = []
        resultado_postorden = []

        self.arbol.inorden(
            self.arbol.raiz, resultado_inorden
        )
        self.arbol.preorden(
            self.arbol.raiz, resultado_preorden
        )
        self.arbol.postorden(
            self.arbol.raiz, resultado_postorden
        )

        self.informacion.config(
            text=(
                f"Inorden: {resultado_inorden}\n"
                f"Preorden: {resultado_preorden}\n"
                f"Postorden: {resultado_postorden}"
            )
        )

        cantidad = self.arbol.contar(self.arbol.raiz)
        altura = self.arbol.altura(self.arbol.raiz)

        self.estadisticas.config(
            text=f"Nodos: {cantidad} | Altura: {altura}"
        )

        if self.arbol.raiz is not None:
            # Obtener los nodos en orden
            nodos = []

            def obtener_nodos(nodo):
                if nodo is not None:
                    obtener_nodos(nodo.izquierdo)
                    nodos.append(nodo)
                    obtener_nodos(nodo.derecho)

            obtener_nodos(self.arbol.raiz)

            posiciones = {}
            separacion = 100
            ancho = max(800, len(nodos) * separacion + 100)

            # Asignar posición a cada nodo
            for i, nodo in enumerate(nodos):
                posiciones[id(nodo)] = (
                    50 + i * separacion,
                    60
                )

            # Dibujar las conexiones
            def dibujar_lineas(nodo, nivel=0):
                if nodo is None:
                    return

                x, _ = posiciones[id(nodo)]
                y = 60 + nivel * 90

                for hijo in [nodo.izquierdo, nodo.derecho]:
                    if hijo is not None:
                        x_hijo, _ = posiciones[id(hijo)]
                        y_hijo = 60 + (nivel + 1) * 90

                        self.lienzo.create_line(
                            x, y + 20,
                            x_hijo, y_hijo - 20,
                            fill="#555555",
                            width=2
                        )

                dibujar_lineas(nodo.izquierdo, nivel + 1)
                dibujar_lineas(nodo.derecho, nivel + 1)

            # Dibujar los nodos
            def dibujar_nodos(nodo, nivel=0):
                if nodo is None:
                    return

                x, _ = posiciones[id(nodo)]
                y = 60 + nivel * 90

                self.lienzo.create_oval(
                    x - 22, y - 22,
                    x + 22, y + 22,
                    fill="#3498db",
                    outline="#1b4f72",
                    width=2
                )

                self.lienzo.create_text(
                    x, y,
                    text=str(nodo.dato),
                    fill="white",
                    font=("Arial", 11, "bold")
                )

                dibujar_nodos(nodo.izquierdo, nivel + 1)
                dibujar_nodos(nodo.derecho, nivel + 1)

            dibujar_lineas(self.arbol.raiz)
            dibujar_nodos(self.arbol.raiz)

            self.lienzo.configure(
                scrollregion=(0, 0, ancho, (altura + 1) * 90)
            )


# Ejecutar el programa
ventana = tk.Tk()
aplicacion = Aplicacion(ventana)
ventana.mainloop()

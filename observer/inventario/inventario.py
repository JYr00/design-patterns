class Inventario:
    def __init__(self):
        self._producto = None
        self._observadores = []

    def adjuntar(self, observador):
        self._observadores.append(observador)

    def desadjuntar(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self._observadores:
            observador.actualizar(self._producto)

    def agregar_producto(self, producto):
        self._producto = producto
        self.notificar_observadores()
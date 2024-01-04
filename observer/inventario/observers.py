from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def actualizar(self, producto):
        pass

class DepartamentoVentas(Observador):
    def actualizar(self, producto):
        print(f"Departamento de Ventas: Recibido un nuevo producto {producto}.")

class DepartamentoLogistica(Observador):
    def actualizar(self, producto):
        print(f"Departamento de Logística: Recibido un nuevo producto {producto}.")
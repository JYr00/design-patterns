from inventario.inventario import Inventario
from inventario.observers import DepartamentoVentas, DepartamentoLogistica


inventario = Inventario()
ventas = DepartamentoVentas()
logistica = DepartamentoLogistica()

inventario.adjuntar(ventas)
inventario.adjuntar(logistica)

print("agregando productos...")
inventario.agregar_producto("Smartphone")
print("agregando productos...")
inventario.desadjuntar(logistica)
inventario.agregar_producto("Tablet")
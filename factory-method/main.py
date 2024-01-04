
import random
from notificadores.notificador_factory import NotificadorFactory


# tipo = ["email", "sms", "push"]
# random_number = random.randint(0, 2)
tipo = ["email", "sms"]
random_number = random.randint(0, 1)
mensaje = "¡Notificacion enviada correctamente!"

tipoSeleccionado = tipo[random_number]
print(tipoSeleccionado)

factory = NotificadorFactory()
notificador = factory.crear_notificador(tipoSeleccionado)

notificador.enviar_notificacion(mensaje)

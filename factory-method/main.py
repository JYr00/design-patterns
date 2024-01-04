
from notificadores.notificador_factory import NotificadorFactory

factory = NotificadorFactory()

tipo = ["email", "sms", "push"]
notificador = factory.crear_notificador(tipo[0])

mensaje = "¡Bienvenido al sistema de notificaciones!"
notificador.enviar_notificacion(mensaje)

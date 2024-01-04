from abc import ABC, abstractmethod # Abstract Base Class

class Notificador(ABC):
    @abstractmethod
    def enviar_notificacion(self, mensaje):
        pass

class EmailNotificador(Notificador):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando correo electrónico: {mensaje}")

class SMSNotificador(Notificador):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando SMS: {mensaje}")

class PushNotificador(Notificador):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación push: {mensaje}")
from .notificador import EmailNotificador, SMSNotificador, PushNotificador

class NotificadorFactory:
    def crear_notificador(self, tipo):
        if tipo == "email":
            return EmailNotificador()
        elif tipo == "sms":
            return SMSNotificador()
        elif tipo == "push":
            return PushNotificador()
        raise ValueError("Tipo de notificador no reconocido")

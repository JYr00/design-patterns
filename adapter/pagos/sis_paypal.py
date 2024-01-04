class SistemaPagoPayPal:
    def iniciar_sesion(self, usuario, contraseña):
        print(f"Sesión iniciada en PayPal para usuario {usuario}")
        return True

    def realizar_pago(self, monto):
        print(f"Realizando pago de ${monto} a través de PayPal.")
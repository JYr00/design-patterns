class AdaptadorPayPal:
    def __init__(self, sistema_paypal, usuario, contraseña):
        self.sistema_paypal = sistema_paypal
        self.usuario = usuario
        self.contraseña = contraseña
        self.sistema_paypal.iniciar_sesion(usuario, contraseña)

    def cobrar(self, monto):
        self.sistema_paypal.realizar_pago(monto)
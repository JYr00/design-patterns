from pagos.adapter_sis_paypal import AdaptadorPayPal
from pagos.sis_tarjeta_credito import ProcesadorTarjetaCredito
from pagos.sis_paypal import SistemaPagoPayPal


tipo_pago = input("Ingrese el tipo de pago (tarjeta/paypal): ")

if tipo_pago == "tarjeta":
    sistema_de_pago = ProcesadorTarjetaCredito()
elif tipo_pago == "paypal":
    sistema_de_pago = AdaptadorPayPal(SistemaPagoPayPal(), 'usuario_ejemplo', 'contraseña_ejemplo')
else:
    raise ValueError("Tipo de pago no reconocido")


sistema_de_pago.cobrar(100.0)
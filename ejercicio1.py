# Ejemplo de aplicación con notificación
from abc import ABC, abstractmethod

# Abstraccion para el servicio de notificacion ( interface )
class INotificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

# Implementacion del servicio de notificacion para correo electronico
# Clase de BAJO nivel
class EmailNotificador(INotificador):
    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}")

# Implementacion del servicio de notificacion para SMS
# Clase de BAJO nivel ---> (incluye detalles)
class SmsNotificador(INotificador):
    def enviar(self, mensaje):
        print(f"Enviando sms: {mensaje}")

# Clase o modulo de ALTO nivel que maneja la logica de negocios
class App:
    def __init__(self, notificador:INotificador):
        self.notificador = notificador

    def enviar_notificacion(self, mensaje: str):
        self.notificador.enviar(mensaje)
        print(f"Notificacion enviada correctamente")

# Modo de uso

email_notificador = EmailNotificador()
app_con_email = App(email_notificador)
app_con_email.enviar_notificacion("Este es un mensaje de prueba de correo electronico")

sms_notificador = SmsNotificador()
app_con_sms = App(sms_notificador)
app_con_sms.enviar_notificacion("Este es un mensaje de prueba de sms")
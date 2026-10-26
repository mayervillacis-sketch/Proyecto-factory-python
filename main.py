class Notificador:
    def enviar(self, mensaje):
        raise NotImplementedError


class TelegramNotifier(Notificador):
    def enviar(self, mensaje):
        print(f"[Telegram] {mensaje}")


class WhatsAppNotifier(Notificador):
    def enviar(self, mensaje):
        print(f"[WhatsApp] {mensaje}")


class NotificadorFactory:
    @staticmethod
    def crear(tipo):
        if tipo == "telegram":
            return TelegramNotifier()
        if tipo == "whatsapp":
            return WhatsAppNotifier()
        raise ValueError(f"Tipo no soportado: {tipo}")


if __name__ == "__main__":
    notificador = NotificadorFactory.crear("telegram")
    notificador.enviar("Hola desde el patrón Factory")
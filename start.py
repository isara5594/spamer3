from Telegram.telegram import TelegramBot
from Telegram.datos import configuracion

bot = TelegramBot(
    configuracion["usuario"],
    configuracion["api_id"],
    configuracion["api_hash"],
    configuracion["phone"]
)

bot.scraping_grupos()

# ID del grupo de origen
grupo_origen_id = -4598989859 #Aqui pones su chat id del grupo donde esta tus mensajes a enviar

# Listado de Opciones del BOT. Añadir aquí las opciones futuras.
listado_opciones = {
    "¿Quieres REENVIAR mensajes de este grupo a otros grupos? Y/N: ": lambda: bot.reenviar_mensajes(grupo_origen_id),
    "¿Quieres SPAMEAR este grupo? Y/N: ": bot.spamear_grupos,
    "¿Quieres SPAMEAR a los miembros de este grupo? Y/N: ": bot.spamear_usuarios,
    "¿Quieres IMPORTAR los usuarios de este grupo? Y/N: ": bot.secuestrar_usuarios,
    "¿Quieres almacenar la lista de usuarios? Y/N: ": bot.guardar_datos,
}

# Itera sobre el listado de opciones
for pregunta, accion in listado_opciones.items():
    print(pregunta)
    respuesta = input("Respuesta: ").strip().upper()
    if respuesta == "Y":
        accion()

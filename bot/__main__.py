from pyrogram import Client, filters

app = Client(
    name="Renamer Bot",
    api_id=11873433,
    api_hash="96abaf0d59cd1f5482bdc93ba6030424",
    bot_token="5703362416:AAHqmoVBA_GuXuPTQw4kwpeESQzSCfdqwRg"
)

app.start()


@app.on_message(filters=filters.command('start'))
def start(app, message):
    message.reply("hello")

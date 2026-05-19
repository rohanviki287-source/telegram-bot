from telegram.ext import ApplicationBuilder, MessageHandler, filters
import requests, json, os

async def handle(update, context):
    cookie = update.message.text
    payload = {"key": "NFK_dda3ee3932171d33d94067e3", "cookie": cookie}
    response = requests.post("https://nftoken.site/v1/api.php", json=payload)
    await update.message.reply_text(json.dumps(response.json(), indent=2))

app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(MessageHandler(filters.TEXT, handle))
app.run_polling()
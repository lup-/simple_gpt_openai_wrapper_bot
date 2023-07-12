import openai
import os
from telethon import TelegramClient, events

api_id = os.environ.get('TELEGRAM_API_ID', "")
api_hash = os.environ.get('TELEGRAM_API_HASH', "")
bot_token = os.environ.get('TELEGRAM_BOT_TOKEN', "")
openai_api_key = os.environ.get('OPENAI_TOKEN', "")

openai.api_key = openai_api_key
client = TelegramClient('gpt_bot', api_id, api_hash)


@client.on(events.NewMessage)
async def gpt_reply(event):
    question = event.raw_text
    try:
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )

        answer = chat_completion.choices[0].message.content
    except Exception as e:
        answer = str(e)

    await event.reply(answer)

client.start(bot_token=bot_token)
client.run_until_disconnected()

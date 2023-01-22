import parcer
import openai
import telebot
import time
import asyncio
import datetime

def send_message(bot, chat_id, text):
    offset = 0
    while offset < len(text):
        bot.send_message(chat_id, text[offset:offset + 4096])
        offset += 4096

if __name__ == "__main__":
    openai.api_key = parcer.api_parcer(0, "openai")
    telebot_api = parcer.api_parcer(0, "telebot")

    bot = telebot.TeleBot(telebot_api)

    @bot.message_handler(func=lambda message: True)
    def handle_messege(message):
        if len(message.text) > 12 and message.text[:12] == "@AndyDar_bot":
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
            )
            text = '@' + message.from_user.username + " " + response["choices"][0]["text"] + "\n\nконтакты - @adaragor"
            send_message(bot, message.chat.id, text)
            print("working - " + str(datetime.datetime.now()))
    while True:
        try:
            asyncio.run(bot.polling(non_stop=True, interval=1, timeout=0))
        except:
            time.sleep(5)

import telebot
bot = telebot.TeleBot('токен')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Говно":
      bot.send_message(message.from_user.id, "Жизнь твоя говно")
  elif message.text == "Писька":
      bot.send_message(message.from_user.id, "Писюн")
  else:
      bot.send_message(message.from_user.id, "Я не понимаю о чем ты")
      
bot.polling(none_stop=True, interval=0)

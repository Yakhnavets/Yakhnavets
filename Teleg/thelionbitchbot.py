import telebot
bot = telebot.TeleBot('mmmmmm')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Нахуй":
      bot.send_message(message.from_user.id, "Привет, сам иди.")
  elif message.text == "Писька":
      bot.send_message(message.from_user.id, "Писюн")
  else:
      bot.send_message(message.from_user.id, "Я не понимаю о чем ты")
      
bot.polling(none_stop=True, interval=0)

import pyowm
import telebot

owm = pyowm.OWM('1792f58a70c5920d7f16f205a215c6b7')
bot = telebot.TeleBot("956975014:AAFBVe7FUcsziQupGM4NVVpl_w-wX7VfinQ")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура сейчас в районе " + str(temp) + "\n\n"

	if temp < 10:
		answer += "Сейчас ппц как холодно, одевайся как танк!"
	elif temp < 20:
		answer += "Сейчас холодно, оденься потеплее."
	else:
		answer += "Температура норм, одевай что угодно."
	
	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )

while True:
    try:
        log(m='Bot running..')
        bot.polling(none_stop=True, interval=2)

        # Предполагаю, что бот может мирно завершить работу, поэтому
        # даем выйти из цикла
        break

    except Exception as ex:
        log(m='Error - {}'.format(str(ex)))

        log(m='Restarting..')
        bot.stop_polling()

        time.sleep(15)

        log(m='Running again!')
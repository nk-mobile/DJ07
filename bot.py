import telebot
import requests
import json

# Конфигурация
API_URL = 'http://localhost:8000/api/register/'
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    # Получаем данные пользователя
    user_id = message.from_user.id
    username = message.from_user.username

    # Подготавливаем данные для API
    data = {
        'user_id': user_id,
        'username': username
    }

    try:
        # Отправляем POST-запрос к API
        response = requests.post(API_URL, json=data)
        response_data = response.json()

        if response.status_code == 201:
            bot.reply_to(message, "Вы успешно зарегистрированы!")
        elif response.status_code == 400 and 'user_id' in response_data:
            bot.reply_to(message, "Такой пользователь уже зарегистрирован")
        else:
            bot.reply_to(message, f"Произошла ошибка: {response_data}")

    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"Ошибка соединения с сервером: {e}")


if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling()

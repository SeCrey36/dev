import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Устанавливаем уровень логов
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для поиска тиммейтов. Расскажи немного о себе и чему ты хочешь научиться.")

# Обработчик текстовых сообщений
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Спасибо! Мы добавим тебя в базу данных и найдем подходящих тиммейтов для тебя.")

def main():
    # Инициализируем бота и токен
    updater = Updater(token='YOUR_TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    # Обработчик команды /start
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Обработчик текстовых сообщений
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
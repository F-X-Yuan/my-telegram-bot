import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# 设置日志
logging.basicConfig(filename='bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = '7245845406:AAFlVk94N2WjAq2c0axcNrEF8dYiAwXscEo'

async def start(update: Update, context: CallbackContext) -> None:
    logging.info('Received /start command')
    await update.message.reply_text('Hello! I am your private chat bot. How can I help you today?')

async def echo(update: Update, context: CallbackContext) -> None:
    logging.info(f'Received message: {update.message.text}')
    await update.message.reply_text(update.message.text)

def main() -> None:
    # 创建一个Application实例
    application = Application.builder().token(TOKEN).build()

    logging.info('Starting bot...')

    # 添加命令处理器
    application.add_handler(CommandHandler('start', start))

    # 添加消息处理器
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 启动Bot
    application.run_polling()

if __name__ == '__main__':
    main()

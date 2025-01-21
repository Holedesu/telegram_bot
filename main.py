from telegram import Update
from asgiref.sync import sync_to_async
import django
import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from telegram.ext import (ApplicationBuilder,  # noqa: E402
                          CommandHandler,  # noqa: E402
                          ContextTypes)  # noqa: E402
from bot.models import (InfoText, TelegramUser)  # noqa: E402


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user, created = await sync_to_async(TelegramUser.objects.get_or_create)(
        telegram_id=update.effective_user.id,
        defaults={"first_interaction": update.message.date},
    )
    await update.message.reply_text(
        "Добро пожаловать! Для просмотра команд воспользуйтесь /help."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start - Запуск бота с приветственным сообщением\n"
        "/help  - Список команд бота\n"
        "/info  - Отправка ботом случайного сообщения"
    )


async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texts = await sync_to_async(list)(InfoText.objects.all())
    if texts:
        random_text = random.choice(texts)
        await update.message.reply_text(random_text.text)
    else:
        await update.message.reply_text("Сейчас в базе данных "
                                        "нет ни одного сообщения.")


if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token("INSERT_YOUR_TOKEN_INSTEAD_OF_THIS_TEXT")
        .build()
    )

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info_command))

    application.run_polling()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from polynom_sum import *

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    await update.message.reply_text(f'Введите команду /sum и через пробел два многочлена через пробел')
async def sum_poly(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    imput_num, pol1, pol2 = update.message.reply_text.split()
    print(f'пользователь {update.effective_user.first_name} ввел {pol1} и {pol2}')
    pol1 = convert_pol(pol1)
    pol2 = convert_pol(pol2)
    temp = fold_pols(pol1, pol2)
    print(f'сумма полиномов : {get_sum_pol(temp)}')
    await update.message.reply_text(get_sum_pol(temp))



bot_token = "5711017816:AAHl9-ju8GN-fckSbcycPFHJPGCi3-dPXdE"
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sum", sum_poly()))
app.run_polling()
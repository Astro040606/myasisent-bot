import telebot

# BotFather'dan olgan tokenni shu yerga qo'ying
TOKEN = '8322674664:AAHLFWpQBrfX5CcaC3sc-kLpWxTuoGiWMPI'
bot = telebot.TeleBot(TOKEN)

# To'g'ri javoblar kaliti
CORRECT_ANSWERS = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'A',
    6: 'B', 7: 'C', 8: 'D', 9: 'A', 10: 'B'
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men test tekshiruvchi botman. Javoblarni yuboring (masalan: ABCD...).")

@bot.message_handler(func=lambda message: True)
def check_test(message):
    user_input = message.text.strip().upper()
    cleaned_input = [char for char in user_input if char in ['A', 'B', 'C', 'D']]
    
    if len(cleaned_input) != 10:
        bot.reply_to(message, "Iltimos, aynan 10 ta javob yuboring!")
        return

    correct_count = 0
    wrong_answers = []

    for index, user_ans in enumerate(cleaned_input, start=1):
        if user_ans == CORRECT_ANSWERS[index]:
            correct_count += 1
        else:
            wrong_answers.append(f"{index}-savol: xato (to'g'risi: {CORRECT_ANSWERS[index]})")

    result = f"Natija: {correct_count}/10.\n"
    if wrong_answers:
        result += "Xatolar:\n" + "\n".join(wrong_answers)
    else:
        result += "Barakalla! Hammasi to'g'ri!"
        
    bot.reply_to(message, result)

bot.infinity_polling()
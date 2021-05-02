import telebot
from telebot import types
from PIL import Image
token = '1595978915:AAG7qsxwnTyFzGdO3YBodCrrQMgM3Ad_BeI'
bot = telebot.TeleBot(token)
fileID = ""
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, text='Отправь мне фотку и я  конвертирую ее в pdf')
def processPhotoMessage(message):
    global fileID
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(message.text+".jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    image1 = Image.open(r'C:\\Users\\Alisher\\Downloads\\Telegram Desktop\\'+message.text+'.jpg')
    im1 = image1.convert('RGB')
    im1.save(fr'C:\\Users\\Alisher\\Downloads\\Telegram Desktop\\'+message.text+'.pdf')
    bot.send_document(message.from_user.id, open('C:\\Users\\Alisher\\Downloads\\Telegram Desktop\\'+message.text+'.pdf', 'rb'))

def askName(message):
    bot.send_message(message.from_user.id, "How to name file?")
    bot.register_next_step_handler(message, processPhotoMessage);
@bot.message_handler(content_types=['photo'])
def photo(message):
    global fileID
    fileID = message.photo[-1].file_id
askName(message)
@bot.message_handler(commands=['sendVideo'])

def sendVideo(message):
    keyboard = types.InlineKeyboardMarkup();
    key_intergral = types.InlineKeyboardButton(text='Интеграл', callback_data='INTERGRAL');
    keyboard.add(key_intergral);
    key_vishmat = types.InlineKeyboardButton(text='Высшая математика', callback_data='VISHMAT');
    keyboard.add(key_vishmat);
    key_teilor = types.InlineKeyboardButton(text='Теорема Тейлора', callback_data='TEILOR');
    keyboard.add(key_teilor);
    key_riman = types.InlineKeyboardButton(text='Меняем порядок слагаемых: меняется сумма. Теорема Римана', callback_data='RIMAN');
    keyboard.add(key_riman);
    key_opred = types.InlineKeyboardButton(text='Определенный интеграл.', callback_data='OPRED');
    keyboard.add(key_opred);
    bot.send_message(message.from_user.id, text='Выбери видео которое хочешь посмотреть', reply_markup=keyboard)
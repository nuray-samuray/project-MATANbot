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
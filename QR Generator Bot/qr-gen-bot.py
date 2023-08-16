import telebot

import qrcode
from PIL import Image

token = '5218192949:AAFog_tpFeCz-YcU-gNItv_ZIeYg2nB_lf8'

bot=telebot.TeleBot(token)
a = 1

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):

    try:

        a + 1
        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src='C:/Users/dyudy/Desktop/photos/'+file_info.file_path;
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.reply_to(message,"Фото добавлено")
    

    except Exception as e:
        bot.reply_to(message,e )







if(a == 2):
    Logo_link = 'C:/Users/dyudy/Desktop/file_1.jpg'
 
    logo = Image.open(Logo_link)

    basewidth = 100
     
    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
     
    # taking url or text
    url = 'https://www.geeksforgeeks.org/'
     
    # adding URL or text to QRcode
    QRcode.add_data(url)
     
    # generating QR code
    QRcode.make()
     
    # taking color name from user
    QRcolor = 'Grey'
     
    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')
     
    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
           (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
     
    # save the QR code generated
    QRimg.save('file_2.jpg')
     
    print('QR code generated!')

    img2 = open('file_2.jpg', 'rb')



                 
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler(commands=['test'])
def start_message(message):
  bot.send_photo(message.chat.id, img2)



  
bot.infinity_polling()

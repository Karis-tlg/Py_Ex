#SOURCE BY TMR VIRUS
#BOX ZALO: https://zalo.me/g/jymelq533
#Không Xoá Dòng Này Để Ton Trọng Tác Giả!!
from telebot import types
import datetime
import time
import os
import subprocess
import psutil
import sqlite3
import hashlib
import requests
import datetime
import os
import telebot, random, sys
import datetime, base64
from pystyle import *
bot_token = '7097590956:AAH20ZYXoRGnzpCIyLsDOtf7nSmWui4X9u8' 
bot = telebot.TeleBot(bot_token)

allowed_group_id = -6316321401
admin_us = "TmrVirus"
lan = {}
notifi = {}
if not os.path.exists('id'):
    with open('id', 'w') as f:
        pass
allowed_users = []
processes = []
ADMIN_ID = 6316321401
banner = ("""
██████╗  █████╗     ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗
██╔══██╗██╔══██╗    ██║   ██║██║██╔══██╗██║   ██║██╔════╝
██████╔╝███████║    ██║   ██║██║██████╔╝██║   ██║███████╗
██╔══██╗██╔══██║    ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║
██║  ██║██║  ██║     ╚████╔╝ ██║██║  ██║╚██████╔╝███████║
╚═╝  ╚═╝╚═╝  ╚═╝      ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                          """)
colors = Col.red_to_purple
whiteChars = list('═╝╚╔╗║')
space = '   ' * 5
print(Colorate.Format(Center.XCenter(banner), whiteChars, Colorate.Vertical, colors, Col.white))
Write.Print(f"\n{space * 2}XIN CHÀO ADMIN!!!\n", Colors.red_to_blue, interval = 0.01)
Write.Print(f"{space}           BOT HIỆN ĐANG CHẠY RỒI Ạ!!!\n", Colors.red_to_white, interval = 0.01)
ban_id = {}
tg1 = None
def ban_phut(chat_id):
    if chat_id in ban_id:
        check_gio_or_phut, timestamp = ban_id[chat_id]
        if 'm' in check_gio_or_phut.lower():
            current_time = datetime.datetime.now()
            time_ban = check_gio_or_phut.lower().replace('m', '')
            if current_time - timestamp <= datetime.timedelta(minutes=int(time_ban)):
                return 'ban_phut'
            else:
                del ban_id[chat_id]
        elif 'h' in check_gio_or_phut.lower():
            current_time = datetime.datetime.now()
            time_ban = check_gio_or_phut.lower().replace('h', '')
            if current_time - timestamp <= datetime.timedelta(hours=int(time_ban)):
                return 'ban_gio'
            else:
                del ban_id[chat_id]
    else:
        return 'bo_ban'
connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        expiration_time TEXT
    )
''')
connection.commit()
def TimeStamp():
    now = str(datetime.date.today())
    return now
def load_users_from_database():
    cursor.execute('SELECT user_id, expiration_time FROM users')
    rows = cursor.fetchall()
    for row in rows:
        user_id = row[0]
        expiration_time = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
        if expiration_time > datetime.datetime.now():
            allowed_users.append(user_id)

def save_user_to_database(connection, user_id, expiration_time):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO users (user_id, expiration_time)
        VALUES (?, ?)
    ''', (user_id, expiration_time.strftime('%Y-%m-%d %H:%M:%S')))
    connection.commit()

def add_user(message):
    admin_id = message.from_user.id
    if admin_id != ADMIN_ID:
        bot.reply_to(message, 'BẠN KHÔNG CÓ QUYỀN SỬ DỤNG LỆNH NÀY')
        return

    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP ID NGƯỜI DÙNG ')
        return

    user_id = int(message.text.split()[1])
    allowed_users.append(user_id)
    expiration_time = datetime.datetime.now() + datetime.timedelta(days=30)
    connection = sqlite3.connect('user_data.db')
    save_user_to_database(connection, user_id, expiration_time)
    connection.close()

    message_text =f'┏━━━━━━━━━━━━━━━━━━┓\n┣➤ NGƯỜI DÙNG CÓ ID {user_id} \n┣➤ĐÃ ĐƯỢC THÊM VÀO DANH SÁCH ĐƯỢC PHÉP SỬ DỤNG LỆNH /spam┗━━━━━━━━━━━━━━━━━━┛\n'


load_users_from_database()

        
log_file_path = 'time.txt'

def log_to_file(log_message, message):
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_message + '\n')
@bot.message_handler(commands=['spam'])
def lqm_sms(message):
    user_id = message.from_user.id;
    with open('id', 'r') as file:
        if str(message.chat.id) not in file.read():
            # Nếu chưa có, lưu user_id vào tệp 'id'
            with open('id', 'a') as file:
                file.write(str(message.chat.id) + '\n')

    if len(message.text.split()) == 1:
        with open('id', 'r') as file:
            if str(message.chat.id) not in file.read():
                # Nếu chưa có, lưu user_id vào tệp 'id'
                with open('id', 'a') as file:
                    file.write(str(message.chat.id) + '\n')
                
        bot.reply_to(message, 'Click ===> /how')
        
        return

    phone_number = message.text.split()[1]
    if not phone_number.isnumeric():
        with open('id', 'r') as file:
            if str(message.chat.id) not in file.read():
                # Nếu chưa có, lưu user_id vào tệp 'id'
                with open('id', 'a') as file:
                    file.write(str(message.chat.id) + '\n')

        bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
        return

    if phone_number in ['113','911','114','115','+84328774559','0328774559']:
        with open('id', 'r') as file:
            if str(message.chat.id) not in file.read():
                # Nếu chưa có, lưu user_id vào tệp 'id'
                with open('id', 'a') as file:
                    file.write(str(message.chat.id) + '\n')
                
        # Số điện thoại nằm trong danh sách cấm
        bot.reply_to(message,"Bạn Làm Gì Thế Spam Cả Admin Lun Chớ")
        return

    file_path = os.path.join(os.getcwd(), "sms1.py")
    process = subprocess.Popen(["python", file_path, phone_number, "60"])
    file_path = os.path.join(os.getcwd(), "sms.py")
    process = subprocess.Popen(["python", file_path, phone_number, "120"])
    file_path = os.path.join(os.getcwd(), "spamvip.py")
    process = subprocess.Popen(["python", file_path, phone_number, "180"])
    processes.append(process)
    username = message.from_user.username
    with open('id', 'r') as file:
        if str(message.chat.id) not in file.read():
            # Nếu chưa có, lưu user_id vào tệp 'id'
            with open('id', 'a') as file:
                file.write(str(message.chat.id) + '\n')

    video_url = "liemspam.000webhostapp.com/lon.mp4"  # Replace this with the actual video URL      
    message_text =f"""
 🚀Submit Attack Request Successfully
    | Attack Phone: [ {phone_number} ]
    | Time Attack: 120s
    | Power of SMS Spam: 1/3
 🧸Information
    | Admin: @TmrVirus
    | Group Zalo: https://zalo.me/g/hbcumm801
"""
    bot.send_video(message.chat.id, video_url, caption=message_text, parse_mode='html') 
    log_to_file(f'Latest users: {message.from_user.username} | chat_id: {message.chat.id} | Time: {datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")} | Commands: /spam', message)

    log_to_file(f"┏━━━━━━━━━━━━━━━━━━┓\n┣➤ 🚀 Gửi Yêu Cầu Tấn Công Thành Công 🚀 \n┣➤ Admin: Ra Official Virus\n┣➤ Bot 👾: @VirusEnc_bot\n┣➤ Info Người Mới Tham Gia❤️: [ @{message.from_user.username} ] \n┣➤ Tên Người Dùng👑: [ {message.from_user.full_name} ]\n┣➤ Uid Người Dùng🔥:  [ {message.from_user.id} ]\n┣➤ Số Tấn Công 📱: [ {phone_number} ]\n┣➤ Số Lần 📞: Random ✅\n┗━━━━━━━━━━━━━━━━━━┛\n", message)
    
    print(Colorate.Horizontal(Colors.green_to_white, (f'Latest users: {message.from_user.username} | chat_id: {message.chat.id} | Time: {datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")} | Commands: /spam')))


    print(Colorate.Horizontal(Colors.red_to_white, (f"┏━━━━━━━━━━━━━━━━━━┓\n┣➤ 🚀 Gửi Yêu Cầu Tấn Công Thành Công 🚀 \n┣➤ Admin: Ra Official Virus\n┣➤ Bot 👾: @VirusEnc_bot\n┣➤ Info Người Mới Tham Gia❤️: [ @{message.from_user.username} ] \n┣➤ Tên Người Dùng👑: [ {message.from_user.full_name} ]\n┣➤ Uid Người Dùng🔥:  [ {message.from_user.id} ]\n┣➤ Số Tấn Công 📱: [ {phone_number} ]\n┣➤ Số Lần 📞: Random ✅\n┗━━━━━━━━━━━━━━━━━━┛\n")))
    # Add these lines at the beginning of your script
    
    


# ... (Remaining code)

@bot.message_handler(commands=['how'])
def how_to(message):
    with open('id', 'r') as file:
        if str(message.chat.id) not in file.read():
            # Nếu chưa có, lưu user_id vào tệp 'id'
            with open('id', 'a') as file:
                file.write(str(message.chat.id) + '\n')
                
    video_url = "liemspam.000webhostapp.com/lon.mp4"
    

    # Send video by URL
    
    message_text = '''
How to use spam bot:
┏━[ /spam [Phone Number]
┗━━━[Example]━━[ /spam 0987654321
'''
    bot.send_video(message.chat.id, video_url, caption=message_text, parse_mode='html') 

@bot.message_handler(commands=['start'])
def lenh(message):
    with open('id', 'r') as file:
        if str(message.chat.id) not in file.read():
            # Nếu chưa có, lưu user_id vào tệp 'id'
            with open('id', 'a') as file:
                file.write(str(message.chat.id) + '\n')
                
    video_url = "liemspam.000webhostapp.com/lon.mp4"
    

    # Send video by URL
    
    lenh_text = '''
Welcome to Bot Virus Spam
  ┏━━[ /spam (Used to send SMS spam)
  ┣━━━━[ /how (How to use SMS spam)
  ┣━━━━━━[ /start (Start Bot)
  ┗━━━━━━━━[ @TmrVirus ]━━━━━━━
  
    '''
    bot.send_video(message.chat.id, video_url, caption=lenh_text, parse_mode='html') 
    print(Colorate.Horizontal(Colors.green_to_white, (f'Latest users: {message.from_user.username} | chat_id: {message.chat.id} | Time: {datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")} | Commands: /start')))

    print(Colorate.Horizontal(Colors.red_to_white, (f"┏━━━━━━━━━━━━━━━━━━┓\n┣➤ Info Người Mới Tham Gia❤️: [ @{message.from_user.username} ] \n┣➤ Tên Người Dùng👑: [ {message.from_user.full_name} ]\n┣➤ Uid Người Dùng🔥:  [ {message.from_user.id} ]\n┗━━━━━━━━━━━━━━━━━━┛\n")))
    
    
    # Use lenh_text instead of message_text in the next line
    

# Use the polling method to keep the bot running

# ... (remaining code)

@bot.message_handler(commands=['status'])
def status(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    if user_id not in allowed_users:
        bot.reply_to(message, text='Bạn không có quyền sử dụng lệnh này!')
        return
    process_count = len(processes)
    bot.reply_to(message, f'Số quy trình đang chạy: {process_count}.')

@bot.message_handler(commands=['time'])
def show_uptime(message):
    current_time = time.time()
    uptime = current_time - start_time
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    uptime_str = f'{hours} giờ, {minutes} phút, {seconds} giây'
    bot.reply_to(message, f'Bot Đã Hoạt Động Được: {uptime_str}')
    
@bot.message_handler(commands=['stop_spam'])
def stop_spam(message):
    user_id = message.from_user.id
    with open('id', 'r') as file:
        if str(message.chat.id) not in file.read():
            # Nếu chưa có, lưu user_id vào tệp 'id'
            with open('id', 'a') as file:
                file.write(str(message.chat.id) + '\n')
                
    if len(message.text.split()) == 1:
        with open('id', 'r') as file:
            if str(message.chat.id) not in file.read():
                # Nếu chưa có, lưu user_id vào tệp 'id'
                with open('id', 'a') as file:
                    file.write(str(message.chat.id) + '\n')
                
        bot.reply_to(message, 'Vui Lòng Nhập Số Điện Thoại Để Dừng Spam.')
        return

    phone_number = message.text.split()[1]
    stop_spam_for_phone(phone_number)
    
    video_url = "liemspam.000webhostapp.com/lon.mp4"
    

    # Send video by URL
    with open('id', 'r') as file:
        if str(message.chat.id) not in file.read():
            # Nếu chưa có, lưu user_id vào tệp 'id'
            with open('id', 'a') as file:
                file.write(str(message.chat.id) + '\n')
                
    bot.reply_to(message, f"""
Spam Process Finished
   ┏━━━Stop Spam for Phone Number 
   ┗━━━━━━━━━━[{phone_number}] Successfully.  
    """)
    
def stop_spam_for_phone(phone_number):
    for process in processes:
        # Assuming the phone number is an argument passed to the script
        if phone_number in process.args:
            process.terminate()
            processes.remove(process)
            
                    
@bot.message_handler(commands=['restart'])
def restart(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return

    bot.reply_to(message, 'Bot sẽ được khởi động lại trong giây lát...')
    time.sleep(2)
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.message_handler(commands=['stop'])
def stop(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return

    bot.reply_to(message, 'Bot sẽ dừng lại trong giây lát...')
    time.sleep(2)
    bot.stop_polling()


def check_ban_gio_or_phut(chat_id, time_use, time_ban):
    if 'm' in time_ban.lower():
        now = datetime.datetime.now()
        time_ban = time_ban.lower().replace('m', '')
        if now - time_use <= datetime.timedelta(minutes = int(time_ban)):
            return 'ban_phut'
        else:
            if os.path.exists(f"band_{chat_id}"):
                os.remove(f"band_{chat_id}")
            return 'cut'
    elif 'h' in time_ban.lower():
        now = datetime.datetime.now()
        time_ban = time_ban.lower().replace('h', '')
        if now - time_use <= datetime.timedelta(hours = int(time_ban)):
            return 'ban_gio'
        else:
            if os.path.exists(f"band_{chat_id}"):
                os.remove(f"band_{chat_id}")
            return 'cut'
    else:
        return 'cc'
def check_band(chat_id, message):
    if os.path.exists(f"band_{chat_id}"):
        check = open(f"band_{chat_id}", 'r').read()
        js = eval(check)
        if js['time_use'] != None or js['ban_in'] != None:
            if check_ban_gio_or_phut(js['chat_id'], js['time_use'], js['ban_in']) == 'ban_phut':
                cc = js['ban_in'].lower().replace('m', ' Minutes')
                bot.reply_to(message, "Bạn Bị Ban Trong {}".format(cc))
            elif check_ban_gio_or_phut(js['chat_id'], js['time_use'], js['ban_in']) == 'ban_gio':
                cc = js['ban_in'].lower().replace('h', ' Hours')
                bot.reply_to(message, "Bạn Bị Ban Trong {}".format(cc))
        else:
            bot.reply_to(message, "Bạn Bị Ban Khỏi Hệ Thống!")
        return True
    return False
keyboard1 = types.InlineKeyboardMarkup(row_width=3)
keyboard1.add(
        types.InlineKeyboardButton("Contact", callback_data='contact'),
)

keyboard2 = types.InlineKeyboardMarkup(row_width=3)
keyboard2.add(
        types.InlineKeyboardButton("Reply", callback_data='reply'),
)
@bot.message_handler(commands=['noti'])
def noti(message):
    if message.from_user.username != admin_us:
        bot.reply_to(message, "Bạn Không Có Quyền Sử Dụng Lệnh Này")
        return
    args = message.text.split('/noti')
    if args[1] == '':
        bot.reply_to(message, "Xin lỗi bạn không phải là Tmr Virus")
        return
    
    # Load danh sách user_id từ tệp id và chuyển đổi thành một set để loại bỏ các giá trị trùng lặp
    with open('id', 'r') as file:
        user_ids = {line.strip() for line in file.readlines()}
    
    for user_id in user_ids:
        try:
            chat_id = int(user_id)
            with open('tmr.mp4', 'rb') as video:
                bot.send_video(chat_id, video, caption=f"Notification: {args[1]}", parse_mode='html')
                lan[chat_id] = {"count": 0}
        except Exception as e:
            bot.send_message(message.chat.id, f"Lỗi rồi nè Tmr Virus Ơi")

@bot.message_handler(func=lambda message: notifi.get(message.chat.id) == {"current_state": "waiting_for_tn"})
def tn(message):
    chat_id = message.chat.id
    mess = message.text
    bot.send_message(6316321401, f"{chat_id} Gửi Cho Bạn Tin Nhắn: {mess}")
    del notifi[chat_id]

# Xử lý callback query
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'contact':
        bot.send_message(chat_id=call.message.chat.id, text='💬 Liên hệ với Admin Bot:\n[@TmrVirusSpam_Bot](https://t.me/tmrvirus) | [Facebook](https://facebook.com/tmrvirus080)', parse_mode='Markdown')
    elif call.data == 'reply':
        lan[call.message.chat.id]["count"] += 1
        if lan[call.message.chat.id]["count"] >= 3:
            bot.send_message(chat_id=call.message.chat.id, text="Quá Giới Hạn!")
            return
        bot.send_message(chat_id=call.message.chat.id, text="Gửi Tin Nhắn:")
        notifi[call.message.chat.id] = {"current_state": "waiting_for_tn"}
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    
    bot.reply_to(message, 'Invalid order. Please use /start command to see the command list.🚫')
bot.polling()

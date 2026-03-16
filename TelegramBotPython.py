import telebot #Библиотека для Telegram bot API
from datetime import datetime, timedelta #Библиотека функции для работы с датой и временем

TOKEN = "8116424841:AAFyjUkgR0h-Ec5AfYa_0L_WH2a0CvdlKiU" #Токен бота

bot = telebot.TeleBot(TOKEN) #Создание бота с токеном

zapis = {} #Словарь для записей
temp_data = {} #Слоаврь для бронирования

def get_time_slots(): # Функция для получения списка доступного времени на завтра
slots = []
tomorrow = datetime.now() + timedelta(days=1)
for hour in range(9, 18):
time_str = tomorrow.strftime(f"%d.%m.%y {hour}:00") # Создаем строку времени: дата + час +
":00"
slots.append(time_str)
return slots

@bot.message_handler(commands=['start']) # Обработчик команды /start
def start(message): # Отправляем приветственное сообщение с описанием команд
bot.send_message(message.chat.id, "Привет! Я бот для записи\n\nКоманды:\n/book -
записаться\n/all - моя запись\n/cancel - отмена") # Бот отправляет сообщение

@bot.message_handler(commands=['book']) # Обработчик команды /book
def book(message):
chat_id = message.chat.id # Получаем ID чата пользователя
msg = bot.send_message(chat_id, "Введите ваше имя") # Просим пользователя ввести имя
bot.register_next_step_handler(msg, get_name) # Регистрируем функцию get_name

def get_name(message): # Функция для получения имени пользователя
chat_id = message.chat.id # Получаем ID чата
name = message.text # Получаем текст сообдщения
temp_data[chat_id] = {'name': name} # Сохраняем имя во временном словаре по ID пользователя
slots = get_time_slots()

free_slots = []

for slot in slots:
if slot not in zapis:
free_slots.append(slot)

if not free_slots:
bot.send_message(chat_id, "Извините, на завтра нет свободного времени")
return

markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
buttons = []
for slot in free_slots[:8]:
buttons.append(telebot.types.KeyboardButton(slot))
markup.add(*buttons)

msg = bot.send_message(chat_id, f"Приятно познакомиться, {name}!\nВыберите свободное
время", reply_markup=markup)
bot.register_next_step_handler(msg, get_time)

def get_time(message):
chat_id = message.chat.id
selected_time = message.text

if selected_time in zapis:
bot.send_message(chat_id, "Это время уже занято! Начните заново /book",
reply_markup=telebot.types.ReplyKeyboardRemove())
return

name = temp_data[chat_id]['name']
zapis[selected_time] = name

bot.send_message(chat_id,
f"Имя: {name}\n"
f"Время: {selected_time}\n\n"

f"Ждем Вас!",
reply_markup=telebot.types.ReplyKeyboardRemove())

del temp_data[chat_id]

@bot.message_handler(commands=['myrecord'])
def my_record(message):
chat_id = message.chat.id
user_name = message.from_user.first_name
found = False

for time, name in zapis.items():
if name == user_name:
bot.send_message(chat_id, f"Ваша запись: {time}")
found = True
break

if not found:
bot.send_message(chat_id, "У вас нет активных записей")

@bot.message_handler(commands=['cancel'])
def cancel(message):
chat_id = message.chat.id
user_name = message.from_user.first_name
to_delete = None

for time, name in zapis.items():
if name == user_name:
to_delete = time
break

if to_delete:
del zapis[to_delete]
bot.send_message(chat_id, " Ваша запись отменена")
else:

bot.send_message(chat_id, "У вас нет активных записей")

@bot.message_handler(commands=['all'])
def all_records(message):
if message.from_user.id == 1621645110:
if zapis:
text = "📋 Все записи:\n\n"
for time, name in sorted(zapis.items()):
text += f"👤 {name} - {time}\n"
bot.send_message(message.chat.id, text)
else:
bot.send_message(message.chat.id, "Записей нет")
else:
bot.send_message(message.chat.id, "У вас нет доступа")

print("Бот запущен... - Bot.py:116")
bot.polling(none_stop=True)
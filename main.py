from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.errors import SessionPasswordNeededError
from telethon.events import NewMessage
import asyncio
from datetime import datetime, timedelta, date
from colorama import Fore, Style
import os

with open('sec.txt', 'r') as file:
    sec_data = dict(line.strip().split('=') for line in file)
api_id = sec_data['api_id']
api_hash = sec_data['api_hash']
phone_number = sec_data['phone_number']

group_id = grouptgid
os.system('cls' if os.name == 'nt' else 'clear')

search_texts = ['закажу банки для вейпа', 'хочу заказать жижу', 'куплю банки для вейпа по низкой цене',
    'ищу жидкость для вейпинга', 'закажу банку для вейпа с доставкой', 'где купить жидкость для вейпа',
    'приобрету банки для жидкости', 'куплю жидкости разных вкусов', 'покупаю банки для вейпа оптом',
    'закажу жижу в интернет-магазине', 'ищу магазин с ассортиментом жидкостей', 'где купить банки для жидкости',
    'приобрету упаковку жидкости для вейпинга', 'хочу найти банки для заправки', 'закажу новые жидкости для вейпа',
    'куплю сопровождающие товары для вейпинга', 'приобрету недорогие банки для вейпа', 'ищу специализированный магазин жидкостей',
    'где заказать банки для жидкости онлайн', 'покупаю жижу в бутылках', 'закажу расходные материалы для вейпинга',
    'ищу разные вкусы жидкости для вейпинга', 'хочу купить банку для вейпа с большим объемом', 
    'приобрету жидкость с низким содержанием никотина', 'куплю банки для вейпа с удобной системой залития', 
    'закажу жидкость с экзотическими вкусами', 'где купить банки для вейпа различных размеров', 
    'ищу интернет-магазин с широким ассортиментом жидкостей', 'приобрету набор с разными вкусами жидкости', 
    'хочу приобрести банку для вейпинга в стильном дизайне', 'куплю комплектующие для замены в вейпе', 
    'закажу жидкость для вейпа в большом количестве', 'ищу магазин с натуральными жидкостями для вейпинга', 
    'где купить банки для жидкости с высоким качеством', 'приобрету жидкость десертных вкусов для вейпа', 
    'куплю банку для вейпа в магазине рядом с домом', 'закажу быструю доставку жидкостей для вейпа', 
    'ищу банки для жидкости в фирменном стиле', 'хочу купить банки для вейпа в удобных форматах', 
    'приобрету жидкость с крепким ароматом для вейпинга', 'куплю банку для вейпинга с удобными крышками', 
    'закажу жидкость для вейпа с эквивалентом никотина', 'закажу жижу для вейпа с эквивалентом никотина',
    'куплю жижу для вейпа с никотином', 'где купить банки с широким горлом для заправки', 
    'покупаю жидкость для вейпа без дополнительных привкусов', 'ищу качественные банки для жидкости с адаптером', 
    'хочу заказать банку для вейпа с легким открыванием', 'приобрету жидкость для вейпа с цитрусовыми нотками', 
    'куплю банки для вейпа всех цветов радуги', 'закажу ментоловую жидкость для вейпа', 
    'ищу магазин с самыми популярными вкусами жидкости', 'где купить банки для вейпа с доставкой на дом', 
    'приобрету банку для вейпа с простой системой заправки', 'хочу заказать жидкость с медовым ароматом для вейпинга', 
    'куплю дополнительные банки для запаса жидкости', 'закажу жидкость с приятным запахом для вейпа', 
    'ищу жидкость с минимальным содержанием сахара для вейпинга', 'где купить банку для вейпа с удобными наконечниками', 
    'покупаю банки для вейпа с гарантией качества', 'ищу интернет-магазин с предложениями по жидкости для вейпинга', 
    'приобрету эксклюзивные банки для жидкостей с оригинальным дизайном', 'закажу жидкость от известных производителей для вейпа', 
    'где приобрести банку для вейпин','куплю жижу', 'куплю жидкость','затарю жидкость','кто может продать жижи', 'приобрету жижу', 'затарю жижу', 'закуплю жижу', 'скуплю жижу', 'куплю банки', 'приобрету банки', 'затарю банки', 'закуплю банки', 'скуплю банки', 'куплю банку', 'приобрету банку', 'затарю банку', 'закуплю банку', 'скуплю банку', 'куплю 2', 'куплю 3', 'куплю 4', 'куплю 1', 'куплю две', 'куплю одну', 'куплю три','закажу жидкость', 'нужна жидкость', 'куплю запас жижи', 'в поиске банки для вейпа', 'куплю упаковку жижи', 'приобрету новые банки', 'хочу жижу', 'покупаю жидкость']

client = TelegramClient('session_name', api_id, api_hash)

processed_messages = {}

async def main():
    print("*" * 15 + " БОТ ЗАПУЩЕН " + "*" * 15)
    await client.send_message(tgid, "Бот запущен") #
    try:
        await client.start(phone_number)
    except SessionPasswordNeededError:
        password = input("Введите ваш пароль 2FA: ")
        await client.start(phone_number, password)

    channel = await client.get_entity(int(group_id))

    async for message in client.iter_messages(channel):
        if message.message: 
            if message.date.date() == date.today():
                if message.id not in processed_messages:
                    words = message.message.lower()
                    for text in search_texts:
                        if text in words:
                            try:
                                user = await client.get_entity(message.sender_id)
                                if user.username:
                                    corrected_time = message.date + timedelta(hours=3)
                                    info_message = (f"Найден юзер: @{user.username}, "
                                                    f"Сообщение: {message.message} - "
                                                    f"Время отправки сообщения в группу: {corrected_time.strftime('%d.%m.%Y %H:%M')}")
                                    print(Fore.GREEN + f"Найден юзер: @{user.username}, ", end='')
                                    print(Fore.BLUE + f"Сообщение: {message.message} - ", end='')
                                    print(Fore.RED + f"Время отправки сообщения в группу: {corrected_time.strftime('%d.%m.%Y %H:%M')}")
                                    await client.send_message(tgid, info_message) #
                                    processed_messages[message.id] = True 
                            except ValueError:
                                print(f"Пользователь с ID {message.sender_id} не найден.")

async def handler(event):
    message = event.message
    if message.message:
        if message.date.date() == date.today():
            if message.id not in processed_messages:
                words = message.message.lower()
                for text in search_texts:
                    if text in words:
                        try:
                            user = await client.get_entity(message.sender_id)
                            if user.username:
                                corrected_time = message.date + timedelta(hours=3)
                                info_message = (f"Найден юзер: @{user.username}, "
                                                f"Сообщение: {message.message} - "
                                                f"Время отправки сообщения в группу: {corrected_time.strftime('%d.%m.%Y %H:%M')}")
                                print(Fore.GREEN + f"Найден юзер: @{user.username}, ", end='')
                                print(Fore.BLUE + f"Сообщение: {message.message} - ", end='')
                                print(Fore.RED + f"Время отправки сообщения в группу: {corrected_time.strftime('%d.%m.%Y %H:%M')}")
                                await client.send_message(tgid, info_message) #
                                processed_messages[message.id] = True 
                        except ValueError:
                            print(f"Пользователь с ID {message.sender_id} не найден.")

client.add_event_handler(handler, NewMessage(incoming=True, chats=group_id))

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()

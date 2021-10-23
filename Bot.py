import config
import logging

from aiogram import Bot,Dispatcher,executor,types


#init
bot = Bot(token = config.TOKEN)
dp = Dispatcher(bot)

#Log levl
logging.basicConfig(level=logging.INFO)


#remove new user joined messages
@dp.message_handler(content_types = ["new_chat_members"])
async def user_joined(message:types.Message):
    print('JOIN messade removed')
    await message.delete()


#handler without filters handle all text messages
@dp.message_handler()
async def filter_messages (message:types.Message):
    if "плохое слово" in message.text:
        await message.delete()

    
#long-polling
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates = True)
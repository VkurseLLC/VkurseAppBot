from config import *
from db import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Здравствуйте!\n"
                         f"..............\n"
                         f"..............", reply_markup=take_code_markup)


class Form_get_PHONE_NUMBER(StatesGroup):
    name = State()


@dp.message_handler(content_types=['contact', 'text'], state=Form_get_PHONE_NUMBER.name)
async def get_PHONE_NUMBER(message: types.Contact, state: FSMContext):
    await state.finish()
    if message.text == '/cancel' or message.text == '/menu' or message.text == '/start':
        await start(message)

    elif message.contact is not None:        
        if message.contact.user_id == message.from_user.id:
            verification_code = give_code()
            save_auth_dates(create_connection(), message.contact.phone_number.replace('+',''), verification_code)
            await message.answer(f"Отлично\n"
                                f"Ваш код: <code>{verification_code}</code>\n"
                                f"Введите его в приложении", reply_markup=types.ReplyKeyboardRemove(), parse_mode = 'html')
        else:
            await message.answer(f"Номер принадлежит другому человеку, введите свой номер")
            await state.set_state(Form_get_PHONE_NUMBER.name)

    else:
        await message.answer("Не понял вопрос, отправте номер, нажав на кнопку\n"
                             "Или нажмите /cancel для отмены")



@dp.callback_query_handler()
async def process_callback_take_code(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'take_code':
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
        await bot.send_message(callback.from_user.id, text='Чтобы получить код подтверждения,'
                                            'нажмите на кнопку "Отправить номер телефона"👇🏻',
                               reply_markup=markup_number)

        await state.set_state(Form_get_PHONE_NUMBER.name)















if __name__ == '__main__':
    print("Bot is working")
    executor.start_polling(dp)
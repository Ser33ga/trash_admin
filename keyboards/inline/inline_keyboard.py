from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

like = InlineKeyboardButton(
    text='+',
    callback_data='like'
)

dislike = InlineKeyboardButton(
    text='-',
    callback_data='dislike'
)

inline_keyboard_agree = InlineKeyboardMarkup(
    inline_keyboard=[[like],
                     [dislike]]
)

jokes = InlineKeyboardButton(
    text='ТРЕШ ИСТОРИИ‼️‼️',
    callback_data='-1002214386155'
)

recepies = InlineKeyboardButton(
    text='ЖЕСТЬ ИСТОРИИ',
    callback_data='-1002205161628'
)

inline_keyboard_choose_category = InlineKeyboardMarkup(
    inline_keyboard=[[jokes],
                     [recepies]]
)
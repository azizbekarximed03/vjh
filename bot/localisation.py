#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Salom, \n\nBu video siquvchi bot \n\n<b>Menga video jo'nating, men uni kichraytirib beraman. Tushmasangiz /help yuboring</b> \n\n/ \n\nKanalim:: @Azizbek_03"
   
    ABS_TEXT = " Iltimos, faqat o‘zingizni o‘ylamang."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "📥 Yuklayapman 📥 \n"
    
    UPLOAD_START = "📤 Yuboryapman 📤 \n"
    
    COMPRESS_START = "📀 Siqyapman ... 📀"
    
    RCHD_BOT_API_LIMIT = "Siqish generatori maksimal hajmi (50MB). Qayta yuborishga urining."
    
    RCHD_TG_API_LIMIT = "Yuklandi {} soniyada.\nFayl hajmi topildi: {}\nKechirasiz, maksimal cheklov 2gb"
    
    COMPRESS_SUCCESS = "📥 Yuklandi in {}\n\n📀 Siqildi {}\n\n📤 Yuborildi {}\n\nKanalim: @Azizbek_03"

    COMPRESS_PROGRESS = "⏳ Vaqt: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Qo‘shimcha video / fayl thumnail saqlandi. Bu rasm video / file uchun ishlatiladi."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Qo'chimcha humbnail tozalandi"
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media uvofaqqiyatli tozalandi"
    
    SAVED_RECVD_DOC_FILE = "✅ Muvofaqqiyatli yuklandi"
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "Thumbnail topilmadi"
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Allaqachon bitta video ishlovda ⚠️"
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Salom, men video siquvchi botman \n\n1. Menga video yuboring \n2. Videoga reply qiling - /compress va necha % qisqartishimni yozing \nMasalan: <code>/compress 50</code> \n\nKanalim: @Azizbek_03"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    

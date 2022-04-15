# Copyright (C) 2021 By AmortMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبآ عزيزي↤「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」!**\n
🤖 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) **
** يتيح لك تشغيل الموسيقى والفيديو في مجموعات من خلال المكالمات الجديدة في Telegram! **
💡 ** اكتشف جميع أوامر البوت وكيفية عملها من خلال النقر على زر »📚 الأوامر! **
🔖 ** لمعرفة كيفية استخدام هذا البوت ، يرجى النقر فوق » زر دليل الاستخدام! **
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "༺اضفـني الى مجموعتڪ༻",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("༺ڪيفية الاسـتخدام༻", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("༺الاوامــــــر باللغة ar- en༻", callback_data="cbbasic"),
                    InlineKeyboardButton("ʚ -BaKr JaSsEm ɞ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "✿ MY CHANNEL ❀", url=f"https://t.me/EUUUJ"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "༺BR TEAM ༻", url="https://t.me/v00r22"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" الدليل الأساسي لاستخدام هذا البوت:

 1 ↤ أولاً ، أضفني إلى مجموعتك
 2 ↤ بعد ذلك ، قم بترقيتي كمشرف ومنح جميع الصلاحيات باستثناء الوضع الخفي
 3 ↤ بعد ترقيتي ، اكتب /تحديث او /reload مجموعة لتحديث بيانات المشرفين
 3 ↤ أضف @{ASSISTANT_NAME} إلى مجموعتك أو اكتب #اضافه او /userbotjoin لدعوة حساب المساعد
 4 ↤ قم بتشغيل المكالمة  أولاً قبل البدء في تشغيل الفيديو / الموسيقى
 5 ↤ في بعض الأحيان ، يمكن أن تساعدك إعادة تحميل البوت باستخدام الأمر #تحديث او /reloadفي إصلاح بعض المشكلات
 📌 إذا لم ينضم البوت إلى المكالمة ، فتأكد من تشغيل المكالمة  بالفعل ، أو اكتب /userbotleave ثم اكتب /userbotjoin مرة أخرى

 💡 إذا كانت لديك أسئلة  حول هذا البوت ، فيمكنك إخبارنا منن خلال  الدعم الخاصة بي هنا ↤ @BRTEAMSBOT
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""༺مرحـبا بڪم في بوت 🎶BR Music ༻
ْء➖➖➖➖➖➖➖➖➖➖
♻️ اوامـر تشــغيل باللغـة العربيـة 🇮🇶 
 ⚠️ يجب استخدام {# ! \ } امام ڪل الاوامـر 
1⃣ تشغيل+ اسم »» لتشغـيل مـيوزك في المڪالمة 
2⃣ فيديو+ اسم»» لتشغـيل الفيديو في المڪالمة 
3⃣ ايقاف »» لايـقــاف التـشغيل ❗️
4⃣ تكملة »»  استئناف التشغيل 🌀
5⃣ تخطي»» لتشغيل الاغنية التالية
6⃣ توقف »» ايقاف التشغيل موقتآ
7⃣ كتم»» لڪتم البوت 🔇
8⃣ الغاء »»  لرفع الڪتم عن البوت
ء➖➖➖➖➖➖➖➖➖➖➖➖➖
🔸 قائمة »» ↤ تظهر لك قائمة التشغيل
🔹تح + الاسم»» تنزيل فيديو من youtube
🔶 تحميل + الاسم»»  تنزيل صوت من youtube
🔷الصوت + الرقم»» لضبط مستوئ الصوت
🔶 تحديث»» لتحديث البوت و قائمة المشرفين
🔷 اضافة »» لاستدعاء حساب المساعد
🔶 طرد »»»  لطرد حساب المساعد 
🔹البنك »»»  إظهار حالة نت البوت 
🔸معلومات إظهار معلومات البوت  (في المجموعة)

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("༺اوامر باللغة الانڪليزية༻", callback_data="cbadmin")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""  ༺ Hello My Friend to bot  🎶BR Music ༻
ْ➖➖➖➖➖➖➖➖➖➖
♻️ English language operation commands 🍀⚠️ You must use {# !  \ } in front of all orders
 1️⃣ /mPlay + name »» to play your music in the call
 2⃣ /vplay + name to play the video in the call
 3⃣ /stop »» to stop playback ❗️
 4️⃣ /resume »» Resume playback 🌀
 5⃣ /Skip to play the next song
 6️⃣ /Pause »» Pause playback
 7⃣ /vmute »» to mute the bot 🔇
 8⃣  /vunmute »» to remove the bot’s silence🔊
➖➖➖➖➖➖➖➖➖➖
 🔸 /PlayList »» ↤ Shows you the playlist
 🔹 /video + Name »» Download a video from youtube
 🔶 /song + Name »» Download audio from youtube
 🔷/volume + Number»» to adjust the volume level
 🔶 /reload »» to update the bot and the list of moderators
 🔷 /userbotjoin »» to invoke the assistant account
 🔶 /userbotleave »»» to expel the assistant account
 🔹 /ping »»» Show bot net status
 🔸 /alive»» Show bot information (in group)

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 اغلاق", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ قائمة التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()

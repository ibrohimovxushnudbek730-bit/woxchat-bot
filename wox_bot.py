from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random

# === BOT MA'LUMOTLARI ===
TOKEN: Final = "8002979314:AAEhRtwWBAge1jJUo-m_xiIpTiC63PUB6CM"  # tokenni o'z botingnikiga yoz
BOT_USERNAME: Final = "@woxchat_bot"

# === BUYRUQLAR ===
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum jigar! Bot uyg‘ondi 😎")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Shunchaki yoz, men javob beraman 😉")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ha, bu bot ham odamga o‘xshab gaplashadi 😂")


# === JAVOBLAR ===
def handle_response(text: str) -> str:
    text = text.lower()

    javoblar = {
        # SALOMLAR
        "salom": [
            "voo salom jigar 😎",
            "salom, bugun choy sendanmi ☕",
            "salom, kecha wifi ishlaganmi 😂",
            "vaalaykum salom, darsdan chiqdingmi?",
            "salom! bugun kayfiyat bomba-a? 😁"
        ],
        # QANDAYSAN
        "qales": [
            "zo‘rman, o‘zingchi jigar 😎",
            "shunaqa endi, dars yo‘q, kayfiyat yaxshi 😂",
            "rahmat, yashab yuribmiz 😅",
            "botlar ham charchaydi ba’zida 😭",
            "zo‘r, faqat choy sovib qoldi ☕"
        ],
        "qandaysan": [
            "yaxshi, lekin wifi o‘chib qoldi 😩",
            "shunaqa, hayot go‘zal 😎",
            "zo‘r, faqat domla urishdi 😂",
            "rahmat jigar, sen-chi?"
        ],
        # DOMLA
        "domla": [
            "domla keldi, telefonni yashir 😂",
            "domla gapni cho‘zma dedi 😅",
            "domla bugun kayfda emaski 😭",
            "domlani eslatma, yurak og‘riyapti 😩",
            "domla test qilayapti, internetni o‘chir 😱"
        ],
        # DARS
        "dars": [
            "darsdan charchadim 😩",
            "dars bo‘lmasa hayot chiroyli 😎",
            "darsni tashlab choyxona tarafga yur ☕",
            "domla keldi, kitobni och 😂",
            "darsni kim o‘ylab chiqargan o‘zi 😅"
        ],
        # FANLAR
        "matematika": [
            "raqamlar urushib ketdi boshimda 😵‍💫",
            "matematika = azob 😂",
            "x + y = uxlab qoldim 😴"
        ],
        "fizika": [
            "fizika deb eshitsam yuragim titraydi 😭",
            "fizika kuch, lekin men zaifman 😅",
            "fizika uchun choy kerak ☕"
        ],
        "ingliz": [
            "how are you? tired 😩",
            "english? no energy today 😂",
            "teacher yana 'present perfect' dedi 😭"
        ],
        "tarix": [
            "tarix — bu azob 😭",
            "tarixni eslab yuradigan odam bormi o‘zi 😂",
            "tarixdan domla 1 qo‘ydi 😅"
        ],
        # BOT
        "bot": [
            "ha, men botman, lekin yurakli 🤖💔",
            "botga tegma, kayf yo‘q bugun 😎",
            "botni chaqirdingmi, portlayman hozir 💥😂",
            "bot emas, jondan ham yaqin do‘stman 😅",
            "botni bezovta qilma, ish bilan band 😂"
        ],
        # SHOHJAXON
        "shohjaxon": [
            "Shohjaxon keldimi? endi jim bo‘linglar 😎",
            "Shohjaxon yozsa, bot ham tinglaydi 😂",
            "Shohjaxon — guruhning legendasi 💪",
            "Shohjaxon chiqmasa, guruh jim bo‘ladi 😅"
        ],
        # YANGI GAPLAR
        "wifi": [
            "wifi o‘chdimi yana? 😩",
            "wifi bor, lekin yurak yo‘q 😭",
            "wifi ishlasa, men ham ishlayman 😂",
            "wifi charchadi, dam beryapti 😅"
        ],
        "kechasi": [
            "kechasi uxlamaysan-a sen 😏",
            "kechasi ham chatdasanmi? 😂",
            "kechasi kod yozib o‘tiribsanmi? 💻"
        ],
        "uxlab qoldim": [
            "ha, klassik 😂",
            "uyqu — bu san’at 😴",
            "men ham uxlagim kelyapti 😅"
        ],
        "imtihon": [
            "imtihon haqida gapirma 😭",
            "imtihon bo‘lsa, panika bosadi 😩",
            "imtihon — bu sadoqat sinovi 😂"
        ],
        "yozgi ta’til": [
            "yozgi ta’til degani choy va wifi 😎",
            "yozgi ta’tilda ham dars qilishdi 😭",
            "ta’til keldi, ammo pul yo‘q 😅"
        ],
        "yur jigar": [
            "qayerga yuramiz, choyxonagami ☕",
            "bor-e, yur bir aylanimiz 😎",
            "yur, darsni tashlab ketamiz 😂"
        ],
        "nima gap": [
            "hammasi joyida, faqat internet yo‘q 😅",
            "gap yo‘q, choy bor ☕😂",
            "bugun kayfiyat bomba 💣"
        ],
        "ha": [
            "ha deganing yoqdi 😏",
            "ha endi yo‘q dema 😂",
            "ha? bo‘ldi gap shu 😎"
        ],
        "yo‘q": [
            "yo‘qmi? nega endi 😭",
            "yo‘q deganing yurakni sindirdi 😩",
            "yo‘q deyishdan foyda yo‘q 😂"
        ],
        "ketaman": [
            "ketma jigar 😭",
            "mayli, lekin qaytib kel 😅",
            "xayr emas, ko‘rishguncha 👋"
        ],
        "sevaman": [
            "men ham seni sevaman 😍",
            "yo‘q, ishonmayman 😂",
            "senga ishonish xavfli 😏"
        ],
        "rahmat": [
            "doim marhamat! 🙌",
            "arzimaydi 😁",
            "bot ham mehribon bo‘lishi mumkin 😂"
        ]
    }

    for kalit, variantlar in javoblar.items():
        if kalit in text:
            return random.choice(variantlar)

    # Default javob
    return random.choice([
        "ha endi nima gap o‘zi? 😅",
        "yozishni bilmasang, sticker tashla 😂",
        "shu gapni eshitib bot ham o‘ylanib qoldi 😆",
        "kayfiyat yaxshimi jigar?",
        "bugun ham internet sust ishlayapti shekilli 📶"
    ])


# === XABARLARNI QABUL QILISH ===
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response, reply_to_message_id=update.message.message_id)


# === BOTNI ISHGA TUSHURISH ===
if __name__ == '__main__':
    print("Bot ishga tushdi... 😎")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.run_polling(poll_interval=1.0)

"""
ICEBERG Anonim Murojaat Bot
---------------------------
O'quvchilar botga yozadi -> xabar ustozga (admin) hech qanday ism/username
ko'rsatilmasdan yetib boradi. Ustoz o'sha xabarga "Reply" qilib javob yozsa,
javob xuddi shu (lekin ustozga noma'lum) o'quvchiga qaytib boradi.

Bot HECH QACHON kanalga/adminga o'quvchining ismi, username'i yoki
chat_id raqamini ko'rsatmaydi. Ichkarida faqat javobni to'g'ri odamga
yetkazish uchun vaqtinchalik (fayl ichida) moslashtirish saqlanadi.

Ishga tushirish:
    1) pip install -r requirements.txt
    2) .env faylidagi BOT_TOKEN va ADMIN_PASSCODE to'g'ri ekanini tekshiring
    3) python3 bot.py

Ustoz birinchi marta botga shaxsan /register <passcode> yozib o'zini
admin sifatida ro'yxatdan o'tkazadi. Shundan keyin barcha anonim xabarlar
unga keladi.
"""

import json
import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

load_dotenv()

BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_PASSCODE = os.environ.get("ADMIN_PASSCODE", "").strip()

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
ADMIN_FILE = DATA_DIR / "admin.json"
MAPPING_FILE = DATA_DIR / "mapping.json"

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s", level=logging.INFO
)
log = logging.getLogger("iceberg-anonim-bot")


# ---------- oddiy fayl-asosli saqlash ----------

def _load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return default
    return default


def _save_json(path: Path, data):
    path.write_text(json.dumps(data))


def get_admin_chat_id():
    data = _load_json(ADMIN_FILE, {})
    return data.get("admin_chat_id")


def set_admin_chat_id(chat_id: int):
    _save_json(ADMIN_FILE, {"admin_chat_id": chat_id})


def get_mapping() -> dict:
    # kalit: adminga yuborilgan xabar message_id (str), qiymat: asl o'quvchi chat_id
    return _load_json(MAPPING_FILE, {})


def remember_mapping(admin_message_id: int, student_chat_id: int):
    mapping = get_mapping()
    mapping[str(admin_message_id)] = student_chat_id
    # fayl shishib ketmasligi uchun oxirgi 2000 tasini saqlaymiz
    if len(mapping) > 2000:
        keys = list(mapping.keys())[-2000:]
        mapping = {k: mapping[k] for k in keys}
    _save_json(MAPPING_FILE, mapping)


def lookup_student(admin_message_id: int):
    return get_mapping().get(str(admin_message_id))


# ---------- handlerlar ----------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    admin_id = get_admin_chat_id()
    if admin_id and chat_id == admin_id:
        await update.message.reply_text(
            "Assalomu alaykum, Teacher Akmaljon Jalalov!\n\n"
            "Bu botga o'quvchilar anonim murojaat yozadilar, ular sizga "
            "to'g'ridan-to'g'ri (ism-familiyasiz) yetib boradi.\n\n"
            "Javob yozish uchun o'sha xabarni ushlab turib 'Reply' qiling — "
            "javobingiz anonim tarzda o'sha o'quvchiga yetadi, siz kim "
            "ekanini bilmaysiz."
        )
        return

    await update.message.reply_text(
        "Assalomu alaykum! 👋\n\n"
        "Bu — ICEBERG o'quv markazi uchun ANONIM murojaat botí. "
        "Agar sizda biror muammo, taklif yoki shikoyat bo'lsa, shu yerga "
        "yozib qoldiring.\n\n"
        "🔒 Xabaringiz ustozga ismingiz yoki boshqa ma'lumotlaringizsiz, "
        "to'liq anonim tarzda yetkaziladi. Hech kim siz yozganingizni bilmaydi.\n\n"
        "Xabaringizni shu yerga yozing 👇"
    )


async def register_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    existing = get_admin_chat_id()

    if not ADMIN_PASSCODE:
        await update.message.reply_text(
            "ADMIN_PASSCODE .env faylida sozlanmagan. Avval uni sozlang."
        )
        return

    if existing:
        await update.message.reply_text(
            "Admin allaqachon ro'yxatdan o'tgan. Agar bu xato bo'lsa, "
            "serverdagi data/admin.json faylini o'chirib qayta urining."
        )
        return

    args = context.args
    if not args or args[0] != ADMIN_PASSCODE:
        await update.message.reply_text(
            "Noto'g'ri kod. Foydalanish: /register <maxfiy_kod>"
        )
        return

    set_admin_chat_id(chat_id)
    await update.message.reply_text(
        "✅ Siz admin sifatida ro'yxatdan o'tdingiz. Endi barcha anonim "
        "murojaatlar shu chatga keladi."
    )


async def relay_to_admin_or_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message is None:
        return

    chat_id = update.effective_chat.id
    admin_id = get_admin_chat_id()

    # --- Admin yozyapti ---
    if admin_id and chat_id == admin_id:
        if message.reply_to_message:
            student_chat_id = lookup_student(message.reply_to_message.message_id)
            if student_chat_id is None:
                await message.reply_text(
                    "Bu xabar juda eski yoki topilmadi, javobni yubora olmadim."
                )
                return
            try:
                await message.copy(chat_id=student_chat_id)
                await message.reply_text("✅ Javobingiz anonim tarzda yuborildi.")
            except Exception as e:
                log.exception("Javobni yuborishda xato")
                await message.reply_text(f"❌ Yuborilmadi: {e}")
        else:
            await message.reply_text(
                "Bu xabarni o'quvchiga yuborish uchun murojaat xabariga "
                "'Reply' qilib yozing."
            )
        return

    # --- O'quvchi yozyapti (yoki admin hali ro'yxatdan o'tmagan) ---
    if not admin_id:
        await message.reply_text(
            "Bot hali to'liq sozlanmagan, birozdan so'ng qayta urinib ko'ring."
        )
        return

    try:
        copied = await message.copy(
            chat_id=admin_id,
            caption="🆕 Yangi anonim murojaat" if message.caption else None,
        )
        if not message.caption and not message.text:
            pass
        remember_mapping(copied.message_id, chat_id)
        await message.reply_text(
            "✅ Murojaatingiz anonim tarzda yetkazildi. Javob kelsa, shu yerda "
            "ko'rasiz."
        )
    except Exception:
        log.exception("Adminga yuborishda xato")
        await message.reply_text("❌ Yuborishda xatolik yuz berdi, qayta urining.")


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - botni boshlash\n"
        "Xabar yozsangiz, u anonim tarzda ustozga yuboriladi."
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("register", register_admin))
    app.add_handler(MessageHandler(~filters.COMMAND, relay_to_admin_or_reply))

    log.info("Bot ishga tushdi (polling)...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

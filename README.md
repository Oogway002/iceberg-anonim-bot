# ICEBERG Anonim Murojaat Bot

Bot: **@iceberg_anonim_bot**

O'quvchilar botga yozadi -> xabar sizga (ustozga) kim yozganini ko'rsatmasdan
yetib boradi. Siz o'sha xabarga "Reply" qilib javob yozsangiz, javobingiz
xuddi shu (lekin siz bilmaydigan) o'quvchiga qaytadi.

Bot hech qachon o'quvchining ismini, username'ini yoki ID raqamini sizga
ko'rsatmaydi — bu ma'lumot faqat server ichida (`data/mapping.json` faylida)
javobni to'g'ri joyga yuborish uchun vaqtincha saqlanadi, chatda chiqmaydi.

## 1-qadam: Botni ishga tushirish (kompyuteringizda yoki serverda)

```bash
pip install -r requirements.txt
python3 bot.py
```

`.env` faylida token va maxfiy kod allaqachon tayyor:

```
BOT_TOKEN=8997446215:AAHpwfQGjYaZnxERjo2FNRDSnyeBGPKjj8s
ADMIN_PASSCODE=iceberg2026
```

> Xohlasangiz `ADMIN_PASSCODE` ni boshqa so'zga almashtiring — bu kodni
> faqat SIZ bilishingiz kerak, chunki shu kod orqali "admin" (javoblarni
> ko'radigan odam) bo'lib ro'yxatdan o'tiladi.

## 2-qadam: O'zingizni admin qilib belgilash

Bot ishga tushgach, Telegram'da **@iceberg_anonim_bot** ga shaxsan o'zingiz
yozing:

```
/register iceberg2026
```

Shundan keyin barcha anonim murojaatlar shu chatingizga kela boshlaydi.
(Bu faqat bir marta bajariladi — birinchi to'g'ri kod kiritgan odam admin
bo'lib qoladi.)

## 3-qadam: O'quvchilarga bot linkini tarqatish

O'quvchilaringizga shu linkni bering:

**https://t.me/iceberg_anonim_bot**

Ular botga /start bosib, keyin xabarini yozishi kifoya.

## Javob berish

Sizga kelgan har bir anonim xabarni ushlab turib **Reply** qiling va
javobingizni yozing — bot buni avtomatik ravishda o'sha (noma'lum)
o'quvchiga yetkazadi.

## Botni doimiy (24/7) ishlatish

Yuqoridagi buyruq botni faqat terminal ochiq turgan vaqtda ishlaydi.
Doimiy ishlashi uchun uni biror serverga qo'yish kerak, masalan:

- **Railway.app**, **Render.com** yoki **Fly.io** — bepul/arzon tarif bilan
  Python skriptni doimiy ishga tushirish mumkin ("Background Worker" /
  "Worker" turini tanlang, `python3 bot.py` ni start command qiling,
  `BOT_TOKEN` va `ADMIN_PASSCODE` ni "Environment Variables" bo'limiga
  qo'shing).
- O'zingizda doimiy ishlaydigan Windows/Linux kompyuter yoki VPS bo'lsa,
  shunchaki `python3 bot.py` ni fon rejimida (masalan `screen` yoki
  `systemd` yordamida) ishga tushirsangiz bo'ladi.

Agar xohlasangiz, qaysi platformaga joylashni tanlab bering — men
qadam-baqadam ko'rsataman (masalan Railway yoki Render'ga ro'yxatdan
o'tib, shu kodni joylashtirish).

## Xavfsizlik eslatmasi

`BOT_TOKEN` — bu botni to'liq boshqarish kaliti. Uni hech kimga bermang
va GitHub kabi ochiq joyga yuklamang.

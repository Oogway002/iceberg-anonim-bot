# ICEBERG Anonim Murojaat Bot

Bot: **@iceberg_anonim_bot**
Manba kodi: https://github.com/Oogway002/iceberg-anonim-bot
Hosting: **Render.com** (bepul "Web Service" tarifida, webhook rejimida)

O'quvchilar botga yozadi -> xabar sizga (ustozga) kim yozganini ko'rsatmasdan
yetib boradi. Siz o'sha xabarga "Reply" qilib javob yozsangiz, javobingiz
xuddi shu (lekin siz bilmaydigan) o'quvchiga qaytadi.

Bot hech qachon o'quvchining ismini, username'ini yoki ID raqamini sizga
ko'rsatmaydi — bu ma'lumot faqat server ichida (`data/mapping.json` faylida)
javobni to'g'ri joyga yuborish uchun vaqtincha saqlanadi, chatda chiqmaydi.

## Muhim: `BOT_TOKEN` endi faylda emas

Xavfsizlik uchun `.env` fayli **ochiq (public) repoga yuklanmadi**. Token va
parol Render dashboard'ida "Environment Variables" bo'limida saqlanadi:

```
BOT_TOKEN=8997446215:AAHpwfQGjYaZnxERjo2FNRDSnyeBGPKjj8s
ADMIN_PASSCODE=iceberg2026
```

Lokal kompyuterda sinab ko'rmoqchi bo'lsangiz, shu ikki qatorni o'zingiz
`.env` nomli faylga yozib qo'ying (loyihaning asosiy papkasida, `bot.py`
bilan bir joyda).

## O'zingizni admin qilib belgilash

Bot ishga tushgach, Telegram'da **@iceberg_anonim_bot** ga shaxsan o'zingiz
yozing:

```
/register iceberg2026
```

Bot sizga Chat ID'ingizni ko'rsatadi — shuni nusxalab, Render'dagi
Environment Variables bo'limiga `ADMIN_CHAT_ID` nomi bilan qo'shib qo'ying
(bu ixtiyoriy, lekin server qayta ishga tushganda ham admin sifatida
qolishingizni kafolatlaydi).

Shundan keyin barcha anonim murojaatlar shu chatingizga kela boshlaydi.

## O'quvchilarga bot linkini tarqatish

**https://t.me/iceberg_anonim_bot**

Ular botga /start bosib, keyin xabarini yozishi kifoya.

## Javob berish

Sizga kelgan har bir anonim xabarni ushlab turib **Reply** qiling va
javobingizni yozing — bot buni avtomatik ravishda o'sha (noma'lum)
o'quvchiga yetkazadi.

## Hosting haqida eslatma (bepul tarif)

Render'ning bepul "Web Service" tarifi ~15 daqiqa harakatsizlikdan so'ng
"uxlab qoladi". O'quvchi xabar yozganda Telegram serverlari botni avtomatik
"uyg'otadi" — faqat birinchi xabar biroz (10-50 soniya) kechikishi mumkin,
undan keyin tezroq ishlaydi. Bu pulsiz yechim uchun normal holat.

## Xavfsizlik eslatmasi

`BOT_TOKEN` — bu botni to'liq boshqarish kaliti. Uni hech kimga bermang.
Shu sababli u ochiq GitHub repoga emas, faqat Render'ning maxfiy
Environment Variables bo'limiga qo'yilgan.

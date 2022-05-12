from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

###
b1 = KeyboardButton('Өмірбаяны')
b2 = KeyboardButton('Балалары')
b3 = KeyboardButton('Вернуться вверх')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.row(b1, b2).add(b3)

###
m1 = KeyboardButton('Өмірбаяны')
m2 = KeyboardButton('Вернуться вверх')
kb_min = ReplyKeyboardMarkup(resize_keyboard=True)
kb_min.add(m1, m2)

###
b4 = KeyboardButton('Көлбай')
b5 = KeyboardButton('Бүріс')

kb_sh = ReplyKeyboardMarkup(resize_keyboard=True)
kb_sh.add(b4, b5)

###
b6 = KeyboardButton('Түгелбай')
b7 = KeyboardButton('Бекарыстан')
b8 = KeyboardButton('Жанарыстан')
b9 = KeyboardButton('Беркімбай')
b10 = KeyboardButton('Шегенбай')
b11 = KeyboardButton('Еркіш')
b12 = KeyboardButton('Бәжі')
b13 = KeyboardButton('Тән')
b14 = KeyboardButton('Кемелбай')
b15 = KeyboardButton('Мергенбай')

kb_bu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bu.row(b6, b7).row(b8, b9, b10).row(b11, b12, b13).row(b14, b15)

###
l1 = KeyboardButton('Жансугір')
l2 = KeyboardButton('Бисугір')
l3 = KeyboardButton('Серікбай')
l4 = KeyboardButton('Төпі')
l5 = KeyboardButton('Сатай')
l6 = KeyboardButton('Тезекбай')
l7 = KeyboardButton('Мұса')
l8 = KeyboardButton('Көжекбай')
l9 = KeyboardButton('Пірәлі')

kb_tu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tu.row(l1, l2).row(l3, l4, l5).row(l6, l7, l8).row(l9)

###
v1 = KeyboardButton('Көгенбай')
v2 = KeyboardButton('Налибай')
v3 = KeyboardButton('Қазыбый')
v4 = KeyboardButton('Насынбай')
v5 = KeyboardButton('Толаман')

kb_bek = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bek.row(v1, v2).row(v3, v4, v5)

###
f1 = KeyboardButton('Сатқанбай')
f2 = KeyboardButton('Жиренбай')
f3 = KeyboardButton('Әшірбай')

kb_jan = ReplyKeyboardMarkup(resize_keyboard=True)
kb_jan.add(f1).row(f2, f3)

###
d1 = KeyboardButton('Ертай')
d2 = KeyboardButton('Қошқарбай')
d3 = KeyboardButton('Дукенбай')
d4 = KeyboardButton('Үкібай')
d5 = KeyboardButton('Құтыбай')
d6 = KeyboardButton('Бексұлтан')

kb_ber = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ber.row(d1, d2).row(d3, d4, d5).row(d6)

###
a1 = KeyboardButton('Тұрсынбай')
a2 = KeyboardButton('Әйнек')
a3 = KeyboardButton('Қауқан')

kb_she = ReplyKeyboardMarkup(resize_keyboard=True)
kb_she.add(a1).row(a2, a3)

###
w1 = KeyboardButton('Жүсіпбек')
w2 = KeyboardButton('Есенбек')
w3 = KeyboardButton('Дүйсенбек')

kb_erk = ReplyKeyboardMarkup(resize_keyboard=True)
kb_erk.add(w1).row(w2, w3)

###
t1 = KeyboardButton('Тоқпақ')
t2 = KeyboardButton('Орымбет')
t3 = KeyboardButton('Раңбас')
t4 = KeyboardButton('Шәймен')
t5 = KeyboardButton('Өмірбек')

kb_bj = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bj.row(t1, t2).row(t3, t4, t5)

###
t6 = KeyboardButton('Данияр')

kb_ten = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ten.add(t6)

###
t7 = KeyboardButton('Нармағамбет')

kb_kem = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kem.add(t7)

###
t8 = KeyboardButton('Әбділда')

kb_mer = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mer.add(t8)

###
r1 = KeyboardButton('Әділбек')

kb_jan = ReplyKeyboardMarkup(resize_keyboard=True)
kb_jan.add(r1)

###
r2 = KeyboardButton('Түйебай')

kb_ser = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ser.add(r2)

###
r3 = KeyboardButton('Көжекбай')

kb_top = ReplyKeyboardMarkup(resize_keyboard=True)
kb_top.add(r3)

###
r4 = KeyboardButton('Мейірбек')

kb_mu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mu.add(r4)

###
r5 = KeyboardButton('Жүндібай')
r6 = KeyboardButton('Шағырбай')

kb_ko = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ko.row(r5, r6)

###
r7 = KeyboardButton('Батырбек')
r8 = KeyboardButton('Адырбек')

kb_pi = ReplyKeyboardMarkup(resize_keyboard=True)
kb_pi.row(r7, r8)

###
r9 = KeyboardButton('Топай')
r10 = KeyboardButton('Шанақ')
r11 = KeyboardButton('Сопыбек')
r12 = KeyboardButton('Жәрімбет')
r13 = KeyboardButton('Әшірбек')
r14 = KeyboardButton('Баһрам')

kb_na = ReplyKeyboardMarkup(resize_keyboard=True)
kb_na.row(r9, r10).row(r11, r12, r13).row(r14)

###
z1 = KeyboardButton('Әбіщ')
z2 = KeyboardButton('Қармақ')
z3 = KeyboardButton('Мәшім')

kb_nas = ReplyKeyboardMarkup(resize_keyboard=True)
kb_nas.add(z1).row(z2, z3)

###
x1 = KeyboardButton('Әлібек')
x2 = KeyboardButton('Сұлтанбек')
x3 = KeyboardButton('Сұлтанияр')
x4 = KeyboardButton('Бүркітбай')
x5 = KeyboardButton('Елтияр')

kb_tol = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tol.row(x1, x2).row(x3, x4, x5)

###
x6 = KeyboardButton('Оспан')

kb_sat = ReplyKeyboardMarkup(resize_keyboard=True)
kb_sat.add(x6)

###
x7 = KeyboardButton('Қалмағамбет')
x8 = KeyboardButton('Палмағамбет')

kb_esh = ReplyKeyboardMarkup(resize_keyboard=True)
kb_esh.row(x7, x8)

###
a1 = KeyboardButton('Берділбек')
a2 = KeyboardButton('Махамбет')
a3 = KeyboardButton('Абытхан')
a4 = KeyboardButton('Ахмет')
a5 = KeyboardButton('Құдабай')

kb_er = ReplyKeyboardMarkup(resize_keyboard=True)
kb_er.row(a1, a2).row(a3, a4, a5)

###
a6 = KeyboardButton('Тастен')
a7 = KeyboardButton('Шілтен')
a8 = KeyboardButton('Кәрібай')
a9 = KeyboardButton('Әбила')

kb_ko = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ko.row(a6, a7).row(a8, a9)

###
a10 = KeyboardButton('Султанбай')

kb_du = ReplyKeyboardMarkup(resize_keyboard=True)
kb_du.add(a10)

###
t1 = KeyboardButton('Байбосын')
t2 = KeyboardButton('Әлі')
t3 = KeyboardButton('Жабай')
t4 = KeyboardButton('Әлішер')

kb_ku = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ku.row(t1, t2).row(t3, t4)

###
t5 = KeyboardButton('Бектурған')
t6 = KeyboardButton('Нурсултан')

kb_beks = ReplyKeyboardMarkup(resize_keyboard=True)
kb_beks.row(t5, t6)

###
t7 = KeyboardButton('Ақбала')

kb_ai = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ai.add(t7)

###
t8 = KeyboardButton('Дуйсенхан')

kb_ju = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ju.add(t8)

###
t9 = KeyboardButton('Құттыбай')
t10 = KeyboardButton('Ермекбай')
t11 = KeyboardButton('Ақылхан')

kb_es = ReplyKeyboardMarkup(resize_keyboard=True)
kb_es.row(t9, t10).row(t11)

###
d1 = KeyboardButton('Едіге')
d2 = KeyboardButton('Марат')

kb_dus = ReplyKeyboardMarkup(resize_keyboard=True)
kb_dus.row(d1, d2)

###
d3 = KeyboardButton('Әуезбек')
d4 = KeyboardButton('Мұкарам')
d5 = KeyboardButton('Икрам')

kb_to = ReplyKeyboardMarkup(resize_keyboard=True)
kb_to.row(d3, d4).row(d5)

###
d6 = KeyboardButton('Жұмабек')

kb_ori = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ori.add(d6)

###
d7 = KeyboardButton('Темірхан')

kb_ra = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ra.add(d7)

###
d8 = KeyboardButton('Өміралі')

kb_omi = ReplyKeyboardMarkup(resize_keyboard=True)
kb_omi.add(d8)

###
d9 = KeyboardButton('Әшім')

kb_nar = ReplyKeyboardMarkup(resize_keyboard=True)
kb_nar.add(d9)

###
d10 = KeyboardButton('Ахмет')

kb_adi = ReplyKeyboardMarkup(resize_keyboard=True)
kb_adi.add(d10)

###
d11 = KeyboardButton('Дәуіт')
d12 = KeyboardButton('Мырзан')
d13 = KeyboardButton('Дәулет')
d14 = KeyboardButton('Жұмабек')

kb_mei = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mei.row(d11, d12).row(d13, d14)

###
d15 = KeyboardButton('Бейсен')

kb_jun = ReplyKeyboardMarkup(resize_keyboard=True)
kb_jun.add(d15)

###
d16 = KeyboardButton('Дүйсенбек')
d17 = KeyboardButton('Оразалы')
d18 = KeyboardButton('Құрбанәлі')

kb_sha = ReplyKeyboardMarkup(resize_keyboard=True)
kb_sha.row(d16, d17).add(d18)

###
d19 = KeyboardButton('Байман')
d20 = KeyboardButton('Тутқабек')
d21 = KeyboardButton('Датқабек')
d22 = KeyboardButton('Қуандық')
d23 = KeyboardButton('Жұмабай')

kb_bat = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bat.row(d19, d20).row(d21, d22, d23)

###
d24 = KeyboardButton('Сейтомар')

kb_adr = ReplyKeyboardMarkup(resize_keyboard=True)
kb_adr.add(d24)

###
d25 = KeyboardButton('Қорғанбек')
d26 = KeyboardButton('Дүйсенбек')
d27 = KeyboardButton('Әсілбек')
d28 = KeyboardButton('Сапарбек')

kb_topa = ReplyKeyboardMarkup(resize_keyboard=True)
kb_topa.row(d25, d26).row(d27, d28)

###
d29 = KeyboardButton('Әбибілла')

kb_sha = ReplyKeyboardMarkup(resize_keyboard=True)
kb_sha.add(d29)

###
d30 = KeyboardButton('Өмірбек')
d31 = KeyboardButton('Райымбек')

kb_so = ReplyKeyboardMarkup(resize_keyboard=True)
kb_so.row(d30, d31)

###
d32 = KeyboardButton('Қияс')
d33 = KeyboardButton('Тұрғанбек')

kb_ash = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ash.row(d32, d33)

###
d34 = KeyboardButton('Сейтжан')
d35 = KeyboardButton('Дүйсенбі')

kb_ab = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ab.row(d34, d35)

###
d36 = KeyboardButton('Әбі')
d37 = KeyboardButton('Әбдікерім')
d38 = KeyboardButton('Есмагамбет')

kb_ma = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ma.row(d36, d37).row(d38)

###
d39 = KeyboardButton('Қайырбек')
d40 = KeyboardButton('Ғауһарбек')
d41 = KeyboardButton('Бөрібек')
d42 = KeyboardButton('Сабырбек')
d43 = KeyboardButton('Сапарбек')

kb_el = ReplyKeyboardMarkup(resize_keyboard=True)
kb_el.row(d39, d40).row(d41, d42, d43)

###
d44 = KeyboardButton('Жұмадилла')

kb_os = ReplyKeyboardMarkup(resize_keyboard=True)
kb_os.add(d44)

###
d45 = KeyboardButton('Хасен')
d46 = KeyboardButton('Әсілхан')
d47 = KeyboardButton('Антош')

kb_kal = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kal.row(d45, d46).add(d47)

###
d48 = KeyboardButton('Қайрат')

kb_pal = ReplyKeyboardMarkup(resize_keyboard=True)
kb_pal.add(d48)

###
d49 = KeyboardButton('Әбілқайыр')
d50 = KeyboardButton('Әбдіхалық')
d51 = KeyboardButton('Әбдіқама')
d52 = KeyboardButton('Мәжит')
d53 = KeyboardButton('Шәкір')

kb_ber = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ber.row(d49, d50).row(d51, d52, d53)
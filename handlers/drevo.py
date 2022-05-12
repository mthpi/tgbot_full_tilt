from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboard import *

class FSMshej(StatesGroup):
    s1 = State()
    s2 = State()
    s3 = State()
    s4 = State()
    s5 = State()

    n1 = State()
    n2 = State()
    n3 = State()
    n4 = State()
    n5 = State()
    n6 = State()
    n7 = State()
    n8 = State()
    n9 = State()
    n10 = State()

    o1 = State()
    o2 = State()
    o3 = State()
    o4 = State()
    o5 = State()
    o6 = State()
    o7 = State()
    o8 = State()
    o9 = State()
    o10 = State()

    u1 = State()
    u2 = State()
    u3 = State()
    u4 = State()
    u5 = State()
    u6 = State()
    u7 = State()
    u8 = State()
    u9 = State()
    u10 = State()
    u11 = State()
    u12 = State()
    u13 = State()
    u14 = State()
    u15 = State()
    u16 = State()
    u17 = State()
    u18 = State()
    u19 = State()
    u20 = State()
    u21 = State()
    u22 = State()
    u23 = State()
    u24 = State()
    u25 = State()
    u26 = State()
    u27 = State()
    u28 = State()
    u29 = State()
    u30 = State()
    u31 = State()
    u32 = State()
    u33 = State()
    u34 = State()
    u35 = State()
    u36 = State()
    u37 = State()

    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State()
    q8 = State()
    q9 = State()
    q10 = State()
    q11 = State()
    q12 = State()
    q13 = State()
    q14 = State()
    q15 = State()
    q16 = State()
    q17 = State()
    q18 = State()
    q19 = State()
    q20 = State()
    q21 = State()
    q22 = State()
    q23 = State()
    q24 = State()
    q25 = State()

    c1 = State()
    c2 = State()
    c3 = State()
    c4 = State()
    c5 = State()
    c6 = State()
    c7 = State()
    c8 = State()
    c9 = State()
    c10 = State()
    c11 = State()
    c12 = State()
    c13 = State()
    c14 = State()
    c15 = State()
    c16 = State()
    c17 = State()
    c18 = State()
    c19 = State()
    c20 = State()
    c21 = State()
    c22 = State()
    c23 = State()
    c24 = State()
    c25 = State()
    c26 = State()
    c27 = State()
    c28 = State()
    c29 = State()
    c30 = State()
    c31 = State()
    c32 = State()
    c33 = State()
    c34 = State()
    c35 = State()
    c36 = State()
    c37 = State()
    c38 = State()
    c39 = State()
    c40 = State()
    c41 = State()
    c42 = State()
    c43 = State()
    c44 = State()
    c45 = State()
    c46 = State()
    c47 = State()
    c48 = State()
    c49 = State()
    c50 = State()
    c51 = State()
    c52 = State()
    c53 = State()
    c54 = State()
    c55 = State()






#@dp.message_handlers(commands='start', state=None)
async def shanshar(message: types.Message):
    await bot.send_message(message.from_user.id, 'Шаншар', reply_markup=kb)
    await FSMshej.s1.set()


#@dp.message_handlers(text='Вернуться вверх', state=None)
async def shanshar_1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Шаншар', reply_markup=kb)
    await FSMshej.s1.set()



#@dp.message_handlers(text='Балалары', state=FSMshej.s1)
async def s1(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Шаншар Балалары:', reply_markup=kb_sh)
    await FSMshej.s2.set()



#@dp.message_handlers(text='Бүріс', state=FSMshej.s2)
async def s2(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Бүріс', reply_markup=kb)
    await FSMshej.s3.set()

#@dp.message_handlers(text='Көлбай', state=FSMshej.s2)
async def s3(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Көлбай', reply_markup=kb_min)
    await FSMshej.s4.set()


#@dp.message_handlers(text='Балалары', state=FSMshej.s3)
async def s4(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Бүріс Балалары:', reply_markup=kb_bu)
    await FSMshej.s5.set()



##############
#@dp.message_handlers(text='Түгелбай', state=FSMshej.s5)
async def k1(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Түгелбай', reply_markup=kb)
    await FSMshej.n1.set()

#@dp.message_handlers(text='Бекарыстан', state=FSMshej.s5)
async def k2(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Бекарыстан', reply_markup=kb)
    await FSMshej.n2.set()

#@dp.message_handlers(text='Жанарыстан', state=FSMshej.s5)
async def k3(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Жанарыстан', reply_markup=kb)
    await FSMshej.n3.set()

#@dp.message_handlers(text='Беркімбай', state=FSMshej.s5)
async def k4(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Беркімбай', reply_markup=kb)
    await FSMshej.n4.set()

#@dp.message_handlers(text='Шегенбай', state=FSMshej.s5)
async def k5(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Шегенбай', reply_markup=kb)
    await FSMshej.n5.set()

#@dp.message_handlers(text='Еркіш', state=FSMshej.s5)
async def k6(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Еркіш', reply_markup=kb)
    await FSMshej.n6.set()

#@dp.message_handlers(text='Бәжі', state=FSMshej.s5)
async def k7(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Бәжі', reply_markup=kb)
    await FSMshej.n7.set()

#@dp.message_handlers(text='Тән', state=FSMshej.s5)
async def k8(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Тән', reply_markup=kb)
    await FSMshej.n8.set()

#@dp.message_handlers(text='Кемелбай', state=FSMshej.s5)
async def k9(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Кемелбай', reply_markup=kb)
    await FSMshej.n9.set()

#@dp.message_handlers(text='Мергенбай', state=FSMshej.s5)
async def k10(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Мергенбай', reply_markup=kb)
    await FSMshej.n10.set()
###########


#@dp.message_handlers(text='Балалары', state=FSMshej.n1)
async def p1(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Түгелбай Балалары:', reply_markup=kb_tu)
    await FSMshej.o1.set()


#@dp.message_handlers(text='Балалары', state=FSMshej.n2)
async def p2(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Бекарыстан Балалары:', reply_markup=kb_bek)
    await FSMshej.o2.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.n3)
async def p3(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Жанарыстан Балалары:', reply_markup=kb_jan)
    await FSMshej.o3.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.n4)
async def p4(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Беркімбай Балалары:', reply_markup=kb_ber)
    await FSMshej.o4.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.n5)
async def p5(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Шегенбай Балалары:', reply_markup=kb_she)
    await FSMshej.o5.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.n6)
async def p6(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Еркіш Балалары:', reply_markup=kb_er)
    await FSMshej.o6.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.n7)
async def p7(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Бәжі Балалары:', reply_markup=kb_bj)
    await FSMshej.o7.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.n8)
async def p8(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Тән Балалары:', reply_markup=kb_ten)
    await FSMshej.o8.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.n9)
async def p9(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Кемелбай Балалары:', reply_markup=kb_kem)
    await FSMshej.o9.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.n10)
async def p10(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Мергенбай Балалары:', reply_markup=kb_mer)
    await FSMshej.o10.set()
########

#@dp.message_handlers(text='Жансугір', state=FSMshej.o1)
async def h1(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Жансугір', reply_markup=kb)
    await FSMshej.u1.set()

#@dp.message_handlers(text='Бисугір', state=FSMshej.o1)
async def h2(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Бисугір', reply_markup=kb_min)

#@dp.message_handlers(text='Серікбай', state=FSMshej.o1)
async def h3(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Серікбай', reply_markup=kb)
    await FSMshej.u3.set()

#@dp.message_handlers(text='Төпі', state=FSMshej.o1)
async def h4(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Төпі', reply_markup=kb)
    await FSMshej.u4.set()

#@dp.message_handlers(text='Сатай', state=FSMshej.o1)
async def h5(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Сатай', reply_markup=kb_min)

#@dp.message_handlers(text='Тезекбай', state=FSMshej.o1)
async def h6(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Тезекбай', reply_markup=kb_min)

#@dp.message_handlers(text='Мұса', state=FSMshej.o1)
async def h7(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Мұса', reply_markup=kb)
    await FSMshej.u7.set()

#@dp.message_handlers(text='Көжекбай', state=FSMshej.o1)
async def h8(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Көжекбай', reply_markup=kb)
    await FSMshej.u8.set()

#@dp.message_handlers(text='Пірәлі', state=FSMshej.o1)
async def h9(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Пірәлі', reply_markup=kb)
    await FSMshej.u9.set()


#@dp.message_handlers(text='Көгенбай', state=FSMshej.o2)
async def h10(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Көгенбай', reply_markup=kb_min)

#@dp.message_handlers(text='Налибай', state=FSMshej.o2)
async def h11(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Налибай', reply_markup=kb)
    await FSMshej.u11.set()

#@dp.message_handlers(text='Қазыбый', state=FSMshej.o2)
async def h12(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Қазыбый', reply_markup=kb_min)

#@dp.message_handlers(text='Насынбай', state=FSMshej.o2)
async def h13(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Насынбай', reply_markup=kb)
    await FSMshej.u13.set()

#@dp.message_handlers(text='Толаман', state=FSMshej.o2)
async def h14(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Толаман', reply_markup=kb)
    await FSMshej.u14.set()



#@dp.message_handlers(text='Сатқанбай', state=FSMshej.o3)
async def h15(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Сатқанбай', reply_markup=kb)
    await FSMshej.u15.set()

#@dp.message_handlers(text='Жиренбай', state=FSMshej.o3)
async def h16(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Жиренбай', reply_markup=kb_min)

#@dp.message_handlers(text='Әшірбай', state=FSMshej.o3)
async def h17(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әшірбай', reply_markup=kb)
    await FSMshej.u17.set()



#@dp.message_handlers(text='Ертай', state=FSMshej.o4)
async def h18(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Ертай', reply_markup=kb)
    await FSMshej.u18.set()

#@dp.message_handlers(text='Қошқарбай', state=FSMshej.o4)
async def h19(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Қошқарбай', reply_markup=kb)
    await FSMshej.u19.set()

#@dp.message_handlers(text='Дукенбай', state=FSMshej.o4)
async def h20(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Дукенбай', reply_markup=kb)
    await FSMshej.u20.set()

#@dp.message_handlers(text='Үкібай', state=FSMshej.o4)
async def h21(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Үкібай', reply_markup=kb_min)

#@dp.message_handlers(text='Құтыбай', state=FSMshej.o4)
async def h22(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Құтыбай', reply_markup=kb)
    await FSMshej.u22.set()

#@dp.message_handlers(text='Бексұлтан', state=FSMshej.o4)
async def h23(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Бексұлтан', reply_markup=kb)
    await FSMshej.u23.set()



#@dp.message_handlers(text='Тұрсынбай', state=FSMshej.o5)
async def h24(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Тұрсынбай', reply_markup=kb_min)

#@dp.message_handlers(text='Әйнек', state=FSMshej.o5)
async def h25(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әйнек', reply_markup=kb)
    await FSMshej.u25.set()

#@dp.message_handlers(text='Қауқан', state=FSMshej.o5)
async def h26(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Қауқан', reply_markup=kb_min)



#@dp.message_handlers(text='Жүсіпбек', state=FSMshej.o6)
async def h27(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Жүсіпбек', reply_markup=kb)
    await FSMshej.u27.set()

#@dp.message_handlers(text='Есенбек', state=FSMshej.o6)
async def h28(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Есенбек', reply_markup=kb)
    await FSMshej.u28.set()

#@dp.message_handlers(text='Дүйсенбек', state=FSMshej.o6)
async def h29(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Дүйсенбек', reply_markup=kb)
    await FSMshej.u29.set()



#@dp.message_handlers(text='Тоқпақ', state=FSMshej.o7)
async def h30(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Тоқпақ', reply_markup=kb)
    await FSMshej.u30.set()

#@dp.message_handlers(text='Орымбет', state=FSMshej.o7)
async def h31(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Орымбет', reply_markup=kb)
    await FSMshej.u31.set()

#@dp.message_handlers(text='Раңбас', state=FSMshej.o7)
async def h32(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Раңбас', reply_markup=kb)
    await FSMshej.u32.set()

#@dp.message_handlers(text='Шәймен', state=FSMshej.o7)
async def h33(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Шәймен', reply_markup=kb_min)

#@dp.message_handlers(text='Өмірбек', state=FSMshej.o7)
async def h34(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Өмірбек', reply_markup=kb)
    await FSMshej.u34.set()



#@dp.message_handlers(text='Данияр', state=FSMshej.o8)
async def h35(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Данияр', reply_markup=kb_min)



#@dp.message_handlers(text='Нармағамбет', state=FSMshej.o9)
async def h36(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Нармағамбет', reply_markup=kb)
    await FSMshej.u36.set()


#@dp.message_handlers(text='Әбділда', state=FSMshej.o10)
async def h37(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әбділда', reply_markup=kb_min)
#######


#@dp.message_handlers(text='Балалары', state=FSMshej.u1)
async def g1(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Жансугір Балалары:', reply_markup=kb_jan)
    await FSMshej.q1.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u3)
async def g2(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Серікбай Балалары:', reply_markup=kb_ser)
    await FSMshej.q2.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u4)
async def g3(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Төпі Балалары:', reply_markup=kb_top)
    await FSMshej.q3.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u7)
async def g4(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Мұса Балалары:', reply_markup=kb_mu)
    await FSMshej.q4.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u8)
async def g5(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Көжекбай Балалары:', reply_markup=kb_ko)
    await FSMshej.q5.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u9)
async def g6(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Пірәлі Балалары:', reply_markup=kb_pi)
    await FSMshej.q6.set()



#@dp.message_handlers(text='Балалары', state=FSMshej.u11)
async def g7(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Налибай Балалары:', reply_markup=kb_na)
    await FSMshej.q7.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u13)
async def g8(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Насынбай Балалары:', reply_markup=kb_nas)
    await FSMshej.q8.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u14)
async def g9(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Толаман Балалары:', reply_markup=kb_tol)
    await FSMshej.q9.set()



#@dp.message_handlers(text='Балалары', state=FSMshej.u15)
async def g10(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Сатқанбай Балалары:', reply_markup=kb_sat)
    await FSMshej.q10.set()


#@dp.message_handlers(text='Балалары', state=FSMshej.u17)
async def g11(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әшірбай Балалары:', reply_markup=kb_esh)
    await FSMshej.q11.set()


#@dp.message_handlers(text='Балалары', state=FSMshej.u18)
async def g12(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Ертай Балалары:', reply_markup=kb_er)
    await FSMshej.q12.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u19)
async def g13(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Қошқарбай Балалары:', reply_markup=kb_ko)
    await FSMshej.q13.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u20)
async def g14(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Дукенбай Балалары:', reply_markup=kb_du)
    await FSMshej.q14.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u22)
async def g15(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Құтыбай Балалары:', reply_markup=kb_ku)
    await FSMshej.q15.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u23)
async def g16(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Бексұлтан Балалары:', reply_markup=kb_beks)
    await FSMshej.q16.set()



#@dp.message_handlers(text='Балалары', state=FSMshej.u25)
async def g17(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әйнек Балалары:', reply_markup=kb_ai)
    await FSMshej.q17.set()



#@dp.message_handlers(text='Балалары', state=FSMshej.u27)
async def g18(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Жүсіпбек Балалары:', reply_markup=kb_ju)
    await FSMshej.q18.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u28)
async def g19(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Есенбек Балалары:', reply_markup=kb_es)
    await FSMshej.q19.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u29)
async def g20(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Дүйсенбек Балалары:', reply_markup=kb_dus)
    await FSMshej.q20.set()



#@dp.message_handlers(text='Балалары', state=FSMshej.u30)
async def g21(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Тоқпақ Балалары:', reply_markup=kb_to)
    await FSMshej.q21.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u31)
async def g22(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Орымбет Балалары:', reply_markup=kb_ori)
    await FSMshej.q22.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u32)
async def g23(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Раңбас Балалары:', reply_markup=kb_ra)
    await FSMshej.q23.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u34)
async def g24(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Өмірбек Балалары:', reply_markup=kb_omi)
    await FSMshej.q24.set()

#@dp.message_handlers(text='Балалары', state=FSMshej.u36)
async def g25(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Нармағамбет Балалары:', reply_markup=kb_nar)
    await FSMshej.q25.set()




##################
#@dp.message_handlers(text='Әділбек', state=FSMshej.q1)
async def y1(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әділбек', reply_markup=kb)
    await FSMshej.c1.set()

#@dp.message_handlers(text='Түйебай', state=FSMshej.q2)
async def y2(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Түйебай', reply_markup=kb_min)

#@dp.message_handlers(text='Көжекбай', state=FSMshej.q3)
async def y3(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Көжекбай', reply_markup=kb_min)

#@dp.message_handlers(text='Мейірбек', state=FSMshej.q4)
async def y4(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Мейірбек', reply_markup=kb)
    await FSMshej.c4.set()

#@dp.message_handlers(text='Жүндібай', state=FSMshej.q5)
async def y5(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Жүндібай', reply_markup=kb)
    await FSMshej.c5.set()

#@dp.message_handlers(text='Шағырбай', state=FSMshej.q5)
async def y6(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Шағырбай', reply_markup=kb)
    await FSMshej.c6.set()

#@dp.message_handlers(text='Батырбек', state=FSMshej.q6)
async def y7(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Батырбек', reply_markup=kb)
    await FSMshej.c7.set()

#@dp.message_handlers(text='Адырбек', state=FSMshej.q6)
async def y8(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Адырбек', reply_markup=kb)
    await FSMshej.c8.set()


#@dp.message_handlers(text='Топай', state=FSMshej.q7)
async def y9(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Топай', reply_markup=kb)
    await FSMshej.c9.set()

#@dp.message_handlers(text='Шанақ', state=FSMshej.q7)
async def y10(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Шанақ', reply_markup=kb)
    await FSMshej.c10.set()

#@dp.message_handlers(text='Сопыбек', state=FSMshej.q7)
async def y11(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Сопыбек', reply_markup=kb)
    await FSMshej.c11.set()

#@dp.message_handlers(text='Жәрімбет', state=FSMshej.q7)
async def y12(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Жәрімбет', reply_markup=kb_min)

#@dp.message_handlers(text='Әшірбек', state=FSMshej.q7)
async def y13(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әшірбек', reply_markup=kb)
    await FSMshej.c13.set()

#@dp.message_handlers(text='Баһрам', state=FSMshej.q7)
async def y14(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Баһрам', reply_markup=kb_min)

#@dp.message_handlers(text='Әбіщ', state=FSMshej.q8)
async def y15(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әбіщ', reply_markup=kb)
    await FSMshej.c15.set()

#@dp.message_handlers(text='Қармақ', state=FSMshej.q8)
async def y16(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Қармақ', reply_markup=kb_min)

#@dp.message_handlers(text='Мәшім', state=FSMshej.q8)
async def y17(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Мәшім', reply_markup=kb)
    await FSMshej.c17.set()

#@dp.message_handlers(text='Әлібек', state=FSMshej.q9)
async def y18(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әлібек', reply_markup=kb_min)

#@dp.message_handlers(text='Сұлтанбек', state=FSMshej.q9)
async def y19(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Сұлтанбек', reply_markup=kb_min)

#@dp.message_handlers(text='Сұлтанияр', state=FSMshej.q9)
async def y20(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Сұлтанияр', reply_markup=kb_min)

#@dp.message_handlers(text='Бүркітбай', state=FSMshej.q9)
async def y21(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Бүркітбай', reply_markup=kb_min)

#@dp.message_handlers(text='Елтияр', state=FSMshej.q9)
async def y22(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Елтияр', reply_markup=kb)
    await FSMshej.c22.set()




#@dp.message_handlers(text='Оспан', state=FSMshej.q10)
async def y23(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Оспан', reply_markup=kb)
    await FSMshej.c23.set()

#@dp.message_handlers(text='Қалмағамбет', state=FSMshej.q11)
async def y24(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Қалмағамбет', reply_markup=kb)
    await FSMshej.c24.set()

#@dp.message_handlers(text='Палмағамбет', state=FSMshej.q11)
async def y25(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Палмағамбет', reply_markup=kb)
    await FSMshej.c25.set()



#@dp.message_handlers(text='Берділбек', state=FSMshej.q12)
async def y26(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Берділбек', reply_markup=kb)
    await FSMshej.c26.set()

#@dp.message_handlers(text='Махамбет', state=FSMshej.q12)
async def y27(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Махамбет', reply_markup=kb)
    await FSMshej.c27.set()

#@dp.message_handlers(text='Абытхан', state=FSMshej.q12)
async def y28(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Абытхан', reply_markup=kb)
    await FSMshej.c28.set()

#@dp.message_handlers(text='Ахмет', state=FSMshej.q12)
async def y29(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Ахмет', reply_markup=kb_min)

#@dp.message_handlers(text='Құдабай', state=FSMshej.q12)
async def y30(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Құдабай', reply_markup=kb)
    await FSMshej.c30.set()

#@dp.message_handlers(text='Тастен', state=FSMshej.q13)
async def y31(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Тастен', reply_markup=kb)
    await FSMshej.c31.set()

#@dp.message_handlers(text='Шілтен', state=FSMshej.q13)
async def y32(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Шілтен', reply_markup=kb)
    await FSMshej.c32.set()

#@dp.message_handlers(text='Кәрібай', state=FSMshej.q13)
async def y33(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Кәрібай', reply_markup=kb)
    await FSMshej.c33.set()

#@dp.message_handlers(text='Әбила', state=FSMshej.q13)
async def y34(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әбила', reply_markup=kb)
    await FSMshej.c34.set()

#@dp.message_handlers(text='Султанбай', state=FSMshej.q14)
async def y35(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Султанбай', reply_markup=kb)
    await FSMshej.c35.set()

#@dp.message_handlers(text='Байбосын', state=FSMshej.q15)
async def y36(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Байбосын', reply_markup=kb)
    await FSMshej.c36.set()

#@dp.message_handlers(text='Әлі', state=FSMshej.q15)
async def y37(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әлі', reply_markup=kb)
    await FSMshej.c37.set()

#@dp.message_handlers(text='Жабай', state=FSMshej.q15)
async def y38(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Жабай', reply_markup=kb)
    await FSMshej.c38.set()

#@dp.message_handlers(text='Әлішер', state=FSMshej.q15)
async def y39(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әлішер', reply_markup=kb)
    await FSMshej.c39.set()

#@dp.message_handlers(text='Бектурған', state=FSMshej.q16)
async def y40(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Бектурған', reply_markup=kb)
    await FSMshej.c40.set()

#@dp.message_handlers(text='Нурсултан', state=FSMshej.q16)
async def y41(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Нурсултан', reply_markup=kb)
    await FSMshej.c41.set()


#@dp.message_handlers(text='Ақбала', state=FSMshej.q17)
async def y42(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Ақбала', reply_markup=kb)
    await FSMshej.c42.set()


#@dp.message_handlers(text='Дуйсенхан', state=FSMshej.q18)
async def y43(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Дуйсенхан', reply_markup=kb)
    await FSMshej.c43.set()

#@dp.message_handlers(text='Құттыбай', state=FSMshej.q19)
async def y44(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Құттыбай', reply_markup=kb)
    await FSMshej.c44.set()

#@dp.message_handlers(text='Ермекбай', state=FSMshej.q19)
async def y45(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Ермекбай', reply_markup=kb)
    await FSMshej.c45.set()

#@dp.message_handlers(text='Ақылхан', state=FSMshej.q19)
async def y46(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Ақылхан', reply_markup=kb)
    await FSMshej.c46.set()

#@dp.message_handlers(text='Едіге', state=FSMshej.q20)
async def y47(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Едіге', reply_markup=kb)
    await FSMshej.c47.set()

#@dp.message_handlers(text='Марат', state=FSMshej.q20)
async def y48(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Марат', reply_markup=kb_min)



#@dp.message_handlers(text='Әуезбек', state=FSMshej.q21)
async def y49(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әуезбек', reply_markup=kb_min)

#@dp.message_handlers(text='Мұкарам', state=FSMshej.q21)
async def y50(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Мұкарам', reply_markup=kb_min)

#@dp.message_handlers(text='Икрам', state=FSMshej.q21)
async def y51(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Икрам', reply_markup=kb_min)

#@dp.message_handlers(text='Жұмабек', state=FSMshej.q22)
async def y52(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Жұмабек', reply_markup=kb)
    await FSMshej.c52.set()

#@dp.message_handlers(text='Темірхан', state=FSMshej.q23)
async def y53(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Темірхан', reply_markup=kb_min)

#@dp.message_handlers(text='Өміралі', state=FSMshej.q24)
async def y54(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Өміралі', reply_markup=kb)
    await FSMshej.c54.set()

#@dp.message_handlers(text='Әшім', state=FSMshej.q25)
async def y55(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әшім', reply_markup=kb_min)



#############
#@dp.message_handlers(text='Балалары', state=FSMshej.c1)
async def w1(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әділбек Балалары:', reply_markup=kb_adi)

#@dp.message_handlers(text='Балалары', state=FSMshej.c4)
async def w2(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Мейірбек Балалары:', reply_markup=kb_mei)

#@dp.message_handlers(text='Балалары', state=FSMshej.c5)
async def w3(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Жүндібай Балалары:', reply_markup=kb_jun)

#@dp.message_handlers(text='Балалары', state=FSMshej.c6)
async def w4(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Шағырбай Балалары:', reply_markup=kb_sha)

#@dp.message_handlers(text='Балалары', state=FSMshej.c7)
async def w5(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Батырбек Балалары:', reply_markup=kb_bat)

#@dp.message_handlers(text='Балалары', state=FSMshej.c8)
async def w6(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Адырбек Балалары:', reply_markup=kb_adr)

#@dp.message_handlers(text='Балалары', state=FSMshej.c9)
async def w7(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Топай Балалары:', reply_markup=kb_topa)

#@dp.message_handlers(text='Балалары', state=FSMshej.c10)
async def w8(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Шанақ Балалары:', reply_markup=kb_sha)

#@dp.message_handlers(text='Балалары', state=FSMshej.c11)
async def w9(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Сопыбек Балалары:', reply_markup=kb_so)

#@dp.message_handlers(text='Балалары', state=FSMshej.c13)
async def w10(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әшірбек Балалары:', reply_markup=kb_ash)

#@dp.message_handlers(text='Балалары', state=FSMshej.c15)
async def w11(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Әбіщ Балалары:', reply_markup=kb_ab)

#@dp.message_handlers(text='Балалары', state=FSMshej.c17)
async def w12(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Мәшім Балалары:', reply_markup=kb_ma)

#@dp.message_handlers(text='Балалары', state=FSMshej.c22)
async def w13(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Елтияр Балалары:', reply_markup=kb_el)

#@dp.message_handlers(text='Балалары', state=FSMshej.c23)
async def w14(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Оспан Балалары:', reply_markup=kb_os)

#@dp.message_handlers(text='Балалары', state=FSMshej.c24)
async def w15(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Қалмағамбет Балалары:', reply_markup=kb_kal)

#@dp.message_handlers(text='Балалары', state=FSMshej.c25)
async def w16(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Палмағамбет Балалары:', reply_markup=kb_pal)

#@dp.message_handlers(text='Балалары', state=FSMshej.c26)
async def w17(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Берділбек Балалары:', reply_markup=kb_ber)



def register_handlers_drevo(dp : Dispatcher):
    dp.register_message_handler(shanshar, commands='start', state="*")
    dp.register_message_handler(shanshar_1, text='Вернуться вверх', state="*")
    dp.register_message_handler(s1, text='Балалары', state=FSMshej.s1)
    dp.register_message_handler(s2, text='Бүріс', state=FSMshej.s2)
    dp.register_message_handler(s3, text='Көлбай', state=FSMshej.s2)
    dp.register_message_handler(s4, text='Балалары', state=FSMshej.s3)

    dp.register_message_handler(k1, text='Түгелбай', state=FSMshej.s5)
    dp.register_message_handler(k2, text='Бекарыстан', state=FSMshej.s5)
    dp.register_message_handler(k3, text='Жанарыстан', state=FSMshej.s5)
    dp.register_message_handler(k4, text='Беркімбай', state=FSMshej.s5)
    dp.register_message_handler(k5, text='Шегенбай', state=FSMshej.s5)
    dp.register_message_handler(k6, text='Еркіш', state=FSMshej.s5)
    dp.register_message_handler(k7, text='Бәжі', state=FSMshej.s5)
    dp.register_message_handler(k8, text='Тән', state=FSMshej.s5)
    dp.register_message_handler(k9, text='Кемелбай', state=FSMshej.s5)
    dp.register_message_handler(k10, text='Мергенбай', state=FSMshej.s5)

    dp.register_message_handler(p1, text='Балалары', state=FSMshej.n1)
    dp.register_message_handler(p2, text='Балалары', state=FSMshej.n2)
    dp.register_message_handler(p3, text='Балалары', state=FSMshej.n3)
    dp.register_message_handler(p4, text='Балалары', state=FSMshej.n4)
    dp.register_message_handler(p5, text='Балалары', state=FSMshej.n5)
    dp.register_message_handler(p6, text='Балалары', state=FSMshej.n6)
    dp.register_message_handler(p7, text='Балалары', state=FSMshej.n7)
    dp.register_message_handler(p8, text='Балалары', state=FSMshej.n8)
    dp.register_message_handler(p9, text='Балалары', state=FSMshej.n9)
    dp.register_message_handler(p10, text='Балалары', state=FSMshej.n10)

    dp.register_message_handler(h1, text='Жансугір', state=FSMshej.o1)
    dp.register_message_handler(h2, text='Бисугір', state=FSMshej.o1)
    dp.register_message_handler(h3, text='Серікбай', state=FSMshej.o1)
    dp.register_message_handler(h4, text='Төпі', state=FSMshej.o1)
    dp.register_message_handler(h5, text='Сатай', state=FSMshej.o1)
    dp.register_message_handler(h6, text='Тезекбай', state=FSMshej.o1)
    dp.register_message_handler(h7, text='Мұса', state=FSMshej.o1)
    dp.register_message_handler(h8, text='Көжекбай', state=FSMshej.o1)
    dp.register_message_handler(h9, text='Пірәлі', state=FSMshej.o1)
    dp.register_message_handler(h10, text='Көгенбай', state=FSMshej.o2)
    dp.register_message_handler(h11, text='Налибай', state=FSMshej.o2)
    dp.register_message_handler(h12, text='Қазыбый', state=FSMshej.o2)
    dp.register_message_handler(h13, text='Насынбай', state=FSMshej.o2)
    dp.register_message_handler(h14, text='Толаман', state=FSMshej.o2)
    dp.register_message_handler(h15, text='Сатқанбай', state=FSMshej.o3)
    dp.register_message_handler(h16, text='Жиренбай', state=FSMshej.o3)
    dp.register_message_handler(h17, text='Әшірбай', state=FSMshej.o3)
    dp.register_message_handler(h18, text='Ертай', state=FSMshej.o4)
    dp.register_message_handler(h19, text='Қошқарбай', state=FSMshej.o4)
    dp.register_message_handler(h20, text='Дукенбай', state=FSMshej.o4)
    dp.register_message_handler(h21, text='Үкібай', state=FSMshej.o4)
    dp.register_message_handler(h22, text='Құтыбай', state=FSMshej.o4)
    dp.register_message_handler(h23, text='Бексұлтан', state=FSMshej.o4)
    dp.register_message_handler(h24, text='Тұрсынбай', state=FSMshej.o5)
    dp.register_message_handler(h25, text='Әйнек', state=FSMshej.o5)
    dp.register_message_handler(h26, text='Қауқан', state=FSMshej.o5)
    dp.register_message_handler(h27, text='Жүсіпбек', state=FSMshej.o6)
    dp.register_message_handler(h28, text='Есенбек', state=FSMshej.o6)
    dp.register_message_handler(h29, text='Дүйсенбек', state=FSMshej.o6)
    dp.register_message_handler(h30, text='Тоқпақ', state=FSMshej.o7)
    dp.register_message_handler(h31, text='Орымбет', state=FSMshej.o7)
    dp.register_message_handler(h32, text='Раңбас', state=FSMshej.o7)
    dp.register_message_handler(h33, text='Шәймен', state=FSMshej.o7)
    dp.register_message_handler(h34, text='Өмірбек', state=FSMshej.o7)
    dp.register_message_handler(h35, text='Данияр', state=FSMshej.o8)
    dp.register_message_handler(h36, text='Нармағамбет', state=FSMshej.o9)
    dp.register_message_handler(h37, text='Әбділда', state=FSMshej.o10)

    dp.register_message_handler(g1, text='Балалары', state=FSMshej.u1)
    dp.register_message_handler(g2, text='Балалары', state=FSMshej.u3)
    dp.register_message_handler(g3, text='Балалары', state=FSMshej.u4)
    dp.register_message_handler(g4, text='Балалары', state=FSMshej.u7)
    dp.register_message_handler(g5, text='Балалары', state=FSMshej.u8)
    dp.register_message_handler(g6, text='Балалары', state=FSMshej.u9)
    dp.register_message_handler(g7, text='Балалары', state=FSMshej.u11)
    dp.register_message_handler(g8, text='Балалары', state=FSMshej.u13)
    dp.register_message_handler(g9, text='Балалары', state=FSMshej.u14)
    dp.register_message_handler(g10, text='Балалары', state=FSMshej.u15)
    dp.register_message_handler(g11, text='Балалары', state=FSMshej.u17)
    dp.register_message_handler(g12, text='Балалары', state=FSMshej.u18)
    dp.register_message_handler(g13, text='Балалары', state=FSMshej.u19)
    dp.register_message_handler(g14, text='Балалары', state=FSMshej.u20)
    dp.register_message_handler(g15, text='Балалары', state=FSMshej.u22)
    dp.register_message_handler(g16, text='Балалары', state=FSMshej.u23)
    dp.register_message_handler(g17, text='Балалары', state=FSMshej.u25)
    dp.register_message_handler(g18, text='Балалары', state=FSMshej.u27)
    dp.register_message_handler(g19, text='Балалары', state=FSMshej.u28)
    dp.register_message_handler(g20, text='Балалары', state=FSMshej.u29)
    dp.register_message_handler(g21, text='Балалары', state=FSMshej.u30)
    dp.register_message_handler(g22, text='Балалары', state=FSMshej.u31)
    dp.register_message_handler(g23, text='Балалары', state=FSMshej.u32)
    dp.register_message_handler(g24, text='Балалары', state=FSMshej.u34)
    dp.register_message_handler(g25, text='Балалары', state=FSMshej.u36)

    dp.register_message_handler(y1, text='Әділбек', state=FSMshej.q1)
    dp.register_message_handler(y2, text='Түйебай', state=FSMshej.q2)
    dp.register_message_handler(y3, text='Көжекбай', state=FSMshej.q3)
    dp.register_message_handler(y4, text='Мейірбек', state=FSMshej.q4)
    dp.register_message_handler(y5, text='Жүндібай', state=FSMshej.q5)
    dp.register_message_handler(y6, text='Шағырбай', state=FSMshej.q5)
    dp.register_message_handler(y7, text='Батырбек', state=FSMshej.q6)
    dp.register_message_handler(y8, text='Адырбек', state=FSMshej.q6)
    dp.register_message_handler(y9, text='Топай', state=FSMshej.q7)
    dp.register_message_handler(y10, text='Шанақ', state=FSMshej.q7)
    dp.register_message_handler(y11, text='Сопыбек', state=FSMshej.q7)
    dp.register_message_handler(y12, text='Жәрімбет', state=FSMshej.q7)
    dp.register_message_handler(y13, text='Әшірбек', state=FSMshej.q7)
    dp.register_message_handler(y14, text='Баһрам', state=FSMshej.q7)
    dp.register_message_handler(y15, text='Әбіщ', state=FSMshej.q8)
    dp.register_message_handler(y16, text='Қармақ', state=FSMshej.q8)
    dp.register_message_handler(y17, text='Мәшім', state=FSMshej.q8)
    dp.register_message_handler(y18, text='Әлібек', state=FSMshej.q9)
    dp.register_message_handler(y19, text='Сұлтанбек', state=FSMshej.q9)
    dp.register_message_handler(y20, text='Сұлтанияр', state=FSMshej.q9)
    dp.register_message_handler(y21, text='Бүркітбай', state=FSMshej.q9)
    dp.register_message_handler(y22, text='Елтияр', state=FSMshej.q9)
    dp.register_message_handler(y23, text='Оспан', state=FSMshej.q10)
    dp.register_message_handler(y24, text='Қалмағамбет', state=FSMshej.q11)
    dp.register_message_handler(y25, text='Палмағамбет', state=FSMshej.q11)
    dp.register_message_handler(y26, text='Берділбек', state=FSMshej.q12)
    dp.register_message_handler(y27, text='Махамбет', state=FSMshej.q12)
    dp.register_message_handler(y28, text='Абытхан', state=FSMshej.q12)
    dp.register_message_handler(y29, text='Ахмет', state=FSMshej.q12)
    dp.register_message_handler(y30, text='Құдабай', state=FSMshej.q12)
    dp.register_message_handler(y31, text='Тастен', state=FSMshej.q13)
    dp.register_message_handler(y32, text='Шілтен', state=FSMshej.q13)
    dp.register_message_handler(y33, text='Кәрібай', state=FSMshej.q13)
    dp.register_message_handler(y34, text='Әбила', state=FSMshej.q13)
    dp.register_message_handler(y35, text='Султанбай', state=FSMshej.q14)
    dp.register_message_handler(y36, text='Байбосын', state=FSMshej.q15)
    dp.register_message_handler(y37, text='Әлі', state=FSMshej.q15)
    dp.register_message_handler(y38, text='Жабай', state=FSMshej.q15)
    dp.register_message_handler(y39, text='Әлішер', state=FSMshej.q15)
    dp.register_message_handler(y40, text='Бектурған', state=FSMshej.q16)
    dp.register_message_handler(y41, text='Нурсултан', state=FSMshej.q16)
    dp.register_message_handler(y42, text='Ақбала', state=FSMshej.q17)
    dp.register_message_handler(y43, text='Дуйсенхан', state=FSMshej.q18)
    dp.register_message_handler(y44, text='Құттыбай', state=FSMshej.q19)
    dp.register_message_handler(y45, text='Ермекбай', state=FSMshej.q19)
    dp.register_message_handler(y46, text='Ақылхан', state=FSMshej.q19)
    dp.register_message_handler(y47, text='Едіге', state=FSMshej.q20)
    dp.register_message_handler(y48, text='Марат', state=FSMshej.q20)
    dp.register_message_handler(y49, text='Әуезбек', state=FSMshej.q21)
    dp.register_message_handler(y50, text='Мұкарам', state=FSMshej.q21)
    dp.register_message_handler(y51, text='Икрам', state=FSMshej.q21)
    dp.register_message_handler(y52, text='Жұмабек', state=FSMshej.q22)
    dp.register_message_handler(y53, text='Темірхан', state=FSMshej.q23)
    dp.register_message_handler(y54, text='Өміралі', state=FSMshej.q24)
    dp.register_message_handler(y55, text='Әшім', state=FSMshej.q25)
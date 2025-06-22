# x = int(input('your age: '))
# if x <= 16:
#     raise TypeError('siz hali 18 yoshga tolmagansiz') # raise xatolik yaratadi

# try:
#     a = int(input('your age: '))
# except:
#     print('raqam kiriting: ')

'''
    MEHMON XONA DASTURI

    BOLIM:
    TANLASH
        MEHMON QOSHISH
        ROYXATDAN OCHIRISH
        MEHMONLAR ROYXATI
        DASTURDAN CHIQISH
    HAR BIR FOYDALANUVCHI MALUMOTLARI
        ISMI
        XONASI
        XONA TURI
'''
# mehmonlar = [
#     {"ism": "Ali", "xona": 101, "turi": "Lyuks"},
#     {"ism": "Zuhra", "xona": 202, "turi": "Oddiy"}
# ]
#
# def menyu():
#     print("""
#     1 - Mehmon qo‘shish
#     2 - Ro‘yxatdan o‘chirish
#     3 - Mehmonlar ro‘yxati
#     4 - Dasturdan chiqish
#     """)
#
# def ismlar():
#     return [mehmon["ism"] for mehmon in mehmonlar]
#
# def qoshish():
#     while True:
#             ism = input("Ismi: ")
#
#             # Xona raqamini faqat raqamlardan iborat qilib tekshirish
#             xona = input("Xona raqami: ")
#             if not xona.isdigit():
#                 print("Xato! Xona raqami faqat raqamlardan iborat bo‘lishi kerak.")
#                 continue
#
#             # Xona turini to‘g‘ri kiritish
#             turi = input("Xona turi (lyuks/oddiy): ").lower()
#             if turi not in ["lyuks", "oddiy"]:
#                 print("Xato! Faqat 'lyuks' yoki 'oddiy' deb kiriting.")
#                 continue
#
#             # Hammasi to‘g‘ri bo‘lsa, tsikldan chiqish
#             break
#
#     mehmonlar.append({"ism": ism, "xona": xona, "turi": turi})
#     print(f"{ism} mehmon qo‘shildi!")
#
# def ochirish():
#     ism = input("O‘chirish uchun mehmon ismi: ").capitalize()
#     for mehmon in mehmonlar:
#         if mehmon["ism"] == ism:
#             mehmonlar.remove(mehmon)
#             print(f"{ism} o‘chirildi!")
#             return
#     print("Bu ismli mehmon topilmadi!")
#
# def royxat():
#     if not mehmonlar:
#         print("Hozircha mehmonlar yo‘q!")
#     for m in mehmonlar:
#         print(f"{m['ism']} - Xona: {m['xona']} - {m['turi']}")
#
# while True:
#     menyu()
#     try:
#         tanlov = int(input("Tanlang: "))
#     except ValueError:
#         print("Iltimos, raqam kiriting!")
#         continue
#
#     if tanlov == 1:
#         qoshish()
#     elif tanlov == 2:
#         ochirish()
#     elif tanlov == 3:
#         royxat()
#     elif tanlov == 4:
#         print("Dasturdan chiqildi!")
#         break
#     else:
#         print("Noto‘g‘ri tanlov! Qayta urinib ko‘ring.")






a = int(input())
for i in range(0,5):
    print(i**2)





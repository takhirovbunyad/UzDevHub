#royxat = ['assalom' , 'beker' , 'vouv' , 'dorime' , 'thanos' , 'jjk']
''''''
'''
Lug'atni yangilash: Har bir string uzunligi uchun, lug'atdagi kalit sifatida bu uzunlikni ishlatamiz va shu uzunlikdagi stringni lug'atga qo'shamiz.

Ma
1.royxatni olish
2.uni ichidagi elementlar uzunligini topish
3.kattadan kichikgacha royxatlash
4.dictga kochirish tenglash

def create_dict(a, b):
    result = {}
    for i in range(len(a)):
        result[a[i]] = b[i]
    return result

a = [1, 2, 3]
b = ['a', 'b', 'c']
result_dict = create_dict(a, b)
print(result_dict)


listbox = ['nmadyr1', 'ssalomamerika', 'a']
# print(strcounter(listbox))
Y
2. Bir xil uzunlikdagi ikkita listni parametr sifatida oladigan, kalitlar birinchi ro'yxatning 
elementlari va qiymatlar ikkinchi ro'yxatning mos keladigan elementlari bo'lgan dict qaytaradigan merge_list(l1,l2) funksiya yarating.
M: list_1 = ["a", "b", "c"] 
   list_2 = [1, 2, 3]  	
   merge_list(list_1 ,list_2)  -> {"a":1, "b":2, "c":3}




hehe1 = ['a', 'b', 'c']
hehe2 = [1, 2, 3]
result={}
for i in range(len(hehe1)):
    result[hehe1[i]] = hehe2[i]
# print(result)
'''


# def show_contacts(contacts):
#     """Barcha kontaktlarni ko'rsatadi."""
#     if contacts:
#         print("Kontaktlar ro'yxati:")
#         for name, phone in contacts.items():
#             print(f"{name}: {phone}")
#     else:
#         print("Kontaktlar mavjud emas.")
#
#
# def add_contact(contacts, name, phone):
#     """Yangi kontakt qo'shadi."""
#     if name in contacts:
#         print(f"{name} allaqachon mavjud.")
#     else:
#         contacts[name] = phone
#         print(f"{name} kontaktlari qo'shildi.")
#
#
# def update_contact(contacts, name, phone):
#     """Mavjud kontaktni yangilaydi."""
#     if name in contacts:
#         contacts[name] = phone
#         print(f"{name} kontaktlari yangilandi.")
#     else:
#         print(f"{name} nomli kontakt mavjud emas.")
#
#
# def delete_contact(contacts, name):
#     """Kontaktni o'chiradi."""
#     if name in contacts:
#         del contacts[name]
#         print(f"{name} kontaktlari o'chirildi.")
#     else:
#         print(f"{name} nomli kontakt mavjud emas.")
#
#
# def search_contact(contacts, name):
#     """Kontaktni qidiradi."""
#     if name in contacts:
#         print(f"{name}: {contacts[name]}")
#     else:
#         print(f"{name} nomli kontakt mavjud emas.")
#
#
# # Asosiy dasturni yaratamiz:
# contacts = {"Nodir": "+998918602711", "Laziz": "+998908002534"}
#
# # Foydalanuvchi uchun menyu:
# while True:
#     print("\n1. Kontakt qo'shish")
#     print("2. Kontaktni yangilash")
#     print("3. Kontaktni o'chirish")
#     print("4. Kontaktni qidirish")
#     print("5. Barcha kontaktlarni ko'rish")
#     print("6. Dasturdan chiqish")
#
#     choice = input("Tanlovingizni kiriting (1-6): ")
#
#     if choice == "1":
#         name = input("Kontakt nomini kiriting: ")
    #     phone = input("Telefon raqamini kiriting: ")
    #     add_contact(contacts, name, phone)
    # elif choice == "2":
    #     name = input("Yangilash uchun kontakt nomini kiriting: ")
    #     phone = input("Yangi telefon raqamini kiriting: ")
#         update_contact(contacts, name, phone)
#     elif choice == "3":
#         name = input("Ochirish uchun kontakt nomini kiriting: ")
#         delete_contact(contacts, name)
#     elif choice == "4":
#         name = input("Qidirilayotgan kontakt nomini kiriting: ")
#         search_contact(contacts, name)
#     elif choice == "5":
#         show_contacts(contacts)
#     elif choice == "6":
#         print("Dasturdan chiqilmoqda...")
#         break
#     else:
#         print("Notogi tanlov! Iltimos, qaytadan urinib ko'ring.")
#


def counter_dict(nums):
    natija = {}
    for son in nums:
        if son in natija:
            natija[son] += 1
        else:
            natija[son] = 1
    return natija

# Sinov
# print(counter_dict([2, 1, 1, 1]))  # {2: 1, 1: 3}


def max_ball_students(talabalar):
    ballar = list(talabalar.values())  # Barcha ballarni olish
    ballar.sort()  # Tartiblash
    eng_yaxshi1, eng_yaxshi2 = ballar[-1], ballar[-2]  # Eng katta ikkita ballni olish

    eng_yaxshilar = {}
    for ism, ball in talabalar.items():
        if ball == eng_yaxshi1 or ball == eng_yaxshi2:
            eng_yaxshilar[ism] = ball

    return eng_yaxshilar

# Sinov
# print(max_ball_students({"Akmal": 634, "Tohir": 55, "Nodir": 76, "Zafar": 80}))

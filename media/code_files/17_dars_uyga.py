# # def keyingi_tub(): # funksiya yaratish funksiya nomi
# #     tub_sonlar = []
# #     n = 2 # Eng kichik tub son
# #     while True:
# #         if all(n % tub != 0 for tub in tub_sonlar):
# #             tub_sonlar.append(n)
# #             yield n
# #         n += 1
# #
# # tub_iterator = keyingi_tub()
# #
# # for _ in range(10):
# #     print(next(tub_iterator))
#
#
# import random
#
# a = input('yozing: ')  # Input (masalan 'xyz')
# b = int(input('nechi marta generatsia qilasiz: '))
# '''generatiya'''
# for i in range(b):  # 3 marta generatsiya qilish uchun
#     forrand = list(a)  # Stringni listga aylantiramiz
#     random.shuffle(forrand)  # Aralashtiramiz
#     it = iter(forrand)  # Listni iteratorga aylantiramiz
#     print([next(it) for _ in range(len(forrand))])  # 3 ta harfni avtomatik chiqaramiz
#
# def fibonacci():
#     fib = [0,1]
#     while True:
#         yield fib[0]
#         fib.append(fib[-1] + fib[-2])
#         # fib.pop(0)
#         fib.remove(fib[0])
# # Fibonacci generatorini yaratamiz
# fib = fibonacci()
# a = int(input('nechta fibonacci son kerak:'))
# for _ in range(a):  # 10 ta Fibonacci sonini chiqarish
#     print(next(fib))





c
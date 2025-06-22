'''
'''''''
arena 256 kv
pool 4 kv
free pool ishlatib boshatilgan boladi
block kattaligi har hil
'''
'''
shallow copy
'''
# a = [1]
# b = a.copy()
# b = b.append(2)
# print(a) # bu yerdac ishlaydi lekin

# a = [1, [2]]
# b = a.copy()
# b[1].append(3) #buyerda ishlamaydi bu yereda b ni ozgartirdik lekin baribir a oizgardi
# print(a)
'''
2 ni b ga qoshgdik lekin a ham ozgardi
deep copy
'''
# from copy import deepcopy
# a = [1 , [2]]
# b = deepcopy(a)
# b[1].append(3)
# print(a)
'''
bu yerda ozgarmayapti a boshidagidek!!!'''

# d = {
#     'ism':'abdujabbor',
#     'davlat' : 'uzb'
# }
# # d2 = dict(ism='abdujavbbir' , davlat='uzb') #parametr orqali tenglash
# d['ball']   =   [1 , 3 , 2 ] # bu d ichiga 1 , 3, 2 sonlar listini qoshadi
# print(d)
# d3 = dict([('ism','abdujabbor') , ('davlat' , 'uzb')])
# print(d3)
# print(d2)
# print(d)

'''
dictda ikkita key kirkizsak bittasini oladi va oxirigisini lekin value unday emas
'''

'''

update metodi ikkita dictni EXTEND kabi qoshadi

aq = {
    'ism':1,
    'familya':2,
}
aw = {
    'yosh':3,
    'sharif':4,
}
aq.update(aw)
print(aq)
'''

'''del'''
deleted = {1:1 , 2:2}
del deleted[1]
# print(deleted)

'''POPITEM bu oxiridagi key va val# poperkurva = {1:1 , 2:2}
# h = poperkurva.popitem()
# print(poperkurva) 
# 
ueni olib tashlaydi'''


a = {'mashina':'lambo' , 'davlat':'amerikaaa'}
m = a.pop('davlat')
# print(a)
# print(m)


new = a.get('moshina' , 'keynotfound fuxker' )# birinchi nmani qidirish ikkinchi nmaga tenglab qoshish
# yoki nooooonedeyish xolaganni yozsa bolad
# agar kiritilgan soz xato bolssa nonr=e chiqadi yani bittasini tanla moshin ni chiqaerish yoki none moshinnni chiqaromiman deme none

'''setdrefault()  ni get dan farqi shundaki get agar toposa ikkinchisini chiqaradi  a setdafault bosa topomasa ikkinchiga tenglab qoyadi yani ikkinchisiga tenglaydi va osha narsa qoshiladi!!!'''
newset = a.setdefault('moshin' , 'mashina')
# print(newset , a)

# print(new)
# print(list(a.keys()))




'''counter funksiyasi'''
from collections import Counter
counter = Counter(a.keys())
# print(counter)
'''
['mashina', 'moshin']
Counter({'mashina': 1, 'moshin': 1})
 mana javob bu yerda nashu=ina 1 ta kelgan moshi ham u shuni sanagan
'''

# aw2 = [1,1,1,1,1,1]
# print(Counter(aw2))
'''defaultdict agar soralgan key bolmasa [] ni ozini qaytaradi'''
from collections import defaultdict

a = defaultdict(list) #boshqa type qoyish mumkin
# print(a['this is input'])

''''
setni indexi yoq undagi elementlar bilan ishlab bolmaydi unda elementlr takrorlanmaydi loekin element qoshish yoki ollish mumkin
'''
'''setga 1 bilan true qoyib bolmaydi chunki 1 degani ham true
setni indexi yoq bolgani uchun sikldan foydalanish kerak
setdaham update ishlaydi
discard narsani ochiradi agar u yoq bolsa hatolik bermaydi
'''

settbox = {1 , 2 , 3}

settbox.discard(1)
# print(settbox)
'''  koplab metodlar w2schoolsda  '''

#
# set1 = {1,2,3}
# set2 = {'s' , 'b' , 'v' , 1.3632}
# print(set1.union(set2))

'''intersation_update() '''
x= {1,2,3,4,5}
c1 = {1,3,3764}
#x.intersection_update(c1)# buda x ga tenglab oladi
# s = x.intersection(c1) # buda esa bitta ozgaruvchigfa tenglash kk
# print(s)

'''symmetrik_difference_update - bu ikkalasida ham qatnashmaganini oladi'''
x.symmetric_difference_update(c1) # bundaxam x ga temglayapti yangi yaratmayapti
print(x)




























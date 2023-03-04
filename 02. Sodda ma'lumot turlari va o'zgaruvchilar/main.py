## DARS REJASI ##

# 1. O'zgaruvchilar.
# 2. O'zgaruvchi nomlari.
# 3. "string" ma'lumot turi.
# 4. Maxsus belgilar.
# 5. Formatlangan string. "f-string".
# 6. String metodlari.
# 7. Raqamlar bilan ishlash. (integer, float, complex)
# 8. Boolean - mantiqiy qiymat.
# 9. Ma'lumot turini o'zgartirish.

###############################################################################################

#### 1.O'zgaruvchi. ####

# O'zgaruvchi - qiymat bilan bog'langan va qiymati o'zgartirilishi mumkin bo'lgan ramziy nom.

#### 2.O'zgaruvchi nomlari. ####

# 1. O'zgaruvchi nomlarida simvollardan qatnashishi mumkin emas!
# 2. O'zgaruvchilar nomlari raqamlar bilan boshlanmaydi!
# 3. O'zgaruvchi nomi o'rtasida bo'shliq "probel" qatnashmasligi kerak!

# To'g'ri berilgan!

# username = "John Doe"
# userNAME = "Alex Cross"
# user_name = "admin"
# _username = "admin2"

# Noto'g'ri berilgan!

# 1age = 12
# user&name = "admin"
# user name = "admin2"

#### 3."string" ma'lumot turi. ####

# String - belgilar ketma-ketligidir. U so'zlar yoki jumlalar kabi matnni saqlash uchun ishlatiladi. Satrlar qo'shtirnoq ichida (bitta yoki juft) olinadi.

# Satrli ma'lumotlarga misol:
# your_firstname = "Ozodbek"
# your_lastname = 'Yusupov'
# your_skills = """
# Python, Django
# Javascript, ReactJS
# Dart, Flutter
# """

# print(your_firstname)
# print(your_lastname)
# print(your_skills)

#### 4.Maxsus belgilar. ####

# Maxsus belgilar:
# one_error = 'O\'zbekiston'  # SyntaxError
# print(one_error)

# one_fixed = 'O\'zbekiston' # O'zbekiston

# two_1 = "Python"        # Python
# two_2 = "\tPython"      #       Python

# print(two_1)
# print(two_2)

# three_1 = "Django"               # Django
# three_2 = "Django\nFra\nme\nwo\nrk"    # Django
#                                  # Framework
    
# print(three_1)
# print(three_2)
    
# print("Python")
# print("Django", end="\r") # Kursorni boshiga qaytaradi!

#### 5.Formatlangan string. "f-string". ####

# # F-STRING. 1-metod:
# firstname = "Ozodbek"
# age = 22
# full_info = f"My name is {firstname}. My age: {age}"
# print(full_info) # My name is Ozodbek. My age: 22

# # format(). 2-metod:
# firstname = "Ozodbek"
# age = 22
# full_info = "My name is {}. My age: {}".format(firstname, age)
# print(full_info) # My name is Ozodbek. My age: 22

# # format(). 3-metod:
# full_info = "My name is {firstname}. My age: {age}".format(firstname="Ozodbek", age=22)
# print(full_info) # My name is Ozodbek. My age: 22

# # % belgisidan foydalanish:
# print("My name is %s. My age: %d" % ("Ozodbek", 22)) # My name is Ozodbek. My age: 22

#### 6.String metodlari. ####

# String metodlari:
# print("Uzbekistan".upper())              # UZBEKISTAN
# print("Uzbekistan".lower())              # uzbekistan
# print("python and django".capitalize())  # Python and django
# print("python and django".title())       # Python And Django
# print("Python and Django".split(" "))    # ["Python", "and", "Django"]
# print("     Python".lstrip())            # Python
# print("Python     ".rstrip())            # Python
# print("     Python     ".strip())        # Python
# print("".zfill(6))                       # 000000
# print("-".join("PYTHON"))                # P-Y-T-H-O-N
# print("HELLO".count("L"))                # 2
# print("HELLO".index("O"))                # 4
# print(len("HELLO"))                      # 5
# print("HELLO"[0:2])                      # HE
# print("HELLO"[0:])                       # HELLO
# print("HELLO"[:-1])                      # HELL
# print("PYTHON"[::2])                     # PTO
# print("PYTHON"[::-1])                    # NOHTYP

#### 7.Raqamlar bilan ishlash. [integer, float, complex] ####

# Raqamlar:

# Integer (Bugun sonlar):
# age = 22                # 22
# price = 20000 + 15000   # 35000

# Float (O'nlik sonlar):
# temp = 36.6             # 36.6
# pi = 3.1416             # 3.1416

# Complex (Murakkab sonlar):
# z = complex(3, 4)
# w = 3j + 2j

# print(type(z))          # complex
# print(z.real)           # 3.0
# print(z.imag)           # 4.0

#### 8.Boolean - mantiqiy qiymatlar. ####

# Mantiqiy qiymat (boolean):
# isCool = True
# isHot = False

# 2 < 3  # True
# 2 > 3  # False
# 2 == 3 # False
# 2 >= 3 # False
# 2 <= 3 # True
# 2 != 3 # True

#### 9.Ma'lumot turini o'zgartirish. ####

# Ma'lumot turini tekshirish:
# firstname = "Ozodbek"
# age = 22
# isMarried = False
# print(type(firstname))    # <class 'str'>
# print(type(age))          # <class 'int'>
# print(type(isMarried))    # <class 'bool'>

# Ma'lumot turini o'zgartirish:
# VARIABLE = 1
# print(str(VARIABLE))    # "1"
# print(int(VARIABLE))    # 1
# print(float(VARIABLE))  # 1.0
# print(bool(VARIABLE))   # True

###############################################################################################

# ism = input("Ismingiz nima?: ")
# familiya = input("familyangiz nima?: ")
# email = input("emailingizni kiriting")
# parol = input("parolni kiriting")
# print (ism,familiya,email,parol)

#  2 topshiriq

# 1) teng tomonli uchburchakning tomoni a ga teng uning yuzi s ni toping 
# from math import *
# a = float(input('teng tomonli uchburchak tomonini kiriting:'))
# s = pow(a,2)*sqrt(3/4)
# print(s)
# print()

# 2)a+3b bunda a = 5, b = 5 
# a = input('a ning qiymatini kiriting')
# b = input('b ning qiymatini kiriting')
# c = a+b
# print ()

# 3)
a = 5
b = 5
c = a + 3*b
print(c)

# 4)
a = 5
b = 6 
c = a**+2*a*b+b**2
print(c)
## DARS REJASI ##

# 1. ----
# 2. ----
# 3. ----
# 4. ----
# 5. ----
# 6. ----
# 7. ----

###############################################################################################
import random 

attemps = 0

myName  = input('ismingizni kiriting')
number = random.randint(1,48)
print('salom, men biror sonno taxmin qilayapman 1 va 40')

while attemps < 5:
    print('taxmin qiling')
    gueesed_number = int(input())
    attemps += 1 
       
    if gueesed_number < number:
      print("kiritilgan son men o'ylagandan kichikroq")
    if gueesed_number > number:
        print("kiritilgan son men o'ylaganda kattaroq")
    if gueesed_number == number:
        break 

if gueesed_number == number:
    print(myName, 'you found the in {}' . format(attemps))
if gueesed_number != number:
    print('you foiled the number is {}'. format(number))


# 2 feat


       
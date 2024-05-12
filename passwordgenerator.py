import random
password=[]
n1=int(input('How many Letters you want in your password?'))
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(n1):
    a=random.choice(list1)
    password.append(a)
n2=int(input('How many Symbols you want in your password?'))
list2=['!','@','#','$','%','^','&','*']
for j in range(n2):
    b=random.choice(list2)
    password.append(b)
n3=int(input('How many Numbers you want in your password?'))
list3=['1','2','3','4','5','6','7','8','9','0']
for k in range(n3):
    c=random.choice(list3)
    password.append(c)
level=input('Enter the Level of Password your want to be? [Easy or Hard]')
if level=='easy' or level=='Easy':
    for h in password:
        print(h,end="")
else:
    g=random.shuffle(password)
    for h in password:
        print(h,end="")

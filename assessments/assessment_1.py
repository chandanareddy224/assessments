#1
num=float(input("enter the number:"))
if num > 0:
    print(num,"is positive")
elif num < 0:
    print(num,"is negative")
else:
    print(num,"is not positive and negative")


  
#2
num=int(input("enter number:"))
if num == 0:
    print(num,"is neither even nor odd")
elif num < 0:
    print(num,"is negative")
else:
    if num%2!=0:
        print(num,"is even")
    else:
        print(num,"is odd")



num=int(input("enter the num:"))
for i in range(1,):

    if num < 0:
        print("Number is Negative")

    elif num == 0:
        print("0 is neither Odd nor Even")

    else:   
        if num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")

#3

for i in range(1,101):
    if i%2==0:
        print(i)

i=1
num=2
while i <= 50:
    print(num)
    num=num+2
    i=i+1


for i in range(2,101,2):
    print("even nums are",i)





#4

for i in range(1,100):
    if i%2 != 0:
        print(i)


i=1
num=1
while i <= 50:
    print(num)
    num=num+2
    i=i+1

for i in range (1,100,2):
    print("odd nums are",i)



#5
for i in range (100,1,-2):
    print(i)



num = 100
while num >= 2:
    print(num)
    num -= 2


count = 0
num = 100
while num >= 1:
    if num % 2 == 0:
        print(num)
        count += 1
    num -= 1
    if count == 50:
            break



#6

for i in range (99,0,-2):
    print(i)



num = 99
while num >= 1:
    print(num)
    num -= 2


count = 0
num = 100
while num >= 1:
    if num % 2 != 0:
        print(num)
        count += 1
    num -= 1
    if count == 50:
            break



#7

for i in range (0,21):
    print(i)




i=1
while i<=20:
    print(i)
    i+=1




n=int(input("enter value"))
for i in range(1,n+1):
    print(i)





#8

for i in range(20):
    print("index:", i, "number:", i+1)






#9

n=int(input("enter value"))
for i in range(0,n+1):
    print(i)



n=int(input("enter value"))
i=1
while i<=n:
     print(i)
     i+=1






n=int(input("enter value:"))
for i in range(n, 0, -1):
    print(i)



n= int(input("enter value"))
i=1
while i<=n:
    print(i)
    i+=1



n=int(input("enter value"))
while n>=1:
    print(n)
    n-=1

#25


a=(input("enter number:"))
b=0
for i in a:
    if i=='6' or i=='7':
        break
    b+=int(i)
print("sum is",b)



a=input("enter number:")
b=0
for i in a:
    b+=int(i)
print("sum is",b)




a=int(input("enter number b/w 0 & 50"))
if a>50:
    print("invalid input")
else:
    for i in range(0,51):
        if i == 10:
            continue
        print(i)


a=int(input("enter value"))
b=0
for i in range(1, a+1):
    b=b+2*i
print("sum",a, "numbers is",b  )



a=int(input("enter value"))
b=0
for i in range(1,a+1):
    b=b+2*i-1
print("sum of", a,"numbers is",b)



a=0
for i in range(1,101):
    a+=2*i
print(a)

a=0
for i in range (1,101):
    a+=2*i-1
print(a)



a=0
for i in range(1,21):
    a+=i
print(a)


a=int(input("enter value"))
b=0
for i in range(a, 0, -1):
    b=2*i
    print(b)




a=int(input("enter value"))
b=0
for i in range(a, 0, -1):
    b=2*i-1
    print(b)


a=int(input("enter value"))
b=0
for i in range(1,a+1):
    b=2*i
    print(b)




a=int(input("enter value"))
b=0
for i in range(1,a+1):
    b=2*i-1
    print(b)




#11
for i in range(20,0,-1): #if i put -1 instead of '0' then it will print from 20 to 0
    print(i)


#12

for i in range(-20,0): #if i put 1 instead of '0' then it will print from -20 to 0
    print(i)



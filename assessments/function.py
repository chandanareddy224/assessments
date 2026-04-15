def details():
    name="chandana"
    age=21
    college="sacet"
    email=input("enter your email:")
    phone=int(input("enter you mobile no.:"))

    print("name is", name , "age is", age , "collegename:",college , email, phone)






def even_or_odd():
    num=int(input("enter number:"))
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")




def leapyear_or_not():
    a=int(input("enter year:"))
    if a%4==0 or a%400==0:
        print(a,"is leap year")
    else:
        print(a,"is not a leap year")
leapyear_or_not()
details()

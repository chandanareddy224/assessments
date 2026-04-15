#1) wap to find positive & Negative number but 0 is not pos & Neg no. take i/p from user through keyboard.
def pos_or_neg(n):
    if n>0:
        print("Positive")
    elif n<0:
        print("Negative")
    else:
        print("Zero")

def pos_or_neg2(n):
    print("Positive" if n>0 else "Negative" if n<0 else "Zero")

n=int(input("enter your number:"))
pos_or_neg(n)
pos_or_neg2(n)


#2)wap to find only positive even, odd number, but 0 is not odd & even number, odd or even are Neg no, then display number is/are Negative. take 3 i/p from user.
def even_or_odd(n):
    if n<0: print("Negative")
    elif n==0: print("Zero")
    elif n%2==0: print("Even")
    else: print("Odd")

def even_or_odd2(n):
    print("Negative" if n<0 else ("Even" if n%2==0 and n!=0 else "Odd"))

n=int(input("enter your number:"))
even_or_odd(n)
even_or_odd2(n)


#3) wap to find first 50 Even numbers.

def even_numbers():
    for i in range(2,101,2):
        print(i)

def even_numbers2():
    for i in range(2,101):
        if i%2==0:
            print(i)
even_numbers()
even_numbers2()



#4) wap to find first 50 Odd numbers.
def odd_nos():
    for i in range(1,100,2):
        print(i)
        if i==47:
            break
         #print(i)

def odd_nos2():
    for i in range(1,100):
        if i%2!=0:
            print(i)

odd_nos()
#odd_nos2()




#5) print first 50 even number in reverse orders.

def even_reverse():
    for i in range(100,0,-2):
        print(i)

def even_reverse2():
    for i in range(100,0,-1):
        print(i%2==0)

even_reverse()
even_reverse2()

#6) print first 50 Odd numbers in reverse orders.
def odd_reverse():
    for i in range(99,0,-2):
        print(i)

def odd_reverse2():
    for i in range(99,0):
        print(i%2!=0)

odd_reverse()
odd_reverse2()

#7) print first 20 natural numbers.

def natural_numbers():
    for i in range(1,21):
        print(i)

natural_numbers()


#8) print first 20 natural numbers with index position.

def natural_index():
    for i in range(1,21):
        print("index:",i-1,"number:", i)

def natural_index2():
    for i in range(20):
       print("index:",i,"number:",i+1)

natural_index()
natural_index2()

#9) print N natural numbers in ascending order.

def natural_n(n):
    for i in range(1, n+1):
        print(i)

def natural_n2(n):
    i = 1
    while i <= n:
        print(i)
        i += 1

n = int(input("enter your number: "))

natural_n(n)
natural_n2(n)

#10) print first N natural numbers in reverse order.

def natural_n(n):
    i = n
    while i >= 1:
        print(i)
        i -= 1
def natural_n2(n):
    for i in range(n, 0, -1):
        print(i)

n = int(input("enter your number: "))

natural_n(n)
natural_n2(n)
#11) print first 20 positive numbers in reverse order. like 20 to 1 and 20 to 0.

def reverse_20():
    for i in range(20,0,-1):
        print(i)

reverse_20()

#12) print first 20 Negative numbers in reverse order like -20 to -1 and -20 to -0.

def negative_reverse():
    for i in range(-20,0):
        print(i)

negative_reverse()


#13) print first N even Natural numbers.

def even_n():
    n=int(input())
    for i in range(2,n*2+1,2):
        print(i)

def even_n2():
    a=int(input())
    for i in range(1,a+1):
        print(2*i)

even_n()
even_n2()

#14) print first N odd Natural numbers.

def odd_n():
    n=int(input())
    for i in range(1,n*2,2):
        print(i)

def odd_n2():
    a=int(input())
    b=0
    for i in range(1,a+1):
        b=2*i-1
        print(b)

odd_n()
odd_n2()

#15) print first N even Natural numbers in reverse order.

def even_rev_n():
    n=int(input())
    for i in range(n*2,0,-2):
        print(i)

def even_rev_n2():
    n=int(input())
    for i in range(n*2,0,-1):
        print(i%2==0)

even_rev_n()
even_rev_n2()

#16) print first N odd natural numbers in reverse order.

def odd_rev_n():
    n=int(input())
    for i in range(n*2-1,0,-2):
        print(i)

def odd_rev_n2():
    n=int(input())
    for i in range(n*2-1,0,-1):
        print(i%2!=0)

odd_rev_n()
odd_rev_n2()

#17) print sum of first 20 natural numbers.

def sum20():
    s=0
    for i in range(1,21):
        s+=i
    print(s)

def sum20_2():
    print(sum(range(1,21)))

sum20()
sum20_2()

#18)  print sum of first 100 even natural numbers

def sum_even():
    s=0
    for i in range(2,201,2):
        s+=i
    print(s)

def sum_even2():
    print(sum(i for i in range(2,201) if i%2==0))

sum_even()
sum_even2()

#19) print sum of first 100 odd natural numbers.

def sum_odd():
    s=0
    for i in range(1,200,2):
        s+=i
    print(s)

def sum_odd2():
    print(sum(i for i in range(1,200) if i%2!=0))

sum_odd()
sum_odd2()

#20) print sum of N Even natural numbers.
def sum_even_n():
    n=int(input())
    s=0
    for i in range(2,n*2+1,2):
        s+=i
    print(s)

def sum_even_n2():
    n=int(input())
    print(sum(i for i in range(1,n*2+1) if i%2==0))

sum_even_n()
sum_even_n2()
#21) print sum of N odd natural numbers.
def sum_odd_n():
    n=int(input())
    s=0
    for i in range(1,n*2,2):
        s+=i
    print(s)

def sum_odd_n2():
    n=int(input())
    print(sum(i for i in range(1,n*2) if i%2!=0))

sum_odd_n()
sum_odd_n2()

#22) wap to print 0 to 50 numbers, but user take any numbers of i/p.
def zero_n():
    n=int(input())
    for i in range(n+1):
        print(i)

def zero_n2():
    n=int(input())
    for i in range(n+1):
        print(i>=0)

zero_n()
zero_n2()

#23) wap to print 0 to 50 numbers but Do't display 10 no. user take i/p between 0 to 50. if user take i/p above 50 then display a message 
def skip10():
    n=int(input())
    if n>50:
        print("Invalid")
    else:
        for i in range(n+1):
            if i==10:
                continue
            print(i)

def skip10_2():
    n=int(input())
    for i in range(n+1):
        print(i!=10)

skip10()
skip10_2()

#24) Ask user a number like string "1234" calculate sume of digit e.g: 1+2+3+4 = 10 o/p
def sum_digits():
    a=input()
    b=0
    for i in a:
        b+=int(i)
    print(b)

def sum_digits2():
    a=input()
    print(sum(int(i) for i in a))

sum_digits()
sum_digits2()

#25) wap to calculate sume of digit, user given i/n "1234567", but 6 and 7 do not calculate. e.g=1+2+3+4+5=15 o/p
def skip67():
    a=input()
    b=0
    for i in a:
        if i=='6' or i=='7':
            continue
        b+=int(i)
    print(b)

def skip67_2():
    a=input()
    print(sum(int(i) for i in a if i not in ['6','7']))

skip67()
skip67_2()



#1) wap to find greater / smallest number, take multiple i/p from user. 
def gret_or_small(lst):
    print(max(lst), min(lst))

def gret_or_small2(lst):
    mx=mn=lst[0]
    for i in lst:
        if i>mx: mx=i
        if i<mn: mn=i
    print(mx, mn)

def main():
    lst=list(map(int,input().split()))
    gret_or_small(lst)
    gret_or_small2(lst)
main()
#2) wap to check greatest, smallest, equal, positive and negative numbers, take multiple i/p from user.
def m1(lst):
    print(max(lst), min(lst), all(i>=0 for i in lst))

def m2(lst):
    mx=max(lst); mn=min(lst)
    pos=all(i>=0 for i in lst)
    neg=any(i<0 for i in lst)
    print(mx,mn,pos,neg)

def main():
    lst=list(map(int,input().split()))
    m1(lst)
    m2(lst)
main()
#3) wap to check leap year or not leap year. take i/p from user. 
def m1(y):
    print(y%4==0 and (y%100!=0 or y%400==0))

def m2(y):
    print((y%400==0) or (y%4==0 and y%100!=0))

def main():
    y=int(input())
    m1(y)
    m2(y)
main()
#4) wap to check leap year or not leap yeaar, but negative is not accepted. take i/p from user.
def leapyr_or_not(y):
    if y<0:
        print("Invalid")
    else:
        print(y%4==0 and (y%100!=0 or y%400==0))

y=int(input())
leapyr_or_not(y)


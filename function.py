# import math

# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x

# print(my_abs(-100))



# if int(input())>100:
#     pass
# else:
#     print("aaa")




# def quadratic(a,b,c):
#     x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
#     x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
#     return (x1,x2)

# print('quadratic(2,3,1)=',quadratic(1,5,3))


# def person(name,age,city,job):
#     print(name,age,city,job)

# person('コウキンコウ',29,'TOKYO','IT')  


# def person(name,age,city='TOKYO',job='IT'):
#     print(name,age,city,job)


# person('コウキンコウ',29,job='MMM')  


# def calc(*numbers):
#     sum=0
#     for x in numbers:
#         sum=sum+x**2
#     return sum

# print("calc(1,2,3,4,5)=",calc(1,2,3,4,5))



# def f1(a,b,c=0,*args,**kw):
#     print("a=",a,"b=",b,"c=",c,"args=",args,"kw=",kw)


# def f2(a,b,c=0,*,d,**kw):
#     print("a=",a,"b=",b,"c=",c,"d=",d,"kw=",kw)




# f1(1,2,3,4,5,6,7,8,aa=11,bb=22)
# f2(1,2,d=3,aa=4,bb=5,cc=6)


# args=(1,2,3,4,5)
# kw={"aa":11,"bb":222}

# f1(args,kw)
# f1(*args,**kw)



def move(n,a,b,c):
    if n==1:
        print(a,"⇒",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(5,"A","B","C")
print("END")

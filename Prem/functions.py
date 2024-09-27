# # 1
# # def my_function():
# #     print ("print hello...")
# # my_function()


# # 2
# # def my_function(fname):
# #     print(fname + "Enter here")
# # my_function("Email ID ")
# # my_function("Mobile No ")
# # my_function("Location ")


# # 3
# # Parameters
# # def f(a,b,c):
# #     print("hello",a,b,c)
# # f(1,2,3,)


# # 4
# # keyword arguments
# # def f(**a):
# #     print("Hello",a)
# # f(a=1,b=2)


# # 5
# # Nested functions
# # def outer():
# #     print("Outer func")
# #     def inner():
# #         print("inner func")
# #     inner()    
# # outer()    

# # 6
# # def add(a,b):
# #     # print(a+b)
# #     return a+b
# # def sub(a,b):
# #     #print(a-b)    
# #     return a-3

# # 7
# # calculate
# # sum =10
# # def f():
# #     currentsum = 200
# #     totalsum = sum+currentsum
# #     print(totalsum)
# # f()

# # x = lambda a,b : a - b
# # print(x(100,25.5))

# # x = lambda a,b,c,d : a+b*c-d
# # print(x(100,20,10,5))

# def myfunc(mystr : str='africa',mynum : int=2000) -> str:
#     return f"{mystr} is {mynum}KM away from india"

# a =1

# def myfunc1(mystr='africa',mynum=2000) -> str:
#     global a 
#     a = 10

#     return f"{mystr} is {mynum}KM away from india"

# print(a)  

# print(myfunc1())
# print(myfunc1(mynum=4000))
# print(myfunc1(mynum=4000))


# def swap(a,b):
#     b = b + a
#     a = b - a
#     b = b - a
#     print(f"value of a is:{a}")
#     print(f"value of b is:{b}")
# swap(5,10) 
# swap(10,20)   
# swap(10205,15468)

# def mul(a,b):
#     x = a*b
#     print(f"Multiplication of a and b is {x}")
# mul(10,10) 
# mul(20,20)
# mul(30,30)   

# def div(x,y):
#     a=x/y
#     print(f"division of x and y is {a}")
# div(10,10)
# div(100,20)
# div(30,300)    


# l = [1,2,3,"prem"]
# print(l[-1])

# l = [1,2,3,4,5,6,7,8]
# call = l[4:8]
# print(call)

# fruits = ["car","bike","bycycle"]
# fruits[-1]="Truck"
# print(fruits) 

# l = [30,25,52,4,25,30,25,51,5]
# x=l.index(25)
# print(x)

inp = input().split()
l = [(int(item))**2 for item in inp]
print(l)
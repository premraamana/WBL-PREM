# 1.to remove duplicates from sorted arrays 

# def remove_duplicates(sorted_array):
#      unique_array = []
    
#       for element in sorted_array:
#         if element not in unique_array:
#             unique_array.append(element)
    
#     return unique_array
# sorted_array = [1, 1, 2, 2, 3, 4, 4, 5]
# unique_array = remove_duplicates(sorted_array)
# print("Array after removing duplicates:", unique_array)

# --------------------------------------------------------------------------------------

# Another way to getting unique_aray from the sorted_array

# nums = [1,1,2,2,3,4,4,5,6,6]
# def removeDuplicates(arr):
#     prev_num = arr[0]
#     emptyarr = []
#     emptyarr.append(prev_num)
#     for i in range (len(arr)):
#        if prev_num != arr[i]:
#           emptyarr.append(arr[i])
#           prev_num = arr[i]
#     print(emptyarr)
# removeDuplicates(nums)   

# ---------------------------------------------------------------------------------------

#2 //to find the common elements in three sorted arrays//

# arr1 = [10,20,30,40]
# arr2 = [30,40,50,60]
# arr3 = [30,40,50,60]
# def common_elements(arr1, arr2, arr3):
#       i,j,k=0,0,0
#       common=[]
#       while i < len(arr1) and j < len(arr2) and k < len(arr3):
#             if arr1[i] == arr2[j] == arr3[k]:
#               common.append(arr1[i])
#               i += 1
#               j += 1
#               k += 1
#             elif arr1[i] < arr2[j]:
#               i += 1
#             elif arr2[j] < arr3[k]:
#               j += 1
#             else:
#               k += 1
#       return common 

# print(common_elements(arr1, arr2, arr3))

#  -------------------------------------------------------------------------------------     
           
# 3 Write a python program to flatten a nested list?

# def flatten_list(nested_list):
#     flat_list = []

#     for item in nested_list:
#         if isinstance(item,list):
#             for sub_item in item:
#                 if isinstance (sub_item,list):
#                     for sub_sub_item in sub_item:
#                         flat_list.append(sub_sub_item)
#                 else:
#                     flat_list.append(sub_item)
#         else:
#             flat_list.append(item)        
#     return flat_list
# nested_list = [1,[2,3],4,5,6,7]
# print(flatten_list(nested_list))

# a = "HI VIEW"
# print(a.lower())
 




# def my_profit(price):
#     max_profit=0
#     n=len(price)
#     for i in range(n):
#         for j in range (i+1,n):
#             profit= price[j]-price[i]
#             if profit > max_profit:
#                 max_profit=profit
#     return max_profit 
# price=[9, 6, 7, 5, 4, 8]         
# print("max_profit:",my_profit(price))  



# def reverse_string(s):
#     reverse_str = ""
#     for char in s:
#         reverse_str= char + reverse_str
#     return reverse_str
# print(reverse_string("Hello"))        




# def reverse_string(s):
#     reverse_str=""
#     for char in s:
#         reverse_str= char + reverse_str
#     return reverse_str
# print(reverse_string("python"))        





# def find_max(lst):
#     max_num = 0
#     for num in lst:
#         if num>max_num:
#             max_num=num
#     return max_num
# print(find_max([1, 5, 6, 7, 9]))            


# def max_product(nums):
#     max_product = 0
#     n = len(nums)

#     for i in range(n):
#         for j in range(i + 1, n):
#             product = nums[i] * nums[j]
#             if product > max_product:
#                 max_product = product
#     return max_product 

# print(max_product([2, 2, 2, 2, 2]))                


# def findword(s):
#     lastword = 0
#     foundword =False
#     s= s.strip()
#     for i in range(len(s)-1,-1,-1):
#         if s[i] !=' ':
#             lastword += 1
#             foundword =True
#         elif foundword:
#             break
#     return lastword

# print(findword("Hello innovapath"))


# def findword(k):
#     lenghis = 0
#     foundword = False
#     k = k.strip()
#     for i in range(len(k) - 1, -1, -1): 
#         if k[i] !=' ':
#             lenghis += 1
#             foundword = True
#         elif foundword:
#             break
#     return lenghis

# print(findword("hi welcome to innovapath"))        


# t=(1,2,3,4,5)
# print(*t)

# a = int(input("give a value:"))
# b = int(input("give b value:"))

# print(a,b,sep=" * ",end=" end here..")

# a = 10
# b = 4

# print(a,b,sep=" % ", end= " its modulus..")

# name = input("Enter name: ")
# print("Hello",name, )


# pi = float(input("pi: "))
# print("value of pi:")

#Taking multiple inputs in a single line

# a= input()
# x,y,z = a.split(" ")
# sum = int(x) + int(y) + int(z)
# print(sum)


#Specifying seperator in output

# inp = input("Enter name and age:")
# name, age = inp.split(",")
# print("Name:",name,",age:",age, sep=" ")

#End Parameter in output

# n =int( input("Enter n :"))
# print("countdown: 5 4 3 2 1 ",end = "Blast off!")


# x,y = input("Enter a and b values: ").split(",")
# a = int(x)
# b= int(y)
# print("Addition:",a+b,"Subtraction:",a-b,"Multiplication:",a*b,"Division:",a/b, sep="") 

 #sum of ttwo numbers

# num1 = int(input("Enter a value:"))
# num2 = int(input("Enter b value:"))
# # print("sum:",num1+num2, sep="")
# print(f"sum:{num1+num2}")

#Area of circle

# Radius = int(input("Enter number:"))
# area=3.14*Radius*Radius
# # print("Area of circle:",3.14*Radius*Radius)
# print(f"Area os circle:{area}")


# def max_area_covered(height):
#     max_area = 0
    
#     for i in range(len(height)):
#         for j in range(i + 1, len(height)):
#             area = min(height[i], height[j]) * (j - i)
            
#             if area > max_area:
#                 max_area = area
    
#     return max_area

# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# output = max_area_covered(height)
# print(f"The maximum area the container can store is {output}")


# finding roots

'''

'''

# a = int(input("Enter a value:"))
# b = int(input("Enter b value:"))
# c = int(input("Enter c value:"))

# d = (b**2)-4*a*c
# root1=(-b + (d**(0.5)))/2*a
# root2=(-b - (d**(0.5)))/2*a

# print(f"Root is: {root1,root2}")


# a = int(input("Give a:"))
# b = int(input("Give b:"))

# b = b+a
# a = b-a
# b = b-a

# print(f"value of a is:{a}")
# print(f"value of b is:{b}")

# a = int(input("Enter 'C' value: "))

# F= a*(9/5)+32
# K = 273 + a 
 
# print(f"Tempreture in Fahrenheit: {F}")
# print(f"Tempreture in Kelvin: {K}")

# a = int(input("Enter amount of USD:"))

# b = a*(0.85)

# print(f"EquivalentamountinEUR: {b}")

# num1 = int(input("value a is:"))
# num2 = int(input("value b is:"))
# operator = str(input("operator: "))

# if operator == "+":
#     print(f"Addition of given 2 num is {num1+num2}")
# elif operator == "-":
#     print(f"subtraction of given 2 num is {num1-num2}")
# elif operator =="*":
#     print(f"Multiplication of given 2 num is {num1*num2}")
# elif operator == "/":
#     print(f"Addition of given 2 num is {num1/num2}")
# else:
#     print(f"not a valid number ")


# def findmaxspace(height):
#     max_space =0
#     for i in range (len(height)):
#         for j in range (i+1,len(height)):
#             area=min(height[i],height[j])*(j-i)
#             if area>max_space:
#                 max_space.append(area)
#     return max_space
# height=[1, 8, 6, 2, 5, 4, 8, 3, 7]   
# output=(findmaxspace(height))
# print(f"the max space of the water contains:{output}")



'''string slicing'''


# str = "python"
# print(str[0:3])
 

# s="hello world"
# print(s[1::2])


# s1="hi"
# s2="innovapath"
# result=s1+" "+s2
# print(result)


# s1="innovapath"
# print(len(s1))

# s1 = "inn ovapath"
# print(len(s1))


'''methods of strings'''


'''to make capital letters'''

# s1 = "hello"
# s2 = s1.upper()
# print(s2) 

# s1 = "car"
# s2 = s1.upper()
# print(s2)


'''to make small letters '''



# S1 = " CAR"
# S2 = S1.lower()
# print(S2)

# s1 = "BIKE IS MINE "
# print(s1.lower())


'''to remove trailing spaces around'''


# s1="helloworld"
# print(s1.strip())
 

'''for replacement'''



# s1="hello world"
# print(s1.replace('l','d'))

# s1="hello world"
# print(s1.replace('el','ed'))



'''counting methods'''



# print('hello world'.count('l'))

# print('jjdwcjjjcdcjjjwjdjjjjjdjvjjj'.count('j'))



'''string formattings'''


# age=13
# name="alice"

# print(f"kido {name} has {age} year old.")

# desigination='IT Solutions Pvt Ltd'
# company='Innovapath'

# print(f"The {company} is a {desigination}.")
 

'''simple palindrome or not program using string slicing'''



# s=input("Given a string: ")

# reverse = s[::-1]

# if reverse == s:
#     print("it is a palindrome.")
# else:
#     print("it is not a palindrome.")


# a = input('give x,y,z =')
# x,y,z=a.split(",")

# num1 = int(x)
# num2 = int(y)
# num3 = int(z)
# great = 0 
# if num1>num2:
#     if num1>num3:
#         great = num2
#     else:
#         great = num3
# elif num2 > num1:
#     if num2>num3:  
#         great = num2
#     else:
#         great = num3
# elif num3 >num1:
#     if num3> num2:
#         great = num3
#     else:
#         great = num2   
# print(great)

# square = []
# for i in range(10):
#     square.append(i*i)

# print(square)

# square = [i*i for i in range(10)]
# print(square)

# List1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = []
# for i in (List1):
#     for j in (List2):
#         k=(i*j)
#         result.append(k)

# print(result)


# year = int(input("Enteryear: "))

# leap= False

# if year%400 == 0:
#     leap = True
# elif year%100 ==0:
#     leap = False
# elif year%100 ==0:
#     leap = True
# else:  
#     leap = False    

# print(leap)        

# class parking_lot:
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.carsinside = 0
#     def cars_in(self):
#         if self.carsinside < self.capacity:
#             print(f"car entered.cars inside:{self.carsinside}")
#         else:
#             print(f"parking is full")
#     def car_out(self):
#         if self.carsinside > 0:
#             self.carinside -= 1 
#             print(f"Car exited. Cars inside: {self.carsinside}")   
#         else:
#             print("No cars inside, cannot exit")    
#     def current_status(self):
#         return f"carsinside:{self.carsinside}.capacity:{self.capacity}"
# lot = parking_lot(5)

# lot.cars_in()
# lot.cars_in()
# lot.cars_in()
# lot.cars_in()
# lot.cars_in()
# lot.car_out()
# lot.cars_in()

# print(lot.current_status())




# class Faculty:
#     def __init_(self,firstName,lastNmae,email,facultyId,Address,mobileNumber,subjecsTeaching,salary,dateJoined):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.email = email
#         self.facultyId = facultyId
#         self.Address = Address
#         self.mobileNumber = mobileNumber
#         self.subjecsTeaching = subjectsTeaching
#         self.salary = salary
#         self.dateJoined = dateJoined
#     def getFullName(self):
#         print(self.firstName+''+self.lastName)
        
#     def changeAddress(self,newAddress):
#         self.address  = newAddress
#         print("address change")
        
#     def changeNumber(self,newNumber):
#         self.mobileNumber = newNumber 
#         print("number updated")
        
#     def getSalary(self):
#         print('your salary is ', self.salary)       
                
        
                   
# class MovieTicket:
#     def __init__ (self,movie_name,avail_seats):
#         self.movie_name = movie_name
#         self.avail_seats = int(avail_seats)
        
#     def Book_ticket(self,quantity):
                             
#         if self.avail_seats >= quantity:
#             self.avail_seats -= quantity
#             print (f"booked {quantity}: movie for{self.movie_name}")
#         else:
#             print("no ticket")
    
#     def get_avail_seats(self):
#         return f"availble seats for {self.movie_name} is {self.avail_seats}"
# ticket = MovieTicket("Tenet","25")
# ticket.Book_ticket(20)
# print(ticket.get_avail_seats())           


# class parkinglot:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.carsinside = 0
        
#     def carsin(self):
#         if self.carsinside < self.capacity:
#             self.carsinide += 1
#             print(f"car entered,carsinside:{self.carsinside}")
#         else:
#             print("parking is full")
    
#     def carsout(self):
#         if self.carsinside  > 0:
#             self.carsinside -= 1
#             print(f"car existed, carsinside is:{self.carsinside}")
#         else:
#             print("No car Existed, ")    
            
#     def display(self):
#         return "carsinside:{self.carsinside},capacity of lot :{self.capacity}" 

# lot = parkinglot(5)

# lot.carsin()
# lot.carsin()
# lot.carsin()
# lot.carsin()
# lot.carsin()
# lot.carsout()
# lot.carsin()

# print(lot.display)


# def count_occurrences(input_string):
#     occurrences = {}
    
#     for char in input_string:
#         if char in occurrences:
#             occurrences[char] += 1  
#         else:
#             occurrences[char] = 1  
#     return occurrences

# input_string = "Innovapath IT"

# result = count_occurrences(input_string)
# print(result)

# Write a program to accept two numbers from the user
# and calculate multiplication

# num1 = int(input("Enter the first number: "))

# num2 = int(input("Enter the second number: "))

# num = num1 * num2

# print(num)

# Display three string “Name”, “Is”, “James” as “Name**Is**James”

# print('name','is','james', sep = '**' )

# num1 = float(input("Enter first number: ")
# num2 = float(input("Enter second number: ")
# num = num1 + num2
# print(num)

# Write a program to take three names as input from a user in the 
# single input() function call.

# names = input("Enter six names: ").split()

# name1, name2, name3, name4, name5, name6 = names

# print("Name1:",name1)
# print("Name2:",name2)
# print("Name3:",name3)
# print("Name4:",name4)
# print("Name5:",name5)
# print("Name6:",name6)

# Interchange first and last elements using Temporary Value.

# my_list = [0, 1, 2, 3, 4, 5]

# my_list[0],my_list[-1] = my_list[-1],my_list[0]

# print("Lists after swapping first and last elements from given list: ", my_list)

# check length of the given string.

# str = "geeks"

# print(len(str))

# num1 = int(input("Enter first number is: "))
# num2 = int(input("Enter second number is: "))

# def remove_duplicates(sorted_array):
#       unique_array = []

# for element in sorted_array:
#     if element not in unique_array:
#         unique_array.append(element)

# return unique_array
# sorted_array = [1, 1, 2, 2, 3, 4, 4, 5]
# unique_array = remove_duplicates(sorted_array)
# print("Array after removing duplicates:", unique_array)


# S = [1,2,3,4,5,6,7,8,9,10]

# s = s.split()

# print(s)


# write a program to manage the car parking lot display 
# as how many many cars in side and what is the capacity of parking lot.


# class parkinglot:
    
#     def __init__(self,capacity):
#         self.capacity = capacity 
#         self.carsinside = 0
        
#     def carsin(self):
#         if self.carsinside < self.capacity:
#             self.carsinside += 1
#             print(f"Car is Enter, cars inside is : {self.capacity}")
#         else:
#             print("Parking is full")
       
#     def carsout(self):
#         if self.carsinside > 0:
#             self.carsinside -= 1
#             print(f"car is Exist, cars inside is: {self.capacity}")
#         else:
#             print("no cars inside, dont wait") 
               
#     def current_status(self):
#         return "carsinside:{self.carsinside}, capacity is : {self.capacity}"
    
# lot = parkinglot(5)

# lot.carsin()
# lot.carsin()
# lot.carsin()
# lot.carsin()
# lot.carsin()
# lot.carsout()
# lot.carsin()

# print(parkinglot.current_status())    
        
#  write a program to compute the given 3*3 matrix and
# print in transpose form rows in to columns.
              
# matrix = [[1, 5, 8],
#           [4, 5, 6],
#           [8, 1, 2]]   

# transpose = [[0]*len(matrix) for _ in range(len(matrix[0]))]

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         transpose[j][i] = matrix[i][j]
# print("transpose of the matrix:")

# for row in transpose:
#     print(row)  
      
# find the largest number in the given list.

# def findlargestnum(lst):

#      largest =lst[0]
#      for i in lst:
#         if i > largest:
#             largest = i
#      return largest        
        
# l = [1, 2, 3, 4, 5, 6, 7, 8, 88, 90, 9]   

# print("The largest number in the list is  : ",findlargestnum(l))

# Move all negatives numbers in to first and all positive number
# in to end in a alist with out using inbuilt functions.

# def negatives_and_positives(lst):
    
#     negatives = []
#     positives = []
#     for i in lst:
#         if i > 0:
#            positives.append(i)
#         else:
#             negatives += [i] 
            
#         rearranged_list = negatives + positives   
        
#     return rearranged_list

# l = [-1, 5, 6, -3, 8, -2, 4, -8]  
# print("the list after seperating negatives and positives: ", negatives_and_positives(l))      
         
# Find the Intersection of Two Lists:
# Write a program to find common elements between two lists.


# def intersection_lists(list1,list2):
#     intersection = []
#     for i in range (len(list1)):
#         for j in range (len(list2)):
#             if list1[i] == list2[j]:
#                 if list2[j] not in intersection:
#                     intersection.append(list2[j])
#     return intersection 
# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [9,8,7,6,11,12,13] 
# print("the intersection of two lists are: ", intersection_lists(list1,list2))                


# find the union of two lists: write a program to find all 
# unque elements present in either or both of the two given lists.
# input: list1 = [1,2,3,4], list2 = [3,4,5,6]
# output: [1,2,3,4,5,6]

# def find_union (list1,list2):
#     union = []
    
#     for i in list1:
#         if i not in union:
#             union.append(i)
            
#     for i in list2:
#         if i not in union:
#             union.append(i)
#     return union     
# list1 = [1,2,3,4]
# list2 = [3,4,5,6] 
# print("the union of two lists is: ", find_union (list1,list2))           



# find the differences between two lists:
# write a program to find all elements that are in list1 but not in list2.


# def find_the_difference(list1,list2):
#     differences = []
#     for i in list1:
#         if i not in list2:
#             differences.append(i)
#     return differences 
# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# result = find_the_difference(list1,list2)
# print("The difference between two lists are: ",result)

# find common elements in three lists:
# write a code to find common elements in three lists given

# def find_common(list1,list2,list3):
#     common = []
#     for i in list1:
#         if i in list2 and i in list3:
#             common.append(i)
#     return common
# list1 = [1,2,3]
# list2 = [3,4,5]
# list3 = [2,3,4]
# result = find_common (list1,list2,list3)
# print("the common elements of three lists is: ",result)
            
# WAP to design the screen that shows a parking lots current_status like
# how many cars inside and how many are out and capacity of parking. 

# class parking_lot:
    
#     def  __init__ (self,capacity):
#         self.capacity = capacity
#         self.carsinside = 0
    
#     def carsin(self):
#         if self.carsinside < self.capacity:
#            self.carsinside += 1
#            print(f"car enter, cars inside is : {self.carsinside}")
#         else:
#            print("Parking is full")
    
#     def carsout(self):
#         if self.carsinside > 0:
#             self.carsinside -= 1
#             print(f"car exit, carsinside is: {self.carsinside}")
            
#     def current_status(self):
#         return f" carsinside: {self.carsinside}, capacity of lot is :{self.capacity}"
    
# lot = parking_lot(5)

# lot.carsin()
# lot.carsout()
# lot.carsin()
# lot.carsin()
# lot.carsin()
# lot.carsout()
# lot.carsin()
# lot.carsin()
# lot.carsin()

# print(lot.current_status())
  
# Find elements that are same to be in every lists append it to empty variable              

# def find_common_elements(list1,list2):
#     common_elements =[]
    
#     for i in list1:
#         if i not in common_elements:
#             common_elements.append(i)
            
#     for j in list2:
#         if j not in common_elements:
#             common_elements.append(j)
            
#     return common_elements
# list1 = [1,2,3,4]
# list2 = [1,2,5,6]
# result = find_common_elements(list1,list2)
# print("The common element is :", result)           
 
#  wap to sum a list with out using builtins   

# def sum_num(element):
#     suming = 0 
#     for i in element:
#         suming += i
#     return suming 
# element = [1,2,3]   
# print(sum_num(element))                  

# Design a BankAccount class that has attributes for account holder’s name, balance, and account number. It should have methods to deposit, withdraw, and display the balance.
# Bonus: Add error handling for cases where withdrawal exceeds the balance. 

# class  BankAccount:
    
#     def __init__(self, account_holder, account_number, balance):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.balance = balance
      
#     def Deposite(self,amount):
#         if amount > 0:
#             print(f"amount is credited, new balance is {self.balance}")    
#         else:
#             print("please enter positive number of amount")
         
#     def Withdrawl(self,amount):
#         if amount > self.balance:
#             print(f"insuffficient funds.balance of the acnt is {self.balace}")
#         elif amount < 0:
#             print("please enter a positive number")
#         else:
#             self.balance -= amount
#             print(f"withdrawl amount {amount},balance is {self.balance}")
    
#     def Display_balance(self):
#         return f"account_holder {self.account_holder},account_number{self.account_number},self.balance{self.balance}"
    
    
#     account = BankAccount("prem" , "1400256", 500 )          
                    
#     account.deposite(200)  
#     account.withdrawl(600)
#     account.withdrawl(200)
    
#     print(account.display_balance)     


# finding the length of the last word 

# def find_length(s):
#     last_word = 0
#     found_word = False
#     s= s.strip()
#     for i in range(len(s)-1,-1,-1):        
#         if s[i] !=' ':
#             last_word += 1
#             found_word = True
#         elif  found_word:
#             break
#     return last_word
# print(find_length("hello innovapath"))      


# def my_function():
#     print("hello")
#     my_function()
# my_function()    

# if a person can attend all meetings based on the given intervals.
# check every pair of meetings
# to see if they overlap.

# input = meeting_intervals = [[0, 30], [5, 10], [15, 20]]

# def check_intervals(intervs):
    
#     for i in range(len(intervs)):
        
#         for j in range(i+1,len(intervs)):
            
#             if intervs[i][0] < intervs[j][1] and intervs[j][0] < intervs[i][1]:
                
#                 return "it's not possible to attend the all meetings"
#     return " it's possible to attend the meetings"

# M = [[0,3],[3,8],[7,17],[18,19],[20,22],[23,30]] 
  
# print(check_intervals(M))     

# Consider the number of elements in nums which are not equal to val be k, 
# to get accepted, you need to do the following things:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# def remove_element(nums,val):
#         result = []

#         for num in nums:
#             if num != val:
#                result.append(num)
        
#         for  i in range(len(result)):
#              nums[i] == result[i]
#         return len(result)

# nums = [3, 2, 2, 3]

# val = 3 

# k = remove_element(nums,val)
# print(k)
# print( nums[:k])                  

# print(( lambda number:number**2)(2))
# samplelist=[2,4,6,8]   

# def square(k):
       
    # return k**2  
# result = map(lambda k:k**2,samplelist)
# print(list(result))

# sampleTuple =(1,2,3,4,5,6)
# def square(k):
#     if k%2 ==0:
#         return k**2
#     else:
#         return k**3
# result = map(square,sampleTuple)
# print(tuple(result))
      
# x = '1','2','3','4','5','6'
# # k = x[0:4]

# # print(k) 
# print(type(x))  
  
# a = "hello"

# b = a[::-1]

# print(b)

# lst = [1,2,3,4,5,6]

# sum the list

# def sum_of_list(lst):
#     total = -50
#     for num in lst:
#         total += num
#     return total    
# lst = [1,2,3,4,5,6]
# L = sum_of_list(lst)

# print(L)

# def reveerse_num(k):
#      rev_num = ""
#      k_str = str(k)
#      for i in range(len(k_str)-1,-1,-1):
#          rev_num += k_str[i]
#      return int(rev_num)
# k = 1234506789
# H = reveerse_num(k)
# print(H)    

# N = 1,2,3,4,5,6,7,8,9,10
# write a code to sum of even numbers in a given list.

# def sum_of_even(N):
#     total = 0
#     for num in N:
#         if num%2 ==0:
#             total += num
#     return total
# N = 1,2,3,4,5,6,7,8,9,10
# K= sum_of_even(N)
# print(K)    


# def smallest_element(lst):
#     small = lst[0]
#     for i in lst:
#         if i < small:
#             small = i
#     return small
# lst = [5,1,4,6,78,3]
# print(smallest_element(lst))        

# Find Common Elements in Two Lists
# Write a program to find the common elements between two lists using loops.
# Input: list1 = [1, 2, 3], list2 = [3, 4, 5]
# Output: [3]

# def find_common(list1,list2):
#     common = []
#     for element in list1:
#        if element in list2:
#            common.append(element)
#     return common

# list1 = [3,4,2]
# list2 = [2,8,9]       
# print(find_common(list1,list2))

# check frm 2 , we want frst 10 numbers which are divisible by 2$7

# n=2
# i=0

# while i < 10:
#     if n%2==0 and n%7==0:
#         print(n)
#         i += 1
#     n += 1    

# write a program to find sum of n natural numbers using recursion 

# def my_function(n):
#     if n == 0 :
#         return 0
#     return my_function(n-1)+n

# n = int(input('Enter n value :'))    
# answer = my_function(n)
# print(answer)



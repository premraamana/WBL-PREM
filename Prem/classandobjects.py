# class sample:
#     car =1
#     bike =2
# print(sample.car)
# print(sample.bike)

# obj1 = sample()
# obj2 = sample()
# obj3 = sample()


# print(obj1.car)
# print(obj2.car)
# print(obj3.car)
# print(obj1.bike)
# print(obj2.bike)
# print(obj3.bike)

# obj1.car = 200
# print(obj1.car)
# print(obj2.car)
# print(obj3.car)
# obj1.bike = 250
# print(obj1.bike)

# class Bankacnt:
#     def __init__(self,acntno,acntname,ifsecode,balance):
#       self.acntno=acntno
#       self.acntname=acntname
#       self.ifsecode=ifsecode
#       self.balance=balance
#     # def display(self):
#     #     print(self.acntno,self.acntname,self.ifsecode,self.balance)
#     def withdraw(self,amount):
#         self.balance -= amount
#     def deposit(self,amount):
#         self.balance += amount    
#     def checkbalance(self):
#         print(self.balance)
# obj1=Bankacnt(2255,'prem','sbi001',25464)    
# obj1.withdraw(464)
# obj1.deposit(1000)
# obj1.checkbalance()   

# class Employeemanagement:
#     def __init__(self,name,position,ID):
#        self.name=name
#        self.position=position
#        self.ID=ID 
#     def display(self):
#         print(self.name,self.position,self.ID)
# obj1= Employeemanagement ('prem','Intern',5454)
# obj1.display()

# class studentresults:
#     def __init__(self,name,subject,score):
#         self.name=name
#         self.subject=subject
#         self.score=score
#     def display(self):
#         print(self.name,self.subject,self.score)
# obj1 = studentresults ('prem','python',9.6)   
# obj2 = studentresults ('azmeer','datavisualisation',3.2)
# obj1.display()     
# obj2.display()

# class premcarrentals:
#     def __init__(self,car,seating,price):
#         self.car=car
#         self.seating=seating
#         self.price=price
#     def display(self):
#         print(self.car,self.seating,self.price)
# obj1 = premcarrentals('Dzire',5,2000)   
# obj2 = premcarrentals('baleno',5,2000)
# obj3 = premcarrentals('Creta',5,4000)
# obj4 = premcarrentals('innova',7,6000)
# obj5 = premcarrentals('ertiga',7,5000)

# obj1.display()    
# obj2.display()  
# obj3.display()  
# obj4.display()  
# obj5.display()  

# class sampleClass:
#     bike1=10
#     bike2=20
    
# obj1=sampleClass()
# obj2=sampleClass()
# obj3=sampleClass()
# print(obj1.bike1)
# print(obj3.bike1)
# print(obj2.bike2)
# obj1.bike1=5
# print(obj1.bike1)
# print(obj3.bike1)
# print(obj2.bike2)

# class SampleClass1:
#     def sampleMethod(self):
#         print("hi prem")
# newObj1=SampleClass1()
# newObj1.sampleMethod()
class Bankacnt1:
    def __init__(self,acntno,accountname,ifsecode,balance):
        self.acntno=acntno
        self.accountname=accountname
        self.ifsecode=ifsecode
        self.balance=balance
    # def display(self):
    #     print(self.acntno,self.accountname,self.ifsecode,self.balance)   
# object1.display()
    def withdraw(self,amount):
        self.balance -= amount
    def deposite(self,amount):
        self.balance += amount
    def checkbalance(self):
        print(self.balance)        
              
object1=Bankacnt1(1234,'prem',1254,10000)
object1.checkbalance()
object1.withdraw(2500)
object1.checkbalance()
object1.deposite(7500)
object1.checkbalance()

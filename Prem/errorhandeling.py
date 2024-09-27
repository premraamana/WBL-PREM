# a= 1
# print(b)

# try:
#     print('b')
# except:
#     print("error")
# else:
#     print("no error") 
# finally:
#     print("always")       
'''

 Generators
 example program 
 
''' 
# def countupto(n):
#     for i in range(1,n+1):
#         yield i 
# gen=countupto(500)
# for num in gen:
#     print(num)

# add= lambda x,y: x+y
# result=add(5,10)
# print(result)

# def second_high(nums):
#     if len(nums)<2:
#         raise ValueError("invalid")
#     maxnum=float('-inf')
#     secondmaxnum=float('-inf')
    
#     for num in nums:
#         if num>maxnum:
#             maxnum = num
#     for num in nums:
#         if num<maxnum and num>secondmaxnum:
#                 secondmaxnum = num
    
#     if secondmaxnum == float('-inf'):
#         raise ValueError("error")
#     return secondmaxnum
# print(second_high([3,5,4,8,2,6]))            
                
# for i in range(31):
#     print(i)

# count=0
# while count<5:
#     print(count)
#     count+=1
    
# a = [1,2,3,4,5]
# for z in a:
#     print(z)
# a="apple"
# for k in a:
#     print(k)
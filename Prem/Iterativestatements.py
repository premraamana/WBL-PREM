# candies = 30

# while candies>0:
#     print("give candy to friend")

#     candies -= 1

# candies = 10
# for i in range(candies):
#     if candies > 4:
#         print("6 candies left")
#         continue  
#     print("given")  

# n=int(input("Give'n'value:"))
# i=0
# while i<=n:
    
#     print(i)
#     i+=1

# n = int(input("Give 'n' value: "))
# i = 0
# sum=0
# while i<=n:
#     sum +=i
#     i += 1
# print(sum) 

# n = int(input("Given 'n' value: "))
# i = 1 


# while i <= n:
#     if n % 2 != 0:

#         print(f"{n} is odd")  

#     else:
#         print(f"{n} is not a odd number")
#     break



# n= int(input("give one number: "))


# for i in range(1,11):
   
#         table=i*n
#         print(f"{n}*{i}={table}")
  

# def atendings(interval):
#         n= len(interval)
#         for i in range(n):
#             for j in range(i+1,n):
#                 start1,end1=interval[i]
#                 start2,end2=interval[j]
#                 if start1<end2 and start2<end1:
#                     return False 
#         return True
# interval = [(330,360),(630,640),(1230,1250)]
# print(atendings(interval))        

# def minJumps(nums):
#     def jump_from_position(position):
#         # Base case: If we have reached the last index
#         if position >= len(nums) - 1:
#             return 0
        
#         # Initialize the minimum jumps to a large value
#         min_jumps = float('inf')
        
#         # Explore all possible jumps from the current position
#         for jump_length in range(1, nums[position] + 1):
#             new_position = position + jump_length
#             if new_position < len(nums):
#                 # Recursively find the minimum jumps from the new position
#                 jumps = jump_from_position(new_position)
#                 min_jumps = min(min_jumps, jumps + 1)
        
#         return min_jumps
    
#     # Start from the first position
#     return jump_from_position(0)

# # Example usage:
# nums = [2, 3, 1, 1, 4]
# print(minJumps(nums))  # Output: 2

# nums = [2, 3, 0, 1, 4]
# print(minJumps(nums))  # Output: 2
 
# n= int(input("Give n value:"))
# factorial = 1

# while n>0:
#      factorial = factorial * n
#      n += 1
# print(factorial)


# def sum(a,b):
#         print(a+b)
# sum(5,10)        


import time
print(time.time())
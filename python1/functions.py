# def arrayCheck(nums):
#     for i in range(len(nums)-2):
#         if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
#             return True
#     return False
# print(arrayCheck([1,2,3,4]))        

# def stringBits(str):
#     result=""
#     for i in range(len(str)):
#         if i%2==0:
#             result+=str[i]
#     return result        
# print(stringBits("Hello"))

# def end_other(a,b):
#     a=a.lower()
#     b=b.lower()
#     if a[-1]==b[-1]:
#         return True
#     return False
# print(end_other("Miciy","Naty"))       


# def doubleChar(str):
#     result=""
#     for char in str:
#         result += char*2
#     return result
# print(doubleChar("Mikcy"))     

# def no_teen_sum(a,b,c):
#     return fix_teen(a) + fix_teen(b) + fix_teen(c)

# def fix_teen(n):
#     x=[13,14,17,18,19]
#     if n in x:
#         return 0
#     return n   

# print(no_teen_sum(2,3,17))          


# def count_even(nums):
#     count=0
#     for num in nums:
#         if num % 2==0:
#             count+=1
#     return count
# print(count_even([1,2,3,4,6,8]))           

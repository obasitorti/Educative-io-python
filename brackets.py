# # def check_brackets(bracket):
# #     counter = 0
# #     for i in str (bracket):
# #         if i == "[":
# #             counter += 1

# #         elif i == "]":
# #             counter -= 1
        
# #         if counter < 0:
# #             break
# #     if counter == 0:
# #         return True
# #     else:
# #         return False
     
# # print(check_brackets("[]"))

# def check_sum(num_list):
#     for i in range(len(num_list)):
#         for j in range(i, len(num_list)):
#             if num_list[i] + num_list[j] == 0:
#                 return True
            
#     return False

def fib(n):
    if n <= 0:
        return -1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    else:
        return (fib(n-2) + fib(n-1))


    
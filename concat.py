# def rep_cat(x, z):
#     return str (x)*10 + str (z)*5

# print (rep_cat("x", "y"))

def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    elif n < 0:
        return -1
    else:
        return n * factorial (n-1)
    
print(factorial(5))
 
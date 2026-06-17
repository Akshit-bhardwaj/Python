# Functions in python.


def greet():
    print("Hello boss")
greet()


# Ques 1 Sum of a number.

def sum(a , b):
    return a + b
print(sum(1 , 2))


# Ques 2  Print table by using functions.

def table(a):
    for i in range(1 , a+1):
        print(f"{a} * {i} : " , a * i)

table(10)


# Keyword args.

def intro(name , age):
    return f"Hello my name is {name} and i'm {age} years old"
print(intro(age = 21 , name="akshit"))


# Default args


def your_names(name1 , name2 = "kritika"):
   print(f"Hello i'm {name1} and i'm {name2}")
your_names("AKshit")


# Ques 3 Check if the string is palindrome or not.

# def check_palindorme(str1):
#     str2 = str1[::-1]
#     if str1 == str2:
#         print("String is palindrome")
#     else:
#         print("String is not palindrome")

# check_palindorme("aman")

# By using loop 

# def check_palindorme(str1):
#     rev_str = ""
#     for i in range(len(str1)-1 , -1 , -1):
#         rev_str = rev_str + str1[i]
#     if str1 == rev_str:
#         print("Given string is palndrome")
#     else:
#         print("Not a palindrome string")

# check_palindorme("naman")
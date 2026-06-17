# Now we understand about decorator.

# Decorator is used to decorate the function , when we want to perform some operation before and after the decorator.

# def decorator(func):
#     def wrapper(c , d):
#         print("I run before the function call ")
#         func(c , d)
#         print("I run after the function run ")
#     return wrapper



# @decorator
# def sum(a , b):
#     print(f"sum is {a + b}")
# sum(1 , 2)


def decorator(func):
    def wrapper(*args):
        for i in range(1 , 10):
            print(i)
        func(*args)
        print("I run after the function run ")
    return wrapper



@decorator
def add(*args):
    print(f"sum is {sum(args)}")
add(1 , 2 , 3 , 4 ,5 , 6 , 7)

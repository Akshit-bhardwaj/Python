# Map




lst1 = [1 , 2, 3 , 4]

# def square(num):
#     return num**2


# square_list = map(square, lst1)
# print(list(square_list))

# Filter

def even_check(num):
    print(f"Checking num {num}")
    return num % 2 == 0

numbers = [1,2,3,4 ]

even = filter(even_check,  numbers)
print(list(even))
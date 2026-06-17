# lambda function


# Lambda functions are anonymous function which is used to define function in short and clean format.
# It is used for temporarily or one time.


add = lambda *args : args
print(add(1 , 2 , 3))

check_even_odd =  lambda x : "Even" if x % 2 == 0 else "odd"
print(check_even_odd(4))
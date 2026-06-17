# Exception handling


a = int(input("Enter a number"))

try:
    print(10/a)
except Exception as e:
    print("Sorry" , e)
finally:
    print("Hello")
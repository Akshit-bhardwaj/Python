# Conditional statement questions


# Ques 1 Accept 2 number and find greatest from both of them.


# number1 = int(input("Enter number 1 "))
# number2 = int(input("Enter number 2"))

# if number1 >= number2 :
#     print("Number 1 is greater than number 2")

# else:
#     print("Number 2 is greater than 1 ")



# Ques 2 Accept the gender from the user as char an print the respective greeting message.

# gender = input("Enter your gender : ")

# if gender == "male" or gender == "m":
#     print("Good morning sir")

# elif(gender == "female" or gender == "f"):
#     print("Good morning mam")

# else:
#     print("Good morning Respected")



# Ques 3 Leap year

year = int(input("Enter year : "))

if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0 ):
    print("Leap year")
else:
    print("Not a leap year")
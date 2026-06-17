# Practice questions on Loops , strings , conditions.

# Ques 1 Accept an integer and print hello word n times.



# integer = int(input("Enter a number"))

# for i in range(0 , integer):
#     print("hello")


# Ques 2 Print natural number up to n.


# integer = int(input("Enter a number"))


# for i in range(1 , integer + 1):
#     print(i)



# Ques 3 Reverse for loop print n to 1.

# integer = int(input("Enter a number"))

# for i in range(integer , 0 , -1):
#     print(i)


# Ques 4 Take a number as input and print its table.


# number = int(input("Enter a number"))

# for i in range(1 , 11):
#     print(f"{number} * {i} : " , number * i)



# Ques 5 Sum upto n terms.


# n = int(input("Enter a number"))
# sum = 0

# for i in range(1 , n+1):
#     sum = sum + i
# print(sum)


# Ques 6 Factorial of a number.

# number = int(input("Enter a number"))
# fact = 1

# for i in range(number , 0 , -1):
#     fact = fact * i
# print(fact)




# Ques 7 Print the sum of all odd and even numbers in a range seperately.

# number = int(input("Enter a number"))
# even_sum = 0
# odd_sum = 0

# for i in range(1 , number + 1):
#     if i % 2 == 0:
#         even_sum += i
# print(f"Even number sum : {even_sum}" )

# for j in range(1 , number + 1):
#     if j % 2 != 0 :
#         odd_sum += j
# print(f"Odd number sum : {odd_sum}")
    

# Ques 8 Print all factor of a number.


# number = int(input("Enter a number"))

# for i in range(1 , number+1):
#     if number % i == 0:
#         print(i)
        

# Ques 9 perfect square.


# n =  int(input("Enter a number"))
# square = 0
# for i in range(1 , n+1):
#     if i*i == n:
#         square = i
# print(f"Pefect square is {square} on : " , n)



# Ques 10 Reverse string without using inbuilt function.

# str1 = "Coding ninja"
# str2 = str1[::-1]
# print(str2)


# Ques 11 Check if a string is palindrome.

# str1 = input("Enter a string ")
# str2 = str1[::-1]
# if str1 == str2:
#     print("String is palindrome")
# else:
#     print("Given string is not palindrome") 



# Ques 12 Count all letters , digits and special character from a given string.

# taking_input = input("Enter a sentence ")

# count_int = 0
# count_str = 0
# count_special = 0

# for i in range(len(taking_input)):
#     if taking_input[i].isalpha():
#         count_str += 1
#     elif taking_input[i].isdigit():
#         count_int += 1
#     else: 
#         count_special += 1
# print(count_str)
# print(count_int)
# print(count_special)


# Ques 13 Seperate each digit of a number and print it on the new line.

digit = int(input("Enter a digit"))

while(digit > 0):
    print(digit % 10) # extract last digit
    digit = digit // 10 # To stop the loop when digit becomes smaller than 0.
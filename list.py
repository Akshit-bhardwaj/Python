# List

# fruits = ["Apple" , "Banana" , "cherry"]
# fruits2 = fruits.pop(2)

# for i in fruits:
#     print(i)

# # Mutable v/s immutable.
# # -------------------------
# str1 = "abcd"
# str1[0] = "e"
# print(str1) # gives error

# # -------------------------

# lst1 = ["a" ,"b" , "c"]
# lst1[0] = "e"
# print(lst1) # gives "e" , "b" , "c"




# Ques1 Print positive and negative elements of list.

# lst1 = [1 , 2 , 3 , 4 , -1 , -2 , -3 , 0]

# pos_list = []
# neg_list = []

# for i in lst1:
#     if i > 0:
#         pos_list.append(i)
#     elif i < 0:
#         neg_list.append(i)
#     else:
#         print("0 is nor postive or negative")
# print(pos_list)

# print(neg_list)



# Ques 2 Calculate avg/mean of list.

# lst1 = [1 , 2 , 3]
# sum = 0
# avg = 0
# for i in lst1:
#     sum = sum + i
#     avg = sum/len(lst1)
# print(avg)



# Ques 3 Find the greatest element and print its index too.

lst1 = [1 , 5 , 9 , 11 , 13]


greatest_element = lst1[0]

# for i in lst1:
#     if i > greatest_element:
#         greatest_element = i
# print(greatest_element)


#  ---------------- OR ----------------------------

# for i in range(len(lst1)):
#     if lst1[i] > greatest_element:
#         greatest_element = lst1[i]
#         index = i
# print(greatest_element ,"with index" ,  index)




# Ques 4 Find second greatest element from list.


# lst1 = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 9 , 10]
# greatest_element = lst1[1]
# second_greatest = lst1[0]

# for i in lst1:
#     if i > greatest_element:
#         second_greatest = greatest_element
#         greatest_element = i
#     elif(i > second_greatest and i != greatest_element):
#         second_greatest = i
# print(greatest_element)
# print(second_greatest)


# Ques 5 check if list is sorted or not.


lst1 = [0 , 1 , 2 , 10]
sorted_list = []

for i in range(len(lst1)-1):
    if lst1[i] > lst1[i+1]:
        sorted_list.append(lst1[i]) 
print("list is not sorted")

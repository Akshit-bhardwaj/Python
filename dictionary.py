# Dictionary


# Syntax

# a = {
#     1 : "Hello",
#     2 : "Hello2",
#     3 : "Hello3"
# }
# # print(a)
# # print(type(a))

# # print(a[1])

# for i in a.values():
#     print(i)




# Ques 1 Merge 2 dictionaries.

d1 = {
    "a" : 10,
    "b" : 20,
    "c" : 30
}

d2 = {
    "d" : 40,
    "e" : 50
}


for i in d2:
    d1[i] = d2[i]
print(d2)



# # Ques 2 sum of values
# dict1 = {
#     10 : 100,
#     20 : 200 , 
#     30 : 300
# }

# sum = 0

# for i in dict1.values():
#     sum = sum + i
# print(sum)

# # OR

# for i in dict1:
#     sum = sum + dict1[i]
# print(sum)



# Ques 3 Count the frequency of each elements in a list.


# a = [1 , 2 , 2 , 3 , 3 , 4]

# count_dict = {}

# for i in a:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1
# print(count_dict)


# Ques 4 Write a python program to combine 2 dictionary by adding values for common keys.

# a = {
#     1 : 10,
#     2 : 20,
#     3 : 30,
#     4 : 40
# }

# b = {
#     3 : 10,
#     4 : 20,
#     5 : 30
# }

# for i in b: 
#     if i in a:
#         a[i] = a[i] + b[i]
#     else:
#         a[i] = b[i]

# print(a)

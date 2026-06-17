# File handling project

import os

# print("Press 1 for creating a file")
# print("Press 2 for reading a file")
# print("Press 3 for updating a file")
# print("Press 4 for deleting a file")


# user_input = int(input("Please tell your response : "))
# p = open("file.txt" , "w")
# read_data = open("file.txt" , "r")
# update_file = open("file.txt" , "a")

# if user_input == 1:
#     p.write("File created")
#     p.close()
# elif(user_input == 2):
#     data = read_data.read()
#     print(data)
#     read_data.close()
# elif(user_input == 3):
#     update_file.write("File updated")
#     update_file.close()
# elif(user_input == 4):
#     os.remove("file.txt")




# Or we can use functions.



print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

def creating_file():
    p = open("file.txt" , "w")
    p.write("File created")
    p.close()

def reading_file():
    read_file = open("file.txt" , "r")
    data = read_file.read()
    print(data)
    read_file.close()

def updating_file():
    update_file = open("file.txt" , "a")
    update_file.write("File updated")
    update_file.close()

def deleting_file():
    pass

user_input = int(input("Please tell your operation"))
if user_input == 1:
    creating_file()
elif user_input == 2:
    reading_file()





    



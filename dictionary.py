# # creating an empty dictionary 

# # dict1={}
# # print(dict1)
# # print(type(dict1))

# student={
#     "name" : "Hari",
#     "age " : " 20 ",
#     "course" : "Engineering"

# }

# print(f"Student: {student}")

# # Accesing element in a dictionary
# # Accesing using keys
# student_name= student ["name"]
# student_course=student["course"]
# print(f"Name: {student_name}")
# print(f"Course: {student_course}")
# print(f"Student age: {student['age ']}")


# # Accesing using get( ) method
# student_name= student.get("name")
# student_address = student.get("address","Not Available")
# print(student_name)
# print(student_address)
# print(student.get("course"))

# # Adding new item in dictionary
# student["address"]="bhaktapur"
# print(f"Dictionary after adding address: {student}")

# student["address"]="Chitwan"
# print(f"Dictionary after changing address: {student}")


# # Dictionary methods
# # keys() method will return list of all the keys
# student_keys=student.keys()
# print(f"Keys: {student_keys}")

# # Values() method will return list of all the values 
# student_values = student.values()
# print(f"Values: {student_values}")

# # items() ----> this method will return list of tuples and each tuple 
# # contains key and value pairs

# student_items= student.items()
# print(f"Items: {student_items}")

# # Looping over key- value pairs
# for key,value in student.items():
#     # key, value =x
#     print(f"{key}:{value}")

# # Deleting an item from the dictionary
#     del student ["address"]
#     print(f"Dictionary after deleting addressL {student}")

    
list1= [1,2,3]
list2= [1,2,3]
for v1,v2 in zip(list1,list2):
    print(v1*v2)




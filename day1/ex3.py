# dictionnary
#1. Ask the user for the student's name
# Create the dictionary in the format {'name': '<student_name'>,'marks':[]}
# Return that dictionary

def create_student():
    student_name = input("enter your name: ")
    dict = {"name" : student_name , "marks" :[]}
    dict["age"] = 20
    return dict
#print(create_student())

# 2. add a values to marks
s = create_student()
def add_mark(student, mark):
    student['marks'].append(mark)
    return None

add_mark(s, 5) # when we modified student we modified s => Passing by Reference
# we don't passing the value of s (it's not the dictionary), but rather the location where the 
#dictionnary is store
print(s)
# Passing by Value
z = 5
def add_number(x, y):
    x = x+y
add_number(z, 10)
print(z) # is still 5 because z is primitive value,it's different to x, that's mean is get passing 
# by value

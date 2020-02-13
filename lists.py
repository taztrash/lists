#creating a list of students
students = ["leroy","teddy","collins","maui","steve","sossie"]
print(students)

#creating an empty list
#students = []
print(students)


#indexing
print(students[1])#displays the second student in the list
print(students[0])#displays the first student in the list
print(students[-5:-1])#displays the fifth  student starting from the back of the list upto the second last student in the list
print(students[2:])#displays the thrid student in the list
print(students[2:5])#displays the second student in the list to the fifth stuent

# replacing a student in a list
students[1]="Mwangi" 
print(students)

#loop through the list
for student in students:
    print(student)

#check if item exists
if "maui" in students:
    print("maui is there")

#methods
print(len(students))#
students.append("maui")
print (students)

students.insert(3,"trash")#adds an element at the specified value
print (students)

students.pop(3)#removes the item with the specified value
print(students)

students.sort()#sorts the list alphabetically
print(students)

students.reverse()#reverses the order of the students in the list 
print(students)

students.clear()#removes all the elements from the list
print(students) 
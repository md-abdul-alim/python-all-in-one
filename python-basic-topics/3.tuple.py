"""
-----Tuple is an ordered, immutable and Heterogeneous collection of elements.\n
----------Immutable: Can't be modified after created. Only add/remove
----------Ordered: means can access them by their index.
----------Heterogeneous: Can store multiple data type
-----Tuple can write with or without parentheses.
"""

print("-----Tuple with parentheses-----")
with_p = (1, 2, 'hello', 3.33)
print(with_p[2])
print(with_p[-1])
one, two, hello, float_ = with_p
print(hello, float_)

print("-----Tuple without parentheses-----")
without_p = 11, 22, 'hello', 33.33
print(without_p)

print("-----Tuple for Data Grouping: two-dimensional space, data-----")
print("(x, y) : ", (1, 2))
print("(year, month, day) : ", (1995, 1, 5))

print("-----Tuple/List for Multiple values return-----")


def get_name_and_age():
    name = "Alim"
    age = 29
    return name, age


result = get_name_and_age()
name, age = result
print(result, name, age)

print("-----Tuple for Unpacking basic-----")
personal_info = ("Alim", 29, "Dhaka")
# Unpacking the tuple into individual variables
name, age, city = personal_info

# Printing the unpacked values
print("Name:", name)
print("Age:", age)
print("City:", city)

print("-----Tuple for Unpacking advance-----")
student_records = [("Abdul", 95), ("Alim", 88), ("Milon", 78), ("Munmun", 92)]

names, scores = [], []

# Unpack
for name, score in student_records:
    names.append(name)
    scores.append(score)

# Calculate average score
average_score = sum(scores) / len(scores)
# Find the highest score
max_score, top_student = max((score, name) for name, score in student_records)

print("Names:", names)
print("Scores:", scores)
print("Average Score:", average_score)
print("Top Student:", top_student, "with a score of", max_score)

print("-----Tuple for Data Integrity-----")
# Configuration settings (immutable data)
database_config = ("localhost", 3306, "mydb", "myuser", "mypassword")
# For example, this line would result in an error:
# database_config[1] = 5432  # This would be a TypeError
#
# print("The database configuration is:", database_config)

print("-----Tuple for Dictionary Key-----")
student_grades = {
    ("Abdul", "Alim"): 90,
    ("Esrat", "Jahan"): 88,
}

print("Esrat's Math grade:", student_grades[("Esrat", "Jahan")])

print("-----Tuple for Named Tuples basic-----")
from collections import namedtuple

Person_ = namedtuple('Person', ['name', 'age'])
alim = Person_(name='Alim', age=29)
milon = Person_(name='Milon', age=30)

print(alim.name, " ", alim.age)
print(milon[0], " ", milon[1])
"""
typename:
-----It becomes the name of the new named tuple class.
-----Also used as a factory function for creating instance of the named tuple.
"""
print("-----Tuple for Named Tuples advance-----")
from collections import namedtuple

# Define a named tuple type called 'Student' with fields 'name', 'age', and 'scores'
Student = namedtuple('Student', ['name', 'age', 'scores'])

# Create a list of student records as named tuples
students = [
    Student(name='Abdul', age=20, scores=[85, 90, 78]),
    Student(name='Alim', age=21, scores=[92, 88, 95]),
    Student(name='Milon', age=22, scores=[78, 85, 90]),
]

# Calculate the average score for each student
for student in students:
    average_score = sum(student.scores) / len(student.scores)
    print(f"{student.name}'s average score: {average_score:.2f}")

# Find the student with the highest average score
top_student = max(students, key=lambda student: sum(student.scores) / len(student.scores))
print(f"The top student is {top_student.name} with an average score of {sum(top_student.scores) / len(top_student.scores):.2f}")


print("-----Tuple for Argument Lists-----")


def print_args(*args):
    for arg in args:
        print(arg)


print_args(1, 2, 3)
print_args('apple', 'banana', 'cherry', 'date')
print_args()

values = (10, 20, 30)
print_args(*values)

print("-----Tuple for Parallel Assignment-----")
x = 1
y = 2
x, y = y, x
print(x, y)
"""
Can swap the values of variables without using a temporary variable.
"""
print("-----Tuple for Iterating Through Sequences'-----")
# Two lists representing student names and their corresponding scores
student_names = ["Abdul", "Alim", "Milon"]
student_scores = [90, 85, 78]

# Iterate through both lists using a tuple
for name, score in zip(student_names, student_scores):
    print(f"{name}: {score}")

# You can also use enumerate to access both the index and value
for index, (name, score) in enumerate(zip(student_names, student_scores)):
    print(f"Student {index + 1}: {name} - Score: {score}")

print("-----Tuple for Advanced Data Structures Basic-----")
employee_records = [
    ('Alice', 'Johnson', 'Marketing', 45000),
    ('Bob', 'Smith', 'Finance', 55000),
    ('Charlie', 'Williams', 'Engineering', 60000),
    ('David', 'Brown', 'Sales', 48000),
]

for first_name, last_name, department, salary in employee_records:
    print(f"{first_name} {last_name} works in {department} and earns ${salary} per year.")

print("-----Tuple for Advanced Data Structures Advance-----")
# Define two matrices as lists of tuples
matrix_a = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
]

matrix_b = [
    (9, 8, 7),
    (6, 5, 4),
    (3, 2, 1)
]

# Function to perform matrix multiplication using tuples


def multiply_matrices(mat_a, mat_b):
    result = []
    for i in range(len(mat_a)):
        row = []
        for j in range(len(mat_b[0])):
            cell_value = sum(mat_a[i][k] * mat_b[k][j] for k in range(len(mat_a[0])))
            row.append(cell_value)
        result.append(tuple(row))
    return result


# Multiply the matrices
result_matrix = multiply_matrices(matrix_a, matrix_b)

# Display the result matrix
for row in result_matrix:
    print(row)


students = []
courses = []


def input_number_of_students():
    n = int(input("Enter number of students: "))
    return n


def input_students(n):
    for i in range(n):
        print("\nStudent", i + 1)
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter date of birth: ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob,
            "marks": {}
        }

        students.append(student)


def input_number_of_courses():
    n = int(input("\nEnter number of courses: "))
    return n


def input_courses(n):
    for i in range(n):
        print("\nCourse", i + 1)
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")

        course = {
            "id": course_id,
            "name": name
        }

        courses.append(course)


def input_marks():
    course_id = input("\nEnter course ID: ")

    course = None

    for c in courses:
        if c["id"] == course_id:
            course = c
            break

    if course is None:
        print("Course not found.")
        return

    for student in students:
        mark = float(input(
            "Enter mark for " + student["name"] + ": "
        ))
        student["marks"][course_id] = mark


def list_courses():
    print("\n--- Courses ---")

    for course in courses:
        print(course["id"], "-", course["name"])


def list_students():
    print("\n--- Students ---")

    for student in students:
        print(
            student["id"],
            "-",
            student["name"],
            "-",
            student["dob"]
        )


def show_student_marks():
    course_id = input("\nEnter course ID: ")

    course = None

    for c in courses:
        if c["id"] == course_id:
            course = c
            break

    if course is None:
        print("Course not found.")
        return

    print("\n--- Student Marks ---")

    for student in students:
        if course_id in student["marks"]:
            print(
                student["id"],
                "-",
                student["name"],
                ":",
                student["marks"][course_id]
            )
        else:
            print(
                student["id"],
                "-",
                student["name"],
                ": No mark"
            )



number_of_students = input_number_of_students()
input_students(number_of_students)

number_of_courses = input_number_of_courses()
input_courses(number_of_courses)

input_marks()

list_courses()
list_students()
show_student_marks()
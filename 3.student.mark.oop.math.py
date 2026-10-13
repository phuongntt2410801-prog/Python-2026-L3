import math

class Course:
    def __init__(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # course_id -> float mark
        self.gpa = 0.0

    def add_mark(self, course_id, mark):
        # Use math.floor to round-down to 1-digit decimal upon input
        self.marks[course_id] = math.floor(mark * 10) / 10

    def calculate_gpa(self, courses):
        total_weighted_marks = 0.0
        total_credits = 0
        
        for course_id, mark in self.marks.items():
            if course_id in courses:
                credits = courses[course_id].credits
                total_weighted_marks += mark * credits
                total_credits += credits
        
        if total_credits == 0:
            self.gpa = 0.0
        else:
            self.gpa = total_weighted_marks / total_credits
        return self.gpa

class SchoolManagement:
    def __init__(self):
        self.students = []
        self.courses = {}  # course_id -> Course object

    def input_students(self):
        count = int(input("Enter number of students: "))
        for _ in range(count):
            s_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            self.students.append(Student(s_id, name, dob))

    def input_courses(self):
        count = int(input("Enter number of courses: "))
        for _ in range(count):
            c_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credits = int(input("Enter course credits: "))
            self.courses[c_id] = Course(c_id, name, credits)

    def input_marks(self):
        if not self.courses:
            print("No courses available. Please add courses first.")
            return
        
        print("\n--- Available Courses ---")
        for c_id, course in self.courses.items():
            print(f"[{c_id}] {course.name}")
            
        c_id = input("Select course ID to enter marks: ")
        if c_id not in self.courses:
            print("Invalid course ID!")
            return

        print(f"\nEntering marks for course: {self.courses[c_id].name}")
        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} ({student.id}): "))
            student.add_mark(c_id, mark)

    def list_students(self):
        if not self.students:
            print("No students registered yet.")
            return
            
        # Calculate GPA for all students before sorting
        for student in self.students:
            student.calculate_gpa(self.courses)
            
        # Sort student list by GPA descending using built-in sorting
        self.students.sort(key=lambda s: s.gpa, reverse=True)

        print("\n" + "="*55)
        print(f"{'ID':<8}{'Name':<15}{'DoB':<13}{'GPA (Sorted Descending)':<10}")
        print("="*55)
        for student in self.students:
            print(f"{student.id:<8}{student.name:<15}{student.dob:<13}{student.gpa:<10.1f}")
        print("="*55)

def main():
    system = SchoolManagement()
    
    while True:
        print("\n=== STUDENT MARK MANAGEMENT ===")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. Show Student List (Sorted by GPA)")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            system.input_students()
        elif choice == '2':
            system.input_courses()
        elif choice == '3':
            system.input_marks()
        elif choice == '4':
            system.list_students()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

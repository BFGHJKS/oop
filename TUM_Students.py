
import logging
import os

logging.basicConfig(filename='student_management.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Student:
    def __init__(self, student_id, name, email, faculty=None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.faculty = faculty

class Faculty:
    def __init__(self, faculty_id, name, field):
        self.faculty_id = faculty_id
        self.name = name
        self.field = field
        self.students = []

    def assign_student(self, student):
        student.faculty = self
        self.students.append(student)
        logging.info(f"Student {student.name} assigned to {self.name} faculty.")

    def graduate_student(self, student):
        if student in self.students:
            self.students.remove(student)
            logging.info(f"Student {student.name} graduated from {self.name} faculty.")

class University:
    def __init__(self):
        self.faculties = []

    def create_faculty(self, faculty_id, name, field):
        faculty = Faculty(faculty_id, name, field)
        self.faculties.append(faculty)
        logging.info(f"Faculty {faculty.name} created successfully.")
        return faculty

    def search_faculty_by_student_identifier(self, identifier):
        for faculty in self.faculties:
            for student in faculty.students:
                if student.student_id == identifier or student.email == identifier:
                    return faculty
        return None

    def display_all_faculties(self):
        for faculty in self.faculties:
            print(f"Faculty ID: {faculty.faculty_id}, Name: {faculty.name}, Field: {faculty.field}")

    def display_faculties_by_field(self, field):
        matching_faculties = [faculty for faculty in self.faculties if faculty.field == field]
        for faculty in matching_faculties:
            print(f"Faculty ID: {faculty.faculty_id}, Name: {faculty.name}, Field: {faculty.field}")


def batch_enroll_students(university, faculty_id, file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                student_id, name, email = data
                faculty = next((f for f in university.faculties if f.faculty_id == faculty_id), None)
                if not faculty:
                    print("Faculty not found!")
                    return
                student = Student(student_id, name, email)
                faculty.assign_student(student)
                print(f"{student.name} assigned to {faculty.name} faculty successfully!")
                logging.info(f"Batch enrollment: {student.name} assigned to {faculty.name} faculty.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error during batch enrollment: {e}")


def batch_graduate_students(university, faculty_id, file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                student_id = line.strip()
                faculty = next((f for f in university.faculties if f.faculty_id == faculty_id), None)
                if not faculty:
                    print("Faculty not found!")
                    return
                student = next((s for s in faculty.students if s.student_id == student_id), None)
                if student:
                    faculty.graduate_student(student)
                    print(f"{student.name} graduated from {faculty.name} faculty successfully!")
                    logging.info(f"Batch graduation: {student.name} graduated from {faculty.name} faculty.")
                else:
                    print(f"Student with ID {student_id} not found in the faculty.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error during batch graduation: {e}")


def validate_operation_choice(choice):
    valid_choices = ["1", "2", "3", "4", "5", "0"]
    if choice not in valid_choices:
        raise ValueError("Invalid choice. Please try again.")

def validate_file_path(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File not found.")

def main():
    tum_university = University()

    while True:
        print("\n======= TUM Student Management =======")
        print("1. Create a new faculty")
        print("2. Search faculty by student identifier")
        print("3. Display all faculties")
        print("4. Display faculties by field")
        print("5. Faculty Operations")
        print("0. Exit")

        choice = input("Enter your choice: ")

        try:
            validate_operation_choice(choice)

            if choice == "1":
                faculty_id = input("Enter Faculty ID: ")
                name = input("Enter Faculty Name: ")
                field = input("Enter Field: ")
                tum_university.create_faculty(faculty_id, name, field)
                print("Faculty created successfully!")

            elif choice == "2":
                identifier = input("Enter student identifier (ID or email): ")
                faculty = tum_university.search_faculty_by_student_identifier(identifier)
                if faculty:
                    print(f"The student belongs to {faculty.name} faculty.")
                else:
                    print("Student not found or not assigned to any faculty.")

            elif choice == "3":
                tum_university.display_all_faculties()

            elif choice == "4":
                field = input("Enter the field to display faculties: ")
                tum_university.display_faculties_by_field(field)

            elif choice == "5":
                faculty_id = input("Enter Faculty ID: ")
                faculty = next((f for f in tum_university.faculties if f.faculty_id == faculty_id), None)
                if not faculty:
                    print("Faculty not found!")
                    continue

                print("\nFaculty Operations:")
                print("1. Create and assign a student to faculty")
                print("2. Graduate a student from faculty")
                print("3. Display current enrolled students")
                print("4. Display graduates")
                print("5. Check if a student belongs to this faculty")
                print("6. Batch enroll students via text file")
                print("7. Batch graduate students via text file")
                choice2 = input("Enter your choice: ")

                validate_operation_choice(choice2)

                if choice2 == "1":
                    student_id = input("Enter Student ID: ")
                    name = input("Enter Student Name: ")
                    email = input("Enter Student Email: ")
                    student = Student(student_id, name, email)
                    faculty.assign_student(student)
                    print(f"{student.name} assigned to {faculty.name} faculty successfully!")

                elif choice2 == "2":
                    student_id = input("Enter Student ID to graduate: ")
                    student = next((s for s in faculty.students if s.student_id == student_id), None)
                    if student:
                        faculty.graduate_student(student)
                        print(f"{student.name} graduated from {faculty.name} faculty successfully!")
                    else:
                        print("Student not found in the faculty.")

                elif choice2 == "3":
                    print(f"Current enrolled students in {faculty.name} faculty:")
                    for student in faculty.students:
                        print(f"Student ID: {student.student_id}, Name: {student.name}, Email: {student.email}")

                elif choice2 == "4":
                    print(f"Graduates from {faculty.name} faculty:")
                    for student in faculty.students:
                        print(f"Student ID: {student.student_id}, Name: {student.name}, Email: {student.email}")

                elif choice2 == "5":
                    student_id = input("Enter Student ID to check: ")
                    student = next((s for s in faculty.students if s.student_id == student_id), None)
                    if student:
                        print(f"Yes, {student.name} belongs to {faculty.name} faculty.")
                    else:
                        print("No, the student does not belong to this faculty.")

                elif choice2 == "6":
                    file_path = input("Enter the path to the text file for batch enrollment: ")
                    validate_file_path(file_path)
                    batch_enroll_students(tum_university, faculty_id, file_path)

                elif choice2 == "7":
                    file_path = input("Enter the path to the text file for batch graduation: ")
                    validate_file_path(file_path)
                    batch_graduate_students(tum_university, faculty_id, file_path)

            elif choice == "0":
                print("Exiting program.")
                break

        except ValueError as ve:
            print(f"Error: {ve}")

if __name__ == "__main__":
    main()

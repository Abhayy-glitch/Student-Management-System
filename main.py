def add_student():
    name = input("Enter Student Name: ")

    file = open("students.txt", "a")
    file.write(name + "\n")
    file.close()

    print("Student Added Successfully")


def view_students():
    file = open("students.txt", "r")

    data = file.readlines()

    if len(data) == 0:
        print("No Students Found")
    else:
        print("\nStudent List:")
        for student in data:
            print(student.strip())

    file.close()


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
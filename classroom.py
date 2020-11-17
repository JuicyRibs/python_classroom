import time

users = []


def startMenu():
    print("Welcome to Classroom!")
    start = input("Please input...\n0 for register\n1 for sign in")
    if (start == "0"):
        register()
    elif (start == "1"):
        singIn()
    else:
        print("Invalid command")
        startMenu()


def register():
    stdid = input("Student ID: ")
    for user in users:
        if user["Student ID"] == stdid:
            print("User already exist\nExiting program")
            for i in range(3):
                print(".", end=" ")
                time.sleep(0.5)
                return null
        else:
            continue
            
    info = {
        "Student ID" : stdid,
        "Student Name" : input("Student Name: "),
        "Student Surname" : input("Student Surname: "),
        "Age": input("Age: "),
<<<<<<< HEAD
        "School Name" : input("School Name: "),
        "Year" : input("Year: ")
        "Telephone Number" : input("Telephone Number: "),
        "Course Name" : input("Course Name: "),
        "Hour left" : 100,
        "Username" : input("Username: "),
        "Password" : input("Password: "),
=======
        "School Name" : input("School Name: ")
        "Year" : input("Year: ")
        "Telephone Number" : input("Telephone Number: ")
        "Course Name" : input("Course Name: ")
        "Hour left" : 100
        "Username" : input("Username: ")
        "Password" : input("Password: ")
>>>>>>> main
        "Courses ID" : input("Courses ID: ").split(sep=",")
    }




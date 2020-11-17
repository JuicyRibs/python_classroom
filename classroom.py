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
                return
        else:
            continue
            
    info = {
        "Student ID" : stdid,
        "Student Name" : input("Student Name: "),
        "Student Surname" : input("Student Surname: "),
        "Age": input("Age: "),
        "School Name" : input("School Name: "),
        "Year" : input("Year: "),
        "Telephone": input("Telephone: "),
        "Course Name" : input("Course Name: "),
        "Hour left" : 100,
        "Username" : input("Username: "),
        "Password" : input("Password: "),
        "Courses ID" : input("Courses ID: ").split(sep=",")
    }

    users.append(info)



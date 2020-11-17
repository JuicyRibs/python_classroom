user = {}


def startMenu():
    print("Welcome to Classroom!")
    start = input("Please input...\n0 for register\n1 for sign in")
    if (start == "0"):
        # Go to register
        register()
    elif (start == "1"):
        # Go to sign in
        singIn()
    else:
        print("Invalid command")
        startMenu()


def register():
    stdid = input("Student ID: ")
    if (stdid in user):
        print("User already exist")
        register()
    else:
        info = list([input("Student Name: ")])
        info.append(input("Student Surname: "))
        info.append(input("Age: "))
        info.append(input("School Name: "))
        info.append(input("Year: "))
        info.append(input("Telephone Number: "))
        info.append(input("Course Name: "))
        info.append(100)
        info.append(input("Username: "))
        info.append(input("Password: "))
        info.append(input("Courses ID: ").split(sep=","))
        print(info)


register()

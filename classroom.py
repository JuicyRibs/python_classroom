import time

users = []


def startMenu():
    print("Welcome to Classroom!")
    start = input("Please input...\n0 for register\n1 for sign in\n")
    if (start == "0"):
        return register()
    elif (start == "1"):
        return signIn()
    else:
        print("Invalid command")
        return startMenu()


def register():
    stdid = input("Student ID: ")
    for user in users:
        if user.stdid == stdid:
            print("User already exist\nExiting program")
            for i in range(3):
                print(".", end=" ")
                time.sleep(0.5)
                return startMenu()
        else:
            continue
    name = input("Student Name: ")
    surname = input("Student Surname: ")
    age = input("Age: ")
    school = input("School Name: ")
    year = input("Year: ")
    phone = input("Telephone: ")
    course = input("Course Name: ")
    hour = 100
    username = input("Username: ")
    password = input("Password: ")
    courses = input("Courses ID: ").split(sep=",")

    newUser = student(name, surname, age, stdid, school, year, phone, course, username, password, hour, courses)

    users.append(newUser)
    return landingPage(newUser)

def signIn():
    enterUser = input("Username: ")
    for user in users:
        if (enterUser == user.username):
            enterPw = input("Password: ")
            if (enterPw == user.password):
                print("Sign in success")
                time.sleep(1)
                return landingPage(user)
            else:
                print("Invalid password")
                return signIn()
        print("User not found")
        return signIn()
                
def landingPage(user):
    user.printInfo()

class student:
    def __init__(self, name, surname, age, stdid, school, year, phone, course, username, password, timeleft, courses):
        self.name = name
        self.age = age
        self.surname = surname
        self.age = age
        self.stdid = stdid
        self.school = school
        self.year = year
        self.username = username
        self.password = password
        self.timeleft = timeleft
        self.phone = phone
        self.course = course
        self.courses = courses

    def printInfo(self):
        print("\n\n\n")
        print("Welcome, " + self.name)
        print("Surname: " + self.surname)
        print("Age: " + str(self.age))
        print("student ID: " + str(self.stdid))
        print("School: " + self.school)
        print("year: " + str(self.year))
        print("username: " + self.username)
        print("timeleft: "+str(self.timeleft))
        print("Courses: "+str(self.courses))

# classroom 100 seats


class classRoom:
    def __init__(self, seats):
        self.seats = 100
    # Seat will decrease when has student reserve

    def classRoomInfo(self):
        print(str(self.seats))

startMenu()
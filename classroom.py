import time

users = []

def programInit():
    userdata = open("userdata.txt")
    for line in userdata:
        info = line.split(sep=",")
        std = student(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9],info[10],info[11])
        users.append(std)

def startMenu():
    programInit()
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
    username = input("Username: ")   
    for user in users:
        print(getattr(user, 'username'))
        if getattr(user, 'username') == username:
            print("User already exist\nExiting program")
            for i in range(4):
                print(".", end=" ")
                time.sleep(1)
            exit()
        else:
            continue
    password = input("Password: ")
    name = input("Student Name: ")
    surname = input("Student Surname: ")
    stdid = input("Student ID: ")
    age = input("Age: ")
    school = input("School Name: ")
    year = input("Year: ")
    phone = input("Telephone: ")
    course = input("Course Name: ")
    hour = 100
    courseID = input("Course ID: ")

    newUser = student(name, surname, age, stdid, school, year, phone, course, username, password, hour, courseID)
    addTo = open("userdata.txt", "a")
    addTo.write(name+","+surname+","+age+","+stdid+","+school+","+year+","+phone+","+course+","+username+","+password+","+str(hour)+","+courseID+"\n")
    users.append(newUser)
    addTo.close()
    print("Add more user?\n")
    ex = input("1 to add more\n2 to go back to start menu\n")
    if (ex == "1"):
        return register()
    elif (ex == "2"):
        return startMenu()
    else: exit()

    

def signIn():
    enterUser = input("Username: ")
    for user in users:
        if (enterUser == getattr(user, 'username')):
            enterPw = input("Password: ")
            if (enterPw == getattr(user, 'password')):
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
    def __init__(self, name, surname, age, stdid, school, year, phone, course, username, password, timeleft, courseID):
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
        self.courseID = courseID

    def printInfo(self):
        print("\n\n")
        print("Welcome, ",self.name,self.surname)
        print("Age: " + str(self.age))
        print("student ID: " + str(self.stdid))
        print("School: " + self.school)
        print("year: " + str(self.year))
        print("username: " + self.username)
        print("timeleft: "+str(self.timeleft))
        print("Course ID: "+str(self.courseID))

# classroom 100 seats


class classRoom:
    def __init__(self, seats):
        self.seats = 100
    # Seat will decrease when has student reserve

    def classRoomInfo(self):
        print(str(self.seats))

startMenu()
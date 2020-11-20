import time
import datetime

users = []


def programInit():
    userdata = open("userdata.csv")
    for line in userdata:
        info = line.split(sep=",")
        std = student(info[0], info[1], info[2], info[3], info[4], info[5],
                      info[6], info[7], info[8], info[9], info[10], info[11], info[12])
        users.append(std)

def programExit():
    userdata = open("userdata.csv", 'x')
    for user in users:
        userdata.write("")

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
        if getattr(user, 'username') == username:
            print("User already exist\nExiting program")
            return register()
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

    newUser = student(name, surname, age, stdid, school, year,
                      phone, course, username, password, hour, courseID)
    addTo = open("userdata.csv", "a")
    addTo.write(name+","+surname+","+age+","+stdid+","+school+","+year+"," +
                phone+","+course+","+username+","+password+","+str(hour)+","+courseID+"\n")
    users.append(newUser)
    addTo.close()
    time.sleep(1)
    print("\n", name, surname, "added succesfully!")
    print("Add more user?\n")
    ex = input("1 to add more\n2 to go back to start menu\n")
    if (ex == "1"):
        return register()
    elif (ex == "2"):
        return startMenu()
    else:
        print("Invalid command\nExiting program")
        exit()


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
    return bookSeat(user)


def bookSeat(user):
    now = datetime.datetime.now()
    print("\nToday is", now.strftime("%x"), now.strftime("%X"))
    bookDate = int(input("Enter date of booking: "))
    bookMonth = int(input("Enter month of booking: "))
    bookYear = int(input("Enter year of booking: "))
    book = datetime.datetime(bookYear, bookMonth, bookDate)
    if (book.day-now.day > 3):
        print("Booking is only available 3 days in advance")
        return landingPage(user)
    elif (book.day-now.day < 0):
        print("Invalid date")
        return bookSeat(user)
    else:
        bookTime = input("Enter time of booking (hh:mm): ")
        bookTime = bookTime.split(":")
        bookTime = datetime.datetime(
            bookDate, bookMonth, bookYear, int(bookTime[0]), int(bookTime[1]))
        if ((book.strftime("%x") == now.strftime("%x")) and bookTime.hour - now.hour < 1):
            print("Booking is only available at least 1 hour in advance")
            return bookSeat(user)
        else:
            hours = int(input("How many hours?: "))
            if hours < 1:
                print("Minimum 1 hour")
            else:
                seat = int(input("Enter seat: "))
                if (seat > 100):
                    print("Invalid seat")
                    return bookSeat(user)
                else:
                    subject = input("Enter subject: ")
                    return confirmBooking(user, bookTime, hours, seat, subject)


def confirmBooking(user, bookTime, hours, seat, subject):
    setattr(user, 'bookingHistory', (getattr(user, 'bookingHistory')).append(booking(bookTime, hours, seat, subject)))


class student:
    bookingHistory = []

    def __init__(self, name, surname, age, stdid, school, year, phone, course, username, password, timeleft, courseID):
        student(name, surname, age, stdid, school, year, phone, course, username, password, timeleft, courseID, [])

    def __init__(self, name, surname, age, stdid, school, year, phone, course, username, password, timeleft, courseID, bookingHistory):
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
        self.bookingHistory = bookingHistory

    def printInfo(self):
        print("\n")
        print("Welcome, ", self.name, self.surname)
        print("Age: " + str(self.age))
        print("student ID: " + str(self.stdid))
        print("School: " + self.school)
        print("year: " + str(self.year))
        print("username: " + self.username)
        print("timeleft: "+str(self.timeleft))
        print("Course ID: "+str(self.courseID))

# classroom 100 seats

class booking:
    def __init__(self, bookTime, hours, seat, subject):
        self.bookTime = bookTime
        self.hours = hours
        self.seat = seat
        self.subject = subject
    
        

class classRoom:
    def __init__(self, seats):
        self.seats = 100
    # Seat will decrease when has student reserve

    def classRoomInfo(self):
        print(str(self.seats))


startMenu()

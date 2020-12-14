import datetime
import os

users = []
bookingList = []

def programInit():
    with open("userdata.csv") as userdata:
        for line in userdata:
            info = line.split(sep=",")
            # print(info)
            if (len(info) > 1):
                std = student(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9], info[10])
                users.append(std)
    print(users)
    print(len(users))
    bookingHistory = open("bookingHistory.csv")
    for line in bookingHistory:
        info = line.split(sep=",")
        book = booking(info[0], info[1], info[2], info[3])
        bookingList.append(book)
    bookingHistory.close()
    return startMenu()

def programExit():
    print(users)
    if os.path.exists("userdata.csv"):
        os.remove("userdata.csv")
    with open("userdata.csv", 'w') as userdata:
        for i in range(0,len(users)):
            user = users[i]
            username = getattr(user,"username")
            password = getattr(user,"password")
            name = getattr(user,"name")
            surname = getattr(user,"surname")
            stdid = getattr(user,"stdid")
            age = getattr(user,"age")
            school = getattr(user,"school")
            year = getattr(user,"year")
            phone = getattr(user,"phone")
            hour = getattr(user,"timeleft")
            courseID = getattr(user,"courseID")
            newUser = name+","+surname+","+age+","+stdid+","+school+","+year+"," + phone +","+username+","+password+","+str(hour)+","+courseID
            print(newUser)
            userdata.write(newUser)
    users.clear()
    return exit()

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
    hour = 100
    courseID = input("Course ID: ")
    if (checkCourse(courseID)):
        newUser = student(name, surname, age, stdid, school, year,
                        phone, username, password, hour, courseID)
        users.append(newUser)
        print(users,len(users),sep="\n")
        print("")
        print(name, surname, "added succesfully!")
        print("Add more user?\n")
        ex = input("1 to add more\n2 to go back to start menu\n")
        if (ex == "1"):
            return register()
        elif (ex == "2"):
            return startMenu()
        else:
            print("Invalid command\nExiting program")
            return programExit()
    else:
        print("Invalid course ID\nExiting program")
        return programExit()

def checkCourse(courseID):
    idList = []
    courses = open("courseList.csv",'r')
    for course in courses:
        idList.append((course.split(","))[0])
    if (courseID not in idList):
        return False
    return True

def signIn():
    enterUser = input("Username: ")
    for user in users:
        if (enterUser == getattr(user, 'username')):
            enterPw = input("Password: ")
            if (enterPw == getattr(user, 'password')):
                print("Sign in success")
                return landingPage(user)
            else:
                print("Invalid password")
                return signIn()
    print("User not found")
    return signIn()


def landingPage(user):
    user.printInfo()
    page = input(
        "\nPlease select...\n3 for Booking seat\n4 for Cancel booking\n5 for adding course to system\n6 for changing your course\n")
    if page == "3": 
        return bookSeat(user)
    if page == "4": 
        return cancelBooking(user)
    if page == "5": 
        return addcourse()
    if page == "6": 
        return changecourse(user)

def bookSeat(user):
    now = datetime.datetime.now()
    print("\nToday is", now.strftime("%d-%m-%Y"), now.strftime("%d-%m-%Y"))
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
            bookYear, bookMonth, bookDate, int(bookTime[0]), int(bookTime[1]))
        if ((book.strftime("%d-%m-%Y") == now.strftime("%d-%m-%Y")) and bookTime.hour - now.hour < 1):
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
                    return confirmBooking(user, bookTime, hours, seat)

def cancelBooking(user):
    deleteEntry = []
    usern = getattr(user,"username")
    for entry in bookingList:
        if(getattr(entry,"username") == usern):
            entry.printInfo()
            if (input("Cancel this entry? Y/N: ") == "Y"):
                tUser = getattr(entry,"username")
                tStartTime = getattr(entry,"bookTime")
                tHour = getattr(entry,"hours")
                tSeat = getattr(entry,"seat")
                temp = (tUser+","+tStartTime+","+tHour+","+tSeat)
                setattr(user,"timeleft", getattr(user,"timeleft")+int(tHour))
                deleteEntry.append(temp)
    with open("bookingHistory.csv", 'r') as f:
        lines = f.readlines()
    with open("bookingHistory.csv", 'w') as f:
        for line in lines:
            if line not in deleteEntry:
                f.write(line)
    print("Booking not found.\nExiting program.")
    return programExit()


def confirmBooking(user, bookTime, hours, seat):
    print("\nBooking info")
    print("Booking start",str(bookTime))
    print("Booking hour",hours)
    print("Seat number",seat)
    confirm = input("\nConfirm booking? Y/N :")
    if confirm == "N":
        print("Booking canceled.\nExiting program")
        return programExit()
    elif confirm == "Y":
        newBook = booking(getattr(user,"username"),bookTime, hours, seat)
        bookingList.append(newBook)
        addTo = open("bookingHistory.csv", "a")
        addTo.write(getattr(user,"username")+","+str(bookTime)+","+str(hours)+","+str(seat)+"\n")
        setattr(user,"timeleft",(int(getattr(user,"timeleft"))-int(hours)))
        print("Booking success.\nExiting program.")
        return programExit()


def addcourse():
    sid = input("Enter course id: ")
    if (not checkCourse(sid)):
        name = input("Enter course name: ")
        addTo = open("courseList.csv.csv", "a")
        addTo.write(sid+","+name+"\n")
        print(sid,name,"added.\n")
        addTo.close()
        more = input("Add more course? Y/N :")
        if more=="Y":
            return addcourse()
        else:
            print("Exiting program")
            return programExit()
    else:
        print("Course ID already exists\n")


def changecourse(user):
    course = open("courseList.csv.csv", 'r')
    sidList = []
    for s in course:
        sid = s.split(",")
        sidList.append(sid)
    newSub = input("Enter new course ID: ")
    for s in sidList:
        if newSub == s[0]:
            setattr(user,"courseID",newSub)
            print("\nCourse changed to",s[1],"Course ID",s[0],"\n\nResetting hour to 100...")
            setattr(user,"timeLeft",100)
            print("Exiting program")
            return programExit()
    print("Course not found. Exiting program")
    return programExit()



class student:

    def __init__(self, name, surname, age, stdid, school, year, phone, username, password, timeleft, courseID):
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
        self.courseID = courseID

    def printInfo(self):
        print("\n")
        print("Welcome,", self.name, self.surname)
        print("Age: " + str(self.age))
        print("student ID: " + str(self.stdid))
        print("School: " + self.school)
        print("year: " + str(self.year))
        print("username: " + self.username)
        print("timeleft: "+str(self.timeleft))
        print("Course ID: "+str(self.courseID))


class booking:
    def __init__(self, username, bookTime, hours, seat):
        self.username = username
        self.bookTime = bookTime
        self.hours = hours
        self.seat = seat

    def printInfo(self):
        print("Booking time: ", str(self.bookTime))
        print("Hours: ",self.hours)
        print("Seat Number: ",self.seat)

programInit()


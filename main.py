import datetime
import calendar


class DOB:
    def findDay(self):
        birthday = str(input("Enter your Date of Birth:"))
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = datetime.datetime.strptime(birthday, "%d %m %Y").weekday()
        return days[day]

dob = DOB()
print(dob.findDay())


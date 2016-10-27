class time:
    def __init__(self,hours,minutes,seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def set_Time(self):
        

    def increment(self):
        seconds +=1
        if seconds <= 59 :
            seconds += 1
        if seconds == 60
            seconds = 0
            minutues += 1
        if minuteues == 60:
            minutues = 0
            hours += 1
        if hours == 24:
            hours = 0

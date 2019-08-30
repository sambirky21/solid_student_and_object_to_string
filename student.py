# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)

class Student():

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age}, and in cohort {self.cohort_number}: {self.full_name}.'

    #First Name
    @property # The getter
    def first_name(self):
        try:
            return self.__first_name # Note there are 2 underscores here
        except AttributeError:
            return "First Name"

    @first_name.setter # The setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Please provide a string value for the first_name')

    #Last Name
    @property # The getter
    def last_name(self):
        try:
            return self.__last_name # Note there are 2 underscores here
        except AttributeError:
            return "Last Name"

    @last_name.setter # The setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('Please provide a string value for the last_name')

    #Age
    @property # The getter
    def age(self):
        try:
            return self.__age # Note there are 2 underscores here
        except AttributeError:
            return 0
    @age.setter # The setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please provide a floating point value for the age')

    #Cohort Number
    @property # The getter
    def cohort_number(self):
        try:
            return self.__cohort_number # Note there are 2 underscores here
        except AttributeError:
            return 0

    @cohort_number.setter # The setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError('Please provide an integer value for the cohort number')

    #Full Name
    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return 0

Sam = Student()
Sam.cohort_number = 2
Sam.first_name = "Sam"
Sam.last_name = "Birky"
Sam.age = 26
print(Sam)
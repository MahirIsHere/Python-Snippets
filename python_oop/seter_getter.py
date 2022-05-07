class Student:
    def __init__(self, fname, lname, year):
        self.fname = fname
        self.lname = lname
        self.graduationyear = year

    def get_fname(self):  # getter method
        return self.fname

    def get_lname(self):  # getter method
        return self.lname

    def set_lname(self, lname):
        self.lname = lname

    def get_graduationyear(self):  # getter method
        return self.graduationyear

    def set_lname(self, lname):  # setter-method
        self.lname = lname

    def set_graduationyear(self, year):
        self.graduationyear = year


y = Student("Oloka", "Shushupti", 2021)
print(y.get_fname())  # calling getter method

y.set_graduationyear(2022)
y.set_lname("Rahman")
print(y.get_lname())  # calling getter method

print(y.get_graduationyear())  # calling getter method


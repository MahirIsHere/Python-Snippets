class person():
    population=50
    def init(self,name,age,race):
        self.name = name
        self.age = age
        self.race = race
    @classmethod
    def getPopulation(cls):
        return cls.population
    @staticmethod
    def isAdult(age):
        return age>=18
    def display (self):
        print(self.name, self.age,self.race)
    
    newPerson= person ("Mahir",22,"Bangladeshi")
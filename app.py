from datetime import datetime

class Person(object):

    def __init__(self, firstname, lastname, birthday=[0, 0, 0]):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday

        now = datetime.now()

        self.age = now.year - birthday[2] 


class Employee(Person):

    def can_retire(self):
        if self.age > 60:
            return True
        else:
            return False

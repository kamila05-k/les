"""from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @abstractmethod
    def get_summary(self):
        pass
class Fiction(Book):
    def get_summary(self):
        pass
    def ged_author(self):
        return f"Author {self.author}, title {self.title}"
class Nofiction(Book):
    def get_summary(self):
        return f"Book {self.title}, author {self.author}"

fic = Fiction("Martin Iden", "Jack London")
print(fic.ged_author())
no = Nofiction("Mark Iven", "Adv")
print(no.get_summary())
"""
"""
from abc import ABC, abstractmethod

class Cook(ABC):
    def __init__(self, food):
        self.food = food
    @ abstractmethod
    def Cook(self):
        pass

class Entree(Cook):
    def Cook(self):
        return f"{self.food}"
class Desert(Entree):
    def Cook(self):
        return f"{self.food}"

entree = Entree("Meat of france")
print(entree.Cook())
desert = Desert("Ice eream")
print(desert.Cook())
"""

#from abc import ABC, abstractmethod
class Abstractuser:
    def __init__(self, firs_name, last_name, cmail, password):
        self.firs_name = firs_name
        self.last_name = last_name
        self._cmail = cmail
        self._password = password

class User(Abstractuser):
    def users(self, age, gender):
        self.age = age
        self.gender = gender
        return (self.firs_name, self.last_name, self.age, self.gender)

us = User("Kamila", "Taalaibek kuzu", "kamil.a13", 657)
print(us.users(18, "J"))
print(us._password)
print(us._cmail)











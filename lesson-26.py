"""class Nam:
    def __init__(self, name, paswort):
        self.name = name
        self._paswort = paswort

nam = Nam('Kamila', 1244)
print(nam.name)
print(nam._paswort)

class Nam:
    def __init__(self, name, paswort):
        self.name = name
        self.__paswort = paswort

nam = Nam('Kamila', 1244)
print(nam.name)
print(nam._Nam__paswort)
"""

class Nam:
    def __init__(self, name, age, married):
        self.name = name
        self._age = age
        self.__married = married

nam = Nam("Kamila", 18, "not")
print(nam.name)
print(nam._age)
print(nam._Nam__married)
nam._Nam__married = ("Yes")
print(nam._Nam__married)

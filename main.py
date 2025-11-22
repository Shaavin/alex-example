class Student:
    def __init__(self, name, house):
        self._name = name
        self._house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @property
    def house(self):
        return self._house

    @name.setter
    def name(self, name):
        if not name.strip():
            raise ValueError("Name is required")
        self._name = name

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = Student(name="Harry", house="Gryffindor")
    print(student)

if __name__ == "__main__":
    main()
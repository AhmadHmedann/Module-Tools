class Parent:  # Implement a class   called Parent
    def __init__(
        self, first_name: str, last_name: str
    ):  # Constructor that initializes the object's attributes.
        self.first_name = first_name  # Create the 'first_name' attribute and assign the constructor argument to it
        self.last_name = last_name

    def get_name(self) -> str:  # Return the person's first name.
        return f"{self.first_name} {self.last_name}"


class Child(Parent):  # Implement a class called Child that inherit the class Parent
    def __init__(
        self, first_name: str, last_name: str
    ):  # Constructor for derived class
        super().__init__(
            first_name, last_name
        )  # call the parent class to initialize inherited attributes.
        self.previous_last_names = []  # Create a list to store Previous last names

    def change_last_name(
        self, last_name: str
    ) -> None:  # implement a function that take one  parameter (the new name)
        self.previous_last_names.append(
            self.last_name
        )  # and  store the last name before setting a new value
        self.last_name = last_name

    def get_full_name(
        self,
    ) -> (
        str
    ):  # declare a var and  return full name with "nee "and fist name that assign when the object where declare
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"


person1 = Child(
    "Elizaveta", "Alekseeva"
)  # declare an object of Child class and give two arguments as firstname and last name
print(person1.get_name())  # print full name (Elizaveta Alekseeva)
print(
    person1.get_full_name()
)  # print full name (Elizaveta Alekseeva) we did not change the last name yet
person1.change_last_name(
    "Tyurina"
)  # store the last name in pervious_last_name list then set a new value for last name "Tyurina"
print(person1.get_name())  #  #print full name (Elizaveta Tyurina)
print(person1.get_full_name())  # print Elizaveta Tyurina (née Alekseeva)
person2 = Parent(
    "Elizaveta", "Alekseeva"
)  # declare an object of Parent class and give two arguments as firstname and last name
print(person2.get_name())  # print full name (Elizaveta Alekseeva)
# print(person2.get_full_name())                                            # Error: Parent does not define get_full_name().
# person2.change_last_name("Tyurina")                                     ## Error: Parent does not define change_last_name().
print(person2.get_name())  # print full name (Elizaveta Alekseeva)
# print(person2.get_full_name())                                          # Error: Parent does not define get_full_name().

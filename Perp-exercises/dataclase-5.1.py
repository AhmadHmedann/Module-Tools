from datetime import date
from dataclasses import dataclass


@dataclass(frozen=True)
class Person:

    name: str
    date_of_birth: date
    preferred_operating_system: str

    def age(self) -> int:
        current: date = date.today()
        age: int = current.year - self.date_of_birth.year
        if (current.month, current.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day,
        ):
            age -= 1
        return age

    def is_adult(self) -> bool:
        return self.age() >= 18


imran = Person("Imran", date(2022, 10, 16), "Ubuntu")
print(imran.is_adult())

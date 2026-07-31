from enum import Enum
from typing import List
from dataclasses import dataclass


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: int
    operating_system: OperatingSystem


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


laptops = [
    Laptop(
        id=1,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.ARCH,
    ),
    Laptop(
        id=2,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=3,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=4,
        manufacturer="Apple",
        model="macBook",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.MACOS,
    ),
]


def group_laptops_by_operating_system(
    laptops: List[Laptop],
) -> dict[OperatingSystem, List[Laptop]]:
    available_laptops: dict[OperatingSystem, List[Laptop]] = {
        OperatingSystem.UBUNTU: [],
        OperatingSystem.ARCH: [],
        OperatingSystem.MACOS: [],
    }
    for laptop in laptops:
        available_laptops[laptop.operating_system].append(laptop)

    return available_laptops


def how_many_match(
    person: Person, available_laptops: dict[OperatingSystem, List[Laptop]]
) -> int:
    return len(available_laptops[person.preferred_operating_system])


def most_available_operating_system(
    available_laptops: dict[OperatingSystem, List[Laptop]],
) -> OperatingSystem:
    if not available_laptops:
        raise ValueError("No operating systems available")
    max_len: int = -1
    most_available: OperatingSystem
    for key, val in available_laptops.items():
        if len(val) > max_len:
            max_len = len(val)
            most_available = key

    return most_available


def main() -> None:
    name: str = input("Name: ")
    age: int = int(input("Age: "))

    print("""choose an operating system:
          1.Ubuntu
          2,Arch Linux
          3.macOs""")
    choice: int = int(input("Enter Your choice: "))
    os_map: dict[int, OperatingSystem] = {
        1: OperatingSystem.UBUNTU,
        2: OperatingSystem.ARCH,
        3: OperatingSystem.MACOS,
    }

    preferred_operating_system: OperatingSystem = os_map[choice]

    person1: Person = Person(name, age, preferred_operating_system)

    laptops_by_operating_system = group_laptops_by_operating_system(laptops)
    matching_laptop_count: int = how_many_match(person1, laptops_by_operating_system)
    print("We have", matching_laptop_count, "matches")
    most_available_os: OperatingSystem = most_available_operating_system(
        laptops_by_operating_system
    )
    if person1.preferred_operating_system != most_available_os:
        print("Are you willing to accept ", most_available_os.value, "instead")


if __name__ == "__main__":
    main()

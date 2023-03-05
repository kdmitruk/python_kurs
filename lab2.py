from collections import namedtuple

Person = namedtuple("Person", "first_name, last_name, date_of_birth")


def main():
    p = Person("Jan", "Kowalski", "1.2.1970")
    p.last_name = "Nowak"
    print(p.last_name)


if __name__ == "__main__":
    main()
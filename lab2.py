from collections import namedtuple
import datetime

Person = namedtuple("Person", "first_name, last_name, date_of_birth")

def person_from_line(line : str):
    entry = line.split(",")
    return Person(entry[0],entry[1], datetime.datetime.strptime(entry[2],
                        "%Y-%m-%d"))
def main():
    # p = Person("Jan", "Kowalski", "1.2.1970")
    # p.last_name = "Nowak"
    # print(p.last_name)
    person_str = "Kial,Toffic,1998-07-25"
    p=person_from_line(person_str)
    print(p)

if __name__ == "__main__":
    main()
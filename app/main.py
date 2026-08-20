class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]

        person = Person(name, age)
        person_list.append(person)

    for person_data in people:
        current_person = Person.people[person_data["name"]]

        if person_data.get("wife"):
            current_person.wife = Person.people.get(person_data["wife"])

        if person_data.get("husband"):
            current_person.husband = Person.people.get(person_data["husband"])

    return person_list

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.vehicles = []

    def add_car(self, car):
        self.vehicles.append(car)

    def __repr__(self):
        return f"name={self.name}, email={self.email}, vehicles={self.vehicles}"


class Vehicle:
    def __init__(self, patent, color, owner):
        self.patent = patent
        self.color = color
        self.infractions = []
        self.number_of_infractions = 0
        self.owner = owner
        owner.add_car(self)

    def __repr__(self):
        return f"(patent={self.patent}, color={self.color}, number_of_infractions={self.number_of_infractions})"


class Offical:
    def __init__(self, name, identity_id):
        self.name = name
        self.identity_id = identity_id


class Infraction:
    def __init__(self, date, comments, patent_car, official_id):
        self.date = date
        self.comments = comments
        self.patent_car = patent_car
        self.official_id = official_id

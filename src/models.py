from datetime import date
from .app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    vehicles = db.relationship('Vehicle', backref='owner', lazy=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def add_vehicle(self, car):
        self.vehicles.append(car)

    def count_infraccions(self):
        infracctions = 0
        for vehicle in self.vehicles:
            infracctions += vehicle.number_of_infractions
        return infracctions

    def __repr__(self):
        return f"name={self.name}, email={self.email}"


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patent = db.Column(db.String(20), unique=True, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    infractions = db.relationship('Infraction', backref='vehicle', lazy=True)
    number_of_infractions = db.Column(db.Float, nullable=False, default=0)

    def __init__(self, patent, color, owner):
        self.patent = patent
        self.color = color
        self.owner = owner
        self.number_of_infractions = 0

    def __repr__(self):
        return f"(patent={self.patent}, color={self.color}, number_of_infractions={len(self.infractions)})"

    def add_infraction(self, new_infraction):
        self.infractions.append(new_infraction)
        self.number_of_infractions += 1


class Official(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    identity_id = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, name, identity_id):
        self.name = name
        self.identity_id = identity_id

    def assign_infraction(self, vehicle, comments, official_id="dafaul"):
        official_id = self.id
        new_infraction = Infraction(vehicle, comments, official_id)
        vehicle.add_infraction(new_infraction)


class Infraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=date.today)
    comments = db.Column(db.String(200), nullable=False)
    patent_car = db.Column(db.String(20), nullable=False)
    official_id = db.Column(db.Integer, db.ForeignKey('official.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    amount_to_pay = db.Column(db.Float, nullable=False, default=0)

    def __init__(self, vehicle, comment, official_id):
        self.comments = comment
        self.patent_car = vehicle.patent
        self.official_id = official_id

        self.date = date.today()
        self.vehicle_id = vehicle.id

    def __repr__(self):
        return f"'{self.comments}'"

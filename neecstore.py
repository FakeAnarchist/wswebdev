from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship, backref
from datetime import date
import pandas as pd
from sqlalchemy import or_

engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Team(Base):
    __tablename__= 'teams'
    id = Column(Integer, primary_key = True)
    money= Column(Float)
    team_name= Column(String)

    def __init__(self, team_name, project_name, money):
        self.team_name = team_name
        self.project_name = project_name
        self.money = money

##One to Many
class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    course = Column(String)
    age = Column(Integer)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", backref="persons")

    def __init__(self, name, age, course, team):
        self.name = name
        self.age = age
        self.course = course
        self.team = team

##One to Many
class Contact(Base):
    __tablename__ = 'contacts'
    
    id = Column(Integer, primary_key=True)
    phone = Column(Integer)
    email = Column(String)
    auth = Column(Boolean)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship("Person", backref="contacts")
    
    def __init__(self, phone, email, auth, person):
        self.phone = phone
        self.email = email
        self.auth = auth
        self.person = person

##Sem relacao
class Components(Base):
    __tablename__ = 'components'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    quantity = Column(Integer)
    link = Column(String)
    price = Column(Float)
    
    def __init__(self, name, description, quantity, link, price):
        self.name = name
        self.description = description
        self.quantity = quantity 
        self.link=link
        self.price = price

Base.metadata.create_all(engine)
session = Session()

prego = Components("prego", "para pregar", 20, "www.google.com/prego", 0.50)
martelo = Components("martelo", "para martelar", 45, "www.google.com/martelo", 1.20)

#session.add(martelo)
#session.add(prego)
#session.commit()



while True:
    action = input("enter your action: ")
    if action == "add":
        print("a fazer dps")
    if action == "print":
        components = session.query(Components.link).all()
        for component in components:
            print(component)
    if action == "exit":
        break
    

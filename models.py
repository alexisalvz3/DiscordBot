"""
In this file you must implement all your database models.
If you need to use the methods from your database.py call them
statically. For instance:
       # opens a new connection to your database
       connection = Database.connect()
       # closes the previous connection to avoid memory leaks
       connection.close()
"""
from pymysql import DATETIME
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database import Database


class TestModel:
    """
    This is an object model example. Note that
    this model doesn't implement a DB connection.
    """

    def __init__(self, ctx):
        self.ctx = ctx
        self.author = ctx.message.author.name

    def response(self):
        return f'Hi, {self.author}. I am alive'

Base = declarative_base()



class Country(Base):
  __tablename__ = 'Country'

  Country_id = Column(Integer, primary_key=True, nullable = False)
  Num_Manufacturers = Column(Integer)
  Num_Certs = Column(Integer)

def __init__(self, Country_id, Num_Manufacturers, Num_Certs):
  self.Country_id = Country_id
  self.Num_Manufacturers = Num_Manufacturers
  self.Num_Certs = Num_Certs

class Manufacturer:

  def __init__ (self, manufacturer_id): 
       self.id = manufacturer_id
       self.name = None 
       self.num_carbon = None
       self._load()

  def _load(): 
       manufacturer_data = Database.select(Query.GET_MANUFACTURER, self.id)[0]
       self.name = manufacturer_data['name']
       num_carbon = 
  @staticmethod
  def get(manufacturer_id): 
       return Manufacturer(manufacturer_id)

  @staticmethod
  def getAll():
      tmp_all_manufactureres = Database.select(Query.GET_ALL_MANUFACTURERS)
      manufacturers = [] 
      for tmp_manufacturer in tmp_all_manufactureres: 
          manufacturer = Manufacturer.get(tmp_manufacturer['manufacturer_id'])
          manufacturers.append(manufacturer)
      return manufacturers 
        
      
       
  

class Fullerene(Base):
  __tablename__ = 'Fullerene'

  Fullerene_id = Column(Integer, primary_key=True, nullable=False)
  Num_Carbon = Column(Integer)
  Synthesis_Method = Column(String(45))
  Product_Product_id = Column(Integer, ForeignKey('Product.Product_id'), nullable=False)

  def __init__(self, Fullerene_id, Num_Carbon, Synthesis_Method, Product_Product_id):
    self.Fullerene_id = Fullerene_id
    self.Num_Carbon = Num_Carbon
    self.Synthesis_Method = Synthesis_Method
    self.Product_Product_id = Product_Product_id

class Research_Project(Base):
  __tablename__ = 'Research_Project'

  Project_id = Column(Integer, primary_key=True, nullable=False)
  Researcher_id = Column(Integer, ForeignKey('Researcher.Researcher_id'), nullable=False)
  Research_Topic = Column(String(45))

  def __init__(self, Project_id, Researcher_id, Research_Topic):
    self.Project_id = Project_id
    self.Researcher_id = Researcher_id
    self.Research_Topic = Research_Topic

class Researcher(Base):
  __tablename__ = 'Researcher'

  Researcher_id = Column(Integer, primary_key=True, nullable=False)
  Years_Experience = Column(Integer)
  Num_Publications = Column(Integer)

  def __init__(self, Researcher_id, Years_Experience, Num_Publications):
    self.Researcher_id = Researcher_id
    self.Years_Experience = Years_Experience
    self.Num_Publications = Num_Publications

class Employee(Base):
  __tablename__ = 'Employee'

  Employee_id = Column(Integer, primary_key=True, nullable=False)
  Employee_title = Column(String(45))
  Salary = Column(Integer)
  Team_Team_id = Column(Integer, ForeignKey('Team.Team_id'))
  Manufacturer_Manufacturer_id = Column(Integer, ForeignKey('Manufacturer.Manufacturer_id'), nullable=False)

  def __init__(self, Employee_id, Employee_title, Salary, Team_Team_id, Manufacturer_Manufacturer_id):
    self.Employee_id = Employee_id
    self.Employee_title = Employee_title
    self.Salary = Salary
    self.Team_Team_id = Team_Team_id
    self.Manufacturer_Manufacturer_id = Manufacturer_Manufacturer_id

class Product(Base):
  __tablename__ = 'Product'

  Product_id = Column(Integer, primary_key=True, nullable=False)
  Industry_id = Column(Integer, ForeignKey('Industry.Industry_id'), nullable=False)
  Product_Type = Column(String(45))

  def __init__(self, Product_id, Industry_id, Product_Type):
    self.Product_id = Product_id
    self.Industry_id = Industry_id
    self.Product_Type = Product_Type

class Industry(Base):
  __tablename__ = 'Industry'

  Industry_id = Column(Integer, primary_key=True, nullable=False)
  Name = Column(String(45), nullable = False)
  Total_Revenue = Column(Integer)

  def __init__(self, Industry_id, Name, Total_Revenue):
    self.Industry_id = Industry_id
    self.Name = Name
    self.Total_Revenue = Total_Revenue

class Team(Base):
  __tablename__ = 'Team'

  Team_id = Column(Integer, primary_key=True, nullable=False)
  Team_title = Column(String(45))
  Num_Employees = Column(Integer)
  Manufacturer_Manufacturer_id = Column(Integer, ForeignKey('Manufacturer.Manufacturer_id'), nullable=False)

  def __init__(self, Team_id, Team_title, Num_Employees, Manufacturer_Manufacturer_id):
    self.Team_id = Team_id
    self.Team_title = Team_title
    self.Num_Employees = Num_Employees
    self.Manufacturer_Manufacturer_id = Manufacturer_Manufacturer_id

class User(Base):
  __tablename__ = 'User'

  user_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
  name = Column(String(45))
  Age = Column(Integer)
  role_id = Column(Integer, ForeignKey('Role.Role_id'))

  def __init__(self, user_id,name, Age, role_id):
    self.user_id = user_id
    self.name = name
    self.Age = Age
    self.role_id = role_id

class Role(Base):
  __tablename__ = 'Role'

  Role_id = Column(Integer, primary_key=True, nullable=False)
  Role_name = Column(String(45), nullable = False)
  Role_description = Column(String(45), nullable = False)

  def __init__(self, Role_id, Role_name, Role_description):
    self.Role_id = Role_id
    self.Role_name = Role_name
    self.Role_description = Role_description

class Account(Base):
  __tablename__ = 'Account'

  Account_id = Column(Integer, primary_key=True, nullable=False)
  Email = Column(String(45))
  Password = Column(String(45))
  User_user_id = Column(Integer, ForeignKey('User.user_id'), nullable = False)

  def __init__(self, Account_id, Email, Password, User_user_id):
    self.Account_id = Account_id
    self.Email = Email
    self.Password = Password
    self.User_user_id = User_user_id

class Publication(Base):
  __tablename__ = 'Publication'

  Publication_id = Column(Integer, primary_key=True, nullable=False)
  Researcher_id = Column(Integer, ForeignKey('Researcher.Researcher_id'), nullable = False)
  Date = Column(DATETIME)

  def __init__(self, Publication_id, Researcher_id, Date):
    self.Publication_id = Publication_id
    self.Researcher_id = Researcher_id
    self.Date = Date

class Nanowires(Base):
  __tablename__ = 'Nanowires'

  NanoW_id = Column(Integer, primary_key=True, nullable=False)
  Application = Column(String(45))
  Conductivity = Column(String(45))
  Product_Product_id = Column(Integer, ForeignKey('Product.Product_id'), nullable = False)

  def __init__(self, NanoW_id, Application, Conductivity, Product_Product_id):
    self.NanoW_id = NanoW_id
    self.Application = Application
    self.Conductivity = Conductivity
    self.Product_Product_id = Product_Product_id

class Subdivision(Base):
  __tablename__ = 'Subdivision'

  SubDiv_id = Column(Integer, primary_key=True, nullable=False)
  SubDiv_Name = Column(String(45))
  Head_Industry_id = Column(Integer, ForeignKey('Industry.Industry_id'), nullable = False)

  def __init__(self, SubDiv_id, SubDiv_Name, Head_Industry_id):
    self.SubDiv_id = SubDiv_id
    self.SubDiv_Name = SubDiv_Name
    self.Head_Industry_id = Head_Industry_id
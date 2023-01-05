import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)

class Planeta(Base):
    __tablename__ ='planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_planeta = Column(String(250), nullable=False)
    
class Planetasfavoritos(Base):
    __tablename__ = 'planetafav'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_planeta = Column(Integer, ForeignKey('planetas.id'))
    planeta= relationship(Planeta)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    usuario= relationship(Usuarios)



class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_personaje = Column(String(250), nullable=False)

class Personajesfavoritos(Base):
    __tablename__ = 'personajestafav'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_personajes = Column(Integer, ForeignKey('personaje.id'))
    personajes= relationship(Personaje)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    usuario= relationship(Usuarios)





   


 


    


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

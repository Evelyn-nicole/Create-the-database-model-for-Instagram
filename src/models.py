import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship('Person')


class Follower(Base):
    __tablename__= 'follower'
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, ForeignKey('follower.user_from_id'), ForeignKey('post.user_id'), ForeignKey('comment.author_id'), primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, ForeignKey ('media.post_id'), ForeignKey ('comment.post_id'), primary_key=True)
    user_id = Column(Integer)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    # type = Column()
    url = Column(String(250))
    post_id = Column(Integer)

class Commment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer)
    post_id = Column(Integer)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
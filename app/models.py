from flask import Markup
from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Integer, String



class ProductType(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Product(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    rok = Column(Integer, nullable=False)


    def rok_label(self):
        return Markup("Rok:<strong> {} </strong>".format(self.rok))

    def __repr__(self):
        return self.name


class Client(User):
    __tablename__ = "ab_user"
    extra = Column(String(50), unique=True, nullable=False)

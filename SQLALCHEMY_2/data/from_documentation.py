import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Parent(SqlAlchemyBase):
    __tablename__ = 'parent'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    children = sqlalchemy.orm.relationship("Child")

class Child(SqlAlchemyBase):
    __tablename__ = 'child'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    parent_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('parent.id'))
from api.models import *
from api import app
from api.models import session
from marshmallow import Schema, fields, post_load, pprint


class User(session.Model):
  __tablename__ = 'users'
  id = Column('id', Integer, primary_key=True)
  name = Column('name', String(50))
  address = Column('address', String(255))


  def to_join(self):
    return dict(name = self.name, address = self.address)

  def to_dict(self, user):
    return{
      'id': user.id,
      'name': user.name,
      'address': user.address
    }


  @property
  def __eq__(self, other):
    return type(self) is type(other) and self.id == other.id

  def __ne__(self, other):
    return not self.__eq__(other)


class UserSchema(Schema):
  id = fields.Integer(dump_only=True)
  name = fields.Str(required=True)
  address = fields.Str()

  class Meta:
    strict = True

  def format_name(self, user):
    return "{}, {}".format(user.openid, user.name)
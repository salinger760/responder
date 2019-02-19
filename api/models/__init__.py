from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, event
from sqlalchemy.orm import backref, relation
from api.models import session
# Select the model you want to create
#from api.models import User


def init_db():
  session.Model.metadata.create_all(bind=session.engine)
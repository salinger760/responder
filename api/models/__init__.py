from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
from sqlalchemy.ext.declarative import declarative_base


config = {
  "user": "root",
  "password": "root",
  "host": "127.0.0.1",
  "port": 3306,
  "database": "testdb"
}
dsn_fmt = 'mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s?charset=utf8'
dsn = dsn_fmt % config


engine = create_engine(dsn,
                       convert_unicode=True,
                       encoding = "utf-8",
                       echo = True
                      )

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine
                                        ))

Model = declarative_base(name='Model')
Model.query = db_session.query_property()


def init_db():
  Model.metadata.create_all(bind=engine)
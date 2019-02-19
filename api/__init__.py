import responder
from responder import API

app = responder.API(cors=True)


def init_db():
  Model.metadata.create_all(bind=engine)
from sqlalchemy import create_engine, Column, Integer, Date, ForeignKey, Text, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("visits.db", echo=True)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)


class Visits(Base):
    __tablename__ = "visits"

    visit_id = Column(Integer, primary_key=True)
    visitor_id = Column(Integer, ForeignKey("visitors.id"))
    visit_time = Column(Date)
    visit_info = Column(Text)

class Visitors(Base):
    __tablename__ = "visitors"

    visitor_id = Column(Integer, primary_key=True)
    visitor_first_name = Column(String(255))
    visitor_last_name = Column(String(255))
    visitor_email = Column(String(255))




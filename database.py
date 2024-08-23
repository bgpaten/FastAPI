from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ahyar diganti dengan username mysql/phpmyadmin
# bismillah1 diganti dengan passwordnya
# ApiAplication diganti dengan nama databasenya
URL_DATABASE = "mysql+pymysql://ahyar:bismillah1@localhost:3306/ApiAplication"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

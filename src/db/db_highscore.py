from os import getenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_URL = getenv("DATABASE_URL")
SECRET_KEY = getenv("SECRET_KEY")

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

def add_score(player, score):
    sql = text(
        "INSERT INTO highscores (player, score)"
        " VALUES (:player, :score); "
    )
    session.execute(sql, {"player": player, "score": score})
    session.commit()
    session.close()

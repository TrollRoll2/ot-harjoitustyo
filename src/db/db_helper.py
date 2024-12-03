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

def setup_db():
    sql = text(
        "CREATE TABLE highscores ("
        " id SERIAL PRIMARY KEY, "
        " player VARCHAR(3), "
        " score INT, "
        ");"
    )
    session.execute(sql)
    session.commit()
    session.close()

if __name__ == "__main__":
    setup_db()

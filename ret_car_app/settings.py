from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_CONFIG = {
    "drivername": "mysql+pymysql",
    "host": "localhost",
    "username": "root",
    "password": "fyn873bvtyw9",
    "port": 3306,
    "database": "car_rental"
}

DB_URL = URL.create(**DATABASE_CONFIG)

# Silnik do bazy
engine = create_engine(DB_URL, echo=False)

# sesja
SessionLocal = sessionmaker(bind=engine)

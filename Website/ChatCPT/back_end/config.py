from sqlalchemy import create_engine, Column, Integer

DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'my_user',
    'password': 'my_password',
    'database': 'my_database'
}

engine = create_engine(f'mysql+mysqlconnector://{DATABASE_CONFIG["user"]}:{DATABASE_CONFIG["password"]}@{DATABASE_CONFIG["host"]}/{DATABASE_CONFIG["database"]}')
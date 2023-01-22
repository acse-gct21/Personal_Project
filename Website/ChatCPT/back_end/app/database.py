from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

# Connect to the database
engine = create_engine('mysql+pymysql://my_user:my_password@localhost:3306/my_database')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user
def add_user(username, email, plaintext_password):
    new_user = User(username=username, email=email, password=plaintext_password)
    session.add(new_user)
    session.commit()

# Query all users
def get_all_users():
    return session.query(User).all()

# Update a user's email
def update_user_email(user_id, new_email):
    user_to_update = session.query(User).filter_by(id=user_id).first()
    user_to_update.email = new_email
    session.commit()

# Delete a user
def delete_user(user_id):
    user_to_delete = session.query(User).filter_by(id=user_id).first()
    session.delete(user_to_delete)
    session.commit()
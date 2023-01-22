from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import bcrypt
import hashlib
import os

Base = declarative_base()

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)
    address_line_1 = Column(String(255), nullable=False)
    address_line_2 = Column(String(255))
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zipcode = Column(String(10), nullable=False)
    country = Column(String(50), nullable=False)
    phone_number = Column(String(255))
    email = Column(String(255), unique=True)
    user = relationship("User", back_populates="personal_info")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    personal_info_id = Column(Integer, ForeignKey('profiles.id'))
    personal_info = relationship("Profile", back_populates="user")
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    subscription = relationship("Subscription", back_populates="user")
    payments = relationship("Payment", back_populates="user")
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.hashpw(plaintext.encode(), bcrypt.gensalt())
    
    def set_password(self, plaintext_password):
        self.password = bcrypt.hashpw(plaintext_password.encode(), bcrypt.gensalt())
        
    def check_password(self, plaintext):
        return bcrypt.checkpw(plaintext.encode(), self._password)


class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    user = relationship("User", back_populates="subscription")
    payments = relationship("Payment", back_populates="subscription")

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="payments")
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    subscription = relationship("Subscription", back_populates="payments")
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    method = Column(String(50), nullable=False)
    user = relationship("User", back_populates="payments")
    __table_args__ = (CheckConstraint('amount > 0', name='amount_positive'),)
# Create an SQLAlchemy model form a pre-existing database table
# The table is created in the database using the following SQL command:
# CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY, name VARCHAR(255) NOT NULL,price DECIMAL(10, 2) NOT NULL)

from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductModel(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    def __repr__(self):
        return "<Product(id='%s', name='%s', price='%s')>" % (self.id, self.name, self.price)
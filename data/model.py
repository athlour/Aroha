import datetime
from sqlalchemy import create_engine, ForeignKey, UniqueConstraint
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine('mysql+pymysql://root:password@localhost/aroha', echo=True)
Base = declarative_base()


class Customer(Base):
    __model__ = 'Customer'
    __table_name__ = "customer"
    customer_id = Column(Integer, primary_key=True, unique=True)
    e_mail = Column(String(255), unique=True)
    mobile = Column(String(15))
    name = Column(String(255))
    pan = Column(String(255))
    orders = relationship("bank")
    created_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    __table_args__ = UniqueConstraint('customer_id', 'e_mail',),

    def __init__(self, customer_info):
        self.e_mail = customer_info['email']
        self.mobile = customer_info['mobile']
        self.name = customer_info['name']
        self.pan = customer_info['pan']
        self.status = customer_info['status']


class BankAccount(Base):
    __model__ = 'bank_account'
    __table_name__ = "bank_account"
    id = Column(Integer, primary_key=True, unique=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    account_holder_name = Column(String(255))
    account_ifsc = Column(String(255))
    account_number = Column(Integer)
    account_type = Column(String(255))
    status = Column(String(255))
    created_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    __table_args__ = UniqueConstraint('order_id'),

    def __init__(self, bank_account_info):
        self.customer_id = bank_account_info['customer_id']
        self.account_holder_name = bank_account_info['account_holder_name']
        self.account_ifsc = bank_account_info['account_ifsc']
        self.account_number = bank_account_info['account_number']
        self.account_type = bank_account_info['account_type']
        self.status = bank_account_info['status']


# by executing this file will create tables in the DB
# if __name__ == '__main__':
#     Base.metadata.create_all(engine)


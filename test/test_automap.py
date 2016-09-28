# -*- coding:utf-8 -*-
"""
version: 1.0
author: ZhangJian
site: unkonwn
software: PyCharm
file: test_automap.py
time: 2016/9/28 17:19
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Sequence, String, Integer)
from sqlalchemy import create_engine
from sqlalchemy import *

from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("mysql://root:toor123@localhost:3309/info_center", encoding="utf-8", echo=True)
metadata = MetaData()

Session = sessionmaker(bind=engine)
session = Session()

User = Table('user', metadata,
             Column('user_id', Integer, primary_key=True),
             Column('user_name', String(16), nullable=False),
             Column('email_address', String(60)),
             Column('password', String(20), nullable=False)
             )

user_prefs = Table('user_prefs', metadata,
                   Column('pref_id', Integer, primary_key=True),
                   Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
                   Column('pref_name', String(40), nullable=False),
                   Column('pref_value', String(100))
                   )

metadata.create_all(engine)

# u = User(user_id =1,user_name='zhangsan', email_address='zhangsan@tuniu.com', password='dasd')
# print u
# session.add(u)
# session.commit()
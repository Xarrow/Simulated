# -*- coding:utf-8 -*-
"""
version: 1.0
author: ZhangJian
site: unkonwn
software: PyCharm
file: test_sqlAlachemy2.py
time: 2016/9/29 16:59
"""
import logging

level = logging.DEBUG
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
datefmt = '%Y-%m-%d %H:%M'
logging.basicConfig(level=level, format=format, datefmt=datefmt)
logger = logging.getLogger(__name__)

from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table, Integer, String, Sequence
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
import utils.config as config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Sequence, MetaData

engine = create_engine("mysql://root:toor123@localhost:3309/info_center", echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence("user_seq_id "), primary_key=True)
    name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __repr__(self):
        return "<%s,%s,%s>" % (self.id, self.name, self.password)


Base.metadata.create_all(engine)

user = User(name='zhangsan2', password='najksd')

session = Session(bind=engine)
session.add(user)
session.commit()
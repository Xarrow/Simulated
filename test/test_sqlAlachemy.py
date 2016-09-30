# -*- coding:utf-8 -*-


"""
 Verion: 1.0
 Author: zhangjian
 Site: http://iliangqunru.com
 File: test_sqlAlachemy.py
 Time: 2016/9/28 22:34
"""
import logging
import sys

from sqlalchemy.orm import Session

import utils.config as config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Sequence, MetaData, Table
from sqlalchemy.ext.automap import automap_base

level = logging.DEBUG
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
datefmt = '%Y-%m-%d %H:%M'
logging.basicConfig(level=level, format=format, datefmt=datefmt)
logger = logging.getLogger(__name__)

# FIRST METHOD
engine = create_engine("mysql://root:toor123@localhost:3309/info_center", echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_seq_id'), primary_key=True)
    name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __repr__(self):
        return "<%s,%s,%s>" % (self.id, self.name, self.password)


Base.metadata.create_all(engine)

# user = User(name='zhangsan2', password='najksd')
# # gobal session
# Session = sessionmaker()
# Session.configure(bind=engine)
# # local session
# session = Session()


autoBase = automap_base()
autoBase.prepare(engine, reflect=True)
User = autoBase.classes.user
session = Session(engine)
user = User(name ='dsad',password = 'sdadasd')
session.add(user)
session.commit()

# Method 2
# engine = create_engine(config.MYSQL_CONFIG, echo=True)
# metadata = MetaData()
#
# User = Table('user', metadata,
#              Column('id', Integer, primary_key=True),
#              Column('name', String(50), nullable=False),
#              Column('password', String(50), nullable=False))
#
# metadata.create_all(engine)
#
# u = User(id=1, name='zhangsan', password='dasd')
# sess = Session()
# sess.add(u)

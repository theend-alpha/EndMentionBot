from Database import BASE, SESSION
from sqlalchemy.sql.sqltypes import BigInteger
import threading
from sqlalchemy import Column

class M_users(BASE):
    __tablename__ = "musers"

    id = Column(BigInteger, primary_key=True)

    def __init__(self, id):
        self.id = id

class MS_users(BASE):
    __tablename__ = "msusers"

    chat_id = Column(BigInteger, primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id

M_users.__table__.create(checkfirst=True)

MS_users.__table__.create(checkfirst=True)

User_IL = threading.RLock()

LEL_IL = threading.RLock()

def add_user(id):
    with User_IL:
        SESSION.add(M_users(id))
        SESSION.commit()

def list_users():
    lel = SESSION.query(M_users).all()
    try:
        return lel
    except:
        SESSION.close()

def add_chat(id):
    with LEL_IL:
        SESSION.add(MS_users(id))
        SESSION.commit()

def list_chats():
    lel = SESSION.query(MS_users).all()
    try:
        return lel
    except:
        SESSION.close()

def is_served_chat(id):
    lel = SESSION.query(MS_users).get(id)
    if lel:
        return True
    else:
        return False

def is_served_user(id):
    lel = SESSION.query(M_users).get(id)
    if lel:
        return True
    else:
        return False

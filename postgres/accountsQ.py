from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, relationship
import sys
from postgres.tablesCreation import *

class AccountDBConnection():
    def __init__(self) -> None:
        self.engine = create_engine('postgresql://postgres:admin@localhost:5432/ayomi', echo=False, pool_size=20, max_overflow=30)
        self.Session = sessionmaker(bind=engine)
        
#   Accounts TABLE #######################################
    def AddUser(self, email, psswd):
        self.session = self.Session()
        user = Accounts()
        user.email = email
        user.password = psswd
        self.session.add(user)
        self.session.flush()
        insertedUser = user
        self.session.commit()
        self.session.close()
        return insertedUser

    def LoadUser(self, id):
        self.session = self.Session()
        return self.session.query(Accounts).filter_by(id=id).first()

    def GetUserByPseudo(self, email):
        self.session = self.Session()
        user = self.session.query(Accounts).filter_by(email=email).first()
        return user

    def UpdateEmail(self, oldEmail, newEmail):
        self.session = self.Session()
        userID = self.session.query(Accounts).filter_by(email=oldEmail).first()
        print(oldEmail)
        user = self.session.query(Accounts).get(userID.id)
        user.email = newEmail
        self.session.commit()
            
        return user
    
    

    

   
    



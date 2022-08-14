from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, relationship
import sys
from postgres.tablesCreation import *

class AccountDBConnection():
    def __init__(self) -> None:
        self.engine = create_engine('postgresql://postgres:admin@localhost:5432/ayomi', echo=False, pool_size=20, max_overflow=30)
        self.Session = sessionmaker(bind=engine)
        self.session = ''

#   Decorators     #######################################
    def Decorators(func) : 
        def inner(self, *args) : 
            self.session = self.Session()
            data = func(self, *args) 
            self.session.close()
            return data
        return inner 

#   Accounts TABLE #######################################
    @Decorators
    def AddUser(self, email, psswd):
        user = Accounts()
        user.email = email
        user.password = psswd
        self.session.add(user)
        self.session.flush()
        insertedUser = user
        self.session.commit()
        return insertedUser

    @Decorators
    def LoadUser(self, id):
        return self.session.query(Accounts).filter_by(id=id).first()

    @Decorators
    def GetUserByEmail(self, email):
        self.session = self.Session()
        user = self.session.query(Accounts).filter_by(email=email).first()
        return user

    @Decorators
    def UpdateEmail(self, oldEmail, newEmail):
        userID = self.session.query(Accounts).filter_by(email=oldEmail).first()
        user = self.session.query(Accounts).get(userID.id)
        user.email = newEmail
        self.session.commit()
            
        return user
    
    

# postgres = AccountDBConnection()
# user = postgres.GetUserByEmail('3s@em.fr')
# print(user)

   
    



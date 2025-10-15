import re

class Member:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, val):
        self.name = val
    
    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, val):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if valid:
            self.email = val
        else:
            print("invalid email")
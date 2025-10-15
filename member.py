import re

class Member:
    def __init__(self, name, email):
        self._name = name
        self.email = email
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = val
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, val):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', val)
        if valid:
            self._email = val
        else:
            print("invalid email")
class Meeting:
    def __init__(self, bookedInterval, members, roomId):
        self._bookedInterval = bookedInterval #[start,end]
        self._members = members
        self._roomId = roomId # this id should be a foreign key to a room in which 1 room can have many meetings

    @property
    def bookedInterval(self):
        return self._bookedInterval
    
    @bookedInterval.setter
    def bookedInterval(self, val):
        if isinstance(val, list) and len(val) == 2:
            self._bookedInterval = val
        else:
            print("not valid interval, currently only supports [start,end] values")
    
    @property
    def members(self):
        return self._members
    
    @members.setter
    def members(self, val):
        if isinstance(val, list):
            self._members = val
        else:
            print("new members value is not the correct type, cannot update members")

    @property
    def roomId(self):
        return self._roomId
    
    @roomId.setter
    def roomId(self, val):
        # will leave it as is but here we can search in all the current rooms to check if its a valid id
        self._roomId = val
    
    def getMemberNames(self):
        m = []
        for _,member in enumerate(self.members):
            m.append(member.name)
        return m

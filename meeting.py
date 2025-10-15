class Meeting:
    def __init__(self, bookedInterval, members, roomId):
        self.bookedInterval = bookedInterval #[start,end]
        self.members = members
        self.roomId = roomId

    @property
    def bookedInterval(self):
        return self.bookedInterval
    
    @bookedInterval.setter
    def bookedInterval(self, val):
        if isInstance(val, List[int]) and len(val) == 2:
            self.bookedInterval = val
        else:
            print("not valid interval, currently only supports [start,end] values")
    
    @property
    def members(self):
        return self.members
    
    @members.setter
    def members(self, val):
        if isInstance(val, List[Member]):
            self.members = val
        else:
            print("new members value is not the correct type, cannot update members")

    @property
    def roomId(self):
        return self.roomId
    
    @roomId.setter
    def roomId(self, val):
        # will leave it as is but here we can search in all the current rooms to check if its a valid id
        self.roomId = val
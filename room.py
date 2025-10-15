import Meeting
class Room:
    def __init__(self, id, location, meetings):
        self.id = id
        self.name = name
        self.location = location
        self.meetings = meetings

    @property
    def id(self):
        return self.id
    
    @id.setter
    def id(self, val):
        if isinstance(val,int):
            self.id = val
    
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, val):
        if isinstance(val,str):
            self.name = val
    
    @property
    def location(self):
        return self.location
    
    @location.setter
    def location(self, val):
        # will leave the location as string for now but here we can use a more complex object to store geolocation data latitude, longitude, etc.
        if isinstance(val,str):
            self.location = val
    
    @property
    def meetings(self):
        return self.meetings
    
    @meetings.setter
    def meetings(self, val):
        if isinstance(val,List[Meeting]):
            self.meetings = val
    
    # Calcula el minimo de cuartos en la instancia actual del cuarto (object oriented)
    def getCurrentMinimumRooms():
        if len(self.meetings) == 0:
            return 0
        
        startTimes = []
        endTimes = []
        numRooms = 0

        for i, meeting in enumerate(self.meetings):
            interval = meeting.bookedInterval
            if interval:
                startTime.append(interval[0])
                endTime.append(interval[1])
        
        startTimes.sort()
        endTimes.sort()
        j = 0

        for i in range(len(startTimes)):
            if startTimes[i] < endTimes[j]:
                numRooms += 1
            else:
                j +=1
        return numRooms



    # Calcula el minimo de cuartos on the fly (como lo indica el problema)    
    def getMinimumRooms(meetings: list[Meeting]):
        if len(meetings) == 0:
            return 0
        
        startTimes = []
        endTimes = []
        numRooms = 0
        
        for i, meeting in enumerate(meetings):
            interval = meeting.bookedInterval
            if interval:
                startTime.append(interval[0])
                endTime.append(interval[1])
        
        startTimes.sort()
        endTimes.sort()
        j = 0

        for i in range(len(startTimes)):
            if startTimes[i] < endTimes[j]:
                numRooms += 1
            else:
                j +=1
        
        return numRooms



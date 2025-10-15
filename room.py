from meeting import Meeting
class Room:
    def __init__(self, rId, name,location, meetings=[]):
        self._rId = rId
        self._name = name
        self._location = location
        self._meetings = meetings

    @property
    def rId(self):
        return self._rId
    
    @rId.setter
    def rId(self, val):
        if isinstance(val,int):
            self._rId = val
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        if isinstance(val,str):
            self._name = val
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, val):
        # will leave the location as string for now but here we can use a more complex object to store geolocation data 
        # like latitude, longitude, etc.
        if isinstance(val,str):
            self._location = val
    
    @property
    def meetings(self):
        return self._meetings
    
    @meetings.setter
    def meetings(self, val):
        if isinstance(val,list):
            self._meetings = val
    
    # Gets the minimum rooms for the current meetings (object oriented)
    def getCurrentMinimumRooms(self):
        if len(self._meetings) == 0:
            return 0
        
        startTimes = []
        endTimes = []
        numRooms = 0

        for i, meeting in enumerate(self._meetings):
            interval = meeting.bookedInterval
            if interval:
                startTimes.append(interval[0])
                endTimes.append(interval[1])
        
        startTimes.sort()
        endTimes.sort()
        j = 0

        for i in range(len(startTimes)):
            if startTimes[i] < endTimes[j]:
                numRooms += 1
            else:
                j +=1
        return numRooms



    # Gets the minimum rooms with on the fly meeting lists (como lo indica el problema)    
    def getMinimumRooms(self, meetings: list[Meeting]):
        if len(meetings) == 0:
            return 0
        
        startTimes = []
        endTimes = []
        numRooms = 0
        
        for i, meeting in enumerate(meetings):
            interval = meeting.bookedInterval
            if interval:
                startTimes.append(interval[0])
                endTimes.append(interval[1])
        
        startTimes.sort()
        endTimes.sort()
        j = 0

        for i in range(len(startTimes)):
            if startTimes[i] < endTimes[j]:
                numRooms += 1
            else:
                j +=1
        
        return numRooms



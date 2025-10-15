import Meeting
class Room:
    def __init__(self, name, location, meetings):
        self.name = name
        self.location = location
        self.meetings = meetings
    
    # Calcula el minimo de cuartos en la instancia actual del cuarto (object oriented)
    def getCurrentMinimumRooms():

    # Calcula el minimo de cuartos on the fly (como lo indica el problema)    
    def getMinimumRooms(meetings: List[Meeting]):
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



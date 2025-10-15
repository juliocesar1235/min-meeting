from meeting import Meeting
from room import Room
from member import Member

def main():
    room1 = Room(1,"Tatooine","Building 2, 10th floor")
    room2 = Room(2,"Mustafar", "Building 2, 11th floor")

    members1 = [Member("Julio", "juliog@gmail.com"), Member("Raul", "raul10@gmail.com"), Member("Anakin", "thedarkside@gmail.com")]
    meetings1 = [Meeting([0,10],members1, room1.rId),Meeting([11,15], members1, room1.rId),Meeting([14,16], members1, room1.rId)]
    room1.meetings = meetings1
    print("Meetings in room: "+room1.name)
    for i in range(len(room1.meetings)):
        print(f"Meeting {i+1} " + "Interval:" + str(room1.meetings[i].bookedInterval))
        print("Members", room1.meetings[i].getMemberNames())
    
    badMember = Member("Badd", "mdaeldma")

    members2 = [Member("Jarjar", "binks@gmail.com"), Member("C3PO", "master123@gmail.com")]
    # here it can also be improved to only assign roomIds after we find that dont overlap with other meetings
    meeting4 = Meeting([5,10], members2, room2.rId)
    meeting5 = Meeting([15,20], members2, room2.rId)
    room2.meetings = [meeting4,meeting5]

    minMeetingRooms = room1.getCurrentMinimumRooms()
    print("Calculated with stored meetings", minMeetingRooms)

    minMeetingsRoomsFly = room1.getMinimumRooms(meetings1)
    print("Calculated on the fly with arguments", minMeetingsRoomsFly)

if __name__ == "__main__":
    main()
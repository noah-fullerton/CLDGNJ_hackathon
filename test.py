import db_control

sample_user = {
    "username" : "isolate",
    "password" : "1234",
    "first_name" : "joaquin",
    "last_name" : "trujillo",
    "email" : "joaquintrujillo@mac.com",
    "phone_number" : "1234567890"
}

sample_president = {
    "username" : "nono",
    "password" : "1234",
    "first_name" : "noah",
    "last_name" : "fullerton",
    "email" : "noahmfullerton@gmail.com",
    "phone_number" : "1234567890"

}

sample_club = {
        "name" : "Computer Science Club",
        "description" : "We do cool stuff",
        "president_username" : "nono"
}

sample_event = {
    "name" : "Hackathon",
    "description" : "We do cool stuff",
    "location" : "Cafe",
    "start_date" : "2019-11-11",
    "end_date" : "2019-11-11",
    "club_name" : "Computer Science Club"
}

controller = db_control.Controller()
controller.insertUsers(sample_user)
controller.insertPresidents(sample_president)
controller.insertClubs(sample_club)
controller.insertEvents(sample_event)

print(controller.getUsers())
print(controller.getClubs())
print(controller.getEvents())
print(controller.getSpecificUser({"username": "isolate"}))
print(controller.getSpecificClub({"name": "Computer Science Club"}))
print(controller.getSpecificEvent({"name": "Hackathon"})) 
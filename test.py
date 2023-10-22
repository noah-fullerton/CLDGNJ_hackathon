import db_control

sample_user = {
    "username" : "isolate",
    "password" : "1234",
    "first_name" : "joaquin",
    "last_name" : "trujillo",
    "email" : "joaquintrujillo@mac.com",
    "phone_number" : "1234567890"
}

sample_club = {
        "name" : "Computer Science Club",
        "description" : "We do cool stuff",
        "president_id" : 1
}

sample_event = {
    "name" : "Hackathon",
    "description" : "We do cool stuff",
    "location" : "Cafe",
    "start_date" : "2019-11-11",
    "end_date" : "2019-11-11",
    "club_id" : "1"
}

controller = db_control.Controller()
controller.insertUsers(sample_user)
controller.insertClubs(sample_club)
controller.insertEvents(sample_event)
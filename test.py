import db_control

sample_user = {
    "username" : "isolate",
    "password" : "1234",
    "first_name" : "joaquin",
    "last_name" : "trujillo",
    "email" : "joaquintrujillo@mac.com",
    "phone_number" : "1234567890"
}

controller = db_control.Controller()
controller.insertUsers(sample_user)
from flask import request, Flask, jsonify
import sys
import db_control
import json
from flask_cors import CORS

controller = db_control.Controller()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='sdf3GAF#WDD#D#RFGHjahsa24561'
    return app

app = create_app()
CORS(app)

#for login page get user and pass TODO: CHECK DATABASE FOR ACCOUNT IF EXIST SEND TRUE IF NOT SENF FALSE
@app.route("/", methods=['POST'])
def process():
    data = request.get_json()
    user_name = data['user_name']
    password = data['password']
    #check_login(user_name,password)
    return check_login(user_name,password)

#for new account registration 
#Checks for empty inputs return false
#Checks for char limits
#checks for password comfirmation
#TODO: Put into database

@app.route('/register', methods = ['POST'])
def register():
    data = request.get_json()

    print(json.dumps(data))

    user_name = data['user_name']
    password = data['password']
    confirm_password = data['confirm_password']
    first_name = data['first_name']
    last_name = data['last_name']
    phone_number = data['phone_number']
    email = data['email']

    info_list = [user_name,password,first_name,last_name,phone_number,email]
    # checks if any of the data is empty
    for item in info_list:
        if(item == "" or item == " "):
            return jsonify({'success': 'FALSE'})
    
    # SECURITY CHECK
    # if username has more than 16 characters return FALSE
    if len(user_name) > 16:
        return jsonify({'success': 'FALSE'})
    # if password has less than 6 char OR password has more than 16 char
    if len(password) < 6 or len(password) > 16:
        return jsonify({'success': 'FALSE', 'password_length':'FALSE'})
    # if First Name has more than 50 char
    if len(first_name) > 50:
        return jsonify({'success': 'FALSE'})
    # if Last Name has more than 50 char
    if len(last_name) > 50:
        return jsonify({'success': 'FALSE'})
    
    first_name_split = first_name.split()
    last_name_split = last_name.split()
    password_name_split = password.split()
    username_split = user_name.split()
    special_char_check = ['@', '#', '$', '/', ',' , '{', '}', '&', '*']

    """
    for x in range(50):
        for y in range(len(special_char_check)):
            if(first_name_split[x] == special_char_check[y]):
                return ConnectionResetError
    """
    if password == confirm_password:
        create_user_dict(user_name,password,first_name,last_name,phone_number,email)
        return jsonify({'success': 'TRUE'})
    else:
        return jsonify({'success': 'FALSE'})

#Event route
@app.route("/event", methods=['POST'])
def event_handler():
    data = request.get_json()
    event_name = data['name']
    start_date = data['start_date']
    end_date = data['end_date']
    location = data['location']
    description = data['description']
    #club_name = data['club_name']
    create_event(event_name,start_date,end_date,location,description)
    return jsonify({'success':'TRUE'})

def create_event(event_name, start_date, end_date, location, description):
    sample_event = {
        "name" : event_name,
        "description" : description,
        "location" : location,
        "start_date" : start_date,
        "end_date" : end_date,
    }
    event = controller.insertEvents(sample_event)
    

@app.route("/all_events", methods=['POST'])
def send_events():
    events = controller.getEvents()
    return events


def create_user_dict(user_name, password, first_name, last_name, phone_number, email):
    dict_user ={
        "username" : user_name,
        "password" : password,
        "first_name"  : first_name,
        "last_name" : last_name,
        "phone_number" : phone_number,
        "email" : email
    }
    controller.insertUsers(dict_user)
    return dict_user
    

def check_login(user_name, Password):
    event = controller.getSpecificUser({"username":user_name})
    if event == []:
        return jsonify({"success":"FALSE"})
    elif event[0][1] == user_name and event[0][2] == Password:
        return jsonify({"success":"TRUE"})
    else:       
        return jsonify({"success":"FALSE"})


if __name__ == '__main__': #main name space run here

    print(send_events())
    for line in sys.path: #helps us see what path we are in
        print(line)  # Print path

    app.run(debug=True, host="0.0.0.0")  # run the flask app with debug set to true multiple args
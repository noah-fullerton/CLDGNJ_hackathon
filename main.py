from flask import request, Flask, jsonify
import sys

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='sdf3GAF#WDD#D#RFGHjahsa24561'
    return app

app = create_app()

#for login page get user and pass TODO: CHECK DATABASE FOR ACCOUNT IF EXIST SEND TRUE IF NOT SENF FALSE
@app.route("/", methods=['GET'])
def process():
    data = request.get_json()
    user_name = data['user_name']
    password = data['password']
    check_login(user_name,password)
    return jsonify({'success':'TRUE'})

#for new account registration 
#Checks for empty inputs return false
#Checks for char limits
#checks for password comfirmation
#TODO: Put into database

@app.route('/register', methods = ['GET'])
def register():
    data = request.get_json()
    user_name = data['user_name']
    password = data['password']
    confirm_password = data['confirm_password']
    first_name = data['first_name']
    last_name = data['last_name']
    phone_number = data['phone_number']
    email = data['email']

    info_list = [user_name,password,first_name,last_name,phone_number,email]
    for item in info_list:
        if(item == "" or item == " "):
            return jsonify({'success': 'FALSE'})
    
    if len(user_name) >16:
        return jsonify({'success': 'FALSE'})
    if len(password) <=6 or len(password) > 16:
        return jsonify({'success': 'FALSE'})
    if len(first_name) > 50:
        return jsonify({'success': 'FALSE'})
    if len(last_name) > 50:
        return jsonify({'success': 'FALSE'})

    if password == confirm_password:
        create_user(user_name,password,first_name,last_name,phone_number,email)
        return jsonify({'success': 'TRUE'})
    else:
        return jsonify({'success': 'FALSE'})

#Event route



def create_user(user_name, password, first_name, last_name, phone_number, email):
    #use for database
    pass
    

def check_login(user_name, Password):
    #use for database
    pass


if __name__ == '__main__': #main name space run here

    for line in sys.path: #helps us see what path we are in
        print(line)  # Print path

    app.run(debug=True, host="0.0.0.0")  # run the flask app with debug set to true multiple args
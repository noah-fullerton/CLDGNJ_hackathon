from flask import request, Flask, jsonify
import sys

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='sdf3GAF#WDD#D#RFGHjahsa24561'
    return app

app = create_app()

@app.route("/processjson", methods=['POST'])
def process():
    data = request.get_json()
    name = data['name']
    return jsonify({'result' : 'Sucess'})




if __name__ == '__main__': #main name space run here

    for line in sys.path: #helps us see what path we are in
        print(line)  # Print path
    app.run(debug=True, host="0.0.0.0")  # run the flask app with debug set to true multiple args
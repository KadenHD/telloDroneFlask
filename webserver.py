from re import X
from flask import Flask, render_template, request
from controller import *

app = Flask(__name__)

""" Routes """
@app.route('/', methods=["GET"])
def index():
    title = "Home"
    return render_template("index.html", title=title)

@app.route('/controller', methods=["POST", "GET"])
def controller():
    if request.method == "POST":
        new_direction = request.form.get("direction") #Get the value
        print("Direction:",new_direction)
        telloControler(new_direction) #Send To Tello the command
    title = "Control the Robot !"
    return render_template("controller.html", title=title)
""" /Routes """

def main():
    
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()

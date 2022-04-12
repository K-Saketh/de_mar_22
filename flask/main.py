from urllib import request
from flask import Flask,request   # Imported Flask library
from flasgger import Swagger

app = Flask(__name__)     # Created constructor of the Flask
Swagger(app)
@app.route("/")

def base_route():
    return "Welcome to Praxis"

#@app.route("/my_name")

#def print_name():
#    return "Hi Saketh"

@app.route("/my_name/<name>")
def print_name(name):
    return f"Happy learning {name} at Praxis Bangalore"

@app.route("/hello", methods = ["GET","POST"])
def hello():
    """Let's try Swagger from Flasgger
    ---
    parameters:
        - name: Student
          in: query
          type: string
          required: true
        - name: RollNo
          in: query
          type: string
          required: true
    responses:
        200:
            description: The result is"""

    try:
        stu_name = request.args.get("Student")
        numb = request.args.get("RollNo")
        #return "Oops something went wrong", 400
        return f"Student name is {stu_name} and Roll number is {numb}",200
        #return f"Student name is {stu_name} and Roll number is {numb}"
    except Exception as e:
        return f"Error occured with message: {e}", 401

if __name__ == "__main__":
    #app.run() -----------> Takes port 5000 by default
    #app.run(port = 8000)------> Takes port 8000
    #app.run(host = "0.0.0.0", port = 8000)
    app.run(host = "0.0.0.0", port = 8000, debug = True)
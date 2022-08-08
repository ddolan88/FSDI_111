from flask import Flask


app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name" : "Derek",
        "las_name" : "Dolan",
        "hobbies" : "Gaming",
        "active" : True
    }
    return me

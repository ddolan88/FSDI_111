import requests

from flask import (
    Flask,
    request
)

from app.database import user

app = Flask(__name__)

URL = "http://127.0.0.1:5000/users"


def deactivate_user():
    if __name__ == "__main__":
        fname = input("Type in the user's first name: ")
        lname = input("Type in the user's last name: ")
        hobbies = input("Type in the user's hobbies: ")
        deactivate_user(fname, lname, hobbies)
        response = requests.delete(url, json=user)
    if response.status_code == 204:
        print(
            "Successfully deactivated user info: Got: %s"
            % response.json().get("message")
        )
        url = URL+"/"+id
    else:
        print(
            "Something went wrong while trying to deactivate user"
        )

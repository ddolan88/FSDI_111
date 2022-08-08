import requests

from flask import (
    Flask,
    request
)

from app.database import user

app = Flask(__name__)

URL = "http://127.0.0.1:5000/users"


def change_user_info(first_name, last_name, hobbies):
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "hobbies": hobbies,
    }
    response = requests.post(url, json=user)
    if response.status_code == 204:
        print(
            "Successfully updated user info: Got: %s"
            % response.json().get("message")
        )
        url = URL+"/"+id
    else:
        print(
            "Something went wrong while trying to update user"
        )

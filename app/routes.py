from flask import render_template, Blueprint
from .firebase_config import init_firebase

# Initialize Blueprint
main = Blueprint('main', __name__)

# Fetch data route
@main.route('/')
def index():
    firebase_ref = init_firebase()
    
    # Accessing 'UsersData' node in the database
    users_data = firebase_ref.child('UsersData').get()
    
    # Debugging: Print data to console
    print(users_data)

    return render_template('dashboard.html', data=users_data)


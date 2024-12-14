import os
import firebase_admin
from firebase_admin import credentials, db

def init_firebase():
    # Path to your Firebase credentials JSON
    json_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'service_account.json')
    
    # Initialize Firebase app if it is not already initialized
    if not firebase_admin._apps:
        cred = credentials.Certificate(json_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://pressure-monitoring-b592a-default-rtdb.firebaseio.com/'
        })
    return db.reference('/')  # Root reference to your database

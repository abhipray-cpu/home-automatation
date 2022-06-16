from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
# Fetch the service account key JSON file contents
cred = credentials.Certificate('./configKey.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://channel-relay-control-3a865-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
#declaring the collection objects
relay_channels = db.reference('/channels')
devices = db.reference('/devices')#this will contain all the info related to the device
device_config = db.reference('/configuration')#this will be like a mapping db which will contain port to device mapping using their keys
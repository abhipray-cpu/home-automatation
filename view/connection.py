import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
# Fetch the service account key JSON file contents
cred = credentials.Certificate('./configKey.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': f"{os.environ['DATABASE_URI']}"
})
#declaring the collection objects
relay_channels = db.reference('/channels')
for val in [{"relay1":"off"},{"relay2":"off"},{"relay3":"off"},{"relay4":"off"},
            {"relay5":"off"},{"relay6":"off"},{"relay7":"off"},{"relay8":"off"},
            {"relay9":"off"},{"relay10":"off"},{"relay11":"off"},{"relay12":"off"},
            {"relay13":"off"},{"relay14":"off"},{"relay15":"off"},{"relay16":"off"},]:
    relay_channels.push(val)
devices = db.reference('/devices')#this will contain all the info related to the device
device_config = db.reference('/configuration')#this will be like a mapping db which will contain port to device mapping using their keys
#CRUD operations without any conditions
#this is the create operation
# for val in [{"description":"This is the bedroom1 bulb that we are add...",
# "load":"high",
# "name":"Bedroom Lights",
# "rating":"5",
# "status":"off",
# "type":"Bulb"},
#              {"description": "This is the master bedroom2 bulb that we are add...",
#               "load": "high",
#               "name": "Bedroom Lights",
#               "rating": "5",
#               "status": "off",
#               "type": "Bulb"},
# {"description":"This is the master bedroom3 bulb that we are add...",
# "load":"high",
# "name":"Bedroom Lights",
# "rating":"5",
# "status":"off",
# "type":"Bulb"},
# {"description":"This is the master bedroom4 bulb that we are add...",
# "load":"high",
# "name":"Bedroom Lights",
# "rating":"5",
# "status":"off",
# "type":"Bulb"},
# {"description":"This is the master bedroom5 bulb that we are add...",
# "load":"high",
# "name":"Bedroom Lights",
# "rating":"5",
# "status":"off",
# "type":"Bulb"},
# {"description":"This is the master bedroom6 bulb that we are add...",
# "load":"high",
# "name":"Bedroom Lights",
# "rating":"5",
# "status":"off",
# "type":"Bulb"},
# {"description":"This is the master bedroom7 bulb that we are add...",
# "load":"high",
# "name":"Bedroom Lights",
# "rating":"5",
# "status":"off",
# "type":"Bulb"},
# {"description":"This is the master bedroom8 bulb that we are add...",
# "load":"high",
# "name":"Bedroom Lights",
# "rating":"5",
# "status":"off",
# "type":"Bulb"},
# {"description":"This is the master bedroom9 bulb that we are add...",
# "load":"high",
# "name":"Bedroom Lights",
# "rating":"5",
# "status":"off",
# "type":"Bulb"},
# {"description":"This is the master bedroom10 bulb that we are add...",
# "load":"high",
# "name":"Bedroom Lights",
# "rating":"5",
# "status":"off",
# "type":"Bulb"},
# {"description":"This is the master bedroom11 bulb that we are add...",
# "load":"high",
# "name":"Bedroom Lights",
# "rating":"5",
# "status":"off",
# "type":"Bulb"}]:
#     devices.push(val)


# device_config.push({
#     "channel":"",#this will be empty string initially and will be updated while the device and channel mapping
#     "device":"-MwGkYYOxWC_20yIKdj9"
# })

#this is how we will be reading the data
# print(relay_channels.get())
print(devices.get())
# print(device_config.get())
#
# #this is the update operation that we can perform
# update_obj=devices.child('MwGkYYOxWC_20yIKdj9')
# #while updatingg data make sure that you only updatet he specific data and not the entire document
# #byd default the entire doc will be updated so you need to configure the code to prevent this
# update_obj.update({'name':'This is the updated name of the device'})
# print(devices.get())
#
# #this is how we can deleted the object

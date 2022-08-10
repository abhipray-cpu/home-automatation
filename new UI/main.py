import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5 import QtWidgets
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QColor
import time
import os
from datetime import datetime
try:
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('./configKey.json')
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://channel-relay-control-3a865-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
    # declaring the collection objects
    relay_channels = db.reference('/channels')
    devices = db.reference('/devices')  # this will contain all the info related to the device
    device_config = db.reference(
        '/configuration')  # this will be like a mapping db which will contain port to device mapping using their keys
except Exception as e:
    print(e)

#on pressing analytics a plotly web page will be opened which will be used to display the information

#this will the flow of the code
'''
add a device and then leave it 
if the device is then mapped to a channel then it can be 
controlled usig the the gui via the firebase real time database
and in the home page a recursive function will be calleld which will be called
after every 10s to update the status of the devices 
'''

# global relay channel id
globalId = list(relay_channels.get().keys())

class AddDevice(QMainWindow):
    def __init__(self):
        super(AddDevice, self).__init__()
        loadUi("Add_device.ui", self)
        self.setWindowTitle('IOT controller')
        self.home.clicked.connect(self.homeUp)
        self.control.clicked.connect(self.controlUP)
        self.configure.clicked.connect(self.configureUp)
        self.add_device.clicked.connect(self.addDeviceUp)
        self.device_list.clicked.connect(self.deviceList)
        self.AddBtn.clicked.connect(self.getDetails)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(1, 1), blurRadius=8
        )
        self.AddBtn.setGraphicsEffect(effect)

    def getDetails(self):
        try:
            device_name = self.NameEdit.text()
            device_type = self.DeviceTypeCombo.currentText()
            rating = self.doubleSpinBox.value()
            desc = self.description.toPlainText()
            if rating > 5.0000 and rating < 50.0000:
                load = "low"
            elif rating > 50.0000 and rating < 100.000:
                load = "medium"
            else:
                load = "high"

            if device_name=="" or device_type=="" or rating == "" or desc == "" or load == "" :
                self.show("Plz fill in all the details","Missing data")
            else:
                self.push_data(
                {"name": device_name, "type": device_type, "rating": rating, "description": desc, "load": load})

        except Exception as e:
            print(e)
            self.showMessage('There occured an error plz try again',"System error")

    def push_data(self,data:object):
        try:
            devices.push(data)
            self.showMessage("The device was added successfully","Success!!")
            self.NameEdit.clear()
            self.DeviceTypeCombo.SelectedIndex=0
            self.doubleSpinBox.setValue(5.00000)
            self.description.clear()
        except Exception as e:
            print(e)
            self.showMessage(e,"System error")

    def showMessage(self,msg:str,title:str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')

    def homeUp(self):
        widget.setCurrentIndex(0)

    def configureUp(self):
        widget.setCurrentIndex(1)

    def addDeviceUp(self):
        widget.setCurrentIndex(2)

    def deviceList(self):
        widget.setCurrentIndex(3)

    def controlUP(self):
        widget.setCurrentIndex(4)

class Configure(QMainWindow):
    def __init__(self):
        super(Configure, self).__init__()
        loadUi("Configure.ui",self)
        self.home.clicked.connect(self.homeUp)
        self.setWindowTitle('IOT controller')
        self.control.clicked.connect(self.controlUP)
        self.configure.clicked.connect(self.configureUp)
        self.add_device.clicked.connect(self.addDeviceUp)
        self.device_list.clicked.connect(self.deviceList)
        self.AvailabelDevieList.setDragDropMode(self.AvailabelDevieList.InternalMove)
        self.lst = []
        self.maping = dict()
        self.fetch_device_1()
        self.HelpBtn.clicked.connect(self.help)
        self.refresh.clicked.connect(self.refreshSlot)
        self.CommitChangeBtn.clicked.connect(self.commit_changes)

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(2, 2), blurRadius=12
        )
        self.HelpBtn.setGraphicsEffect(effect)
        self.CommitChangeBtn.setGraphicsEffect(effect)
        self.refresh.setGraphicsEffect(effect)

    def help(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("This is like a matching pattern the device in the left side will be mapped to the device int the right side at the same index \n Device1 \t \t \t Channel1 \n Device2 \t \t \t Channel2 \n then device 1 will be mapped to channel 1 and device 2 to channel 2 of the port")
        msgBox.setWindowTitle("Help")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
    def refreshSlot(self):
        self.fetch_device_2()
    def fetch_device_1(self):

        try:
            device_list = devices.get()
            configuration = device_config.get()
            for val in configuration:
                self.lst.append(device_list[val['device_id']]["name"])
                self.maping[device_list[val['device_id']]["name"]] = device_list[val['device_id']]
            for device in self.lst:
                try:
                    self.AvailabelDevieList.addItem(f"{device}")
                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)
            self.fetch_device_2()

    def fetch_device_2(self):
        device_list = devices.get()
        for val in device_list:
            self.lst.append(device_list[val]["name"])
            self.maping[device_list[val]["name"]]=val
        self.AvailabelDevieList.clear()
        for device in self.lst:
            try:
                self.AvailabelDevieList.addItem(f"{device}")
            except Exception as e:
                print(e)

    def commit_changes(self):
        new_config=[]
        for val in range(0,self.AvailabelDevieList.count()):
            new_config.append(self.AvailabelDevieList.item(val).text())
        print(new_config)
        try:
            data = []
            i = 1
            for val in new_config:
                data.append({"device_id": self.maping[val], "relayChannel": i})
                i = i + 1
                if i > 16:
                    break

            #updating the collection
            try:
                for deviceId in device_config.get():
                    device_config.child(deviceId).set({})
            except Exception as e:
                print(e)
            for device in data:
                device_config.push(device)

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Success!!")
            msgBox.setWindowTitle("The configuration was successfully updated")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                print('OK clicked')


        except Exception as e:
            print(e)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Error!!")
            msgBox.setWindowTitle("There was a system error!")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                print('OK clicked')
    def homeUp(self):
        widget.setCurrentIndex(0)
    def configureUp(self):
        widget.setCurrentIndex(1)
    def addDeviceUp(self):
        widget.setCurrentIndex(2)
    def deviceList(self):
        widget.setCurrentIndex(3)
    def controlUP(self):
        widget.setCurrentIndex(4)



class deviceControl(QMainWindow):
    def __init__(self):
        super(deviceControl, self).__init__()
        loadUi("deviceControl.ui",self)
        self.setWindowTitle('IOT controller')
        self.home.clicked.connect(self.homeUp)
        self.control.clicked.connect(self.controlUP)
        self.configure.clicked.connect(self.configureUp)
        self.add_device.clicked.connect(self.addDeviceUp)
        self.device_list.clicked.connect(self.deviceList)
        self.Device1Check.stateChanged.connect(self.relay1Control)
        self.Device2Check.stateChanged.connect(self.relay2Control)
        self.Device3Check.stateChanged.connect(self.relay3Control)
        self.Device4Check.stateChanged.connect(self.relay4Control)
        self.Device5Check.stateChanged.connect(self.relay5Control)
        self.Device6Check.stateChanged.connect(self.relay6Control)
        self.Device7Check.stateChanged.connect(self.relay7Control)
        self.Device8Check.stateChanged.connect(self.relay8Control)
        self.Device9Check.stateChanged.connect(self.relay9Control)
        self.Device10Check.stateChanged.connect(self.relay10Control)
        self.Device11Check.stateChanged.connect(self.relay11Control)
        self.Device12Check.stateChanged.connect(self.relay12Control)
        self.Device13Check.stateChanged.connect(self.relay13Control)
        self.Device14Check.stateChanged.connect(self.relay14Control)
        self.Device15Check.stateChanged.connect(self.relay15Control)
        self.Device16Check.stateChanged.connect(self.relay16Control)
        # this is the styling that will be used for on and off labels
        self.offStyle = "background-color: qlineargradient(spread:pad, x1:0.632, y1:0.613, x2:1, y2:0, stop:0.328358 rgba(183, 57, 114, 255), stop:0.462687 rgba(141, 112, 139, 255), stop:0.880597 rgba(110, 243, 226, 255));"
        self.onStyle = "background-color: qlineargradient(spread:pad, x1:0.632, y1:0.613, x2:1, y2:0, stop:0.328358 rgba(0, 207, 124, 255), stop:0.462687 rgba(141, 112, 139, 255), stop:0.880597 rgba(110, 243, 226, 255));"
        self.fetchData()


    def fetchData(self):
        states = relay_channels.get()
        stateList = list(states.keys())
        print(states[stateList[0]])
        if states[stateList[0]]['state'] == 'on':
            self.Device1Check.setChecked(True)
            self.satus1.setText('ON')
            self.satus1.setStyleSheet(self.onStyle)
        else:
            self.Device1Check.setChecked(False)
            self.satus1.setText('OFF')
            self.satus1.setStyleSheet(self.offStyle)
        if states[stateList[1]]['state'] == 'on':
            self.Device2Check.setChecked(True)
            self.satus2.setText('ON')
            self.satus2.setStyleSheet(self.onStyle)
        else:
            self.Device2Check.setChecked(False)
            self.satus2.setText('OFF')
            self.satus2.setStyleSheet(self.offStyle)
        if states[stateList[2]]['state'] == 'on':
            self.Device3Check.setChecked(True)
            self.satus3.setText('ON')
            self.satus3.setStyleSheet(self.onStyle)
        else:
            self.Device3Check.setChecked(False)
            self.satus3.setText('OFF')
            self.satus3.setStyleSheet(self.offStyle)
        if states[stateList[3]]['state'] == 'on':
            self.Device4Check.setChecked(True)
            self.satus4.setText('ON')
            self.satus4.setStyleSheet(self.onStyle)
        else:
            self.Device4Check.setChecked(False)
            self.satus4.setText('OFF')
            self.satus4.setStyleSheet(self.offStyle)
        if states[stateList[4]]['state'] == 'on':
            self.Device5Check.setChecked(True)
            self.satus5.setText('ON')
            self.satus5.setStyleSheet(self.onStyle)
        else:
            self.Device5Check.setChecked(False)
            self.satus5.setText('OFF')
            self.satus5.setStyleSheet(self.offStyle)
        if states[stateList[5]]['state'] == 'on':
            self.Device6Check.setChecked(True)
            self.satus6.setText('ON')
            self.satus6.setStyleSheet(self.onStyle)
        else:
            self.Device6Check.setChecked(False)
            self.satus6.setText('OFF')
            self.satus6.setStyleSheet(self.offStyle)
        if states[stateList[6]]['state'] == 'on':
            self.Device7Check.setChecked(True)
            self.satus7.setText('ON')
            self.satus7.setStyleSheet(self.onStyle)
        else:
            self.Device7Check.setChecked(False)
            self.satus7.setText('OFF')
            self.satus7.setStyleSheet(self.offStyle)
        if states[stateList[7]]['state'] == 'on':
            self.Device8Check.setChecked(True)
            self.satus8.setText('ON')
            self.satus8.setStyleSheet(self.onStyle)
        else:
            self.Device8Check.setChecked(False)
            self.satus8.setText('OFF')
            self.satus8.setStyleSheet(self.offStyle)
        if states[stateList[8]]['state'] == 'on':
            self.Device9Check.setChecked(True)
            self.satus9.setText('ON')
            self.satus9.setStyleSheet(self.onStyle)
        else:
            self.Device9Check.setChecked(False)
            self.satus9.setText('OFF')
            self.satus9.setStyleSheet(self.offStyle)
        if states[stateList[9]]['state'] == 'on':
            self.Device10Check.setChecked(True)
            self.satus10.setText('ON')
            self.satus10.setStyleSheet(self.onStyle)
        else:
            self.Device10Check.setChecked(False)
            self.satus10.setText('OFF')
            self.satus10.setStyleSheet(self.offStyle)
        if states[stateList[10]]['state'] == 'on':
            self.Device11Check.setChecked(True)
            self.satus11.setText('ON')
            self.satus11.setStyleSheet(self.onStyle)
        else:
            self.Device11Check.setChecked(False)
            self.satus11.setText('OFF')
            self.satus11.setStyleSheet(self.offStyle)
        if states[stateList[11]]['state'] == 'on':
            self.Device12Check.setChecked(True)
            self.satus12.setText('ON')
            self.satus12.setStyleSheet(self.onStyle)
        else:
            self.Device12Check.setChecked(False)
            self.satus12.setText('OFF')
            self.satus12.setStyleSheet(self.offStyle)
        if states[stateList[12]]['state'] == 'on':
            self.Device13Check.setChecked(True)
            self.satus13.setText('ON')
            self.satus13.setStyleSheet(self.onStyle)
        else:
            self.Device13Check.setChecked(False)
            self.satus13.setText('OFF')
            self.satus13.setStyleSheet(self.offStyle)
        if states[stateList[13]]['state'] == 'on':
            self.Device14Check.setChecked(True)
            self.satus14.setText('ON')
            self.satus14.setStyleSheet(self.onStyle)
        else:
            self.Device14Check.setChecked(False)
            self.satus14.setText('OFF')
            self.satus14.setStyleSheet(self.offStyle)
        if states[stateList[14]]['state'] == 'on':
            self.Device15Check.setChecked(True)
            self.satus15.setText('ON')
            self.satus15.setStyleSheet(self.onStyle)
        else:
            self.Device15Check.setChecked(False)
            self.satus15.setText('OFF')
            self.satus15.setStyleSheet(self.offStyle)
        if states[stateList[15]]['state'] == 'on':
            self.Device16Check.setChecked(True)
            self.satus16.setText('ON')
            self.satus16.setStyleSheet(self.onStyle)
        else:
            self.Device16Check.setChecked(False)
            self.satus16.setText('OFF')
            self.satus16.setStyleSheet(self.offStyle)

    def relay1Control(self):
        try:
            state = self.Device1Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[0]}').update({"channel": "1", "state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[0]}').update({"channel": "1", "state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()

    def relay2Control(self):
        try:
            state = self.Device2Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[1]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[1]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay3Control(self):
        try:
            state = self.Device3Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[2]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[2]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay4Control(self):
        try:
            state = self.Device4Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[3]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[3]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay5Control(self):
        try:
            state = self.Device5Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[4]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[4]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay6Control(self):
        try:
            state = self.Device6Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[5]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[5]}').update({"state": "off","time":-1})
                self.fetchData()

        except Exception as e:
            print(e)
            self.showMessage()
    def relay7Control(self):
        try:
            state = self.Device7Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[6]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[6]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay8Control(self):
        try:
            state = self.Device8Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[7]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[7]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay9Control(self):
        try:
            state = self.Device9Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[8]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[8]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay10Control(self):
        try:
            state = self.Device10Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[9]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[9]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay11Control(self):
        try:
            state = self.Device11Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[10]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[10]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay12Control(self):
        try:
            state = self.Device12Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[11]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[11]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay13Control(self):
        try:
            state = self.Device13Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[12]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[12]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay14Control(self):
        try:
            state = self.Device14Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[13]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[13]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay15Control(self):
        try:
            state = self.Device15Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[14]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[14]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()
    def relay16Control(self):
        try:
            state = self.Device16Check.isChecked()
            if state == True:
                relay_channels.child(f'{globalId[15]}').update({"state": "on","time":time.ctime()})
                self.fetchData()
            else:
                relay_channels.child(f'{globalId[15]}').update({"state": "off","time":-1})
                self.fetchData()
        except Exception as e:
            print(e)
            self.showMessage()

    def showMessage(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('There was an error while changinh the state of the relay channel plz try again or check your connection')
        msgBox.setWindowTitle('Error!!')
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')





    def homeUp(self):
        widget.setCurrentIndex(0)
    def configureUp(self):
        widget.setCurrentIndex(1)
    def addDeviceUp(self):
        widget.setCurrentIndex(2)
    def deviceList(self):
        widget.setCurrentIndex(3)
    def controlUP(self):
        widget.setCurrentIndex(4)

class DeviceList(QMainWindow):
    def __init__(self):
        super(DeviceList, self).__init__()
        loadUi("DeviceList.ui",self)
        self.setWindowTitle('IOT controller')
        self.home.clicked.connect(self.homeUp)
        self.control.clicked.connect(self.controlUP)
        self.configure.clicked.connect(self.configureUp)
        self.add_device.clicked.connect(self.addDeviceUp)
        self.device_list.clicked.connect(self.deviceList)
        self.fetchDetils()
        stylesheetHeader = "::section{background-color:rgba(0,0,0,0.4);color:white}"
        self.TableWidget.horizontalHeader().setStyleSheet(stylesheetHeader)
        self.TableWidget.verticalHeader().setStyleSheet(stylesheetHeader)
        header = self.TableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

    def fetchDetils(self):
        device_list=devices.get()
        Devices=[]
        for device in device_list:
            Devices.append(device_list[device])
        data=[]
        for i in range(0,len(Devices)):
            entry=[Devices[i]['name'],Devices[i]['type'],Devices[i]['description'],
                   Devices[i]['rating'],Devices[i]['load']]
            data.append(entry)
        #inserting data into QTable widget
        self.TableWidget.setRowCount(len(data))
        row = 0
        for item in data:
            col = 0
            for key in range(0,5):
                self.TableWidget.setItem(row, col, QTableWidgetItem(f'{item[key]}'))
                col = col + 1
            row = row + 1


    def homeUp(self):
        widget.setCurrentIndex(0)
    def configureUp(self):
        widget.setCurrentIndex(1)
    def addDeviceUp(self):
        widget.setCurrentIndex(2)
    def deviceList(self):
        widget.setCurrentIndex(3)
    def controlUP(self):
        widget.setCurrentIndex(4)

class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        loadUi("Home.ui",self)
        self.setWindowTitle('IOT controller')
        self.home.clicked.connect(self.homeUp)
        self.control.clicked.connect(self.controlUP)
        self.configure.clicked.connect(self.configureUp)
        self.add_device.clicked.connect(self.addDeviceUp)
        self.device_list.clicked.connect(self.deviceList)
        self.getData()
        self.pushButton.clicked.connect(self.getData)
        header = self.TableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        stylesheetHeader = "::section{background-color:rgba(0,0,0,0.4);color:white}"
        self.TableWidget.horizontalHeader().setStyleSheet(stylesheetHeader)
        self.TableWidget.verticalHeader().setStyleSheet(stylesheetHeader)

        #this function will basically sun up the data and create the data we want

    def getData(self):
        try:
            # get the configuration data this will be used via indexing
            duration = []
            configurations = relay_channels.get()
            duration = []  # this will contain the time duration for which the device was active
            # getting the device data
            devList = device_config.get()

            deviceList = []
            for val in devList:
                deviceList.append(devList[val]['device_id'])

            devData = []
            Devices = devices.get()
            i = 1
            for val in deviceList:
                currDevice = Devices[val]
                devData.append({'col1': f'Device{i}', 'col2': currDevice['name'], 'col3': currDevice['type'],
                                'col4': currDevice['description'], 'col5': currDevice['rating']})
                i = i + 1


            for val in configurations:
                duration.append(configurations[val]['time'])

            currTime = []

            # this will get the device data
            # this will get the on duration
            for val in duration:
                if val == -1:
                    currTime.append(0)
                else:
                    currentTime = f'{time.ctime()}'
                    currentTime = datetime.strptime(currentTime, '%c')
                    on = datetime.strptime(val, '%c')
                    duration = ((
                                            currentTime - on).total_seconds()) / 60  # since hour is required for watt/hr power reading
                    currTime.append(duration)
            # summing up the data
            print(len(currTime))
            print(len(devData))
            i = 0
            finalData = []
            for value in devData:
                lastVal=float(currTime[i]) * float(value['col5'])
                entry = [value['col1'], value['col2'], value['col3'], value['col4'], value['col5'], currTime[i],
                         f'{lastVal}Watts']
                finalData.append(entry)
                i = i + 1

            self.setTable(finalData)
        except Exception as e:
            print(e)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText('The system ran into an error')
            msgBox.setWindowTitle('Fuck Off!!!!')
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                print('OK clicked')




    def setTable(self,data):
        self.TableWidget.setRowCount(16)
        row = 0
        for item in data:
            col = 0
            for key in range(0,7):
                self.TableWidget.setItem(row, col, QTableWidgetItem(f'{item[key]}'))
                col = col + 1
            row = row + 1
    def homeUp(self):
        widget.setCurrentIndex(0)
    def configureUp(self):
        widget.setCurrentIndex(1)
    def addDeviceUp(self):
        widget.setCurrentIndex(2)
    def deviceList(self):
        widget.setCurrentIndex(3)
    def controlUP(self):
        widget.setCurrentIndex(4)


#instantiating the widget classed


app = QApplication(sys.argv)
addDevcie = AddDevice()
configure = Configure()
controlDevice = deviceControl()
deviceList = DeviceList()
home = Home()

widget=QtWidgets.QStackedWidget()


widget.addWidget(home)
widget.addWidget(configure)
widget.addWidget(addDevcie)
widget.addWidget(deviceList)
widget.addWidget(controlDevice)


widget.setFixedWidth(1200)
widget.setFixedHeight(900)
widget.show()

try:
    sys.exit(app.exec_())

except:
    print("Exiting the app!!")
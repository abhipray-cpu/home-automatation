# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/Add_device.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formFrame = QtWidgets.QFrame(self.centralwidget)
        self.formFrame.setGeometry(QtCore.QRect(10, 10, 911, 511))
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        self.deviceNameLabel = QtWidgets.QLabel(self.formFrame)
        self.deviceNameLabel.setObjectName("deviceNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.deviceNameLabel)
        self.deviceNameLineEdit = QtWidgets.QLineEdit(self.formFrame)
        self.deviceNameLineEdit.setObjectName("deviceNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.deviceNameLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.deviceTypeLabel = QtWidgets.QLabel(self.formFrame)
        self.deviceTypeLabel.setObjectName("deviceTypeLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.deviceTypeLabel)
        self.deviceTypeComboBox = QtWidgets.QComboBox(self.formFrame)
        self.deviceTypeComboBox.setObjectName("deviceTypeComboBox")
        self.deviceTypeComboBox.addItem("")
        self.deviceTypeComboBox.addItem("")
        self.deviceTypeComboBox.addItem("")
        self.deviceTypeComboBox.addItem("")
        self.deviceTypeComboBox.addItem("")
        self.deviceTypeComboBox.addItem("")
        self.deviceTypeComboBox.addItem("")
        self.deviceTypeComboBox.addItem("")
        self.deviceTypeComboBox.addItem("")
        self.deviceTypeComboBox.addItem("")
        self.deviceTypeComboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.deviceTypeComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.loadTypeLabel = QtWidgets.QLabel(self.formFrame)
        self.loadTypeLabel.setObjectName("loadTypeLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.loadTypeLabel)
        self.loadTypeComboBox = QtWidgets.QComboBox(self.formFrame)
        self.loadTypeComboBox.setObjectName("loadTypeComboBox")
        self.loadTypeComboBox.addItem("")
        self.loadTypeComboBox.addItem("")
        self.loadTypeComboBox.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.loadTypeComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.deviceDescriptionLabel = QtWidgets.QLabel(self.formFrame)
        self.deviceDescriptionLabel.setObjectName("deviceDescriptionLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.deviceDescriptionLabel)
        self.deviceDescriptionLineEdit = QtWidgets.QLineEdit(self.formFrame)
        self.deviceDescriptionLineEdit.setObjectName("deviceDescriptionLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.deviceDescriptionLineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.formFrame)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 26))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        self.menuConfigure_Devices = QtWidgets.QMenu(self.menubar)
        self.menuConfigure_Devices.setObjectName("menuConfigure_Devices")
        self.menuDevice_Type = QtWidgets.QMenu(self.menubar)
        self.menuDevice_Type.setObjectName("menuDevice_Type")
        self.menuDevice_List = QtWidgets.QMenu(self.menubar)
        self.menuDevice_List.setObjectName("menuDevice_List")
        self.menuDashboard = QtWidgets.QMenu(self.menubar)
        self.menuDashboard.setObjectName("menuDashboard")
        self.menuToggle = QtWidgets.QMenu(self.menubar)
        self.menuToggle.setObjectName("menuToggle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuConfigure_Devices.menuAction())
        self.menubar.addAction(self.menuDevice_Type.menuAction())
        self.menubar.addAction(self.menuDevice_List.menuAction())
        self.menubar.addAction(self.menuDashboard.menuAction())
        self.menubar.addAction(self.menuToggle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.deviceNameLabel.setText(_translate("MainWindow", "Device Name"))
        self.deviceNameLineEdit.setPlaceholderText(_translate("MainWindow", "Add a device name"))
        self.deviceTypeLabel.setText(_translate("MainWindow", "Device Type"))
        self.deviceTypeComboBox.setItemText(0, _translate("MainWindow", "Bulb"))
        self.deviceTypeComboBox.setItemText(1, _translate("MainWindow", "Fan"))
        self.deviceTypeComboBox.setItemText(2, _translate("MainWindow", "Screen"))
        self.deviceTypeComboBox.setItemText(3, _translate("MainWindow", "Charger"))
        self.deviceTypeComboBox.setItemText(4, _translate("MainWindow", "Speaker"))
        self.deviceTypeComboBox.setItemText(5, _translate("MainWindow", "RGB Strip"))
        self.deviceTypeComboBox.setItemText(6, _translate("MainWindow", "LED Bulb"))
        self.deviceTypeComboBox.setItemText(7, _translate("MainWindow", "Lamp"))
        self.deviceTypeComboBox.setItemText(8, _translate("MainWindow", "Tubelight"))
        self.deviceTypeComboBox.setItemText(9, _translate("MainWindow", "Camera"))
        self.deviceTypeComboBox.setItemText(10, _translate("MainWindow", "Some other small appliance"))
        self.loadTypeLabel.setText(_translate("MainWindow", "Load Type"))
        self.loadTypeComboBox.setItemText(0, _translate("MainWindow", "Low load"))
        self.loadTypeComboBox.setItemText(1, _translate("MainWindow", "Medium Load"))
        self.loadTypeComboBox.setItemText(2, _translate("MainWindow", "Heavy Load"))
        self.deviceDescriptionLabel.setText(_translate("MainWindow", "Device Description"))
        self.deviceDescriptionLineEdit.setPlaceholderText(_translate("MainWindow", "Add a device description "))
        self.pushButton.setText(_translate("MainWindow", "Add Device"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.menuConfigure_Devices.setTitle(_translate("MainWindow", "Configure Devices"))
        self.menuDevice_Type.setTitle(_translate("MainWindow", "Add Device "))
        self.menuDevice_List.setTitle(_translate("MainWindow", "Device List"))
        self.menuDashboard.setTitle(_translate("MainWindow", "Dashboard"))
        self.menuToggle.setTitle(_translate("MainWindow", "Toggle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

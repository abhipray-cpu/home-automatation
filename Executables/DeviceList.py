# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/DeviceList.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 871, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(17)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(16, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(16, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(16, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(16, 3, item)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 26))
        self.menubar.setObjectName("menubar")
        self.menuHoe = QtWidgets.QMenu(self.menubar)
        self.menuHoe.setObjectName("menuHoe")
        self.menuConfigure_Device = QtWidgets.QMenu(self.menubar)
        self.menuConfigure_Device.setObjectName("menuConfigure_Device")
        self.menuAdd_Device = QtWidgets.QMenu(self.menubar)
        self.menuAdd_Device.setObjectName("menuAdd_Device")
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
        self.menubar.addAction(self.menuHoe.menuAction())
        self.menubar.addAction(self.menuConfigure_Device.menuAction())
        self.menubar.addAction(self.menuAdd_Device.menuAction())
        self.menubar.addAction(self.menuDevice_List.menuAction())
        self.menubar.addAction(self.menuDashboard.menuAction())
        self.menubar.addAction(self.menuToggle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Device Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Description"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Device1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Fan"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Device2"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "Bulb"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "Not in use"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "Device3"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "Charger"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "Device4"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "Screen"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogai teri maa ka bhosda"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "Device5"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "Speaker"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hoagyi teri maa ka bhosad"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "Device6"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("MainWindow", "RGB Light"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(5, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", "Device7"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("MainWindow", "Tube Light"))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(6, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainWindow", "Device8"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("MainWindow", "Fan"))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(7, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("MainWindow", "Device9"))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("MainWindow", "Bulb"))
        item = self.tableWidget.item(8, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(8, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("MainWindow", "Device10"))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("MainWindow", "Fan"))
        item = self.tableWidget.item(9, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(9, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("MainWindow", "Device11"))
        item = self.tableWidget.item(10, 1)
        item.setText(_translate("MainWindow", "Fan"))
        item = self.tableWidget.item(10, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(10, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("MainWindow", "Device12"))
        item = self.tableWidget.item(11, 1)
        item.setText(_translate("MainWindow", "Bulb"))
        item = self.tableWidget.item(11, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(11, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("MainWindow", "Device13"))
        item = self.tableWidget.item(12, 1)
        item.setText(_translate("MainWindow", "Charger"))
        item = self.tableWidget.item(12, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(12, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("MainWindow", "Device14"))
        item = self.tableWidget.item(13, 1)
        item.setText(_translate("MainWindow", "Screen"))
        item = self.tableWidget.item(13, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(13, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(14, 0)
        item.setText(_translate("MainWindow", "Device15"))
        item = self.tableWidget.item(14, 1)
        item.setText(_translate("MainWindow", "Screen"))
        item = self.tableWidget.item(14, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(14, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut teri maa ka bhosda"))
        item = self.tableWidget.item(15, 0)
        item.setText(_translate("MainWindow", "Device16"))
        item = self.tableWidget.item(15, 1)
        item.setText(_translate("MainWindow", "Bulb"))
        item = self.tableWidget.item(15, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(15, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut hogayi teri maa ka bhosda"))
        item = self.tableWidget.item(16, 0)
        item.setText(_translate("MainWindow", "Device17"))
        item = self.tableWidget.item(16, 1)
        item.setText(_translate("MainWindow", "Fan"))
        item = self.tableWidget.item(16, 2)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tableWidget.item(16, 3)
        item.setText(_translate("MainWindow", "Teri maa ki chut teri maa ka bhosda"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menuHoe.setTitle(_translate("MainWindow", "Hoe"))
        self.menuConfigure_Device.setTitle(_translate("MainWindow", "Configure Device"))
        self.menuAdd_Device.setTitle(_translate("MainWindow", "Add Device"))
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

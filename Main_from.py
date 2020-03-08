# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_from.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1267, 952)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.head_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.head_label.sizePolicy().hasHeightForWidth())
        self.head_label.setSizePolicy(sizePolicy)
        self.head_label.setText("")
        self.head_label.setPixmap(QtGui.QPixmap("image/QT.ico"))
        self.head_label.setObjectName("head_label")
        self.gridLayout.addWidget(self.head_label, 0, 0, 1, 1)
        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/quit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quit_btn.setIcon(icon)
        self.quit_btn.setIconSize(QtCore.QSize(24, 24))
        self.quit_btn.setObjectName("quit_btn")
        self.gridLayout.addWidget(self.quit_btn, 0, 1, 1, 1)
        self.tittle = QtWidgets.QLabel(self.centralwidget)
        self.tittle.setTextFormat(QtCore.Qt.AutoText)
        self.tittle.setObjectName("tittle")
        self.gridLayout.addWidget(self.tittle, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delete_all_btn = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/delete.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_all_btn.setIcon(icon1)
        self.delete_all_btn.setIconSize(QtCore.QSize(24, 24))
        self.delete_all_btn.setObjectName("delete_all_btn")
        self.horizontalLayout.addWidget(self.delete_all_btn)
        self.insert_btn = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insert_btn.setIcon(icon2)
        self.insert_btn.setIconSize(QtCore.QSize(24, 24))
        self.insert_btn.setObjectName("insert_btn")
        self.horizontalLayout.addWidget(self.insert_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1267, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.save_action = QtWidgets.QAction(MainWindow)
        self.save_action.setObjectName("save_action")
        self.menu.addAction(self.save_action)
        self.menu.addSeparator()
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quit_btn.setText(_translate("MainWindow", "退出"))
        self.tittle.setText(_translate("MainWindow", "待办事项"))
        self.delete_all_btn.setText(_translate("MainWindow", "删除全部"))
        self.insert_btn.setText(_translate("MainWindow", "新增事务"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.action.setText(_translate("MainWindow", "保存"))
        self.save_action.setText(_translate("MainWindow", "保存"))
        self.save_action.setToolTip(_translate("MainWindow", "保存"))
        self.save_action.setShortcut(_translate("MainWindow", "Ctrl+S"))


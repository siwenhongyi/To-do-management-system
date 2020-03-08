# -*- coding: utf-8 -*-
import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class log_on(QWidget):
	def __init__(self, parent=None, flags=Qt.WindowFlags()):
		super().__init__(parent=parent, flags=flags)
		self.setWindowTitle('注册')
		self.resize(300,300)
		self.setFixedSize(self.width(),self.height())
		self.setWindowFlags(Qt.WindowCloseButtonHint)
		#控件
		self.Frame=QFrame(self)
		self.verticalLayout = QVBoxLayout(self.Frame)
		#self.verticalLayout.setAlignment(Qt.AlignCenter)



		self.lineEdit_account = QLineEdit()
		self.lineEdit_account.setStyleSheet("selection-background-color: rgb(26, 26, 255);")
		self.lineEdit_account.setPlaceholderText("请输入超过六位账号")
		self.verticalLayout.addWidget(self.lineEdit_account)
		
		self.lineEdit_name = QLineEdit()
		self.lineEdit_name.setStyleSheet("selection-background-color: rgb(26, 26, 255);")
		self.lineEdit_name.setPlaceholderText("请输入用户名")
		self.verticalLayout.addWidget(self.lineEdit_name)


		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setEchoMode(QLineEdit.Password)
		self.lineEdit_password.setPlaceholderText("请输入密码")
		self.verticalLayout.addWidget(self.lineEdit_password)

		self.lineEdit_password_again = QLineEdit()
		self.lineEdit_password_again.setEchoMode(QLineEdit.Password)
		self.lineEdit_password_again.setPlaceholderText("请重复输入密码")
		self.verticalLayout.addWidget(self.lineEdit_password_again)


		self.pushButton_enter = QPushButton()
		self.pushButton_enter.setText("注册")
		self.verticalLayout.addWidget(self.pushButton_enter)

		self.setLayout(self.verticalLayout)
		###### 绑定按钮事件
		self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
		#super().__init__(parent=parent, flags=flags)

	def on_pushButton_enter_clicked(self):
		a=self.lineEdit_account.text()
		b=self.lineEdit_password.text()
		c=self.lineEdit_password_again.text()
		if len(a)<6:
			reply = QMessageBox.warning(self,"警告","账号小于6位！")
			self.lineEdit_account.clear()
			self.lineEdit_password.clear()
			self.lineEdit_password_again.clear()
			return False

		elif b!=c:
			reply = QMessageBox.warning(self,"警告","两次密码不同，请重新输入！")
			self.lineEdit_password.clear()
			self.lineEdit_password_again.clear()
			return False
		else:
			sql = sqlite3.connect('user_data.db')
			t = sql.execute("select id from user where id = '" + a +"';").fetchone()
			if t != None:
				reply = QMessageBox.warning(self,"警告","账户已经存在，请重新输入！")
				self.lineEdit_account.clear()
				sql.close()
				return False
			else:
				b=self.lineEdit_name.text()
				values = "('"+a+"','"+b+"','"+c+"');"
				print(values)
				sql.execute("insert into user values" +values)
				sql.commit()
				reply = QMessageBox.warning(self,"注册成功","账户注册成功！")
				sql.close()
				self.close()
				return True

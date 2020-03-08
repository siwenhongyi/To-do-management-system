# -*- coding:utf-8 -*-
import sys
import sqlite3
import log_on
from MainWindow import Main_Window
from PyQt5 import QtGui
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from Header import TitleBar,FramelessWindow

StyleSheet = """
/*最小化最大化关闭按钮通用默认背景*/
#buttonMinimum,#buttonMaximum,#buttonClose {
    border: none;
}
/*悬停*/
#buttonMinimum:hover,#buttonMaximum:hover {

    color: white;
}
#buttonClose:hover {
    color: white;
}
/*鼠标按下不放*/
#buttonMinimum:pressed,#buttonMaximum:pressed {

}
#buttonClose:pressed {
    color: white;

}
"""   #标题栏Button的样式

StyleSheet_2 = """
QComboBox{
        height: 20px;
        border-radius: 4px;
        border: 1px solid rgb(111, 156, 207);
        background: white;
}
QComboBox:enabled{
        color: grey;
}
QComboBox:!enabled {
        color: rgb(80, 80, 80);
}
QComboBox:enabled:hover, QComboBox:enabled:focus {
        color: rgb(51, 51, 51);
}
QComboBox::drop-down {
        background: transparent;
}
QComboBox::drop-down:hover {
        background: lightgrey;
}

QComboBox QAbstractItemView {
        border: 1px solid rgb(111, 156, 207);
        background: white;
        outline: none;
}

 QLineEdit {
        border-radius: 4px;
        height: 20px;
        border: 1px solid rgb(111, 156, 207);
        background: white;
}
QLineEdit:enabled {
        color: rgb(84, 84, 84);
}
QLineEdit:enabled:hover, QLineEdit:enabled:focus {
        color: rgb(51, 51, 51);
}
QLineEdit:!enabled {
        color: rgb(80, 80, 80);
}


"""   #QComobox和QLineEdite的样式

StyleSheet_btn = """
QPushButton{
    height:30px;
    background-color: transparent;
    color: grey;
    border: 2px solid #555555;
    border-radius: 6px;

}
QPushButton:hover {
    background-color: white;
    border-radius: 6px;

}
"""  #登录Button的样式


class loginWnd(QWidget):
	'''登录窗口'''
	def __init__(self, *args, **kwargs):
		super(loginWnd, self).__init__()
		self._layout = QVBoxLayout(spacing=0)
		self._layout.setContentsMargins(0, 0, 0, 0)
		self.setAutoFillBackground(True)
		self.setWindowOpacity(0.1)
		self.setLayout(self._layout)
		self.setAttribute(Qt.WA_DeleteOnClose)
		self._setup_ui()

	def _setup_ui(self):

		self.main_layout = QGridLayout()
		self.main_layout.setAlignment(Qt.AlignCenter)


		name_label = QLabel('账号')
		name_label.setStyleSheet("color:grey;")
		passwd_label = QLabel('密码')
		passwd_label.setStyleSheet("color:grey;")

		self.name_box = QComboBox()
		self.name_box.setEditable(True)
		self.passwd_box = QLineEdit()
		self.passwd_box.setEchoMode(QLineEdit.Password)
		self.name_box.setStyleSheet(StyleSheet)
		self.passwd_box.setStyleSheet(StyleSheet_2)

		label = QLabel()

		login_btn = QPushButton("登录")
		login_btn.setStyleSheet(StyleSheet_2)
		login_btn.setStyleSheet(StyleSheet_btn)
		logon_btn = QPushButton("注册")
		logon_btn.setStyleSheet(StyleSheet_2)
		logon_btn.setStyleSheet(StyleSheet_btn)

		self.main_layout.addWidget(name_label,0,0,1,1)
		self.main_layout.addWidget(passwd_label,3,0,1,1)
		self.main_layout.addWidget(self.name_box,0,1,1,2)
		self.main_layout.addWidget(self.passwd_box,3,1,1, 2)
		self.main_layout.addWidget(label,4,0,1,3)
		self.main_layout.addWidget(label,2,0,1,3)
		self.main_layout.addWidget(login_btn,5,0,1,3)
		self.main_layout.addWidget(label,6,0,1,3)
		self.main_layout.addWidget(logon_btn,7,0,1,3)
		self._layout.addLayout(self.main_layout)
		login_btn.clicked.connect(self.login_enter_chicked)
		logon_btn.clicked.connect(self.logon_enter_clicked)

	def login_enter_chicked(self):
		a=self.name_box.currentText()
		b=self.passwd_box.text()
		if a=='' or b=='':
			reply = QMessageBox.warning(self,"警告","账户或密码不能为空！")
			return False
		sql = sqlite3.connect("user_data.db")
		password = sql.execute("select password from user where id = " + a).fetchone()
		sql.close()
		if password and b==password[0]:
			self.t = Main_Window(a)
			self.t.show()
			self.close()
			return True
		else:
			reply = QMessageBox.warning(self,"警告","账户或密码错误，请重新输入！")
			self.passwd_box.clear()
			return False





	def logon_enter_clicked(self):
		self.t = log_on.log_on()
		self.t.show()
		return


def main():
	''':return:'''

	app = QApplication(sys.argv)
	mainWnd = FramelessWindow()
	mainWnd.setIconSize(30)
	mainWnd.setAutoFillBackground(True)
	mainWnd.setWindowTitle('login')
	mainWnd.setWindowIcon(QIcon('D:\学习资料\Projects\Python\待办事项管理系统\image\QT.ico'))
	mainWnd.setFixedSize(QSize(500,400))  #因为这里固定了大小，所以窗口的大小没有办法任意调整，想要使resizeWidget函数生效的话要把这里去掉，自己调节布局和窗口大小
	mainWnd.resize(500,400)
	mainWnd.setWidget(loginWnd(mainWnd))  # 把自己的窗口添加进来
	mainWnd.show()
	app.exec_()

main()
import sys
import sqlite3
import log_in
from Main_from import Ui_MainWindow
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Insert_D(QDialog):
	dialogSignel=pyqtSignal(int,list)
	def __init__(self,parent=None):
		super(Insert_D, self).__init__(parent)
		layout=QHBoxLayout(self)
		self.setFixedSize(1000,150)
		self.setWindowTitle('新增事务')
		self.line_name = QLineEdit()
		self.line_name.setPlaceholderText("输入代办事务名称")
		self.datetime=QDateTimeEdit(self)
		self.datetime.setCalendarPopup(True)
		self.datetime.setDateTime(QDateTime.currentDateTime())
		self.line_en = QLineEdit()
		self.line_en.setPlaceholderText("输入持续时间")

		layout.addWidget(self.line_name)
		layout.addWidget(self.datetime)
		layout.addWidget(self.line_en)

		buttons=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel,Qt.Horizontal,self)
		layout.addWidget(buttons)
		buttons.accepted.connect(self.accept)#点击ok
		buttons.rejected.connect(self.reject)#点击cancel
	def accept(self):
		re = []
		re.append(self.line_name.text())
		re.append(self.datetime.text())
		re.append(self.line_en.text())
		self.dialogSignel.emit(0,re)
		self.destroy()
	def reject(self):
		self.dialogSignel.emit(1,["清空"])
		self.destroy()


class Main_Window(QMainWindow,Ui_MainWindow):
	def __init__(self,a: str , parent=None, flags=Qt.WindowFlags()):
		super().__init__(parent=parent, flags=flags)
		self.setupUi(self)
		self.account = a
		self.setWindowTitle(self.account)
		self.event_tabel = QTableWidget()

		self.nodatahead_label =  QLabel()
		self.nodatahead_label.setAutoFillBackground(True)
		pur = QPixmap('image/nodata.jpg')
		self.nodatahead_label.setPixmap(pur)

		self.event_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

		self.delete_all_btn.clicked.connect(self.delete_all)
		self.insert_btn.clicked.connect(self.insert)
		self.quit_btn.clicked.connect(self.close)
		self.save_action.triggered.connect(self.save)




		self.set_data()


	def set_data(self):
		sql = sqlite3.connect('user_data.db')
		cur = sql.cursor()
		cur.execute("select event_id,name,st_time,en_time from event where user_id = '"+self.account+"' order by st_time")
		rows = cur.fetchall()
		rowc = len(rows)
		cur.close()
		sql.close()
		if rowc > 0:
			self.which = True
			vol = len(rows[0])
			self.event_tabel.clear()
			self.event_tabel.setRowCount(rowc)
			self.event_tabel.setColumnCount(len(rows[0]))
			self.event_tabel.setHorizontalHeaderLabels(['事务序号','事务名称','开始时间','持续时间'])
			for i in range(rowc):
				for j in range(vol):
					temp = rows[i][j]
					data = QTableWidgetItem(str(temp))
					if j == 0:
						data.setFlags(QtCore.Qt.ItemIsEnabled)
					self.event_tabel.setItem(i,j,data)
			self.verticalLayout.addWidget(self.event_tabel)
		else:
			self.which =  False
			self.verticalLayout.addWidget(self.nodatahead_label)
	def save(self):
		rowc = self.event_tabel.rowCount()
		sql = sqlite3.connect('user_data.db')
		for i in  range(rowc):
			event_id ="'" + str(i) + "'"
			event_name ="'" + self.event_tabel.item(i,1).text() + "'"
			event_st = "'" + self.event_tabel.item(i,2).text() + "'"
			even_en = "'" + self.event_tabel.item(i,3).text() + "'"
			sql.execute("update event set name = " + event_name + ",st_time = " + event_st + ",en_time = " + even_en + "where event_id = " + event_id + "and user_id = '" + self.account + "';")

		sql.commit()
		sql.close()

	def delete_all(self):
		sql = sqlite3.connect("user_data.db")
		sql.execute("delete from event where user_id = '" + self.account + "';")
		sql.commit()
		sql.close()
		if self.which:
			self.verticalLayout.removeWidget(self.event_tabel)
			self.gridLayout.removeWidget(self.event_tabel)
		else:
			self.verticalLayout.removeWidget(self.nodatahead_label)
			self.gridLayout.removeWidget(self.nodatahead_label)
		self.event_tabel.setRowCount(0)
		self.set_data()

	def insert(self):
		t=Insert_D(self)
		#t.setWindowModality(Qt.ApplicationModal)
		t.datetime.dateChanged.connect(self.slot_inner)
		t.dialogSignel.connect(self.slot_emit)
		#t.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		t.show()
		if self.which:
			self.verticalLayout.removeWidget(self.event_tabel)
			self.gridLayout.removeWidget(self.event_tabel)
		else:
			self.verticalLayout.removeWidget(self.nodatahead_label)
			self.gridLayout.removeWidget(self.nodatahead_label)
	def slot_inner(self,b):
		print(b)
		return
	def slot_emit(self,a,b):
		print(str(a)+str(b))
		if a == 0:
			new_id =self.event_tabel.rowCount() + 1
			print(new_id)
			new_name = ",'" + b[0] + "'"
			new_date =",'" + b[1] + "'"
			new_en = ",'" + b[2] + "'"
			if new_name!=",''" and new_en != ",''":
				sql = sqlite3.connect('user_data.db')
				sql.execute("insert into event values("+str(new_id) + ",'" +self.account + "'" + new_name + new_date + new_en + ");")
				sql.commit()
				sql.close()
		self.set_data()
		
# -*- coding: utf-8 -*-

import sys
import SQLite
import log_in
import MainWindow
from Header import TitleBar,FramelessWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize,Qt

from PyQt5.QtWidgets import *



def main():
	SQLite.main()
	log_in.main()

if __name__ == '__main()__':
	main()
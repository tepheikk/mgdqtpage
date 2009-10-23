# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pythonUi.ui'
#
# Created: Fri Oct 23 17:28:26 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PageEditor(object):
    def setupUi(self, PageEditor):
        PageEditor.setObjectName("PageEditor")
        PageEditor.resize(640, 480)
        self.centralwidget = QtGui.QWidget(PageEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.pagelist = QtGui.QListWidget(self.centralwidget)
        self.pagelist.setGeometry(QtCore.QRect(30, 60, 201, 321))
        self.pagelist.setObjectName("pagelist")
        self.pagetitle = QtGui.QLineEdit(self.centralwidget)
        self.pagetitle.setGeometry(QtCore.QRect(350, 20, 251, 22))
        self.pagetitle.setObjectName("pagetitle")
        self.texteditor = QtGui.QTextEdit(self.centralwidget)
        self.texteditor.setGeometry(QtCore.QRect(250, 60, 361, 321))
        self.texteditor.setObjectName("texteditor")
        self.savebutton = QtGui.QPushButton(self.centralwidget)
        self.savebutton.setGeometry(QtCore.QRect(240, 390, 115, 32))
        self.savebutton.setObjectName("savebutton")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 0, 31, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 40, 62, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 62, 17))
        self.label_3.setObjectName("label_3")
        self.newbutton = QtGui.QPushButton(self.centralwidget)
        self.newbutton.setGeometry(QtCore.QRect(0, 390, 115, 32))
        self.newbutton.setObjectName("newbutton")
        self.quitbutton = QtGui.QPushButton(self.centralwidget)
        self.quitbutton.setGeometry(QtCore.QRect(490, 390, 115, 32))
        self.quitbutton.setObjectName("quitbutton")
        PageEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PageEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        PageEditor.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PageEditor)
        self.statusbar.setObjectName("statusbar")
        PageEditor.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(PageEditor)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(PageEditor)
        QtCore.QMetaObject.connectSlotsByName(PageEditor)

    def retranslateUi(self, PageEditor):
        PageEditor.setWindowTitle(QtGui.QApplication.translate("PageEditor", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.savebutton.setText(QtGui.QApplication.translate("PageEditor", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PageEditor", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PageEditor", "Content", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PageEditor", "Pages", None, QtGui.QApplication.UnicodeUTF8))
        self.newbutton.setText(QtGui.QApplication.translate("PageEditor", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.quitbutton.setText(QtGui.QApplication.translate("PageEditor", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("PageEditor", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("PageEditor", "Quit", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-
import os
import sys
from PyQt4 import QtGui, QtCore
import sqlite3, Ui_PageEditor
from Ui_PageEditor import Ui_PageEditor
import _midgard as midgard

class MyTest(QtGui.QMainWindow, Ui_PageEditor):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.quitbutton.clicked.connect(self.quitcallback)
        self.newbutton.clicked.connect(self.newcallback)
        self.pagelist.itemDoubleClicked.connect(self.open_page)
        self.savebutton.clicked.connect(self.savecallback)
        
        self.update_list()
        
    def update_list(self):
        self.pagelist.clear()
        qb = midgard.query_builder('midgard_page')
        qb.add_order('title', 'ASC')
        res = qb.execute()
        for r in res:
            self.pagelist.insertItem(r.id, r.title)

    def savecallback(self):
        self.mgd_page.content = ("%s" % self.texteditor.toPlainText())
        self.mgd_page.title = ("%s" % self.pagetitle.text())
        self.mgd_page.update()
        self.update_list()
        
    def quitcallback(self):
        exit()
    
    def open_page(self, item=False):
        item = self.pagelist.currentItem()
        qb = midgard.query_builder('midgard_page')
        title = ("%s" % item.text())
        qb.add_constraint('title', '=', title)
        res = qb.execute()
        
        if len(res) == 0:
            return False
        
        self.mgd_page = res[0]
        self.texteditor.setText(res[0].content)
        self.pagetitle.setText(res[0].title)
        
        return True
    
    def newcallback(self):
        print "jee"
        page = midgard.mgdschema.midgard_page()
        page.title = "New page"
        page.create()
        page.title = ("New page (%s)" % page.id)
        page.update()
        self.update_list()    


configuration = midgard.config()
configuration.dbtype = 'SQLite'
configuration.database = 'new_db'
configuration.blobdir = os.path.join(os.path.expanduser("~"), "midgardblobs");
configuration.loglevel = 'message'

connection = midgard.connection()
connection.open_config(configuration)
midgard.storage.create_base_storage()
midgard.storage.create_class_storage('midgard_page')

app = QtGui.QApplication(sys.argv)

window = MyTest()
window.show()

sys.exit(app.exec_())
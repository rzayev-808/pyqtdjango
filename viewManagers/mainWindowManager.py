from views.mainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QHeaderView
from apps.obj.models import Product
from PyQt5.QtSql import *
from PyQt5 import QtCore
import os
from django.conf import settings


class mainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.addBtn.clicked.connect(self.addProduct)
        self.tableModel = QSqlQueryModel()
        self.tableModel.setHeaderData(0, QtCore.Qt.Horizontal, "Adi")
        self.tableModel.setHeaderData(1, QtCore.Qt.Horizontal, "Qiymet")
        self.tableModel.setHeaderData(2, QtCore.Qt.Horizontal, "Ulduz")
        self.tableView.setModel(self.tableModel)
        self.connection = self.create_db()

    def addProduct(self):
        name = self.nameLinEdit.text()
        price = self.priceLineEdit.text()
        stars = self.starsLineEdit.text()

        try:
            p = Product(name=name, price=price, star=stars)
            p.save()
        except Exception as e:
            print(e)

        if self.connection:
            query = QSqlQuery(str(Product.objects.all().values('name', 'price', 'star').query), self.db)
            self.tableModel.setQuery(query)
            self.tableView.setModel(self.tableModel)
            self.tableView.hide()
            self.tableModel.setHeaderData(0, QtCore.Qt.Horizontal, "Adi")
            self.tableModel.setHeaderData(1, QtCore.Qt.Horizontal, "Qiymeti")
            self.tableModel.setHeaderData(2, QtCore.Qt.Horizontal, "Reyting")
            for i in range(self.tableView.horizontalHeader().count()):
                self.tableView.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
            self.tableView.show()

    def create_db(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        db_name = os.path.join(settings.BASE_DIR, 'db.sqlite3')
        self.db.setDatabaseName(db_name)

        if not self.db.open():
            print("Baza tapilmadi")
            return False
        else :
            return True
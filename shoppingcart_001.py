import sys
import os
from PySide2 import QtGui,QtWidgets,QtCore
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
cartItems= []
cartTotal=0

itemPrices = {"Shirt":200,"Jacket":700,"Socks":100,"Vest":150,"Trouser":500}

class Form(QObject):
    def __init__(self, ui_file, parent = None):
        super(Form,self).__init__(parent)
        #load UI file
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        Loader = QUiLoader()
        self.window = Loader.load(ui_file)
        ui_file.close()

        # initialize Ui buttons.etc
        cmbItemList = self.window.findChild(QComboBox, "cmbItemList")
        btnAdd = self.window.findChild(QPushButton,"btnAdd")
        cmbItemList.addItem("Shirt")
        cmbItemList.addItem("Vest")
        cmbItemList.addItem("Trouser")
        cmbItemList.addItem("Socks")
        cmbItemList.addItem("Jacket")

        #make clickable event on button
        btnAdd.clicked.connect(self.updateCart)

        self.window.show()

    def addItem(self,ItemName):
        # Add current item in comboBox to listview
        lstViewCart = self.window.findChild(QListWidget, 'lstViewCart')
        cmbItemList = self.window.findChild(QComboBox, "cmbItemList")
        cartItems.append(ItemName)
        lstViewCart.addItem(cmbItemList.currentText())
    def updateCart(self):
        global cartItems, cartTotal, itemPrices
        #loop through all items in cart
        for item in cartItems:
            price = itemPrices.get(item, 0)
            cartTotal+=price
        lblTotal = self.window.findChild(QLabel, "lblTotal")
        cmbItemList = self.window.findChild(QComboBox, "cmbItemList")
        self.addItem(cmbItemList.currentText())
        lblSummary = self.window.findChild(QLabel, 'lblSummary')
        # Update cart summary
        cartSummary = dict((item, cartItems.count(item)) for item in cartItems)
        lblSummary.setText(str(cartSummary))
        lblTotal.setText(str(cartTotal))
        cartTotal=0


if __name__ == '__main__':
    #LOAD UI
    app = QApplication(sys.argv)
    form = Form('cart.ui')
    sys.exit(app.exec_())
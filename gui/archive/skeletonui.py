# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'traxis/gui/skeleton.ui'
#
# Created: Sun Oct 26 01:29:06 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gui_main(object):
    def setupUi(self, gui_main):
        gui_main.setObjectName("gui_main")
        gui_main.setEnabled(True)
        gui_main.resize(1024, 574)
        self.graphicsView = QtWidgets.QGraphicsView(gui_main)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1024, 341))
        self.graphicsView.setObjectName("graphicsView")
        self.zoom = QtWidgets.QFrame(gui_main)
        self.zoom.setGeometry(QtCore.QRect(610, 347, 411, 21))
        self.zoom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.zoom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.zoom.setObjectName("zoom")
        self.zoominButton = QtWidgets.QPushButton(self.zoom)
        self.zoominButton.setGeometry(QtCore.QRect(363, 2, 31, 19))
        self.zoominButton.setObjectName("zoominButton")
        self.zoomSlider = QtWidgets.QSlider(self.zoom)
        self.zoomSlider.setGeometry(QtCore.QRect(223, 2, 131, 19))
        self.zoomSlider.setSliderPosition(50)
        self.zoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSlider.setObjectName("zoomSlider")
        self.zoomoutButton = QtWidgets.QPushButton(self.zoom)
        self.zoomoutButton.setGeometry(QtCore.QRect(183, 2, 31, 19))
        self.zoomoutButton.setObjectName("zoomoutButton")
        self.zoomEdit = QtWidgets.QTextEdit(self.zoom)
        self.zoomEdit.setGeometry(QtCore.QRect(113, 1, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.zoomEdit.setFont(font)
        self.zoomEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.zoomEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.zoomEdit.setObjectName("zoomEdit")
        self.zoomLabel = QtWidgets.QLabel(self.zoom)
        self.zoomLabel.setGeometry(QtCore.QRect(34, 2, 71, 19))
        self.zoomLabel.setObjectName("zoomLabel")
        self.calcBox = QtWidgets.QGroupBox(gui_main)
        self.calcBox.setGeometry(QtCore.QRect(7, 350, 191, 221))
        self.calcBox.setObjectName("calcBox")
        self.pushButton = QtWidgets.QPushButton(self.calcBox)
        self.pushButton.setGeometry(QtCore.QRect(34, 20, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.calcBox)
        self.pushButton_2.setGeometry(QtCore.QRect(35, 100, 121, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.calcBox)
        self.pushButton_3.setGeometry(QtCore.QRect(35, 140, 121, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.calcBox)
        self.pushButton_4.setGeometry(QtCore.QRect(35, 180, 121, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.calcBox)
        self.pushButton_5.setGeometry(QtCore.QRect(35, 60, 71, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(self.calcBox)
        self.textEdit.setGeometry(QtCore.QRect(113, 60, 41, 21))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget = QtWidgets.QTabWidget(gui_main)
        self.tabWidget.setGeometry(QtCore.QRect(208, 350, 201, 221))
        self.tabWidget.setObjectName("tabWidget")
        self.pointsTab = QtWidgets.QWidget()
        self.pointsTab.setObjectName("pointsTab")
        self.tabWidget.addTab(self.pointsTab, "")
        self.tracksTab = QtWidgets.QWidget()
        self.tracksTab.setObjectName("tracksTab")
        self.tabWidget.addTab(self.tracksTab, "")
        self.consoleWidget = QtWidgets.QTabWidget(gui_main)
        self.consoleWidget.setEnabled(True)
        self.consoleWidget.setGeometry(QtCore.QRect(420, 350, 601, 221))
        self.consoleWidget.setAutoFillBackground(False)
        self.consoleWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.consoleWidget.setDocumentMode(False)
        self.consoleWidget.setTabsClosable(False)
        self.consoleWidget.setMovable(False)
        self.consoleWidget.setObjectName("consoleWidget")
        self.consoleTab = QtWidgets.QWidget()
        self.consoleTab.setObjectName("consoleTab")
        self.progressBar = QtWidgets.QProgressBar(self.consoleTab)
        self.progressBar.setGeometry(QtCore.QRect(410, 178, 181, 15))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.consoleWidget.addTab(self.consoleTab, "")

        self.retranslateUi(gui_main)
        self.tabWidget.setCurrentIndex(0)
        self.consoleWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(gui_main)

    def retranslateUi(self, gui_main):
        _translate = QtCore.QCoreApplication.translate
        gui_main.setWindowTitle(_translate("gui_main", "Dialog"))
        self.zoominButton.setText(_translate("gui_main", "+"))
        self.zoomoutButton.setText(_translate("gui_main", "-"))
        self.zoomEdit.setHtml(_translate("gui_main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">100.00%</span></p></body></html>"))
        self.zoomLabel.setText(_translate("gui_main", "Specify zoom:"))
        self.calcBox.setTitle(_translate("gui_main", "Calculations"))
        self.pushButton.setText(_translate("gui_main", "Place Point"))
        self.pushButton_2.setText(_translate("gui_main", "Set Reference Angle"))
        self.pushButton_3.setText(_translate("gui_main", "Fit Track to Points"))
        self.pushButton_4.setText(_translate("gui_main", "Get Optical Density"))
        self.pushButton_5.setText(_translate("gui_main", "Set dL:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pointsTab), _translate("gui_main", "Points"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tracksTab), _translate("gui_main", "Tracks"))
        self.consoleWidget.setTabText(self.consoleWidget.indexOf(self.consoleTab), _translate("gui_main", "Console"))

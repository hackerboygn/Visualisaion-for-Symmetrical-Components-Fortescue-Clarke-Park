# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'symmGui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 421)
        MainWindow.setMinimumSize(QtCore.QSize(493, 404))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setBaseSize(QtCore.QSize(493, 404))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_equations = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_equations.setFont(font)
        self.lbl_equations.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lbl_equations.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_equations.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_equations.setObjectName("lbl_equations")
        self.verticalLayout_2.addWidget(self.lbl_equations)
        self.lbl_units = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_units.setFont(font)
        self.lbl_units.setObjectName("lbl_units")
        self.verticalLayout_2.addWidget(self.lbl_units)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_phaseBMag = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseBMag.setFont(font)
        self.lbl_phaseBMag.setObjectName("lbl_phaseBMag")
        self.gridLayout.addWidget(self.lbl_phaseBMag, 1, 0, 1, 1)
        self.ledt_phaseAOmega = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseAOmega.setObjectName("ledt_phaseAOmega")
        self.gridLayout.addWidget(self.ledt_phaseAOmega, 0, 3, 1, 1)
        self.lbl_phaseAPhi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseAPhi.setFont(font)
        self.lbl_phaseAPhi.setObjectName("lbl_phaseAPhi")
        self.gridLayout.addWidget(self.lbl_phaseAPhi, 0, 4, 1, 1)
        self.lbl_phaseAMag = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseAMag.setFont(font)
        self.lbl_phaseAMag.setObjectName("lbl_phaseAMag")
        self.gridLayout.addWidget(self.lbl_phaseAMag, 0, 0, 1, 1)
        self.ledt_phaseAMag = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseAMag.setObjectName("ledt_phaseAMag")
        self.gridLayout.addWidget(self.ledt_phaseAMag, 0, 1, 1, 1)
        self.ledt_phaseAPhi = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseAPhi.setObjectName("ledt_phaseAPhi")
        self.gridLayout.addWidget(self.ledt_phaseAPhi, 0, 5, 1, 1)
        self.ledt_phaseCMag = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseCMag.setObjectName("ledt_phaseCMag")
        self.gridLayout.addWidget(self.ledt_phaseCMag, 2, 1, 1, 1)
        self.ledt_phaseBPhi = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseBPhi.setObjectName("ledt_phaseBPhi")
        self.gridLayout.addWidget(self.ledt_phaseBPhi, 1, 5, 1, 1)
        self.lbl_phaseCMag = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseCMag.setFont(font)
        self.lbl_phaseCMag.setObjectName("lbl_phaseCMag")
        self.gridLayout.addWidget(self.lbl_phaseCMag, 2, 0, 1, 1)
        self.ledt_phaseCOmega = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseCOmega.setObjectName("ledt_phaseCOmega")
        self.gridLayout.addWidget(self.ledt_phaseCOmega, 2, 3, 1, 1)
        self.lbl_phaseCOmega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseCOmega.setFont(font)
        self.lbl_phaseCOmega.setObjectName("lbl_phaseCOmega")
        self.gridLayout.addWidget(self.lbl_phaseCOmega, 2, 2, 1, 1)
        self.ledt_pllOmega = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_pllOmega.setObjectName("ledt_pllOmega")
        self.gridLayout.addWidget(self.ledt_pllOmega, 3, 1, 1, 1)
        self.lbl_pllOmega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_pllOmega.setFont(font)
        self.lbl_pllOmega.setObjectName("lbl_pllOmega")
        self.gridLayout.addWidget(self.lbl_pllOmega, 3, 0, 1, 1)
        self.ledt_phaseCPhi = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseCPhi.setObjectName("ledt_phaseCPhi")
        self.gridLayout.addWidget(self.ledt_phaseCPhi, 2, 5, 1, 1)
        self.lbl_phaseCPhi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseCPhi.setFont(font)
        self.lbl_phaseCPhi.setObjectName("lbl_phaseCPhi")
        self.gridLayout.addWidget(self.lbl_phaseCPhi, 2, 4, 1, 1)
        self.ledt_pllPhi = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_pllPhi.setObjectName("ledt_pllPhi")
        self.gridLayout.addWidget(self.ledt_pllPhi, 3, 3, 1, 1)
        self.ledt_time = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_time.setObjectName("ledt_time")
        self.gridLayout.addWidget(self.ledt_time, 4, 1, 1, 1)
        self.lbl_time = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_time.setFont(font)
        self.lbl_time.setObjectName("lbl_time")
        self.gridLayout.addWidget(self.lbl_time, 4, 0, 1, 1)
        self.ledt_phaseBOmega = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseBOmega.setObjectName("ledt_phaseBOmega")
        self.gridLayout.addWidget(self.ledt_phaseBOmega, 1, 3, 1, 1)
        self.lbl_phaseBPhi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseBPhi.setFont(font)
        self.lbl_phaseBPhi.setObjectName("lbl_phaseBPhi")
        self.gridLayout.addWidget(self.lbl_phaseBPhi, 1, 4, 1, 1)
        self.lbl_pllPhase = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_pllPhase.setFont(font)
        self.lbl_pllPhase.setObjectName("lbl_pllPhase")
        self.gridLayout.addWidget(self.lbl_pllPhase, 3, 2, 1, 1)
        self.lbl_phaseBOmega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseBOmega.setFont(font)
        self.lbl_phaseBOmega.setObjectName("lbl_phaseBOmega")
        self.gridLayout.addWidget(self.lbl_phaseBOmega, 1, 2, 1, 1)
        self.ledt_phaseBMag = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseBMag.setObjectName("ledt_phaseBMag")
        self.gridLayout.addWidget(self.ledt_phaseBMag, 1, 1, 1, 1)
        self.lbl_phaseAOmega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseAOmega.setFont(font)
        self.lbl_phaseAOmega.setObjectName("lbl_phaseAOmega")
        self.gridLayout.addWidget(self.lbl_phaseAOmega, 0, 2, 1, 1)
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setBold(True)
        font.setWeight(75)
        self.btn_update.setFont(font)
        self.btn_update.setObjectName("btn_update")
        self.gridLayout.addWidget(self.btn_update, 4, 5, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 26))
        self.menubar.setObjectName("menubar")
        self.menu1 = QtWidgets.QMenu(self.menubar)
        self.menu1.setObjectName("menu1")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.file_saveData = QtWidgets.QAction(MainWindow)
        self.file_saveData.setObjectName("file_saveData")
        self.help_Documentation = QtWidgets.QAction(MainWindow)
        self.help_Documentation.setObjectName("help_Documentation")
        self.help_About = QtWidgets.QAction(MainWindow)
        self.help_About.setObjectName("help_About")
        self.file_saveSetting = QtWidgets.QAction(MainWindow)
        self.file_saveSetting.setObjectName("file_saveSetting")
        self.menu1.addSeparator()
        self.menu1.addAction(self.file_saveData)
        self.menu1.addAction(self.file_saveSetting)
        self.menuHelp.addAction(self.help_Documentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.help_About)
        self.menubar.addAction(self.menu1.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.file_saveData.triggered.connect(self.test)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ledt_phaseAMag, self.ledt_phaseAOmega)
        MainWindow.setTabOrder(self.ledt_phaseAOmega, self.ledt_phaseAPhi)
        MainWindow.setTabOrder(self.ledt_phaseAPhi, self.ledt_phaseBMag)
        MainWindow.setTabOrder(self.ledt_phaseBMag, self.ledt_phaseBOmega)
        MainWindow.setTabOrder(self.ledt_phaseBOmega, self.ledt_phaseBPhi)
        MainWindow.setTabOrder(self.ledt_phaseBPhi, self.ledt_phaseCMag)
        MainWindow.setTabOrder(self.ledt_phaseCMag, self.ledt_phaseCOmega)
        MainWindow.setTabOrder(self.ledt_phaseCOmega, self.ledt_phaseCPhi)
        MainWindow.setTabOrder(self.ledt_phaseCPhi, self.ledt_pllOmega)
        MainWindow.setTabOrder(self.ledt_pllOmega, self.ledt_pllPhi)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_equations.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Equations:</span></p><p><img src=\":/equations_/equations_all_inputs_150.png\"/></p></body></html>"))
        self.lbl_units.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Units : angular freq. are in rad/s; phases are in rad, time in seconds</span></p></body></html>"))
        self.lbl_phaseBMag.setText(_translate("MainWindow", "<html><head/><body><p>Mag<span style=\" vertical-align:sub;\">b</span><span style=\" font-style:normal;\"> : </span></p></body></html>"))
        self.ledt_phaseAOmega.setToolTip(_translate("MainWindow", "The angular frequency of Phase-A input"))
        self.lbl_phaseAPhi.setText(_translate("MainWindow", "<html><head/><body><p>&phi;<span style=\" vertical-align:sub;\">a</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.lbl_phaseAMag.setText(_translate("MainWindow", "<html><head/><body><p>Mag<span style=\" vertical-align:sub;\">a</span><span style=\" font-style:normal;\"> : </span></p></body></html>"))
        self.ledt_phaseAMag.setToolTip(_translate("MainWindow", "The magnitude of Phase-A input"))
        self.ledt_phaseAPhi.setToolTip(_translate("MainWindow", "The initial phase of Phase-A input"))
        self.ledt_phaseCMag.setToolTip(_translate("MainWindow", "The magnitude of Phase-C input"))
        self.ledt_phaseBPhi.setToolTip(_translate("MainWindow", "The initial phase of Phase-B input"))
        self.lbl_phaseCMag.setText(_translate("MainWindow", "<html><head/><body><p>Mag<span style=\" vertical-align:sub;\">c</span><span style=\" font-style:normal;\"> : </span></p></body></html>"))
        self.ledt_phaseCOmega.setToolTip(_translate("MainWindow", "The angular frequency of Phase-C input"))
        self.lbl_phaseCOmega.setText(_translate("MainWindow", "<html><head/><body><p>ω<span style=\" vertical-align:sub;\">c</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_pllOmega.setToolTip(_translate("MainWindow", "The angular frequency of the PLL"))
        self.lbl_pllOmega.setText(_translate("MainWindow", "<html><head/><body><p>ω<span style=\" vertical-align:sub;\">PLL</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_phaseCPhi.setToolTip(_translate("MainWindow", "The initial phase of Phase-C input"))
        self.lbl_phaseCPhi.setText(_translate("MainWindow", "<html><head/><body><p>&phi;<span style=\" vertical-align:sub;\">c</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_pllPhi.setToolTip(_translate("MainWindow", "The initial phase of the PLL"))
        self.ledt_time.setToolTip(_translate("MainWindow", "The total time"))
        self.lbl_time.setText(_translate("MainWindow", "<html><head/><body><p>t<span style=\" font-style:normal;\"> : </span></p></body></html>"))
        self.ledt_phaseBOmega.setToolTip(_translate("MainWindow", "The angular frequency of Phase-B input"))
        self.lbl_phaseBPhi.setText(_translate("MainWindow", "<html><head/><body><p>&phi;<span style=\" vertical-align:sub;\">b</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.lbl_pllPhase.setText(_translate("MainWindow", "<html><head/><body><p>&phi;<span style=\" vertical-align:sub;\">PLL</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.lbl_phaseBOmega.setText(_translate("MainWindow", "<html><head/><body><p>ω<span style=\" vertical-align:sub;\">b</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_phaseBMag.setToolTip(_translate("MainWindow", "The magnitude of Phase-B input"))
        self.lbl_phaseAOmega.setText(_translate("MainWindow", "<html><head/><body><p>ω<span style=\" vertical-align:sub;\">a</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.btn_update.setText(_translate("MainWindow", "Update"))
        self.menu1.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.file_saveData.setText(_translate("MainWindow", "Save Data"))
        self.help_Documentation.setText(_translate("MainWindow", "Documentation"))
        self.help_About.setText(_translate("MainWindow", "About"))
        self.file_saveSetting.setText(_translate("MainWindow", "Save Setting"))

    def test(self):

        print('You clicked!')


import equations

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


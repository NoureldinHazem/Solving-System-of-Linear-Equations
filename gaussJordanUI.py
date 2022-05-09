from PyQt5 import QtCore, QtGui, QtWidgets
from eqnconvert import *
from gaussJordan import jordan


class Ui_gauss_jordanWindow(object):

    eqns = []
    results = []

    ############################################
    # importing the equations from a file
    ############################################
    def importBtnClicked(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Single File', QtCore.QDir.rootPath(), '*.txt')
        if filename != "":
            with open(filename, "r") as file:
                eqns = file.readlines()[2:]
                for eqn in eqns:
                    self.eqnTxt.append(str(eqn.strip()))

    ##########################
    #all logic goes here
    ##########################
    def calcClicked(self):
        self.eqns = self.eqnTxt.toPlainText().splitlines()
        eqns = readeqn_from_ui(self.eqns)
        matrix = list_to_matrix(eqns)
        self.results = jordan(matrix,len(self.eqns))
        output_filename = self.outfile.toPlainText()
        writefile(self.results, output_filename)


    def setupUi(self, jordanWindow):
        jordanWindow.setObjectName("jordanWindow")
        jordanWindow.resize(1888, 887)
        jordanWindow.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, "
            "stop:0 rgba(88, 82, 93, 122), stop:0.272251 rgba(177, 169, 198, 69), "
            "stop:0.413613 rgba(206, 217, 208, 145), stop:0.445026 rgba(203, 203, 203, 208), "
            "stop:0.507853 rgba(179, 179, 179, 130), stop:0.518717 rgba(207, 207, 207, 130), "
            "stop:0.55 rgba(202, 202, 202, 255), stop:0.57754 rgba(220, 196, 236, 130), "
            "stop:0.617801 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")

        self.centralwidget = QtWidgets.QWidget(jordanWindow)
        self.centralwidget.setObjectName("centralwidget")
        # ------------------------------------------------------------------------------------
        self.outfile = QtWidgets.QTextEdit(self.centralwidget)
        self.outfile.setGeometry(QtCore.QRect(430, 860, 950, 100))
        self.outfile.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), "
            "stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), "
            "stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), "
            "stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), "
            "stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), "
            "stop:1 rgba(156, 226, 191, 69));")

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.outfile.setFont(font)
        self.outfile.setObjectName("Comments")
        # ------------------------------------------------------------------------------------
        # ------------------------------------------------------------------------------------
        self.eqnTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.eqnTxt.setGeometry(QtCore.QRect(430, 160, 950, 400))
        self.eqnTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), "
            "stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), "
            "stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), "
            "stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), "
            "stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), "
            "stop:1 rgba(156, 226, 191, 69));")

        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.eqnTxt.setFont(font)
        self.eqnTxt.setObjectName("eqnTxt")
        # ------------------------------------------------------------------------------------
        self.calculateJordanBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calculateJordanBtn.clicked.connect(self.calcClicked)
        self.calculateJordanBtn.setGeometry(QtCore.QRect(570, 600, 341, 121))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.calculateJordanBtn.setFont(font)
        self.calculateJordanBtn.setAutoFillBackground(False)
        self.calculateJordanBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), "
            "stop:1 rgba(0, 0, 127, 255));\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;\n"
            "color: rgb(255, 255, 255);")

        self.calculateJordanBtn.setObjectName("calculateJordanBtn")
        # ------------------------------------------------------------------------------------
        self.funcLabel = QtWidgets.QLabel(self.centralwidget)
        self.funcLabel.setGeometry(QtCore.QRect(800, 70, 250, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.funcLabel.setFont(font)
        self.funcLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                     "background-color: rgba(255, 255, 255, 0);")
        self.funcLabel.setObjectName("funcLabel")
        # ------------------------------------------------------------------------------------
        self.outfilelbl = QtWidgets.QLabel(self.centralwidget)
        self.outfilelbl.setGeometry(QtCore.QRect(750, 800, 500, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.outfilelbl.setFont(font)
        self.outfilelbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                     "background-color: rgba(255, 255, 255, 0);")
        self.outfilelbl.setObjectName("commentlbl")
        # ------------------------------------------------------------------------------------
        self.importBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importBtn.setGeometry(QtCore.QRect(950, 600, 341, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.importBtn.setFont(font)
        self.importBtn.setAutoFillBackground(False)
        self.importBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), "
            "stop:1 rgba(91, 10, 145));\n"
            "color: rgb(255, 255, 255);\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;")
        self.importBtn.setObjectName("importBtn")
        self.importBtn.clicked.connect(self.importBtnClicked)
        # ------------------------------------------------------------------------------------
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.clicked.connect(jordanWindow.close)
        self.backBtn.setGeometry(QtCore.QRect(1600, 850, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.backBtn.setFont(font)
        self.backBtn.setAutoFillBackground(False)
        self.backBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), "
            "stop:1 rgba(170,0,0,255));\n"
            "color: rgb(255, 255, 255);\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;")
        self.backBtn.setObjectName("backBtn")
        jordanWindow.setCentralWidget(self.centralwidget)
        # ------------------------------------------------------------------------------------
        self.statusbar = QtWidgets.QStatusBar(jordanWindow)
        self.statusbar.setObjectName("statusbar")
        jordanWindow.setStatusBar(self.statusbar)
        # ------------------------------------------------------------------------------------
        self.retranslateUi(jordanWindow)
        QtCore.QMetaObject.connectSlotsByName(jordanWindow)

    def retranslateUi(self, jordanWindow):
        _translate = QtCore.QCoreApplication.translate
        jordanWindow.setWindowTitle(_translate("jordanWindow", "Jordan Method"))
        self.calculateJordanBtn.setText(_translate("jordanWindow", "Calculate Gauss Jordan Elimination"))
        self.funcLabel.setText(_translate("jordanWindow", "Equations"))
        self.importBtn.setText(_translate("jordanWindow", "Import Equations From File"))
        self.backBtn.setText(_translate("jordanWindow", "Back"))
        self.outfilelbl.setText(_translate("jordanWindow", "Name Of Output File"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    gauss_jordanWindow = QtWidgets.QMainWindow()
    ui = Ui_gauss_jordanWindow()
    ui.setupUi(gauss_jordanWindow)
    gauss_jordanWindow.show()
    sys.exit(app.exec_())

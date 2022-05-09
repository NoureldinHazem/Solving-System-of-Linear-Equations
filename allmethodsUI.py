from PyQt5 import QtCore, QtGui, QtWidgets
from eqnconvert import *
from gaussElimination import calculate_gauss
from luDecomposition import calculate_lu
from gaussJordan import jordan


class Ui_allmethods_Window(object):

    eqns = []
    results_gauss = []
    results_lu = []
    results_jordan = []

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
        matrix_gauss = list_to_matrix(eqns)
        matrix_lu = list_to_matrix(eqns)
        matrix_jordan = list_to_matrix(eqns)
        self.results_gauss = calculate_gauss(matrix_gauss, len(self.eqns))
        self.results_lu = calculate_lu(matrix_lu, len(self.eqns))
        self.results_jordan = jordan(matrix_jordan, len(self.eqns))
        output_filename = self.outfile.toPlainText()
        writefile(self.results_gauss, output_filename + "Gauss")
        writefile(self.results_lu, output_filename + "LU")
        writefile(self.results_jordan, output_filename + "Jordan")


    def setupUi(self, allmethodsWindow):
        allmethodsWindow.setObjectName("allmethodsWindow")
        allmethodsWindow.resize(1888, 887)
        allmethodsWindow.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, "
            "stop:0 rgba(88, 82, 93, 122), stop:0.272251 rgba(177, 169, 198, 69), "
            "stop:0.413613 rgba(206, 217, 208, 145), stop:0.445026 rgba(203, 203, 203, 208), "
            "stop:0.507853 rgba(179, 179, 179, 130), stop:0.518717 rgba(207, 207, 207, 130), "
            "stop:0.55 rgba(202, 202, 202, 255), stop:0.57754 rgba(220, 196, 236, 130), "
            "stop:0.617801 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")

        self.centralwidget = QtWidgets.QWidget(allmethodsWindow)
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
        self.calculateBisectionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calculateBisectionBtn.clicked.connect(self.calcClicked)
        self.calculateBisectionBtn.setGeometry(QtCore.QRect(570, 600, 341, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.calculateBisectionBtn.setFont(font)
        self.calculateBisectionBtn.setAutoFillBackground(False)
        self.calculateBisectionBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), "
            "stop:1 rgba(0, 0, 127, 255));\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;\n"
            "color: rgb(255, 255, 255);")

        self.calculateBisectionBtn.setObjectName("calculateBisectionBtn")
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
        self.backBtn.clicked.connect(allmethodsWindow.close)
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
        allmethodsWindow.setCentralWidget(self.centralwidget)
        # ------------------------------------------------------------------------------------
        self.statusbar = QtWidgets.QStatusBar(allmethodsWindow)
        self.statusbar.setObjectName("statusbar")
        allmethodsWindow.setStatusBar(self.statusbar)
        # ------------------------------------------------------------------------------------
        self.retranslateUi(allmethodsWindow)
        QtCore.QMetaObject.connectSlotsByName(allmethodsWindow)

    def retranslateUi(self, allmethodsWindow):
        _translate = QtCore.QCoreApplication.translate
        allmethodsWindow.setWindowTitle(_translate("allmethodsWindow", "All Methods"))
        self.calculateBisectionBtn.setText(_translate("allmethodsWindow", "Calculate All Methods"))
        self.funcLabel.setText(_translate("allmethodsWindow", "Equations"))
        self.importBtn.setText(_translate("allmethodsWindow", "Import Equations From File"))
        self.backBtn.setText(_translate("allmethodsWindow", "Back"))
        self.outfilelbl.setText(_translate("allmethodsWindow", "Name Of Output File"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    allmethodsWindow = QtWidgets.QMainWindow()
    ui = Ui_allmethods_Window()
    ui.setupUi(allmethodsWindow)
    allmethodsWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from gaussEliminationUI import Ui_gauss_eliminationWindow
from gaussJordanUI import Ui_gauss_jordanWindow
from luDecompositionUI import Ui_lu_decompositionWindow
from allmethodsUI import Ui_allmethods_Window

class Ui_linear_equations(object):

    def openGauss_Elimination(self):
        self.gauss_eliminationWindow = QtWidgets.QMainWindow()
        self.ui = Ui_gauss_eliminationWindow()
        self.ui.setupUi(self.gauss_eliminationWindow)
        self.gauss_eliminationWindow.show()

    def openLU_Decomposition(self):
        self.lU_decompositionWindow = QtWidgets.QMainWindow()
        self.ui = Ui_lu_decompositionWindow()
        self.ui.setupUi(self.lU_decompositionWindow)
        self.lU_decompositionWindow.show()

    def openGauss_Jordan(self):
        self.gauss_jordanWindow = QtWidgets.QMainWindow()
        self.ui = Ui_gauss_jordanWindow()
        self.ui.setupUi(self.gauss_jordanWindow)
        self.gauss_jordanWindow.show()

    def openAll_Methods(self):
        self.allmethodsWindow = QtWidgets.QMainWindow()
        self.ui = Ui_allmethods_Window()
        self.ui.setupUi(self.allmethodsWindow)
        self.allmethodsWindow.show()

    def setupUi(self, linearEquations):
        linearEquations.setObjectName("linearEquations")
        linearEquations.resize(1909, 901)
        linearEquations.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, "
                                      "stop:0 rgba(88, 82, 93, 122), "
                                      "stop:0.272251 rgba(177, 169, 198, 69), "
                                      "stop:0.413613 rgba(206, 217, 208, 145), "
                                      "stop:0.445026 rgba(203, 203, 203, 208), "
                                      "stop:0.507853 rgba(179, 179, 179, 130), "
                                      "stop:0.518717 rgba(207, 207, 207, 130), "
                                      "stop:0.55 rgba(202, 202, 202, 255), "
                                      "stop:0.57754 rgba(220, 196, 236, 130), "
                                      "stop:0.617801 rgba(243, 216, 220, 69), "
                                      "stop:1 rgba(156, 226, 191, 69));")

        self.centralwidget = QtWidgets.QWidget(linearEquations)
        self.centralwidget.setObjectName("centralwidget")

        # -----------------------------------------------------------------------------------------------------

        self.gauss_eliminationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.gauss_eliminationBtn.clicked.connect(self.openGauss_Elimination)
        self.gauss_eliminationBtn.setGeometry(QtCore.QRect(730, 310, 421, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gauss_eliminationBtn.setFont(font)
        self.gauss_eliminationBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), "
            "stop:1 rgba(0, 0, 127, 255));\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;\n"
            "color: rgb(255, 255, 255);")
        self.gauss_eliminationBtn.setObjectName("gauss_eliminationBtn")

        # -----------------------------------------------------------------------------------------------------

        self.lU_decompositionBtn = QtWidgets.QPushButton(self.centralwidget)

        self.lU_decompositionBtn.clicked.connect(self.openLU_Decomposition)
        self.lU_decompositionBtn.setGeometry(QtCore.QRect(730, 440, 421, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lU_decompositionBtn.setFont(font)
        self.lU_decompositionBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
            "stop:0 rgba(0, 0, 0, 255), stop:1 rgba(91, 10, 145));\n"
            "color: rgb(255, 255, 255);\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;")
        self.lU_decompositionBtn.setObjectName("lU_decompositionBtn")

        # -----------------------------------------------------------------------------------------------------

        self.gauss_jordanBtn = QtWidgets.QPushButton(self.centralwidget)
        self.gauss_jordanBtn.clicked.connect(self.openGauss_Jordan)
        self.gauss_jordanBtn.setGeometry(QtCore.QRect(730, 570, 421, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gauss_jordanBtn.setFont(font)
        self.gauss_jordanBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
            "stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 127, 127, 255));\n"
            "color: rgb(255, 255, 255);\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;")
        self.gauss_jordanBtn.setObjectName("gauss_jordanBtn")

        # -----------------------------------------------------------------------------------------------------

        self.all_methodsBtn = QtWidgets.QPushButton(self.centralwidget)

        self.all_methodsBtn.clicked.connect(self.openAll_Methods)
        self.all_methodsBtn.setGeometry(QtCore.QRect(730, 700, 421, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.all_methodsBtn.setFont(font)
        self.all_methodsBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
            "stop:0 rgba(0, 0, 0, 255), stop:1 rgba(249,215,28));\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;\n"
            "color: rgb(255, 255, 255);")
        self.all_methodsBtn.setObjectName("all_methodsBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(0, 0, 127);\n"
                                 "background-color: rgba(255, 255, 255, 0);")
        self.label.setGeometry(QtCore.QRect(420, 70, 1541, 231))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        linearEquations.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(linearEquations)
        self.statusbar.setObjectName("statusbar")
        linearEquations.setStatusBar(self.statusbar)

        self.retranslateUi(linearEquations)
        QtCore.QMetaObject.connectSlotsByName(linearEquations)

    def retranslateUi(self, linearEquations):
        _translate = QtCore.QCoreApplication.translate
        linearEquations.setWindowTitle(_translate("linearEquations", "System of Linear Equations"))
        self.gauss_eliminationBtn.setText(_translate("linearEquations", "Gauss Elimination"))
        self.lU_decompositionBtn.setText(_translate("linearEquations", "LU Decomposition"))
        self.gauss_jordanBtn.setText(_translate("linearEquations", "Gauss Jordan"))
        self.all_methodsBtn.setText(_translate("linearEquations", "All Methods"))
        self.label.setText(_translate("linearEquations", "Please select the desired method"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    linearEquations = QtWidgets.QMainWindow()
    ui = Ui_linear_equations()
    ui.setupUi(linearEquations)
    linearEquations.show()
    sys.exit(app.exec_())

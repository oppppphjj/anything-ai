# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from initGUI.DragAndDropLabel import DragAndDropLabel
from serverCore.filestore import VisualTable


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 70, 731, 511))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "\n"
                                 "border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 151, 511))
        self.label_2.setStyleSheet("background-color: rgb(104, 104, 104);\n"
                                   "\n"
                                   "border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.btn_tochat = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tochat.setGeometry(QtCore.QRect(120, 100, 151, 71))
        self.btn_tochat.setObjectName("btn_tochat")
        self.btn_tostudy = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tostudy.setGeometry(QtCore.QRect(120, 180, 151, 71))
        self.btn_tostudy.setStyleSheet("")
        self.btn_tostudy.setObjectName("btn_tostudy")
        self.btn_toimage = QtWidgets.QPushButton(self.centralwidget)
        self.btn_toimage.setGeometry(QtCore.QRect(120, 260, 151, 71))
        self.btn_toimage.setObjectName("btn_toimage")
        self.btn_toaboutus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_toaboutus.setGeometry(QtCore.QRect(120, 340, 151, 71))
        self.btn_toaboutus.setObjectName("btn_toaboutus")
        self.btn_tomain = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tomain.setGeometry(QtCore.QRect(150, 520, 91, 31))
        self.btn_tomain.setStyleSheet("border-image: url(:/openAI/openAI公司名称图片.png);")
        self.btn_tomain.setText("")
        self.btn_tomain.setObjectName("btn_tomain")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(280, 110, 561, 461))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_main = QtWidgets.QWidget()
        self.page_main.setObjectName("page_main")
        self.label_3 = QtWidgets.QLabel(self.page_main)
        self.label_3.setGeometry(QtCore.QRect(130, 90, 261, 51))
        self.label_3.setStyleSheet("border-image: url(:/openAI/openAI商标.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_main)
        self.label_4.setGeometry(QtCore.QRect(210, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_main)
        self.page_chat = QtWidgets.QWidget()
        self.page_chat.setObjectName("page_chat")
        self.label_5 = QtWidgets.QLabel(self.page_chat)
        self.label_5.setGeometry(QtCore.QRect(220, 0, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.text_edit = QtWidgets.QTextEdit(self.page_chat)
        self.text_edit.setGeometry(QtCore.QRect(10, 50, 551, 291))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.text_edit.setFont(font)
        self.text_edit.setReadOnly(True)
        self.text_edit.setObjectName("text_edit")
        self.input_edit = QtWidgets.QLineEdit(self.page_chat)
        self.input_edit.setGeometry(QtCore.QRect(10, 380, 451, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.input_edit.setFont(font)
        self.input_edit.setObjectName("input_edit")
        self.send_button = QtWidgets.QPushButton(self.page_chat)
        self.send_button.setGeometry(QtCore.QRect(470, 380, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.send_button.setFont(font)
        self.send_button.setObjectName("send_button")
        self.stackedWidget.addWidget(self.page_chat)
        self.page_study = QtWidgets.QWidget()
        self.page_study.setObjectName("page_study")

        self.file_label = DragAndDropLabel(self.page_study)
        self.file_label.setGeometry(QtCore.QRect(10, 280, 151, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.file_label.setFont(font)
        self.file_label.setStyleSheet("border:1px solid rgb(214, 214, 214)")
        self.file_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_label.setObjectName("file_label")
        self.learn_textEdit = QtWidgets.QTextEdit(self.page_study)
        self.learn_textEdit.setEnabled(True)
        self.learn_textEdit.setGeometry(QtCore.QRect(240, 20, 311, 381))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.learn_textEdit.setFont(font)
        self.learn_textEdit.setObjectName("learn_textEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_study)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 410, 431, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.ask_btn = QtWidgets.QPushButton(self.page_study)
        self.ask_btn.setGeometry(QtCore.QRect(460, 410, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.ask_btn.setFont(font)
        self.ask_btn.setObjectName("ask_btn")
        self.btn_learn = QtWidgets.QPushButton(self.page_study)
        self.btn_learn.setGeometry(QtCore.QRect(170, 330, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.btn_learn.setFont(font)
        self.btn_learn.setStyleSheet("border:1px solid rgb(0, 0, 0)")
        self.btn_learn.setObjectName("btn_learn")
        self.label_6 = QtWidgets.QLabel(self.page_study)
        self.label_6.setGeometry(QtCore.QRect(80, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        # 获取
        self.learn_tableView = VisualTable(self.page_study)
        self.learn_tableView.setGeometry(QtCore.QRect(0, 80, 231, 171))
        self.learn_tableView.setStyleSheet("border:none")
        self.learn_tableView.setObjectName("learn_tableView")
        self.label_7 = QtWidgets.QLabel(self.page_study)
        self.label_7.setGeometry(QtCore.QRect(0, 60, 71, 16))
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page_study)
        self.page_ltoi = QtWidgets.QWidget()
        self.page_ltoi.setObjectName("page_ltoi")
        self.image_edit = QtWidgets.QLineEdit(self.page_ltoi)
        self.image_edit.setGeometry(QtCore.QRect(30, 380, 411, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.image_edit.setFont(font)
        self.image_edit.setObjectName("image_edit")
        self.create_button = QtWidgets.QPushButton(self.page_ltoi)
        self.create_button.setGeometry(QtCore.QRect(460, 380, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.create_button.setFont(font)
        self.create_button.setObjectName("create_button")
        self.label_10 = QtWidgets.QLabel(self.page_ltoi)
        self.label_10.setGeometry(QtCore.QRect(180, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(21)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.image_label = QtWidgets.QLabel(self.page_ltoi)
        self.image_label.setGeometry(QtCore.QRect(120, 80, 256, 256))
        self.image_label.setStyleSheet("background-color: rgb(197, 233, 255);")
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.stackedWidget.addWidget(self.page_ltoi)
        self.page_aboutus = QtWidgets.QWidget()
        self.page_aboutus.setObjectName("page_aboutus")
        self.label_9 = QtWidgets.QLabel(self.page_aboutus)
        self.label_9.setGeometry(QtCore.QRect(50, 40, 71, 41))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.page_aboutus)
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setGeometry(QtCore.QRect(760, 70, 81, 41))
        self.horizontalFrame.setStyleSheet("QPushButton{\n"
                                           "    border:none;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "    padding-bottom:5px;\n"
                                           "}")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_min = QtWidgets.QPushButton(self.horizontalFrame)
        self.btn_min.setText("")
        # 添加icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/jian.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_min.setIcon(icon)

        self.btn_min.setObjectName("btn_min")
        self.horizontalLayout.addWidget(self.btn_min)
        self.btn_close = QtWidgets.QPushButton(self.horizontalFrame)
        self.btn_close.setEnabled(True)
        self.btn_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/cha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QtCore.QSize(13, 13))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.btn_toaboutus_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_toaboutus_2.setGeometry(QtCore.QRect(120, 420, 151, 71))
        self.btn_toaboutus_2.setObjectName("btn_toaboutus_2")
        self.label.raise_()
        self.label_2.raise_()
        self.btn_tochat.raise_()
        self.btn_tostudy.raise_()
        self.btn_toimage.raise_()
        self.btn_toaboutus.raise_()
        self.btn_tomain.raise_()
        self.horizontalFrame.raise_()
        self.stackedWidget.raise_()
        self.btn_toaboutus_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.btn_close.clicked.connect(MainWindow.close)  # type: ignore
        self.btn_min.clicked.connect(MainWindow.showMinimized)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_tochat.setText(_translate("MainWindow", "与GPT对话"))
        self.btn_tostudy.setText(_translate("MainWindow", "使GPT学习"))
        self.btn_toimage.setText(_translate("MainWindow", "文字→图片"))
        self.btn_toaboutus.setText(_translate("MainWindow", "关于我们"))
        self.label_4.setText(_translate("MainWindow", "欢迎来到"))
        self.label_5.setText(_translate("MainWindow", "talk with AI"))
        self.send_button.setText(_translate("MainWindow", "send"))
        self.file_label.setText(_translate("MainWindow", "请拖入文档"))
        self.ask_btn.setText(_translate("MainWindow", "提问"))
        self.btn_learn.setText(_translate("MainWindow", "学习"))
        self.label_6.setText(_translate("MainWindow", "let AI learning"))
        self.label_7.setText(_translate("MainWindow", "已学习文档"))
        self.create_button.setText(_translate("MainWindow", "create"))
        self.label_10.setText(_translate("MainWindow", "以文丹青"))
        self.btn_toaboutus_2.setText(_translate("MainWindow", "fine-tuning"))
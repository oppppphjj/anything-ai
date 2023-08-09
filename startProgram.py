import os.path
import sys
import requests
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap, QStandardItem, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import pages.main as main
import resource.res_rc
from AIcore.openAI import openAImyAPI
from serverCore import fileClassification


class demoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)

        # 页面切换
        self.ui.btn_tochat.clicked.connect(lambda: self.showPageTalkWithAI())  # type: ignore
        self.ui.btn_tostudy.clicked.connect(lambda: self.showPageMakeAIStudy())  # type: ignore
        self.ui.btn_toimage.clicked.connect(lambda: self.showPagelanguageToImage())  # type: ignore
        self.ui.btn_toaboutus.clicked.connect(lambda: self.showPageAboutUs())  # type: ignore
        self.ui.btn_tomain.clicked.connect(lambda: self.showPageMain())  # type: ignore

        # 信号与槽函数的连接
        # 聊天
        self.ui.send_button.clicked.connect(lambda: self.send_message(self.ui.input_edit, self.ui.text_edit))  # type: ignore
        # 生成绘画
        self.ui.create_button.clicked.connect(
            lambda: self.send_imgePrompt(self.ui.image_edit, self.ui.image_label))  # type: ignore
        # 以文本未基础对话
        self.ui.ask_btn.clicked.connect(lambda: self.send_ask(self.ui.lineEdit_2, self.ui.learn_textEdit, self.ui.file_label.text()))
        # 文本学习
        self.ui.btn_learn.clicked.connect(lambda: self.openAI_learn(self.ui.learn_textEdit, self.ui.learn_tableView, self.ui.file_label))

        # 下面两段会有未解析的特性引用
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.show()

    # 实现窗口拖动
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    # 相关的槽函数，懒得解耦啦
    def showPageTalkWithAI(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        print("点击了showPageTalkWithAI")

    def showPageMakeAIStudy(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        print("点击了showPageMakeAIStudy")

    def showPagelanguageToImage(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        print("点击了showPagelanguageToImage")

    def showPageAboutUs(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        print("点击了showPageAboutUs")

    def showPageMain(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        print("点击了showPageMain")

    def send_message(self, input_edit, text_edit):
        user_input = input_edit.text()
        text_edit.append("用户: " + user_input + "\n")  # 将用户输入显示在 QTextEdit 中
        # 在这里进行机器回复的处理，将回复添加到 QTextEdit 中
        # 例如，你可以使用 OpenAI 的 API 进行聊天机器人回复
        # 使用接口
        myApi = openAImyAPI()
        machine_reply = "GPT：" + myApi.createChat(user_input)
        text_edit.append(machine_reply + "\n")
        input_edit.clear()  # 清空用户输入
        print("发送消息")

    def send_imgePrompt(self, image_edit, image_label):
        # 使用接口
        myApi = openAImyAPI()
        url = myApi.createImage(image_edit.text())
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
        image_label.setPixmap(pixmap)
        print("生成图片")

    def send_ask(self,input_edit,text_edit, url):
        user_input = input_edit.text()
        text_edit.append("用户: " + user_input + "\n")  # 将用户输入显示在 QTextEdit 中

        # 提取文本内容
        fileContext = fileClassification.Datapreprocessing().fileClassification(url)

#       ----使用API、改变text_edit----
        machine_reply = "GPT：" + openAImyAPI().createlearn(fileContext, user_input)
        text_edit.append(machine_reply + "\n")

        input_edit.clear()
        print("提问完成")

    def openAI_learn(self, text_edit, tableView, filelabel):
        # 提示可以开始提问
        text_edit.append("GPT:我已完成学习请开始提问吧！\n")  # 将用户输入显示在 QTextEdit 中

        file_path = filelabel.text()
        file_name = os.path.basename(file_path)
        print(file_name)

        new_item = QStandardItem(file_name)
        # 划分file类型，设置图标
        if file_name.endswith('.docx'):
            icon = QIcon()  # 请将文件路径替换为实际的图标文件路径
            icon.addPixmap(QtGui.QPixmap(":/icon/word_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif file_name.endswith('.pdf'):
            icon = QIcon()  # 请将文件路径替换为实际的图标文件路径
            icon.addPixmap(QtGui.QPixmap(":/icon/pdf_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif file_name.endswith('.txt'):
            icon = QIcon()  # 请将文件路径替换为实际的图标文件路径
            icon.addPixmap(QtGui.QPixmap(":/icon/txt_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif file_name.endswith('.xlsx'):
            icon = QIcon()  # 请将文件路径替换为实际的图标文件路径
            icon.addPixmap(QtGui.QPixmap(":/icon/xlsx_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon = QIcon()

        new_item.setIcon(icon)
        # 建立加入到学习信息表中
        # new_item.setSizeHint(new_item.sizeHint().setWidth(230))
        # new_item.setSizeHint(new_item.sizeHint().setHeight(31))
        tableView.model.appendRow([new_item])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = demoWindow()
    sys.exit(app.exec_())

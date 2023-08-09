from PyQt5 import QtGui
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QTableView, QHeaderView

class VisualTable(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 初始化model
        self.model = QStandardItemModel(self)
        self.setModel(self.model)

        # 隐藏行与列
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.setColumnWidth(1, 230)
        # self.setLayout()
        # self.setMaximumSize(100,100)
        # self.setMinimumSize(100,100)

        # self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)


    #     # # 制造一个model
    #     # self.model = QStandardItemModel(self)
    #     # self.setModel(self.model)
    #     #
    #     # #
    #     # self.populate_table()
    #
    #
    # def populate_table(self):
    #     items = [
    #         ('dox', '文件1.dox'),
    #         ('dox', '文件2.dox'),
    #         ('pdf', '文件3.pdf')
    #     ]
    #     self.model.setColumnCount(1)
    #     self.model.setRowCount(len(items))
    #
    #     for row, (file_type, item_text) in enumerate(items):
    #         item = QStandardItem(item_text)
    #         self.model.setItem(row, 0, item)
    #
    #         if file_type == 'dox':
    #             icon = QIcon()  # 请将文件路径替换为实际的图标文件路径
    #             icon.addPixmap(QtGui.QPixmap(":/icon/word_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #         elif file_type == 'pdf':
    #             icon = QIcon()  # 请将文件路径替换为实际的图标文件路径
    #             icon.addPixmap(QtGui.QPixmap(":/icon/pdf_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #         elif file_type == 'txt':
    #             icon = QIcon()  # 请将文件路径替换为实际的图标文件路径
    #             icon.addPixmap(QtGui.QPixmap(":/icon/txt_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #         elif file_type == 'xlsx':
    #             icon = QIcon()  # 请将文件路径替换为实际的图标文件路径
    #             icon.addPixmap(QtGui.QPixmap(":/icon/xlsx_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #         else:
    #             icon = QIcon()
    #
    #         item.setIcon(icon)
    #
    #
    #
    # def show_selected_item(self, index):
    #     item = self.model.itemFromIndex(index)
    #     if item:
    #         selected_item_text = item.text()
    #         self.setWindowTitle(f'Selected: {selected_item_text}')


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel


class DragAndDropLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignCenter)
        self.setText("Drag and drop a file here!")
        self.setStyleSheet("""
            QLabel {
                border: 2px dashed #aaa;
                padding: 20px;
            }
        """)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            print(file_path)
            self.setText(file_path)

    def dragLeaveEvent(self, event):
        self.setStyleSheet("""
            QLabel {
                border: 2px dashed #aaa;
                padding: 20px;
            }
        """)

    def dragMoveEvent(self, event):
        self.setStyleSheet("""
            QLabel {
                border: 2px dashed #555;
                padding: 20px;
            }
        """)

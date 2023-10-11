import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QTextBrowser,
    QTextEdit,
    QWidget,
    QVBoxLayout,
    QFileDialog,
    QCheckBox,
    QLabel,
    QListView,
    QHBoxLayout,
)
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor
from PyQt5.QtCore import QModelIndex, Qt

from tools import *

class MainWindow(QMainWindow):
    def __init__(self):
        self.filters = []
        self.duplicates = {}
        self.listDuplicates = []
        self.numero = 0

        super().__init__()

        self.setWindowTitle("Поиск дубликатов")

        self.centralwidget = QWidget()

        self.video_filter = QCheckBox("Видео (avi, mov, mkv)", checked=True)
        self.book_filter = QCheckBox("Книги (pdf, txt, fb2, djvu)", checked=True)
        self.audio_filter = QCheckBox("Аудиофайлы (mp3)", checked=True)
        self.img_filter = QCheckBox("Изображения (jpg, png)", checked=True)

        self.open_dir = QPushButton("Open Dir")
        self.open_dir.clicked.connect(self.open_dir_dialog)

        self.label_path = QLabel("")
        self.label_index = QLabel("0/0")

        self.listView = QListView()
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.listView.setObjectName("listView-1")
        self.listView.clicked[QModelIndex].connect(self.on_clicked_list_view)
        self.listView.setFocusPolicy(Qt.NoFocus)

        self.horizontal_layout = QHBoxLayout()

        self.button_next = QPushButton("Next")
        self.button_next.clicked.connect(self.nextItem)

        self.button_prev = QPushButton("Prev")
        self.button_prev.clicked.connect(self.backItem)

        self.button_apply = QPushButton("Apply")
        self.button_apply.clicked.connect(self.apply)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.video_filter)
        self.layout.addWidget(self.book_filter)
        self.layout.addWidget(self.audio_filter)
        self.layout.addWidget(self.img_filter)

        self.layout.addWidget(self.open_dir)
        self.layout.addWidget(self.label_path)
        self.layout.addWidget(self.label_index)
        self.layout.addWidget(self.listView)

        self.horizontal_layout.addWidget(self.button_prev)
        self.horizontal_layout.addWidget(self.button_next)

        self.layout.addLayout(self.horizontal_layout)
        self.layout.addWidget(self.button_apply)

        self.centralwidget.setLayout(self.layout)
        self.setCentralWidget(self.centralwidget)

        self.files = []

    def checkFilters(self):
        self.filters = []
        if self.video_filter.checkState():
            self.filters += ["avi", "mov", "mkv"]

        if self.book_filter.checkState():
            self.filters += ["pdf", "txt", "fb2", "djvu"]

        if self.audio_filter.checkState():
            self.filters += ["mp3"]

        if self.img_filter.checkState():
            self.filters += ["jpg", "png"]

    def open_dir_dialog(self):
        self.checkFilters()
        self.base_folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.label_path.setText(self.base_folder)
        self.duplicates = search_duplicates(filter(get_list_names(LocalFileSystem(self.base_folder)), self.filters ))

        self.listDuplicates = list(self.duplicates.keys())

        self.files = []
        for i in self.listDuplicates:
            a = []
            for j in self.duplicates[i]:
                a.append(File(j))
            self.files.append(a)

        self.numero = 0
        self.show_dupes()

    def show_dupes(self):
        self.model.removeRows(0, self.model.rowCount())
        if len(self.listDuplicates) > 0:
            self.label_index.setText( str(self.numero + 1) + "/" + str(len(self.listDuplicates)))
            for i in self.duplicates[self.listDuplicates[self.numero]]:
                self.model.appendRow(QStandardItem(str(i)))
        else:
            self.label_index.setText("0/0")

    def on_clicked_list_view(self, index):
        item = self.model.itemFromIndex(index)
        rgb_color = item.background().color().getRgb()
        if rgb_color == (0, 255, 255, 255):
            rgb_color = (0, 0, 0, 0)
            if "remove" in item.text():
                item.setText(" ".join(item.text().split()[:-1]) + " saved")
                for i in self.files[self.numero]:
                    if i.name == " ".join(item.text().split()[:-1]):
                        i.to_save()

            else:
                item.setText(item.text() + " saved")
                for i in self.files[self.numero]:
                    if i.name == item.text():
                        i.to_save()
        else:
            rgb_color = (0, 255, 255, 255)
            if "saved" in item.text():
                item.setText(" ".join(item.text().split()[:-1]) + " remove")
                for i in self.files[self.numero]:
                    if i.name == " ".join(item.text().split()[:-1]):
                        i.to_del()
            else:

                for i in self.files[self.numero]:
                    if i.name == item.text():
                        i.to_del()
                        item.setText(item.text() + " remove")

        item.setBackground(QColor(*rgb_color))


    def read(self, data):
        text = self.textw.toPlainText()
        self.textw.setText(text + data)

    def nextItem(self):
        if self.numero + 1 < len(self.listDuplicates):
            self.numero += 1
            self.show_dupes()

    def backItem(self):
        if self.numero > 0:
            self.numero -= 1
            self.show_dupes()

    def apply(self):
        remove_file(list_files_to_files_to_remove(self.files))
        self.model.removeRows(0, self.model.rowCount())
        self.label_index.setText("0/0")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
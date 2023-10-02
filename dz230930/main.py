import sys
import os
import collections

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget, QLineEdit, QCheckBox,
)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()
        self.stacklayout = QHBoxLayout()
        self.stacklayout2 = QHBoxLayout()
        self.boxlayout = QVBoxLayout()

        self.boxlayout.addLayout(self.stacklayout)
        self.boxlayout.addLayout(self.stacklayout2)
        pagelayout.addLayout(self.boxlayout)


        btn = QPushButton("Найти")
        btn.pressed.connect(self.reserch)
        self.stacklayout.addWidget(btn)


        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

        self.value_a = QLineEdit(self)
        self.stacklayout.addWidget(self.value_a)

        a = QLabel("Фильтр")
        self.stacklayout2.addWidget(a)

        self.value_b = QLineEdit(self)

        self.stacklayout2.addWidget(self.value_b)


        self.checkbox = QCheckBox("Вложения", self)
        self.stacklayout2.addWidget(self.checkbox)

        self.label = QLabel("")

        self.boxlayout.addWidget(self.label)

        self.labelPodrobno = QLabel("")
        self.labelPodrobno.setWordWrap(True)
        self.boxlayout.addWidget(self.labelPodrobno)

        self.labelvniz = QLabel("")
        self.labelvniz.setWordWrap(True)
        self.boxlayout.addWidget(self.labelvniz)

        self.labelvverh= QLabel("")
        self.labelvverh.setWordWrap(True)
        self.boxlayout.addWidget(self.labelvverh)




    def reserch(self):
        def getrashirenue(s):
            for i in range(len(s) - 1, -1, -1):
                if s[i] == ".":
                    return s[:i], s[i + 1:]
            return s, ""

        def parse_folder(path):
            files = []
            for file in os.listdir(path):
                if os.path.isdir(path + '/' + file):
                    files.extend(parse_folder(path + '/' + file))
                else:
                    files.append((file, os.path.getsize(path + "/" + file)))
            return files

        directory = self.value_a.text()
        if os.path.isdir(directory):
            d = collections.defaultdict(list)
            if not self.checkbox.checkState():
                files = [(file, os.path.getsize(directory + "/" + file)) for file in os.listdir(directory) if os.path.isfile(f'{directory}/{file}')]
            else:
                files = parse_folder(directory)

            for i in files:
                f, r = getrashirenue(i[0])
                d[r].append([f, i[1]])

            self.label.setText("Колво файлов : " + str(len(files)))
            s = ""
            a = self.value_b.text().split()
            for i in d.keys():
                if i not in a:
                    s += i + ": " + str(len(d[i])) + " "
            self.labelPodrobno.setText(s)

            files = []
            for i in d.keys():
                if i not in a:
                    files += d[i]

            files.sort(key=lambda x: x[1])
            s1 = ""
            s2 = ""
            for i in range(min(20, len(files))):
                s1 += files[i][0] + " " + str(files[i][1]) + "\n"
                s2 += files[len(files) - 1 - i][0] + " " + str(files[len(files) - 1 - i][1]) + "\n"

            self.labelvniz.setText(s1)
            self.labelvverh.setText(s2)



        else:
            self.label.setText("Нет такой папки")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
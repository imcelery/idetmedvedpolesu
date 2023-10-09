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

        btn = QPushButton("Отфильтровать")
        btn.pressed.connect(self.filter)
        self.stacklayout2.addWidget(btn)


        self.checkbox = QCheckBox("Вложения", self)
        self.stacklayout.addWidget(self.checkbox)

        self.label = QLabel("")

        self.boxlayout.addWidget(self.label)

        self.labelPodrobno = QLabel("")
        self.labelPodrobno.setWordWrap(True)
        self.boxlayout.addWidget(self.labelPodrobno)

        l = QLabel("Самые маленькие")
        self.boxlayout.addWidget(l)

        self.labelvniz = QLabel("")
        self.labelvniz.setWordWrap(True)
        self.boxlayout.addWidget(self.labelvniz)

        l = QLabel("Самые большие")
        self.boxlayout.addWidget(l)

        self.labelvverh= QLabel("")
        self.labelvverh.setWordWrap(True)
        self.boxlayout.addWidget(self.labelvverh)

        self.d = collections.defaultdict(list)
        self.founded = False
        self.filters = set()
        self.inversFilter = True

    def toKB(self, i):
        i = i // 1024
        if i < 1024:
            return str(i) + "kb"
        i = i // 1024
        if i < 1024:
            return str(i) + "mb"
        i = i // 1024
        return str(i) + "gb"

    def draw(self):
        if self.founded:
            s = ""
            dSorted = collections.defaultdict(list)
            if self.inversFilter:
                for i in self.d.keys():
                    if i not in self.filters:
                        dSorted[i] = self.d[i]
                        s += i + ": " + str(len(self.d[i])) + " "
            else:
                for i in self.d.keys():
                    if i in self.filters:
                        dSorted[i] = self.d[i]
                        s += i + ": " + str(len(self.d[i])) + " "
            self.label.setText("Колво файлов : " + str(sum(list(map(len, dSorted.values())))))
            self.labelPodrobno.setText(s)

            files = []
            for i in dSorted.keys():
                for j in dSorted[i]:
                    files.append((j[0] + "." + i, j[1]))

            files.sort(key=lambda x: x[1])
            s1 = ""
            s2 = ""
            for i in range(min(20, len(files))):
                s1 += files[i][0] + " " + self.toKB(files[i][1]) + "\n"
                s2 += files[len(files) - 1 - i][0] + " " + self.toKB(files[len(files) - 1 - i][1]) + "\n"

            self.labelvniz.setText(s1)
            self.labelvverh.setText(s2)
        else:
            self.label.setText("Нет такой папки")

    def filter(self):
        a = self.value_b.text()
        if len(a) > 0:
            if a[0] == "!":
                self.inversFilter = True
                a = a[1:]
            else:
                self.inversFilter = False
            self.filters = set(a.split())
        else:
            self.inversFilter = True
            self.filters = set()
        self.draw()

    def reserch(self):
        def getrashirenue(s):
            for i in range(len(s) - 1, -1, -1):
                if s[i] == ".":
                    return s[:i], s[i + 1:]
            return s, ""

        def parse_folder(path, b):
            if b:
                filess = []

                for address, dirs, files in os.walk(path):
                    for name in files:
                        filess.append((os.path.join(address, name), os.path.getsize(os.path.join(address, name))))
                return filess
            else:
                return [(os.path.join(path, f), os.path.getsize(os.path.join(path, f))) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


        directory = self.value_a.text()
        if os.path.isdir(directory):
            self.founded = True
            self.d.clear()
            files = parse_folder(directory, self.checkbox.checkState())
            for i in files:
                f, r = getrashirenue(i[0])
                self.d[r].append([f, i[1]])
        else:
            self.founded = False
            self.label.setText("Нет такой папки")
        self.draw()



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
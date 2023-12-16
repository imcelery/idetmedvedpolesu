from threading import Thread
import sqlite3
import datetime
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel, QMainWindow


sizeX = 400
sizeY = 400

class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        self.setWidgetResizable(True)

        content = QWidget(self)
        self.setWidget(content)

        lay = QVBoxLayout(content)

        self.label = QLabel(content)

        self.label.setWordWrap(True)

        lay.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)


class AppUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("News ")
        self.text = ""
        self.setFixedSize(sizeX, sizeY)

    def setNews(self, news):
        self.text = ""
        for i in news:
            self.text += f"{i.date}   {i.text} \n  {i.previu}\n\n"
            self.text += "\n"


        label = ScrollLabel(self)

        label.setText(self.text)

        label.setGeometry(0, 0, sizeX, sizeY)



class DownloadThread(Thread):
    def __init__(self, url):
        """Инициализация потока"""
        Thread.__init__(self)
        self.url = url
        self.text = None

    def run(self):
        try:
            self.text = requests.get(self.url, auth=('user', 'pass')).text
        except requests.RequestException:
            pass

    def isWorking(self):
        return self.is_alive()

    def getText(self):
        if self.text is not None:
            return self.text
        return None


class Downloader:
    def __init__(self, urls=[]):
        self.urls = urls
        self.texts = []
        self.threads = []
        self.downloadStatus = []

    def download(self):

        for i in self.urls:
            thread = DownloadThread(i)
            thread.run()
            self.threads.append(thread)
            self.downloadStatus.append(1)
            self.texts.append(None)

        while sum(self.downloadStatus):
            for i in range(len(self.threads)):
                if not self.threads[i].isWorking():
                    self.downloadStatus[i] = 0
                    self.texts[i] = self.threads[i].getText()
        return self.texts


class Parser1:
    def __init__(self):
        self.news = []

    def parse(self, text):
        while text.find("listing__column listing__column_sections listing__column_sections_") != -1:
            a = text.find("listing__column listing__column_sections listing__column_sections_")
            text = text[a:]
            a = text.find("card__heading_sections card__heading_sections_")
            text = text[a + 15:]
            a = text.find(">")
            text = text[a + 1:]
            a = text.find(">")
            text = text[a + 1:]
            a = text.find("</a>")

            newsText = text[:a].strip()
            while newsText.find(">") != -1:
                newsText = newsText[newsText.find(">") +1:]
            newsText = newsText.strip()
            text = text[a + 1:]


            a = text.find("datetime=")
            text = text[a:]
            a = text.find(">")

            date = text[10:a - 1].strip()

            text = text[a + 1:]

            text = text[a + 10:]

            a = text.find("card__summary card__summary_sections card__summary_sections_")
            text = text[a:]
            a = text.find(">")
            text = text[a + 2:]
            a = text.find("<")
            previu = text[:a - 1].strip()
            previu.replace(">", "")
            previu.strip()
            text = text[a + 10:]
            self.news.append(News(date, newsText, previu))

        return self.news

class Parser2:
    def __init__(self):
        self.news = []

    def parse(self, text):
        while text.find("list-item") != -1:
            a = text.find("list-item")
            text = text[a:]
            a = text.find("list-item__title color-font-hover-only")
            text = text[a + 15:]
            a = text.find(">")
            text = text[a + 1:]
            a = text.find("</a>")

            newsText = text[:a].strip()
            text = text[a + 1:]


            a = text.find("list-item__date")
            text = text[a+17:]

            date =str(datetime.datetime.date(datetime.datetime.now())) + " " + text[:5].strip()

            text = text[20:]
            self.news.append(News(date, newsText, ""))
        return self.news[:-1]


class Parser3:
    def __init__(self):
        self.news = []

    def parse(self, text):
        while text.find("last-nn-box") != -1:
            a = text.find("last-nn-box")
            text = text[a:]
            a = text.find("title")
            text = text[a + 7:]
            a = text.find(">")
            newsText = text[:a - 1].strip()

            text = text[a:]
            a = text.find("short-body")
            text = text[a + 12:]
            a = text.find("<")

            previu = text[:a]
            text = text[a + 5:]
            a = text.find("data-utime=")

            text = text[a+24:]
            a = text.find("<")
            b = text[:a].split()
            if len(b) == 3:
                z = text[:a- 1].split(" ")[2]
                if len(z) == 4:
                    z = z[:-1] + "0" + z[-1]
                date =str(datetime.datetime.date(datetime.datetime.now())) + " " + z
                self.news.append(News(date, newsText, previu))

            text = text[40:]
        return self.news

class News:
    def __init__(self, date, text, previu):
        self.date = date
        self.text = text
        self.previu = previu


def execute(func):
    def f(self, *args, **kwargs):
        func(self, *args, **kwargs)
        return self.executor()
    return f

def strict(func):
    def f(self, *args, strict=False, **kwargs):
        func(self, *args, **kwargs)
        if strict:
            self.params = tuple([el.strip("%") for el in self.params])
    return f


class Table:
    def __init__(self, database: str):
        self.database = database
        with sqlite3.connect(database) as connection:
            self.connection = connection
            self.cursor = connection.cursor()
            self._create_table()

    def _create_table(self):
        self._sql_table_init()
        self.cursor.execute(self.s)
        self.connection.commit()

    def _sql_table_init(self):
        raise NotImplementedError()

    def executor(self):
        with sqlite3.connect(self.database) as connection:
            self.connection = connection
            self.cursor = connection.cursor()
            self.cursor.execute(self.query, self.params)
            return self.cursor.fetchall()

class NewsTable(Table):

    def _sql_table_init(self):
        self.s = """       
        CREATE TABLE IF NOT EXISTS NewsTable (
            datetime TEXT,
            previu TEXT,
            description TEXT
        )"""

    @execute
    def select_news(self):
        self.query = """
        SELECT NewsTable.datetime, NewsTable.description, NewsTable.previu
        FROM NewsTable
        GROUP BY NewsTable.datetime, NewsTable.description
        ORDER BY NewsTable.datetime
        """
        self.params = ()

    @execute
    def insert(self, datetime, description, previu):
        self.query = """INSERT INTO NewsTable (datetime, description, previu) 
                        VALUES (?, ?, ?)"""
        self.params = (datetime, description, previu)


class NewsApp:
    def __init__(self):
        self.urls = ["https://russian.rt.com/world", "https://ria.ru/world/", "https://www.uralweb.ru/news/"]
        self.parsers = [Parser1(), Parser2(), Parser3()]
        self.texts = [None for _ in range(len(self.urls))]
        self.downloader = Downloader(self.urls)
        self.news = []
        self.UI = None
        self.db_name = "news_db"
        self.db = NewsTable(self.db_name)

    def updTable(self):
        self.news = []
        self.texts = self.downloader.download()
        for i in range(len(self.texts)):
            if self.texts[i] is not None:
                self.news += self.parsers[i].parse(self.texts[i])

        for i in self.news:
            if i is not None:
                self.db.insert(i.date, i.text, i.previu)


    def start(self):
        self.news = []
        for i in self.db.select_news():
            self.news.append(News(i[0], i[1], i[2]))
        App = QApplication(sys.argv)
        self.UI = AppUI()
        self.UI.setNews(self.news)
        self.UI.show()
        sys.exit(App.exec())




if __name__ == '__main__':
    app = NewsApp()
    print("Обнорвляем таблицу")
    app.updTable()
    print("Таблица обноленна")
    app.start()

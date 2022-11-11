import sys
from new import x
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QListWidget
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
import sqlite3

conn = sqlite3.connect('mydb.db')
c = conn.cursor()

c.execute(""" CREATE TABLE if not exists todo_list(
list_item text)
 """)
conn.commit()

conn.close()


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("todo.ui", self)
        self.setWindowTitle("Todo app")
        self.button_handlers()
        self.grab_all()
        self.api()

    def button_handlers(self):

        self.addbtn.clicked.connect(self.add)
        self.deletebtn.clicked.connect(self.delete_btn)
        self.clearbtn.clicked.connect(self.clear_btn)
        self.db_btn.clicked.connect(self.dbbtn)
        # self.db_btn.clicked.connect(self.add_to_db)
        self.show()

    def grab_all(self):
        conn = sqlite3.connect('mydb.db')
        c = conn.cursor()

        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()

        conn.commit()

        conn.close()

        for record in records:
            self.list.addItem(str(record[0]))

    def api(self):
        sam = x['symbol'], x['quote']['USD']['price']

        self.label_2.setText(str(sam))

    def add(self):
        # grab the text from the input
        item = self.input.text()
        # add item to list
        # print("hello")
        self.list.addItem(item)
        #       clear the item box
        self.input.setText("")

    def clear_btn(self):
        self.list.clear()

    def delete_btn(self):
        clicked = self.list.currentRow()
        # self.input.setText(str(clicked))
        self.list.takeItem(clicked)

    def dbbtn(self):

        conn = sqlite3.connect('mydb.db')
        c = conn.cursor()

        c.execute("DELETE  FROM todo_list;",)
        records = c.fetchall()

        items = []
        for index in range(self.list.count()):
            items.append(self.list.item(index))

            for item in items:
                # print(item.text())
                c.execute("INSERT INTO todo_list VALUES (:item)", {
                    'item': item.text(),
                })

        conn.commit()

        conn.close()

        msg = QMessageBox()
        msg.setWindowTitle("Saved to database")
        msg.setText("Added to database")
        x = msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec())

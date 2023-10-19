import sys
from PyQt5.QtWidgets import *
from ui_main_python import Ui_MainWindow
from text_read_python import Ui_TextReadWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.page1 = QWidget()
        self.page2 = QWidget()
        self.page3 = QWidget()

        self.page1.setStyleSheet("background-color: red;")
        self.page2.setStyleSheet("background-color: green;")
        self.page3.setStyleSheet("background-color: blue;")

        self.ui.Pages_Widget.addWidget(self.page1)
        self.ui.Pages_Widget.addWidget(self.page2)
        self.ui.Pages_Widget.addWidget(self.page3)

        self.ui.Btn_Menu_1.clicked.connect(self.show_page1)
        self.ui.Btn_Menu_2.clicked.connect(self.show_page2)

        # Btn_Menu_3 tıklandığında text_read_python.py penceresini açacak buton ekleyelim
        self.btn_open_text_read = QPushButton("Hızlı Okuma Testi")
        self.btn_open_text_read.clicked.connect(self.show_text_read_window)
        layout = QVBoxLayout(self.ui.Btn_Menu_3)
        layout.addWidget(self.btn_open_text_read)

    def show_page1(self):
        self.ui.Pages_Widget.setCurrentWidget(self.page1)

    def show_page2(self):
        self.ui.Pages_Widget.setCurrentWidget(self.page2)

    def show_text_read_window(self):
        self.text_read_window = TextReadWindow()
        self.text_read_window.show()

class TextReadWindow(QMainWindow):
    def __init__(self):
        super(TextReadWindow, self).__init__()
        self.ui = Ui_TextReadWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Main()
    pencere.show()
    sys.exit(app.exec_())

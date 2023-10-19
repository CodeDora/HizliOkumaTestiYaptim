import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class Ui_TextReadWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)  # Pencere boyutunu sabitledik
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame_texts = QtWidgets.QFrame(self.centralwidget)
        self.frame_texts.setGeometry(QtCore.QRect(10, 10, 781, 361))
        self.frame_texts.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_texts.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_texts.setObjectName("frame_texts")

        self.label = QtWidgets.QLabel(self.frame_texts)
        self.label.setGeometry(QtCore.QRect(100, 20, 600, 400))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 60px;")

        self.Btn_Basla = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Basla.setGeometry(QtCore.QRect(350, 500, 157, 50))
        self.Btn_Basla.setStyleSheet("QPushButton{\n"
        "background-color: rgb(255, 255, 255);\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 10px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(180, 85, 0);\n"
        "}")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Basla.setFont(font)
        self.Btn_Basla.setText("Başlat")
        self.Btn_Basla.setCheckable(True)
        self.Btn_Basla.setAutoExclusive(True)
        self.Btn_Basla.setObjectName("Btn_Basla")

        self.sure_label = QtWidgets.QLabel(self.centralwidget)
        self.sure_label.setGeometry(QtCore.QRect(190, 458, 100, 50))
        self.sure_label.setStyleSheet("color: white; font-size: 16px;")
        self.sure_label.setText("Süre (saniye):")

        self.sure_metin = QtWidgets.QLineEdit(self.centralwidget)
        self.sure_metin.setGeometry(QtCore.QRect(300, 470, 40, 30))
        self.sure_metin.setStyleSheet("color: white; font-size: 16px;")
        self.sure_metin.setText("1")

        self.uygula_btn = QtWidgets.QPushButton(self.centralwidget)
        self.uygula_btn.setGeometry(QtCore.QRect(350, 470, 80, 30))
        self.uygula_btn.setText("Uygula")
        self.uygula_btn.setStyleSheet("QPushButton{\n"
        "background-color: rgb(255, 255, 255);\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 10px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(180, 85, 0);\n"
        "}")

        self.ekle_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ekle_btn.setGeometry(QtCore.QRect(430, 470, 80, 30))
        self.ekle_btn.setText("Metin Ekle")
        self.ekle_btn.setStyleSheet("QPushButton{\n"
        "background-color: rgb(255, 255, 255);\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 10px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(180, 85, 0);\n"
        "}")
        self.ekle_btn.clicked.connect(self.open_input_dialog)

        self.metin = "Bu bir örnek metindir. Bu metni kullanarak hızlı okuma testi yapabilirsiniz."
        self.kelimeler = self.metin.split()
        self.kelime_index = 0

        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.show_next_word)

        self.Btn_Basla.clicked.connect(self.start_reading)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Btn_Basla.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.uygula_btn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.ekle_btn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hızlı Okuma Testi"))

    def open_input_dialog(self):
        text, ok = QtWidgets.QInputDialog.getText(None, "Metin Ekle", "Metni Buraya Girin:")
        if ok:
            self.metin = text
            self.kelimeler = self.metin.split()
            self.kelime_index = 0
            self.label.setText(self.kelimeler[self.kelime_index])

    def show_next_word(self):
        if self.kelime_index < len(self.kelimeler):
            kelime = self.kelimeler[self.kelime_index]
            if len(kelime) >= 4:
                orta_harf = kelime[len(kelime) // 2 - 1:len(kelime) // 2 + 1]
                kelime = kelime.replace(orta_harf, f"<font color='red'>{orta_harf}</font>")
            self.label.setText(kelime)
            self.kelime_index += 1
        else:
            self.kelime_index = 0
            self.timer.stop()

    def start_reading(self):
        self.timer.stop()
        self.kelime_index = 0
        sure = float(self.sure_metin.text())
        self.timer.start(int(sure * 1000))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TextReadWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

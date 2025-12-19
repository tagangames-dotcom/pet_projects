import sys
import webbrowser
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from osint_new_Window import Ui_MainWindow  # твой сгенерированный файл

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключаем кнопку к функции
        self.ui.pushButton.clicked.connect(self.build_dork)
        self.setWindowIcon(QIcon(r"D:\программироваание проекты\pet_projects\1764466492.ico"))

    def build_dork(self):
        # Получаем текстовые поля
        base = self.ui.lineEdit.text()
        site = self.ui.lineEdit_2.text()
        query_parts = []

        # Основной текст
        if base:
            query_parts.append(base)

        # Тип файла (RadioButton)
        filetype = None
        if self.ui.radioButton.isChecked():       filetype = "pdf"
        elif self.ui.radioButton_2.isChecked():  filetype = "doc"
        elif self.ui.radioButton_3.isChecked():  filetype = "docx"
        elif self.ui.radioButton_4.isChecked():  filetype = "xls"
        elif self.ui.radioButton_5.isChecked():  filetype = "xlsx"
        elif self.ui.radioButton_6.isChecked():  filetype = "ppt"
        elif self.ui.radioButton_7.isChecked():  filetype = "pptx"
        elif self.ui.radioButton_8.isChecked():  filetype = "txt"

        if filetype:
            query_parts.append(f"filetype:{filetype}")

        # Поиск по сайту
        if site:
            query_parts.append(f"site:{site}")

        # Дополнительные операторы
        if self.ui.checkBox.isChecked() and base:
            query_parts.append(f"intitle:{base}")
        if self.ui.checkBox_2.isChecked() and base:
            query_parts.append(f"inurl:{base}")
        if self.ui.checkBox_3.isChecked() and base:
            query_parts.append(f"intext:{base}")

        # Собираем финальный запрос
        final_query = " ".join(query_parts)

        # Выводим в консоль
        print("Финальный запрос:", final_query)

        # Открываем Google
        if final_query:
            google_url = f"https://www.google.com/search?q={final_query}"
            webbrowser.open(google_url)

# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

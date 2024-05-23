import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QInputDialog
from PyQt5.uic import loadUi

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        loadUi('example.ui', self)

        self.addButton.clicked.connect(self.add_document)
        self.deleteButton.clicked.connect(self.delete_document)
        self.confirmButton.clicked.connect(self.confirm_document)
        self.rejectButton.clicked.connect(self.reject_document)

    def add_document(self):
        document_name, ok = QInputDialog.getText(self, 'Добавить документ', 'Введите название документа:')
        if ok:
            author, ok = QInputDialog.getText(self, 'Добавить документ', 'Введите автора:')
            if not ok:
                return
            date, ok = QInputDialog.getText(self, 'Добавить документ', 'Введите дату:')
            if not ok:
                return
            status = "Не подтвержден"

            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(document_name))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(author))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(date))
            self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(status))

    def delete_document(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            self.tableWidget.removeRow(selected_row)

    def confirm_document(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            item = self.tableWidget.item(selected_row, 3)
            item.setText("Подтвержден")
    def reject_document(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            item = self.tableWidget.item(selected_row, 3)
            item.setText("Отклонен")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

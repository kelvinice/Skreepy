import sys

from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow


############################################


def init():
    app = QApplication(sys.argv)
    width = app.desktop().screenGeometry().width()
    height = app.desktop().screenGeometry().height()

    # fake = Faker()
    # print(fake.address())
    w = MainWindow(width, height, "Skreepy")
    w.setVisible(True)

    # print(super_global.expected)

    # Initializing database connection
    # Connection()

    sys.exit(app.exec_())


if __name__ == '__main__':
    init()
    # scraper.main.legacy_main()

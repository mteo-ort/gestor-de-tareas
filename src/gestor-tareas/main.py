
import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestor de Tareas")
        self.setMinimumSize(800, 500)

        label = QLabel("¡Bienvenido al Gestor de Tareas!")
        label.setStyleSheet("font-size: 20px;")

        self.setCentralWidget(label)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

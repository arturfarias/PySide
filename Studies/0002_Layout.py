import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton
from PySide6.QtWidgets import QGridLayout, QWidget, QVBoxLayout, QHBoxLayout


class BoxLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout() # Posicionamento vertical

        btn1 = QPushButton('Botão 1') # Criando o widget
        btn2 = QPushButton('Botão 2')
        btn3 = QPushButton('Botão 3')

        layout.addWidget(btn1) # Adcioando ao Layout
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        self.setLayout(layout) # Define o gerenciador de layout

class GridLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout() # Posicionamento em Grid

        # row: A linha onde o widget será colocado (começa em 0)
        # column: A coluna onde o widget será colocado (começa em 0)
        # rowSpan: Opcional, quantas linhas o widget ocupa (padrão = 1)
        # columnSpan: Opcional, quantas colunas o widget ocupa (padrão = 1)
        layout.addWidget(QPushButton('Botão 1'), 0, 0) # (widget, row, column, rowSpan, columnSpan)
        layout.addWidget(QPushButton('Botão 2'), 0, 1)
        layout.addWidget(QPushButton('Botão 3'), 1, 0)
        layout.addWidget(QPushButton('Botão 4'), 1, 1)
        layout.addWidget(QPushButton('Botão 4'), 2, 0, 1, 2)

        self.setLayout(layout)

class Nested(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout() # Posicionamento vertical
        top_layout = QHBoxLayout() # Posicionamento horizontal

        top_layout.addWidget(QPushButton('Botão 1'))
        top_layout.addWidget(QPushButton('Botão 2'))

        main_layout.addLayout(top_layout) # Adciona um layout em outro
        main_layout.addWidget(QPushButton('Botão 3'))
        main_layout.addWidget(QPushButton('Botão 4'))

        self.setLayout(main_layout)


class Windows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts')
        self.setCentralWidget(Nested())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Windows()
    window.show()

    sys.exit(app.exec())
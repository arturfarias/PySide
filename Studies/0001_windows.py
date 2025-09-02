import sys

from PySide6.QtWidgets import QApplication, QMainWindow

class Windows(QMainWindow):
    def __init(self):
        super().__init__(self)

        self.setWindowTitle('Title text') 

        # x: distância da borda esquerda
        # y: distância da borda superior
        self.setGeometry(100, 100, 600, 400)  # x, y, largura, altura


if __name__ == "__main__":
    app = QApplication(sys.argv) # Cria a aplicação

    # Cria a janela principal
    window = Windows()
    window.show()

    sys.exit(app.exec()) # Executa o loop principal
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget

class Windows(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget() # Criando um widget central (necessario em QMainWindow)
        self.setCentralWidget(central_widget) # Definindo central_widget como o widget central


        self.setWindowTitle('Button') 

        layout = QVBoxLayout()
        
        self.button = QPushButton('Click Me') # Criando o botão
        self.button.clicked.connect(self.callback_function) # Conectando o botão ao metodo a ser chamado

        layout.addWidget(self.button)
        central_widget.setLayout(layout) # Adcionando o layout ao widget central
    
    def callback_function(self): # Metodo a ser chamado
        self.button.setText('OK!') # Muda o texto do botão
        self.button.setEnabled(False) # Desabilita o botão (True habilita novamente)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Windows()
    window.show()

    sys.exit(app.exec())
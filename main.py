from PyQt5 import QtWidgets
import sys
from controler.aplicacao import Aplicacao

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    janela = Aplicacao()  # cria a insatncia da aplicação
    sys.exit(app.exec_()) # executa o loop principal

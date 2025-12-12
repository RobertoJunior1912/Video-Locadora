from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from model.Pessoa import Funcionario
from model.Pessoa import Cliente

class Aplicacao:

    def __init__(self):
        self.form_validar_usuario = uic.loadUi('view/validar_usuario.ui')
        self.form_validar_usuario.botao_logar.clicked.connect(self.botao_logar_validar_usuario)
        self.form_validar_usuario.botao_sair.clicked.connect(self.botao_sair_validar_usuario)
        self.form_validar_usuario.show()

    def botao_logar_validar_usuario(self):
        self.login = self.form_validar_usuario.txt_login.text()
        self.senha = self.form_validar_usuario.txt_senha.text()
        funcionario = Funcionario()
        validou = funcionario.validar_usuario(self.login, self.senha)

        if validou:
            self.form_menu_principal = uic.loadUi('view/menu_principal.ui')

            if hasattr(self.form_menu_principal, 'botao_cadastrar_funcionario'):
                self.form_menu_principal.botao_cadastrar_funcionario.triggered.connect(self.opcao_cadastrar_funcionario)
            if hasattr(self.form_menu_principal, 'botao_cadastrar_cliente'):
                self.form_menu_principal.botao_cadastrar_cliente.triggered.connect(self.opcao_cadastrar_cliente)
            if hasattr(self.form_menu_principal, 'sair_menu'):
                self.form_menu_principal.sair_menu.triggered.connect(self.opcao_sair)
            self.form_menu_principal.show()
            self.form_validar_usuario.close()
        else:
            QMessageBox.information(self.form_validar_usuario, 'Alerta!', 'Usuário inválido ou senha incorreta!')
            self.form_validar_usuario.txt_login.setText('')
            self.form_validar_usuario.txt_senha.setText('')


    def botao_sair_validar_usuario(self):
        QtWidgets.QApplication.quit()

    def opcao_sair(self):
        QtWidgets.QApplication.quit()

    def opcao_cadastrar_funcionario(self):
        self.form_cadastrar_funcionario = uic.loadUi('view/cadastrar_funcionario.ui')
        self.form_cadastrar_funcionario.botao_cadastrar_funcionario.clicked.connect(self.botao_cadastrar_cadastarfuncionario)
        self.form_cadastrar_funcionario.botao_voltar_funcionario.clicked.connect(self.botao_voltar_cadastrarfuncionario)
        self.form_cadastrar_funcionario.show()

    def opcao_cadastrar_cliente(self):
        self.form_cadastrar_cliente = uic.loadUi('view/cadastrar_cliente.ui')
        self.form_cadastrar_cliente.botao_cadastrar_cliente.clicked.connect(self.botao_cadastrar_cadastarcliente)
        self.form_cadastrar_cliente.botao_voltar_cliente.clicked.connect(self.botao_voltar_cadastrarcliente)
        self.form_cadastrar_cliente.show()

    def botao_cadastrar_cadastarfuncionario(self):
        self.codigo = self.form_cadastrar_funcionario.txt_codigo_funcionario.text()
        self.nome = self.form_cadastrar_funcionario.txt_nome_funcionario.text()
        self.data_nascimento = self.form_cadastrar_funcionario.txt_data_funcionario.text()
        self.cpf = self.form_cadastrar_funcionario.txt_cpf_funcionario.text()
        self.login = self.form_cadastrar_funcionario.txt_login_funcionario.text()
        self.senha = self.form_cadastrar_funcionario.txt_senha_funcionario.text()

        funcionario = Funcionario()
        funcionario.cadastrar(self.codigo, self.nome, self.data_nascimento, self.cpf, self.login, self.senha)
        QMessageBox.information(self.form_cadastrar_funcionario,'Alerta', 'Usuário cadastrado!')

        self.form_cadastrar_funcionario.txt_codigo_funcionario.setText('')
        self.form_cadastrar_funcionario.txt_nome_funcionario.setText('')
        self.form_cadastrar_funcionario.txt_data_funcionario.setText('')
        self.form_cadastrar_funcionario.txt_cpf_funcionario.setText('')
        self.form_cadastrar_funcionario.txt_login_funcionario.setText('')
        self.form_cadastrar_funcionario.txt_senha_funcionario.setText('')


    def botao_voltar_cadastrarfuncionario(self):
        self.form_cadastrar_funcionario.close()

    def botao_cadastrar_cadastarcliente(self):
        self.codigo = self.form_cadastrar_cliente.txt_codigo_cliente.text()
        self.nome = self.form_cadastrar_cliente.txt_nome_cliente.text()
        self.data_nascimento = self.form_cadastrar_cliente.txt_data_cliente.text()
        self.cpf = self.form_cadastrar_cliente.txt_cpf_cliente.text()
        self.login = self.form_cadastrar_cliente.txt_login_cliente.text()
        self.senha = self.form_cadastrar_cliente.txt_senha_cliente.text()
        self.limite_credito = self.form_cadastrar_cliente.txt_limite_credito.text()
        self.saldo_devedor = 0

        cliente = Cliente()
        cliente.cadastrar(self.codigo, self.nome, self.data_nascimento, self.cpf, self.login, self.senha, self.limite_credito, self.saldo_devedor)
        QMessageBox.information(self.form_cadastrar_cliente, 'Alerta', 'Cliente cadastrado!')

        self.form_cadastrar_cliente.txt_codigo_cliente.setText('')
        self.form_cadastrar_cliente.txt_nome_cliente.setText('')
        self.form_cadastrar_cliente.txt_data_cliente.setText('')
        self.form_cadastrar_cliente.txt_cpf_cliente.setText('')
        self.form_cadastrar_cliente.txt_login_cliente.setText('')
        self.form_cadastrar_cliente.txt_senha_cliente.setText('')
        self.form_cadastrar_cliente.txt_limite_credito_cliente.setText('')

    def botao_voltar_cadastrarcliente(self):
        self.form_cadastrar_cliente.close()
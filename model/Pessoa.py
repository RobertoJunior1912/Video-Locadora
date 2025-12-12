class Pessoa:

    def __init__(self):
        self.codigo = 0
        self.nome = ""
        self.data_nascimento = ""
        self.cpf = ""
        self.login = ""
        self.senha = ""

    def cadastrar(self,codigo, nome, data_nascimento, cpf, login, senha):
        self.codigo = codigo
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.login = login
        self.senha = senha
        print(self.codigo, self.nome, self.data_nascimento, self.cpf, self.login, self.senha)

    def validar_usuario(self, login, senha):
        validou = False
        #if self.login == login and self.senha == senha:
        #    validou = True
        if login == "123" and senha == "456":
            validou = True
        return validou

    def trocar_senha(self, codigo, senha_atual, senha_nova):
        trocou = False
        if self.codigo == codigo:
            if self.senha == senha_atual:
                self.senha = senha_nova
                trocou = True
        return trocou


class Funcionario(Pessoa):

    def __init__(self):
        super().__init__()


class Cliente(Pessoa):

    def __init__(self):
        super().__init__()
        self.saldo_devedor = 0
        self.limite_credito = 0

    def cadastrar(self, codigo, nome, data_nascimento, cpf, login, senha, limite_credito, saldo_devedor):
        self.codigo = codigo
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.login = login
        self.senha = senha
        self.saldo_devedor = saldo_devedor
        self.limite_credito = limite_credito
        print('CadastrarCliente: ',self.codigo, self.nome, self.data_nascimento, self.cpf, self.login, self.senha, self.limite_credito, self.saldo_devedor)

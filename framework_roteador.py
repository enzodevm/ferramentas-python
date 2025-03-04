class MeuFramework: def init(self): self.rotas = {}

def adicionar_rota(self, caminho, funcao):
    self.rotas[caminho] = funcao

def executar(self, caminho, *args, **kwargs):
    if caminho in self.rotas:
        return self.rotas[caminho](*args, **kwargs)
    else:
        return "Erro 404: Rota não encontrada"

Criando uma instância do framework

app = MeuFramework()

Definindo rotas

def home(): return "Página inicial"

def sobre(): return "Página sobre"

app.adicionar_rota("/", home) app.adicionar_rota("/sobre", sobre)

Testando o framework

print(app.executar("/"))        # Saída: Página inicial print(app.executar("/sobre"))    # Saída: Página sobre print(app.executar("/contato"))  # Saída: Erro 404: Rota não encontrada


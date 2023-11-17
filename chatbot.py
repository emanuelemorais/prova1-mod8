import re

class Chatbot():
    def __init__(self):

        self.intencoes = {
            r'.*?([aA]tualizar|[mM]udar|[dD]esatualizado)(?:.*)([pP]agamento|[cC]art[ãa]o?\s?de?\s?([cC]r[ée]dito|[Dd]ebito)|[pP]roceder)': "atualizar pagamento",
            r'.*?([Ss]tatus|[Rr]astr?(eio|ear)|[oO]nde)(?:.*)([pP]edido|[eE]ntrega)' : "acompanhar pedido",
            r'.*?([oO]l[áa]|[oO]i|[Bb]om\s[dD]ia|[Bb]oa\s[Tt]arde|[Bb]oa\s[Nn]oite)' : "inicio de conversa"
            
        }

        self.acoes = {
            "atualizar pagamento" : "Vá no seu perfil em nosso site e clique em metódo de pagamento.",
            "acompanhar pedido" : "Vá em nosso site e clique em meus pedidos. Por lá será possível ver o status da sua entrega.",
            "inicio de conversa" : "O que deseja?"
        }

    def verifica_intencao(self):
        for i in self.intencoes:
            match = re.search(i, self.chave, re.IGNORECASE | re.UNICODE)
            if match:
                return self.intencoes[i]
            else: 
                pass

        print("Não encontrei")

    def verifica_acao(self):
       if self.intencao in self.acoes:
            print(self.acoes[self.intencao])
    

    def inicia_chatbot(self):
        while True:
            self.chave = input("Olá, o que deseja? (Digite 'sair' para encerrar o bate papo) ")

            if self.chave == 'sair':
                print("Até a próxima!")
                break

            self.intencao = self.verifica_intencao()
            self.acao = self.verifica_acao()

def main():
    try:
        c = Chatbot()
        c.inicia_chatbot()
    except Exception as e:
        print("Erro em iniciar chatbot: ", e)

if __name__ == '__main__':
    main()
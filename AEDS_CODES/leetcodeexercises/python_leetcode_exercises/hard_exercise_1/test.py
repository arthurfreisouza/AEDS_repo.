class MinhaClasse:
    def obter_nome_instancia(self):
        return self.__class__.__name__

# Exemplo de uso
objeto = MinhaClasse()
nome_instancia = objeto.obter_nome_instancia()
print(nome_instancia)

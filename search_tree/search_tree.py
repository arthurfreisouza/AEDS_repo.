class Node:
    def __init__(self, value : int): # Cada nó da árvore binária tem 1 referência tanto para o nó da esquerda quanto para o nó da direita.
        self.value_ = value
        self.left_ =  None
        self.right_ = None

    def show_node(self): # Função para mostrar o valor do nó.
        print(self.value_)


class SearchTree:
    def __init__(self):
        self.root_ = None # Referência que apontará para o início da árvore (nó raiz).
        self.rows_ = [] # Lista que conterá as strings para usar o site webgraphviz.

    def isEmpty(self): # Checando se a árvore está vazia.
        return self.root_ == None

    def insert(self, value_ : int):
        new_node = Node(value_)
        if self.isEmpty(): # Caso a árvore esteja vazia, o nó raiz apontará para o novo nó.
            self.root_ = new_node
        else:
            pointer = self.root_ # Ponteiro que irá percorrer a árvore para encontrar a posição que será inserido o novo nó.
            while True:
                father = pointer # Irá armazenar sempre, o nó anterior para que o ponteiro possa iterar para os valores a frente da árvore.
                if value_ < pointer.value_: # Se o valor for menor do que o valor do nó, ele irá percorrer a esquerda.
                    pointer = pointer.left_ 
                    if pointer == None: # Chegando na posição mais a esquerda, onde o nó será inserido.
                        father.left_ = new_node
                        self.rows_.append(str(father.value_) + "->" + str(new_node.value_)) # lista que conterá o fluxograma da árvore.
                        return
                else:
                    pointer = pointer.right_ # Caso o valor seja maior do que o valor atual do nó da árvore, então irei iterar para a direita dela.
                    if pointer == None:
                        father.right_ = new_node # Chegando na posição mais a direita, onde o nó será inserido.
                        self.rows_.append(str(father.value_) + "->" + str(new_node.value_)) # lista que conterá o fluxograma da árvore.
                        return



    def search(self, value_ : int): # Fazendo a busca na árvore.
        pointer = self.root_ # Pegando o nó raiz que irei usar para iterar e percorrer toda a árvore.
        while pointer.value_ != value_: # Irei iterar enquanto eu não encontrar o valor que estou procurando.
            if pointer.value_ < value_: # Percorrendo para a direita, pois o valor é maior do que o valor do nó atual.
                pointer = pointer.right_
            else:
                pointer = pointer.left_ # Caso o valor seja menor do que o nó atual, irei procurar na esquerda.
            if pointer == None: # Caso eu tenha percorrido a árvore e não tenha encontrado nenhum valor correspondente ao desejado.
                return None
        return pointer
    
    def pre_order(self, node : Node):
        if node != None:
            print(node.value_) # Printando o valor do nó atual.
            self.pre_order(node.left_) # Irei printar, inicialmente, o trajeto da árvore que ela seguirá para a esquerda.
            self.pre_order(node.right_) # Após ter printado os valores do trajeto a esquerda, voltar printando os valores da direita.   

    def in_order(self, node : Node): # Irá imprimir todos os valores da árvore em ordem crescente.
        if node != None:
            self.in_order(node.left_) # Através desse loop, sempre irei para a parte mais esquerda do árvore, ou seja, para a parte que contém o menor valor.
            print(node.value_) # Sempre que eu chegar na parte de menor valor atual, irei imprimi-lo.
            self.in_order(node.right_) # Irei fazer a mesma coisa para a direita, e irei continuar pegando os menores valores com o node.left.

    def pos_order(self, node : Node): # Primeiro irei visitar os nós filhos e imprimi-lo, depois irei para o nó raiz e imprimi-lo.
        if node != None:
            self.pos_order(node.left_) # Darei prioridade para os nós da esquerda (menor valor).
            self.pos_order(node.right_)
            print(node.value_)


    def remove_element(self, value_ : int):
        if self.isEmpty(): # Não há como excluir elementos de árvores vazias.
            print(" The tree is empty ...")
            return
        else:
            actual = self.root_
            father = self.root_ # Terá salvo sempre o nó de trás.
            e_left = True # Indicará se o elemento que estou apagando está na esquerda ou direita. Ele será comparado em relação ao nó pai.
            while actual.value_ != value_:
                father = actual # Atualizando o valor do pai.

                # Esquerda.
                if actual.value_ > value_:
                    e_left = True # Caso o valor seja menor, ele estará a esquerda do nó pai.
                    actual = actual.left_ # Atualizando meu valor atual.

                # Direita.
                else:
                    e_left = False # se ele for maior, estará a direita do nó pai.
                    actual = actual.right_ # Atualizando o valor atual.

                if actual == None: # Caso não encontre o valor desejado.
                    return False
            # Nesse ponto, a variável father terá o nó pai do nó desejado apagar.
            # A variável e_left indicará se o valor está na direita ou esquerda do nó pai, ou seja, se será maior ou menor do que o nó pai.
                

            if actual.left_ == None and actual.right_ == None: # Caso o nó que quero apagar seja um nó folha....
                if actual == self.root_: # Se o nó folha for o início da lista...
                    self.root_ = None
                elif e_left == True: # Se ele estiver a esquerda do nó pai, irei excluir a posição na esquerda do nó pai.
                    father.left_ = None # O excluindo.
                    self.rows_.remove(str(father.value_) + "->" + str(actual.value_)) # Excluindo a relação.
                else:
                    father.right_ = None # Apontando o nó da direita para o valor None, visto que irei apagá-lo agora.
                    self.rows_.remove(str(father.value_) + "->" + str(actual.value_))# Excluindo a relação.
       
            elif actual.right_ == None:# Caso o nó que quero apagar não seja um nó folha e o valor esteja do lado esquerd 
                self.rows_.remove(str(father.value_) + "->" + str(actual.value_))
                self.rows_.remove(str(actual.value_) + "->" + str(actual.left_.value_)) 
                if actual == self.root_: # Caso eu queira apagar a raiz, a nova raiz será a variável que está na esquerda do nó atual.
                    self.root_ = actual.left_ 
                elif e_left == True: # a variável e_left está indicando que o nó atual estará na esquerda da variável father.
                    father.left_ = actual.left_ # Apagando o nó da esquerda, note que eu já sei que o nó só tem 1 filho, e ele está na esquerda.
                else:
                    father.right_ = actual.left_ # Caso contrário, apagar o nó da direita.

            elif actual.left_ == None: # Caso o nó que eu quero apagar tenha um filho na direita...
                self.rows_.remove(str(father.value_) + "->" + str(actual.value_))
                self.rows_.remove(str(actual.value_) + "->" + str(actual.right_.value_))
                if actual == self.root_: # Caso seja o nó raiz..
                    self.root_ = actual.right_
                elif e_left == True: # Sabendo que o a variável atual está a esquerda do nó pai.
                    father.left_ = actual.right_ 
                else: # Caso a variável atual esteja a direita do nó pai...
                    father.right_ = actual.right_

            else: # Caso o nó possua 2 filhos...
                sucessor = self.get_sucessor(actual)
                if actual == self.root_:
                    self.root_ = sucessor
                elif e_left == True: # Analisando se a variável actual está a esquerda ou direita do nó pai.
                    father.left_ = sucessor # Caso esteja na esquerda (menor)....
                else:
                    father.right_ = sucessor # Caso esteja na direita (maior)....
                sucessor.left_ = actual.left_

    def get_sucessor(self, node : Node):
        pai_sucessor = node
        sucessor = node
        actual = node.right_ # Pegarei o nó a direita do nó que eu desejo encontrar o sucessor.
        while actual != None: # O loop será percorrido enquanto eu não encontrar o sucessor em ordem (irá percorrer para a esquerda buscando o menor valor para o sucessor).
            pai_sucessor = sucessor # Ao final, terá o nó pai do sucessor.
            sucessor = actual # Pegará o valor que será o sucessor do nó que será apagado.
            actual = actual.left_

        if sucessor != node.right_: # Caso o nó que será sucessor não seja o nó que está  imediatamente a direita do nó que quero remover...
            pai_sucessor.left_ = sucessor.right_
            sucessor.right_ = node.right_
        return sucessor






                    


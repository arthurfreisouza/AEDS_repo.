class Adjacente:
  def __init__(self, vertice, custo):
    self.vertice = vertice
    self.custo = custo

class Vertice:
  def __init__(self, rotulo):
    self.rotulo = rotulo
    self.visitado = False
    self.adjacentes = []

  def adiciona_adjacente(self, adjacente : Adjacente):
    self.adjacentes.append(adjacente)

  def mostra_adjacentes(self):
    for i in self.adjacentes:
      print(i.vertice.rotulo, i.custo)

class Grafo:
  arad = Vertice('Arad')
  zerind = Vertice('Zerind')
  oradea = Vertice('Oradea')
  sibiu = Vertice('Sibiu')
  timisoara = Vertice('Timisoara')
  lugoj = Vertice('Lugoj')
  mehadia = Vertice('Mehadia')
  dobreta = Vertice('Dobreta')
  craiova = Vertice('Craiova')
  rimnicu = Vertice('Rimnicu')
  fagaras = Vertice('Fagaras')
  pitesti = Vertice('Pitesti')
  bucharest = Vertice('Bucharest')
  giurgiu = Vertice('Giurgiu')

  arad.adiciona_adjacente(Adjacente(zerind, 75))
  arad.adiciona_adjacente(Adjacente(sibiu, 140))
  arad.adiciona_adjacente(Adjacente(timisoara, 118))

  zerind.adiciona_adjacente(Adjacente(arad, 75))
  zerind.adiciona_adjacente(Adjacente(oradea, 71))

  oradea.adiciona_adjacente(Adjacente(zerind, 71))
  oradea.adiciona_adjacente(Adjacente(sibiu, 151))

  sibiu.adiciona_adjacente(Adjacente(oradea, 151))
  sibiu.adiciona_adjacente(Adjacente(arad, 140))
  sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
  sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

  timisoara.adiciona_adjacente(Adjacente(arad, 118))
  timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

  lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
  lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

  mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
  mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

  dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
  dobreta.adiciona_adjacente(Adjacente(craiova, 120))

  craiova.adiciona_adjacente(Adjacente(dobreta, 120))
  craiova.adiciona_adjacente(Adjacente(pitesti, 138))
  craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

  rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
  rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
  rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

  fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
  fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

  pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
  pitesti.adiciona_adjacente(Adjacente(craiova, 138))
  pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

  bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
  bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
  bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))



import numpy as np


class Stack:
    def __init__(self, cap_ : int = 10): # A capacidade será 10, caso nenhum valor seja passado.
        self.__capacidade = cap_
        self.__last_pos = -1
        self.__arr = np.empty(self.__capacidade, dtype = str) # Iniciando 1 array vazio.

    def push(self, value):
        if self.isFull(): # Caso o array esteja cheio : 
            raise Exception("Its full ! ")
        else:
            if self.isEmpty(): # Caso o array esteja vazio : 
                print("Creating the array ...")
            self.__last_pos = self.__last_pos + 1 # Posição inicial = -1, -1 + 1 = 0, então o primeiro elemento vai para a posição 0.
            self.__arr[self.__last_pos] = value

    def imprime(self): # Varrerá todo o array, imprimindo todos os valores...
        for i in range(self.__last_pos + 1):
            str_ = str(i) + " - " + str(self.__arr[i])
            print(str_)

    def ver_topo(self):
        if self.__last_pos == -1: # Caso o array esteja vazio.
            return -1
        else:
            return self.__arr[self.__last_pos]
    
    def pop(self):
        if self.isEmpty(): # Verifica se está vazio...
            raise Exception("Its empty ! ")
        else:
            self.__arr[self.__last_pos] = 0
            self.__last_pos = self.__last_pos - 1
    
    def peek(self): # Pega o topo da pilha.
        if self.__last_pos == -1:
            print("Pilha vazia..")
        else:
            return self.__arr[self.__last_pos]
    
    def isEmpty(self): # Ṕega se a pilha está vazia.
        cond = (self.__last_pos == -1)
        return cond == True
    
    def isFull(self): # Pega se a pilha está cheia.
        cond = (self.__last_pos == self.__capacidade - 1)
        return cond == True
    



    class BuscaProfundidade:
       def __init__(self, inicio):
          self.inicio = inicio
          self.inicio.visitado = True
          self.pilha = Stack(20)
          self.pilha.push(inicio)

        def buscar(self):
          topo = self.pilha.peek()
          print('Topo : {}'.format(topo.rotulo))
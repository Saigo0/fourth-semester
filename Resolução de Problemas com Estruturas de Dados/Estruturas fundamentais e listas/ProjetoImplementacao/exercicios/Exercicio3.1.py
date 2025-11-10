from Node import Node
from Livro import Livro
from LinkedList import LinkedList



lista = LinkedList()
livro = Livro("Berserk Vol.1")
livro2 = Livro("<NAME>")
lista.add_last("livro2")
lista.add_first(livro)
lista.add_last(livro2)
print(lista.size2())

